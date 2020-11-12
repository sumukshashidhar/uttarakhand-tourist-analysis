#!/usr/local/bin/python3
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

def input_picker():
    print("Please select \n1. Locations\n2. Unique Spots")
    try:
        inp = int(input())
    except:
        print("Please enter a number")
        exit()


def get_good_reviews(df):
    """
    I am defining a good review as something that is highly
    polar and highly subjective
    """

    def get_some_reviews(dfx):
        


def plot_review_graph_for_spot(df):
    print("We are now plotting a review graph")
    px.scatter(
            data_frame=df,
            x="review_polarity",
            y="review_subjectivity"
            )

if __name__ == "__main__":
    input_picker()

