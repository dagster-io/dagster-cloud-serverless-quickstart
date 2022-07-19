import csv
import requests
from dagster import asset, define_asset_job, repository


@asset
def cereals():
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    cereal_rows = [row for row in csv.DictReader(lines)]

    return cereal_rows


@asset
def nabisco_cereals(cereals):
    """Cereals manufactured by Nabisco"""
    return [row for row in cereals if row["mfr"] == "N"]


all_cereals_job = define_asset_job(name="all_cereals_job")


@repository
def repo():
    return [
        cereals,
        nabisco_cereals,
        all_cereals_job,
    ]
