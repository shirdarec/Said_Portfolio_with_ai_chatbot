import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
st.title("Achivements")
Rage_badge = """
<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="365e7215-70ac-4ce6-8556-45611fb09f47" data-share-badge-host="https://www.credly.com"></div>
<script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
"""
Hope_Badge = """<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="e3b54dd6-1ad7-462d-95ee-75491fb55c2f" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>"""
Keyholders_badge = """<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="0385f6ff-609e-4ed1-9234-fce7dd813a88" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>"""
Azure_fundamentals = """<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="667db6e7-111e-4a71-9028-cfcbb512cdcf" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>"""
# Hackathons section
st.header("📚 Publications")
st.write("**SCAI 2024: https://ecp.ep.liu.se/index.php/sais/article/view/999**")

# Awards section
st.header("🏅 Awards")

# Certifications section
st.header("📜 Certifications")

# Creating a dataframe for certifications
certifications_data = {
    "Vendor": ["Microsoft", "Microsoft", "Udemy" ],
    "Series": ["PL-300T00-A: Microsoft Power BI Data Analyst", "AZ-900 Azure Fundamentals", "The Web Developer Bootcamp 2023"],
    "Awarded": ["Sept/2024", "Oct/2024", "Jan/2023"],
    "Expiration": ["Aug/2025", "Never", "Never"]
}

certifications_df = pd.DataFrame(certifications_data)
st.table(certifications_df)
#Badge Section
st.header("Badges")
col3, col4 = st.columns(2)

with col3:
    components.html(Azure_fundamentals, height=270, width=165)
with col4:
    components.html(Azure_fundamentals, height=270, width=165)
