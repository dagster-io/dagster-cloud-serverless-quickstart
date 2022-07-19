# Serverless deploy demo

## Set up secrets

Set up secrets on your newly created repository by navigating to the `Settings` panel in your repo, clicking `Secrets` on the sidebar, and selecting `Actions`. Then, click `New repository secret`.

| Name                      | Description                                                                                                                                                                                                     |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DAGSTER_CLOUD_API_TOKEN` | An agent token, for more details see [the Dagster Cloud docs](https://docs.dagster.cloud/auth#managing-user-and-agent-tokens).                                                                                  |
| `ORGANIZATION_ID`         | The organization ID of your Dagster Cloud organization, found in the URL. For example, `pied-piper` if your organization is found at `https://dagster.cloud/pied-piper` or `https://pied-piper.dagster.cloud/`. |
