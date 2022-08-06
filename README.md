# Dagster Cloud Serverless Deployment Quickstart

## Create a new project from this template

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
