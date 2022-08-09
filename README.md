# Dagster Cloud Serverless Deployment Quickstart

Welcome to your Dagster Cloud sample code repo. Here, you can find the code that's being deployed to your Dagster Cloud instance. For more in-depth information, check out our [Serverless](https://docs.dagster.io/dagster-cloud/deployment/serverless) docs.

Pushing to production will automatically kick off a [workflow](./.github/workflows/deploy.yml) which will redeploy your code to your `prod` deployment.

Creating a pull request will kick off a [workflow](./.github/workflows/deploy.yml) which will create a new [**Branch Deployment**](https://docs.dagster.io/dagster-cloud/developing-testing/branch-deployments), an ephemeral deployment where you can test your changes.

# Setting up Quickstart Template Manually

If you had Dagster Cloud clone and set up this repo for you, no need to follow these instructions.

Click the `Use this Template` button and provide details for your new repo.

<img width="953" alt="Screen Shot 2022-07-06 at 7 24 02 AM" src="https://user-images.githubusercontent.com/10215173/177577141-b6a91585-a276-49d3-b66b-e47bd26665a0.png">

## Set up secrets

Set up secrets on your newly created repository by navigating to the `Settings` panel in your repo, clicking `Secrets` on the sidebar, and selecting `Actions`. Then, click `New repository secret`.

| Name                      | Description                                                                                                                                                                                                     |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DAGSTER_CLOUD_API_TOKEN` | An agent token, for more details see [the Dagster Cloud docs](https://docs.dagster.cloud/auth#managing-user-and-agent-tokens).                                                                                  |
| `ORGANIZATION_ID`         | The organization ID of your Dagster Cloud organization, found in the URL. For example, `pied-piper` if your organization is found at `https://dagster.cloud/pied-piper` or `https://pied-piper.dagster.cloud/`. |

## Verify Builds are Successful

At this point, the Workflow should complete successfully. If builds are failing, ensure that your secrets are properly set and that your deployment has finished activating.
