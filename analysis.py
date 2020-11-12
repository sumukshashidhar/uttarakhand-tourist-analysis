"""
A simple python program.
"""
#TODO: Write Proper Documentation


# IMPORTS & REQUIREMENTS
# IMPORTS
import plotly.express as px
import pandas as pd

# DATA REQUIREMENTS
data = "./processed_data/polarity_included.csv"

# preparing a pandas dataframe
df = pd.read_csv(data)

# the df has an unnecessary column
df = df.drop(columns = ["Unnamed: 0"])

# quantify positivity and negativity
df["review_verdict"] = df.review_verdict.replace({
        "positive":1,
        "negative":0,
        "neutral":0.5
    })


# make a list of our unique spots
residences = df.spot.unique()


