import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title='VayuSense - Test Deployment',
    page_icon='🌿',
    layout='wide'
)

st.title("🌿 VayuSense - Deployment Test")
st.write("Testing if basic dependencies work...")

# Test pandas
df = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})
st.write("✅ Pandas and NumPy working")

# Test plotly
fig = px.scatter(df, x='x', y='y', title='Test Plot')
st.plotly_chart(fig)
st.write("✅ Plotly working")

st.success("Basic dependencies are working! The main app should work too.")
