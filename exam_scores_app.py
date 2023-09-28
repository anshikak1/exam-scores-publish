import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

LOGGER = get_logger(__name__)

# Load the exam_scores.csv dataset
@st.cache_data
def load_data():
    return pd.read_csv('exam_scores.csv')

def create_bar_chart(data):
    st.header("Bar Chart of Top 10 Students")
    top_10_students = data.sort_values(by='Score', ascending=False).head(10)
    fig, ax = plt.subplots()
    ax.bar(top_10_students['Student_Name'], top_10_students['Score'])
    ax.set_xlabel('Student Name')
    ax.set_ylabel('Exam Score')
    ax.set_xticklabels(top_10_students['Student_Name'], rotation=45)
    st.pyplot(fig)

def main():
    # Load data
    data = load_data()

    # Title of the app
    st.title("Exam Score Analysis")

    # Second Visualization - Bar Chart of Top 10 Students
    create_bar_chart(data)

if __name__ == "__main__":
    main()