from typing import Dict, List

import pandas as pd
from scipy.stats import pearsonr, spearmanr
from .md import get_flac_markdown, get_badd_markdown, get_adaface_markdown


def analysis(
    csv_path: str,
    task: str,
    target: str,
    sensitive: List[str],
    sp_th: float = 0.1,
    rep_th: float = 0.1,
):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    representation_bias_result = analyze_representation_bias(df, sensitive)

    # Provide suggestions based on the task and analysis results
    suggestions = []
    results_dict = {"task": task, "biases": [], "mitigation": []}
    bias_threshold = rep_th
    c = 0
    for key, value in representation_bias_result.items():
        if isinstance(value, dict):
            # print(value)
            max_proportion = max(value.values())
            min_proportion = min(value.values())
            if max_proportion - min_proportion > bias_threshold * sum(value.values()):
                suggestions.append(
                    f"There is representation bias for {key} ({(max_proportion-min_proportion)*100:.2f}% gap between most and less represented group)."
                )

                results_dict["biases"].append(suggestions[-1])

    sc = find_spurious_correlations(df, target, sensitive, sp_th)
    if task.lower() == "face verification":
        suggestions.append(
            "Consider using AdaFace for training a fairer face verification model."
        )
        results_dict["mitigation"].append(suggestions[-1])

    elif task.lower() == "image classification":
        if len(sc) == 1:
            suggestions.append(
                f"There is spurious correlation of {(sc[0][2])*100:.2f}% between {sc[0][0]} and {sc[0][1]}."
            )
            results_dict["biases"].append(suggestions[-1])
            results_dict["mitigation"].append(
                "Consider using the FLAC method to mitigate it."
            )
        elif len(sc) > 1:
            for tar, sen, per in sc:
                suggestions.append(
                    f"There is spurious correlation of {per*100:.2f}% between {tar} and {sen}."
                )
                results_dict["biases"].append(suggestions[-1])
            results_dict["mitigation"].append(
                "Given that there are multiple spurious correlations, consider using the BAdd method to mitigate it."
            )

    nl = "\n"
    markdown = f"""
# Task: {results_dict['task']}

## Biases:
{''.join([f"- {bias}{nl}" for bias in results_dict['biases']])}

## Mitigation:
{''.join([f"- {mitigation}{nl}" for mitigation in results_dict['mitigation']])}
"""
    flac_present = any("flac" in text.lower() for text in results_dict["mitigation"])
    badd_present = any("badd" in text.lower() for text in results_dict["mitigation"])
    adaface_present = any(
        "adaface" in text.lower() for text in results_dict["mitigation"]
    )

    if flac_present:
        markdown += get_flac_markdown()
    elif badd_present:
        markdown += get_badd_markdown()
    elif adaface_present:
        markdown += get_adaface_markdown()
    elif len(results_dict["biases"] > 0):
        markdown += get_flac_markdown()
    return markdown


def find_spurious_correlations(
    df, target_column, attribute_columns, threshold=0.01, method="pearson"
):
    """
    Finds spurious correlations between attributes and the target column in a DataFrame.

    Parameters:
        df (DataFrame): The DataFrame containing attributes and the target column.
        attribute_columns (list): List of attribute column names.
        target_column (str): The name of the target column.
        threshold (float): The threshold for correlation coefficient above which correlations are considered significant.
        method (str): The method to compute correlation. Options: 'pearson' (default) or 'spearman'.

    Returns:
        spurious_correlations (list of tuples): List of tuples containing attribute-target pairs with spurious correlations.
    """
    spurious_correlations = []

    if method == "pearson":
        corr_func = pearsonr
    elif method == "spearman":
        corr_func = spearmanr
    else:
        raise ValueError(
            "Invalid correlation method. Please choose 'pearson' or 'spearman'."
        )
    df[target_column], _ = pd.factorize(df[target_column])
    # print(df)
    for column in attribute_columns:
        codes, _ = pd.factorize(df[column])
        correlation, _ = corr_func(codes, df[target_column])
        # print(correlation)
        if abs(correlation) > threshold:
            spurious_correlations.append((column, target_column, abs(correlation)))

    return spurious_correlations


def analyze_representation_bias(
    df: pd.DataFrame, sensitive: List[str]
) -> Dict[str, Dict[str, float]]:
    """
    Analyzes representation bias with respect to sensitive attributes.

    Parameters:
    csv_path (str): The path to the CSV file.
    sensitive (List[str]): A list of column names of the sensitive attributes.

    Returns:
    Dict[str, Dict[str, float]]: A dictionary with representation bias scores.
    """

    # Initialize the result dictionary
    result = {}

    # Analyze representation bias for each sensitive attribute
    for attribute in sensitive:
        attribute_counts = df[attribute].value_counts(normalize=True)
        result[attribute] = attribute_counts.to_dict()

    return result


# md = analysis(
#     "./data/rfw.csv",
#     "image classification",
#     "Gender",
#     ["Age Category", "Age"],
#     0.01,
#     0.01,
# )
# print(md)
