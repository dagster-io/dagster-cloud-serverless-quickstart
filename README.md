# Dagster Cloud Serverless Deployment Quickstart

> [!IMPORTANT] 
> You do not need to use this repo to use Dagster Cloud Serverless. When you create an account on Dagster Cloud, it creates a repo for you with the GitHub actions installed. If you want to deploy another project you can use the "Add code locations" button on the Deployments page. This repo provides an alternative way to create a project linked to Dagster Cloud serverless.

Welcome to your Dagster Cloud sample code repo. Here, you can find the code that's being deployed to your Dagster Cloud instance. For more information on Dagster+ Serverless, see our [Serverless docs](https://docs.dagster.io/deployment/dagster-plus/serverless).

Pushing to production will automatically kick off a [workflow](./.github/workflows/dagster-plus-deploy.yml), which will redeploy your code to your `prod` deployment.

Creating a pull request will kick off a [workflow](./.github/workflows/dagster-plus-deploy.yml), which will create a new [**Branch Deployment**](https://docs.dagster.io/deployment/dagster-plus/ci-cd/branch-deployments), an ephemeral deployment where you can test your changes.

# Setting up quickstart template manually

> [!NOTE]
> If you had Dagster Cloud clone and set up this repo for you, you don't need to follow these instructions.

## 1. Clone template repo

Click the `Use this Template` button, then select `Create a new repository`, and provide details for your new repo.

<img width="953" alt="Use this template button" src="">

## 2. Set up secrets

Set up secrets on your newly created repository by navigating to the `Settings` panel in your repo, clicking `Secrets and variables` on the sidebar, and selecting `Actions`. Then, click `New repository secret`.

| Name                      | Description                                                                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `DAGSTER_CLOUD_API_TOKEN` | An agent token. For more details see [the Dagster+ docs](https://docs.dagster.io/deployment/dagster-plus/management/tokens/agent-tokens). |

## 3. Update workflows

Replace the `ORGANIZATION_NAME` in `.github/workflows/dagster-plus-deploy.yml` with your Dagster cloud organization name:

```
  DAGSTER_CLOUD_URL: "https://ORGANIZATION_NAME.dagster.cloud"
```

## 4. Verify builds are successful

At this point, the workflow should complete successfully. If builds are failing, ensure that your secrets are properly set and that your deployment has finished activating.

## Next steps

Now that your GitHub repository is setup with CI/CD to deploy to Dagster Cloud, you can add your own Dagster code. To run this project locally with dagit, first install its local developement dependencies:

```bash
pip install -e ".[dev]"
```

Once you've done this, you can run:

```
dg dev
```

to view this repo in Dagster UI

You can also copy any existing [Dagster examples or quickstart projects](https://github.com/dagster-io/dagster/tree/master/examples) into this GitHub repository.
