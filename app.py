import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Google Sheets Access Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("stock-checker-460406-123456abc.json", scope)
client = gspread.authorize(creds)

# Sheet Open karo by URL
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1sHgWUfGsZk1s7w_Xy8UbHoVcsio1fJzdYUPQou5jPa0/edit?gid=0#gid=0").sheet1

# Data lo
data = sheet.get_all_records()
df = pd.DataFrame(data)

# Streamlit UI
st.title("📦 Stock Search")

# 🔍 Search bar only
query = st.text_input("Enter item name or code").strip().lower()

# Filter only if query is given
if query:
    filtered_df = df[df["Item Details"].str.lower().str.contains(query)]

    if not filtered_df.empty:
        st.write(filtered_df)
    else:
        st.warning("❌ No matching item found.")

