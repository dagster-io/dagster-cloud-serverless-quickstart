import os

from dagster import define_asset_job, load_assets_from_package_module, repository, with_resources
from dagster_aws.s3 import s3_pickle_io_manager, s3_resource

from my_dagster_project import assets


@repository
def my_dagster_project():

    # # To take advantage of Dagster's incremental re-execution functionality (e.g. retry from failure),
    # # you'll need to set up an IO manager that can move the data across runs.
    # # Learn more at https://docs.dagster.io/concepts/io-management/io-managers#applying-io-managers-to-assets
    # # NOTE: Uncomment the example code below to use an s3_pickle_io_manager to pass data between runs.

    # # Vary s3_prefix based on environment:
    # # In this example, we vary folder per branch deployment (PR number) and prod.
    # # Read about best practice at https://docs.dagster.io/guides/dagster/branch_deployments
    # if os.getenv("DAGSTER_CLOUD_IS_BRANCH_DEPLOYMENT"):
    #     s3_prefix = f"MY_S3_PREFIX/branch_{os.getenv('DAGSTER_CLOUD_PULL_REQUEST_ID')}"
    # else:
    #     s3_prefix = "MY_S3_PREFIX"

    # # The resource uses boto under the hood, so if you are accessing your private buckets, you will need
    # # to provide the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables.
    # # Read about adding sehttps://docs.dagster.io/dagster-cloud/deployment/serverless#adding-secrets
    # resource_defs = {
    #     "io_manager": s3_pickle_io_manager.configured(
    #         {
    #             "s3_bucket": "MY_S3_BUCKET",
    #             "s3_prefix": s3_prefix,
    #         }
    #     ),
    #     "s3": s3_resource,
    # }

    # return [
    #     *with_resources(
    #         definitions=load_assets_from_package_module(assets), resource_defs=resource_defs
    #     ),
    #     define_asset_job(name="all_assets_job"),
    # ]

    return [
        load_assets_from_package_module(assets),
        define_asset_job(name="all_assets_job"),
    ]
