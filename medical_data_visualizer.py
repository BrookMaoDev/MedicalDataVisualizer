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
    bmi = float(row["weight"]) / float(row["height"]) ** 2
    return int(bmi > 25)


df["overweight"] = df.apply(overweight, axis=1)

# 3
df["cholesterol"] = df.apply(lambda row: int(row["cholesterol"] > 1), axis=1)
df["gluc"] = df.apply(lambda row: int(row["gluc"] > 1), axis=1)


# 4
def draw_cat_plot():
    # 5
    df_cat = None

    # 6
    df_cat = None

    # 7

    # 8
    fig = None

    # 9
    fig.savefig("catplot.png")
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None

    # 14
    fig, ax = None

    # 15

    # 16
    fig.savefig("heatmap.png")
    return fig
