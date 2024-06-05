import pandas as pd
from io import BytesIO
from azure.storage.blob import BlobServiceClient
from .constants import ZERO_DAY_MIN_AREA, CSV_COLUMNS
from .utils import create_keyvault_client
import matplotlib.pyplot as plt
from statannotations.Annotator import Annotator
import seaborn as sns
import itertools


def preprocess_analysis_dataframe(input_df):
    """Preprocess raw wound healing study dataframe to prepare for plotting and stats

    :param input_df: pandas.DataFrame object containing raw `study_summary_metrics.csv`
    :return: pandas.DataFrame object containing processed would healing study stats
    """
    df = input_df[input_df["valid_area"]].copy(deep=True)

    # Preprocess filename into specific columns
    df["Study name"] = df["filename"].str.split("_").str[0]
    df["Porcine ID"] = df["filename"].str.split("_").str[1]
    df["Wound site location"] = df["filename"].str.split("_").str[2]
    df["Days"] = df["filename"].str.split("_").str[3]
    df["Days"] = df["Days"].str[1:].astype(int)
    df["Product type"] = df["filename"].str.split("_").str[4]
    df = df.rename(columns={"wounded_area (cm^2)": "Wounded area (cm^2)"})

    # Filter out edge cases
    filter_mask = (df["Days"] == 0) & (df["Wounded area (cm^2)"] < ZERO_DAY_MIN_AREA)
    df = df[~filter_mask]
    df = df[CSV_COLUMNS]
    df = df.sort_values("Days")

    df_deduped = df.drop_duplicates(
        ["Study name", "Porcine ID", "Wound site location", "Product type"],
        keep="first",
    )
    df_deduped = df_deduped.rename(
        columns={"Wounded area (cm^2)": "Wounded area baseline"}
    )
    _ = df_deduped.pop("Days")

    df = df.merge(
        df_deduped,
        on=["Study name", "Porcine ID", "Wound site location", "Product type"],
        how="inner",
    )
    df["Percent reduction\nfrom baseline"] = (
        100
        * (df["Wounded area (cm^2)"] - df["Wounded area baseline"])
        / df["Wounded area baseline"]
    )

    return df


def read_summary_metrics_csv(config: dict) -> pd.DataFrame:
    """Read study_summary_metrics.csv from Azure cloud storage and preprocess for plot generation.

    :param config: configuration dictionary
    :return: pandas.DataFrame object containing processed would healing study stats
    """

    # Get Azure API keys
    keyvault_secret_client = create_keyvault_client(config=config)
    storage_api_secret = keyvault_secret_client.get_secret(config["storage_secret"])

    # Connect to Storage account
    blob_service_client = BlobServiceClient.from_connection_string(
        storage_api_secret.value
    )
    # load file from blob
    blob_name = f"{config['output_folder'] + 'morphometrics/study_summary_metrics.csv'}"
    blob_service_client = BlobServiceClient.from_connection_string(
        storage_api_secret.value
    )
    container_client = blob_service_client.get_container_client(
        config["storage_container"]
    )
    blob_client = container_client.get_blob_client(blob_name)
    blob_data = blob_client.download_blob().readall()
    df = pd.read_csv(BytesIO(blob_data))

    df = preprocess_analysis_dataframe(input_df=df)
    return df


def generate_wound_healing_plots(config: dict) -> None:
    """Generate custom wound healing study plots

    :param config: configuration dictionary
    :return: None. Generate several seaborn plots and save locally.
    """

    would_study_df = read_summary_metrics_csv(config=config)

    # General wound healing study summary
    plt.figure(figsize=(10, 5))
    _ = sns.boxplot(
        x="Days", y="Wounded area (cm^2)", hue="Product type", data=would_study_df
    )
    plt.savefig("wound_healing_plot.png")
    plt.close()

    # Day 0 normalized would healing study summary
    plt.figure(figsize=(10, 5))
    _ = sns.boxplot(
        x="Days",
        y="Percent reduction\nfrom baseline",
        hue="Product type",
        data=would_study_df,
    )
    plt.savefig("normalized_wound_healing_plot.png")
    plt.close()

    # Statistical test between day 0 and last day
    min_days = would_study_df["Days"].min()
    max_days = would_study_df["Days"].max()
    final_df = would_study_df[would_study_df["Days"].isin([min_days, max_days])]
    products_mask = final_df["Days"] == max_days
    products = final_df[products_mask]["Product type"].unique()
    fig = plt.figure(figsize=(10, 5))
    ax = sns.boxplot(
        x="Days",
        y="Percent reduction\nfrom baseline",
        hue="Product type",
        data=final_df,
    )

    pairs = [((min_days, product), (max_days, product)) for product in products]
    annotator = Annotator(
        ax,
        pairs,
        data=final_df,
        x="Days",
        y="Percent reduction\nfrom baseline",
        hue="Product type",
    )
    annotator.configure(test="Mann-Whitney", text_format="star", loc="outside")
    _ = annotator.apply_and_annotate()
    fig.tight_layout()
    plt.savefig("wound_healing_first_final_day_stats.png")
    plt.close()

    # Statistical tests between final day inter-products
    fig = plt.figure(figsize=(10, 5))
    ax = sns.boxplot(
        x="Days",
        y="Percent reduction\nfrom baseline",
        hue="Product type",
        data=final_df,
    )

    final_day_combos = list(itertools.combinations(products, 2))
    pairs = [
        ((max_days, product_combo[0]), (max_days, product_combo[1]))
        for product_combo in final_day_combos
    ]
    annotator = Annotator(
        ax,
        pairs,
        data=final_df,
        x="Days",
        y="Percent reduction\nfrom baseline",
        hue="Product type",
    )
    annotator.configure(test="Mann-Whitney", text_format="star", loc="outside")
    _ = annotator.apply_and_annotate()
    fig.tight_layout()
    plt.savefig("wound_healing_final_day_stats.png")
    plt.close()
