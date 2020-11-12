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
df["review_verdict"] = df.review_verdict.replace({"positive": 1, "negative": 0, "neutral": 0.5})


# make a list of our unique spots
residences = df.spot.unique()


def input_picker():
    print("Please select \n1. Locations\n2. Unique Spots")
    try:
        inp = int(input())
    except ValueError:
        print("Please enter a number")
        exit()
    return None


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
        maxers = []
        for _ in range(3):
            maxine = 0, 0, 0, None
            for ind in dfx.index:
                mult = dfx["review_polarity"][ind] * dfx["review_subjectivity"][ind]
                if maxine[0] < mult:
                    maxine = mult, dfx["review_polarity"][ind], dfx["review_subjectivity"][ind], ind
                elif maxine[0] == mult:
                    maxabs = abs(maxine[1] - maxine[2])
                    contender_abs = abs(dfx["review_polarity"][ind] - dfx["review_subjectivity"][ind])
                    if contender_abs > maxabs:
                        maxine = mult, dfx["review_polarity"][ind], dfx["review_subjectivity"][ind], ind
                    else:
                        pass
                else:
                    pass
            maxers.append(maxine[3])
            print(maxine)
            dfx = dfx.drop(df.index[ind])
            print(len(dfx.index))
        return maxers

    print(len(df.index))
    print(df.loc[df["review_verdict"] == 1])
    pos = get_some_reviews(df.loc[df["review_verdict"] == 1])
    # neg = get_some_reviews(df.loc[df["review_verdict"] == 0])
    return(pos)


if __name__ == "__main__":
    print(get_good_reviews(df.loc[df["spot"] == residences[0]]))

