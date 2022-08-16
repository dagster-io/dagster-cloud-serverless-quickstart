import os

from dagster import define_asset_job, load_assets_from_package_module, repository, with_resources
from dagster_aws.s3 import s3_pickle_io_manager, s3_resource

from my_dagster_project import assets


@repository
def my_dagster_project():
    # When you define a downstream asset that depends on another asset, to take advantage of Dagster's
    # incremental re-execution functionality (e.g. retry from failure), you'll need to set up an IO
    # manager that can move the data across runs. Learn more at https://docs.dagster.io/concepts/io-management/io-managers#applying-io-managers-to-assets
    #
    # NOTE: In this starter project, we provide a commented example that uses an s3_pickle_io_manager to
    # pass data between runs. To get started:
    # 1. Uncomment the code below.
    # 2. Replace "MY_S3_BUCKET" and "MY_S3_PREFIX" with your own values.
    #   * This example also varies s3 prefix based on environments. Read more about branch deployment
    #   best practices at https://docs.dagster.io/guides/dagster/branch_deployments
    # 3. Provide the "AWS_ACCESS_KEY_ID" and "AWS_SECRET_ACCESS_KEY" environment variables if you
    # are accessing your private buckets.
    #   * Learn about adding secrets in Serverless at https://docs.dagster.io/dagster-cloud/deployment/serverless#adding-secrets

    # if os.getenv("DAGSTER_CLOUD_IS_BRANCH_DEPLOYMENT"):
    #     s3_prefix = f"MY_S3_PREFIX/branch_{os.getenv('DAGSTER_CLOUD_PULL_REQUEST_ID')}"
    # else:
    #     s3_prefix = "MY_S3_PREFIX"
    #
    # resource_defs = {
    #     "io_manager": s3_pickle_io_manager.configured(
    #         {"s3_bucket": "MY_S3_BUCKET", "s3_prefix": s3_prefix}
    #     ),
    #     "s3": s3_resource,
    # }
    #
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
