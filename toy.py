import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

LOGGER = get_logger(__name__)

# Load the toy_dataset.csv dataset
@st.cache_data
def load_data():
    return pd.read_csv('toy_dataset.csv')

def create_histogram(data, column_name):
    st.header(f"Histogram of {column_name}")
    fig, ax = plt.subplots()
    sns.histplot(data[column_name], bins=10, kde=True, ax=ax)
    ax.set_xlabel(column_name)
    ax.set_ylabel('Count of Population')
    st.pyplot(fig)

def create_bar_chart(data, column_name):
    st.header(f"Bar Chart of {column_name} Count")
    count_data = data[column_name].value_counts()
    fig, ax = plt.subplots()
    count_data.plot(kind='bar', ax=ax)
    ax.set_xlabel(column_name)
    ax.set_ylabel('Count of Population')
    st.pyplot(fig)

def main():
    # Load data
    data = load_data()

    # Title of the app
    st.title("Data Visualization")

    # First Visualization - Histogram of Age
    create_histogram(data, 'Age')

    # Second Visualization - Bar Chart of Gender Count
    create_bar_chart(data, 'Gender')

if __name__ == "__main__":
    main()
