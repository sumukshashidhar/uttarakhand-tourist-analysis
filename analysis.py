#!/usr/local/bin/python3
"""
A simple python program.
"""
# TODO: Write Proper Documentation


# IMPORTS & REQUIREMENTS
# IMPORTS
import plotly.express as px
import pandas as pd

# DATA REQUIREMENTS
data = "./processed_data/polarity_included.csv"

# preparing a pandas dataframe
df = pd.read_csv(data)

# the df has an unnecessary column
df = df.drop(columns=["Unnamed: 0"])

# quantify positivity and negativity
df["review_verdict"] = df.review_verdict.replace(
    {"positive": 1, "negative": 0, "neutral": 0.5})

# make a different type of index

# make a list of our unique spots
residences = df.spot.unique()


def input_picker():
    print("Please select \n1. Locations\n2. Unique Spots")
    try:
        inp = int(input())
        if inp == 1:
            pass
        elif inp == 2:
            pass
        else:
            pass
    except ValueError:
        print("Please enter a number")
        exit()
    return None


def get_review_from_index(dfa, idx):
    return dfa.loc[dfa.index == idx].values[0]


def get_good_reviews(df):
    """Sending in a dataframe to get both positive and negative reviews back

    Args:
        df (pandas dataframe): a dataframe of all reviews
    """
    def get_some_reviews(dfx):
        """
        This outputs three good reviews from the ones supplied.
        We are trying to maximise two variables here
        """
        maxine = 0, 0, 0, None
        for ind in dfx.index:
            mult = dfx["review_polarity"][ind] * \
                dfx["review_subjectivity"][ind]
            if maxine[0] < mult:
                maxine = mult, dfx["review_polarity"][ind], dfx["review_subjectivity"][ind], ind
            elif maxine[0] == mult:
                maxabs = abs(maxine[1] - maxine[2])
                contender_abs = abs(
                    dfx["review_polarity"][ind] - dfx["review_subjectivity"][ind])
                if contender_abs > maxabs:
                    maxine = mult, dfx["review_polarity"][ind], dfx["review_subjectivity"][ind], ind
                else:
                    pass
            else:
                pass
        return maxine[3]

    reviews = []
    for iter in range(3):
        val = get_some_reviews(df.loc[df["review_verdict"] == 1])
        reviews.append(get_review_from_index(df, val)[1])
        df = df.drop(df.index[val])
    return(reviews)


if __name__ == "__main__":
    print(get_good_reviews(df.loc[df["spot"] == residences[0]]))
