import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

LOGGER = get_logger(__name__)

# Load the scores.csv dataset
@st.cache_data
def load_data():
    return pd.read_csv('scores.csv')

def create_histogram(data):
    st.header("Histogram of Exam Scores")
    fig, ax = plt.subplots()
    sns.histplot(data['Exam_Score'], bins=10, kde=True, ax=ax)
    ax.set_xlabel('Exam Scores')
    ax.set_ylabel('Number of Students')
    st.pyplot(fig)

def create_bar_chart(data):
    st.header("Bar Chart of Top 10 Students")
    top_10_students = data.sort_values(by='Exam_Score', ascending=False).head(10)
    fig, ax = plt.subplots()
    ax.bar(top_10_students['Student_Name'], top_10_students['Exam_Score'])
    ax.set_xlabel('Student_Name')
    ax.set_ylabel('Exam Score')
    ax.set_xticklabels(top_10_students['Student_Name'], rotation=45)
    st.pyplot(fig)

def main():
    # Load data
    data = load_data()

    # Title of the app
    st.title("Exam Score Analysis")

    # First Visualization - Histogram of Exam Scores
    create_histogram(data)

    # Second Visualization - Bar Chart of Top 10 Students
    create_bar_chart(data)

if __name__ == "__main__":
    main()
