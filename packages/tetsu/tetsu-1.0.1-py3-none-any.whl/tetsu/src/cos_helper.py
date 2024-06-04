# COS Helper --- Interact with COS via Python

import os

import ibm_boto3
from ibm_boto3.s3.transfer import TransferConfig
import pandas as pd
from ibm_botocore.client import Config

from tetsu.src import cloudant_helper
from tetsu.src.log_helper import logger

logger = logger(name=__name__, handler="console")


class COSHelper:
    def __init__(
        self, environment: str, cos_bucket: str, cloudant_doc=None, creds=None
    ):
        """
        Instantiation of the COSHelper class

        :param environment: The environment (prod or staging)
        :param cos_bucket: The name of the bucket that will be connected to
        :param cloudant_doc: The cloudant document object that will be used to retrieve credentials
                             If None, user env will be searched for a document
        """
        self.cos_bucket = cos_bucket
        if cloudant_doc is None:
            try:
                self.cloudant_doc = os.getenv("cloudant_document")
            except Exception as e:
                raise RuntimeError("cloudant_document environment variable not set", e)
        else:
            self.cloudant_doc = cloudant_doc

        if creds is None:
            self.creds = {
                "cos_api_key": [environment, "cos", "cos_api_key"],
                "cos_resource_crn": [environment, "cos", "cos_resource_crn"],
                "cos_endpoint": [environment, "cos", "cos_endpoint"],
                "cos_auth_endpoint": [environment, "cos", "cos_auth_endpoint"],
            }
        else:
            self.creds = creds
        self.creds = cloudant_helper.get_credentials(
            doc=self.cloudant_doc, creds=self.creds
        )

        self.cos_object = ibm_boto3.client(
            service_name="s3",
            ibm_api_key_id=self.creds["cos_api_key"],
            ibm_service_instance_id=self.creds["cos_resource_crn"],
            ibm_auth_endpoint=self.creds["cos_auth_endpoint"],
            config=Config(signature_version="oauth"),
            endpoint_url=self.creds["cos_endpoint"],
        )

        # This allows for multi-part uploads for files greater than 5MB
        self.config = TransferConfig(
            multipart_threshold=1024 * 1024 * 25,
            max_concurrency=10,
            multipart_chunksize=1024 * 1024 * 25,
            use_threads=True,
        )

    def upload_file(self, files_list: list) -> None:
        """
        This function takes a list of files and uploads them to the specified COS bucket

        :param files_list: The list of files that will be uploaded to the bucket
                           (Needs to be a list even if there is only one file)
        """
        for file in files_list:
            try:
                self.cos_object.upload_file(
                    Filename=file, Bucket=self.cos_bucket, Key=file, Config=self.config
                )
            except Exception as e:
                logger.exception(
                    f"Could not upload file to {self.cos_bucket} due to {e}"
                )
            else:
                logger.info(f"File uploaded to {self.cos_bucket} successfully")

    def upload_df(
        self, df: pd.DataFrame, file_name: str, file_type: str = None
    ) -> None:
        """
        This function takes a dataframe and uploads it to the specified COS bucket

        :param df: The dataframe to be uploaded
        :param file_name: The name of the file once uploaded
        :param file_type: The file type
        """

        if file_type == "csv":
            filename = file_name + ".csv"
            df.to_csv(filename, sep=",", index=False)
        elif file_type == "parquet":
            filename = file_name + ".csv"
            df.to_parquet(filename)
        elif file_type == "pickle":
            filename = file_name + ".pkl"
            df.to_pickle(filename)
        else:
            raise RuntimeError("Please pick from csv, parquet, or pickle")

        try:
            self.cos_object.upload_file(
                Filename=filename,
                Bucket=self.cos_bucket,
                Key=filename,
                Config=self.config,
            )
        except Exception as e:
            logger.exception(
                f"Could not upload {filename} to {self.cos_bucket} due to {e}"
            )
        else:
            logger.info(f"{filename} uploaded to {self.cos_bucket} successfully")

    def download_file(self, files_list: list) -> None:
        """
        This function takes a list of files and downloads them from a COS bucket to the project's WORKDIR

        :param files_list: The list of files that will be downloaded from the bucket
                           (Needs to be a list even if there is only one file)
        """
        for file in files_list:
            try:
                self.cos_object.download_file(
                    Filename=file, Bucket=self.cos_bucket, Key=file
                )
            except Exception as e:
                logger.exception(
                    f"Could not upload file to {self.cos_bucket} due to {e}"
                )
            else:
                logger.info(f"File uploaded to {self.cos_bucket} successfully")
