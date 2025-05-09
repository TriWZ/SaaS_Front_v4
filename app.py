import requests
import streamlit as st

API_BASE = "https://saas-back-v4.onrender.com"

st.title("Triphorium Dashboard")

# 示例：获取能源数据
response = requests.get(f"{API_BASE}/energy/")
if response.status_code == 200:
    st.json(response.json())
else:
    st.error("Backend not reachable.")
