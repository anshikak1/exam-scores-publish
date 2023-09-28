import runpy
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

data = load_data()

# Title of the app
st.title("Exam Score Analysis")

# First Visualization - Histogram of Exam Scores
st.header("Histogram of Exam Scores")

# Create a histogram using Matplotlib
fig, ax = plt.subplots()
sns.histplot(data['Exam Score'], bins=10, kde=True, ax=ax)
ax.set_xlabel('Exam Scores')
ax.set_ylabel('Number of Students')
st.pyplot(fig)

# Second Visualization - Bar Chart of Top 10 Students
st.header("Bar Chart of Top 10 Students")

# Sort the data by exam scores to find the top 10 students
top_10_students = data.sort_values(by='Exam Score', ascending=False).head(10)

# Create a bar chart using Matplotlib
fig2, ax2 = plt.subplots()
ax2.bar(top_10_students['Student Name'], top_10_students['Exam Score'])
ax2.set_xlabel('Student Name')
ax2.set_ylabel('Exam Score')
ax2.set_xticklabels(top_10_students['Student Name'], rotation=45)
st.pyplot(fig2)

# Third Visualization - Box plot of Exam Scores
st.header("Box Plot of Exam Scores")

# Create a box plot using Seaborn
fig, ax = plt.subplots()
sns.boxplot(data['Exam Score'], ax=ax, orient='v', width=0.2)
ax.set_ylabel('Exam Scores')
st.pyplot(fig)


if __name__ == "__main__":
    runpy()
