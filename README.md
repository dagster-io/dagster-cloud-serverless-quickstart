# Dagster+ Serverless deployment quickstart

> [!IMPORTANT] 
> You do not need to use this repo to use Dagster+ Serverless. When you create an account on Dagster+, it creates a repo for you with the GitHub actions installed. If you want to deploy another project, you can use the **Add code locations** button on the Deployments page. This repo provides an alternative way to create a project linked to Dagster+ Serverless.

Welcome to your Dagster+ sample code repo. Here, you can find the code that's being deployed to your Dagster+ instance. For more information on Dagster+ Serverless, see our [Serverless docs](https://docs.dagster.io/deployment/dagster-plus/serverless).

Pushing to production (the `main` branch) will automatically kick off a [workflow](./.github/workflows/dagster-plus-deploy.yml), which will redeploy your code to your `prod` deployment.

Creating a pull request will kick off a [workflow](./.github/workflows/dagster-plus-deploy.yml), which will create a new [**Branch Deployment**](https://docs.dagster.io/deployment/dagster-plus/ci-cd/branch-deployments), an ephemeral deployment where you can test your changes.

# Setting up quickstart template manually

> [!IMPORTANT]
> If you had Dagster+ clone and set up this repo for you, you don't need to follow these instructions.

## 1. Clone template repo

Click the **Use this Template** button, then select **Create a new repository**, and provide details for your new repo.

<img width="953" alt="Use this template button" src="https://community-engineering-artifacts.s3.amazonaws.com/images/screenshot-quickstart-create-repository.png">

## 2. Set up secrets

Set up secrets on your newly created repo by navigating to the **Settings** panel in your repo, clicking **Secrets and variables** in the left sidebar, and selecting **Actions**. Then, click **New repository secret**.

| Name                      | Description                                                                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `DAGSTER_CLOUD_API_TOKEN` | An agent token. For more details see [the Dagster+ agent tokens guide](https://docs.dagster.io/deployment/dagster-plus/management/tokens/agent-tokens). |

## 3. Update workflows

Replace the `ORGANIZATION_NAME` in `.github/workflows/dagster-plus-deploy.yml` with your Dagster+ organization name:

```
  DAGSTER_CLOUD_URL: "https://ORGANIZATION_NAME.dagster.cloud"
```

## 4. Verify builds are successful

At this point, the workflow should complete successfully. If builds are failing, ensure that your secrets are properly set and that your deployment has finished activating.

## 5. Run this project locally

Now that your GitHub repo is setup with CI/CD to deploy to Dagster+, you can run this project locally and add your own Dagster code.

1. Create a virtual environment with `uv` or `venv`.
2. Install local developement dependencies with `uv` or `pip`:

```bash
uv pip install -e ".[dev]"
```

or 

```bash
pip install -e ".[dev]"
```
3. Run `dg dev` to view this repo in the Dagster UI:

```bash
dg dev
```

> [!TIP]
> We have a number of additional [Dagster example projects](https://github.com/dagster-io/dagster/tree/master/examples) that you can clone and run locally, or use to create new [code locations](https://docs.dagster.io/deployment/code-locations/dagster-plus-code-locations) in Dagster+ Serverless.
