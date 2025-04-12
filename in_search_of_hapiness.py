import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In search for happiness")

option_x = st.selectbox("Select the data for the X-acis:  ",
                      ("GDP", "Happiness", "Generosity"))

option_y = st.selectbox("Select the data for the Y-acis:  ",
                      ("GDP", "Happiness", "Generosity"))



df = pd.read_csv("files/happy.csv")

# Add graph chart,import and use plotly.express library
# Match the value for the X-acis
match option_x:
    case "GDP":
        x_array = df["gdp"]
    case "Happiness":
        x_array = df["happiness"]
    case "Generosity":
        x_array = df["generosity"]

# Match the value for the Y-acis
match option_y:
    case "GDP":
        y_array = df["gdp"]
    case "Happiness":
        y_array = df["happiness"]
    case "Generosity":
        y_array = df["generosity"]


# Create a figure , use x, y and name
st.subheader(f"{option_x} and  {option_y}")
figure = px.scatter(x=x_array, y=y_array, labels={"x": option_x, "y": option_y})
st.plotly_chart(figure)



