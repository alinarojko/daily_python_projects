import glob
import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

filepaths = sorted(glob.glob("dairy/*.txt"))
analyzer = SentimentIntensityAnalyzer()
positivity = []
negativity = []
for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores["pos"])
    negativity.append(scores["neg"])
    print(scores)

dates = [name.strip(".txt").strip("diary/") for name in filepaths]
print(dates)

st.title("Dairy Tone")
st.subheader("Positivity")


df = pd.DataFrame({"Date": dates, "Positivity": positivity, "Negativity": negativity})

figure1 = px.line(df, x="Date", y="Positivity", labels={"Date": "Date", "Positivity": "Positivity"})
st.plotly_chart(figure1)
st.subheader("Negativity")
figure2 = px.line(df, x="Date", y="Negativity", labels={"Date": "Date", "Negativity": "Negativity"})
st.plotly_chart(figure2)



