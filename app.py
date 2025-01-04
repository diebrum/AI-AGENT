
import streamlit as st
import plotly.express as px
import pandas as pd

# Title
st.title("Interactive Dashboard with Streamlit and Plotly")

# Description text
st.write("""
This app demonstrates an interactive dashboard created with Streamlit and Plotly.
You can explore the data and interact with the chart below.
""")

# Sample Data
data = {
    "Category": ["A", "B", "C", "D", "E"],
    "Values": [10, 20, 15, 30, 25]
}
df = pd.DataFrame(data)

# Interactive Chart
st.write("### Select a Category")
selected_categories = st.multiselect(
    "Choose categories to display",
    options=df["Category"].tolist(),
    default=df["Category"].tolist()
)

# Filter Data Based on Selection
filtered_df = df[df["Category"].isin(selected_categories)]

# Create Plotly Chart
fig = px.bar(
    filtered_df,
    x="Category",
    y="Values",
    title="Bar Chart of Selected Categories",
    labels={"Values": "Value Count"},
    template="plotly_white"
)

# Display Chart
st.plotly_chart(fig, use_container_width=True)

