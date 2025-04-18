import time

import pandas
import streamlit as st
import requests
import selectorlib
import smtplib, ssl
from datetime import datetime
# import panda
# import plotly.express as px
import sqlite3

URL = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


connection = sqlite3.connect("temperature.db")
# cursor = connection.cursor()

def scrape(URL):
    responce = requests.get(URL, headers=HEADERS, timeout=10)
    source = responce.text
    return source

source = scrape(URL)
def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    temperature = extractor.extract(source)['temperatureId']
    return temperature

def store(temperature):
    date = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperature VALUES(?, ?)", (date, temperature))
    connection.commit()



def read():
    cursor = connection.cursor()

    date = cursor.execute("SELECT data FROM temperature")
    date = cursor.fetchall()
    date = [item[0] for item in date]

    temperature = cursor.execute("SELECT temperature FROM temperature")
    temperature = cursor.fetchall()
    temperature = [item[0] for item in temperature]

    rows = [date, temperature]
    return rows


if __name__ == "__main__":
    source = scrape(URL)
    extracted = extract(source)
    store(extracted)
    content = read()

    for date, temperature in zip(content[0], content[1]):
        print(f"{date}: {temperature}")
    time.sleep(2)


# Plotting a figure with Streamlit
# connnection = sqlite3.connect("temperature.db")
# cursor = connection.cursor()
# cursor.execute("SELECT date FROM temperature")
# date = cursor.fetchall()
# date = [item[0] for item in date]

# cursor.execute("SELECT temperature FROM temperature")
# temperature = cursor.fetchall()
# temperature = [item[0] for item in temperature]

# figure = px.line(x=date, y=temperature,
#                  labels={"x": "Date", "y": "Temperature"})





