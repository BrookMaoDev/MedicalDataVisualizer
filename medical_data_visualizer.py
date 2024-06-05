import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")


# 2
def overweight(row: pd.Series) -> int:
    """
    Returns 1 for overweight and 0 otherwise.
    """
    CENTIMETERS_PER_METER = 100
    bmi = (
        float(row["weight"])
        / (float(row["height"]) / CENTIMETERS_PER_METER) ** 2
    )
    return int(bmi > 25)


df["overweight"] = df.apply(overweight, axis=1)

# 3
df["cholesterol"] = df.apply(lambda row: int(row["cholesterol"] > 1), axis=1)
df["gluc"] = df.apply(lambda row: int(row["gluc"] > 1), axis=1)


# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(
        id_vars=["cardio"],
        value_vars=[
            "cholesterol",
            "gluc",
            "smoke",
            "alco",
            "active",
            "overweight",
        ],
        var_name="variable",
        value_name="value",
    )

    # 6
    df_cat = (
        df_cat.groupby(["cardio", "variable", "value"])
        .size()
        .reset_index(name="total")
    )

    # 7
    chart = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar",
    )

    # 8
    fig = chart.figure

    # 9
    fig.savefig("catplot.png")
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
        & (df["ap_lo"] <= df["ap_hi"])
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr, mask=mask, ax=ax, annot=True, fmt=".1f")

    # 16
    fig.savefig("heatmap.png")
    return fig
