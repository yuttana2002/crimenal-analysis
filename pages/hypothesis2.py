import streamlit as st

col1, col2, col3 = st.columns([1,2,3])

col1.page_link("main.py", label="หน้าหลัก", )
col2.page_link("pages/hypothesis1.py", label="สมมุติฐานที่ 1", icon="1️⃣")
col3.page_link("pages/hypothesis2.py", label="สมมุติฐานที่ 2", icon="2️⃣", disabled=False)