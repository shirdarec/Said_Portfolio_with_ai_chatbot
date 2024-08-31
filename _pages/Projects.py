st.title("Projects")
left_column, right_column = st.columns([1, 1])


with left_column:
    st.markdown("----")
    #st.image(r"images/PortfolioPal.png", width=500)
    st.image("https://media.giphy.com/media/vwBWZO3fWPjV9ZVm2j/giphy.gif", use_column_width=True)
    st.markdown(
        "### AI Powered Portfolio with chatbot - PortfolioPal",
    )
    st.markdown("June-2024")
    st.markdown(
        "<div style='text-align: justify'>"
        "Personal portfolio featuring an AI-powered chatbot built with Streamlit, utilizing advanced prompt engineering techniques like few-shot training for an interactive and intelligent user experience."
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div style='text-align: justify'>"
        "<br>"
        "<a href='https://github.com/shirdarec?tab=repositories'><img src='https://upload.wikimedia.org/wikipedia/commons/a/ad/Link-dynamic-premium.png' width='40'></a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "<a href='https://github.com/shirdarec/Said_Portfolio_with_ai_chatbot'><img src='https://upload.wikimedia.org/wikipedia/commons/c/c2/GitHub_Invertocat_Logo.svg' width='40'></a>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown("----")

    st.image(r"images/paper.jfif", use_column_width=True)
    st.markdown("### Using Machine Learning to Find a Competitive-edge Among Elite Beachvolleyball Players")
    st.markdown("March-2023")
    st.markdown(
        "<div style='text-align: justify'>"
        "The paper is about finding the difference between elite and semi-elite beach volleyball players using a convolutional neural network for classification. Accelerometer data was converted to spectrograms and then fed into the model for analysis. Local Interpretable Model-Agnostic Explanations (LIME) were utilized to interpret the results. These two approaches are a unique contribution to the sport of beach volleyball. With the skilful guidance of our supervisors, we are proud to have achieved significant results and to present our unique contribution to the field."
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div style='text-align: justify'>"
        "<br>"
        "<a href='https://ecp.ep.liu.se/index.php/sais/article/view/999'><img src='https://upload.wikimedia.org/wikipedia/commons/a/ad/Link-dynamic-premium.png' width='40'></a>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown("----")

    st.image(r"images/project1.jpg", use_column_width=True)
    st.markdown("### Developing and optimizing with backtesting")
    st.markdown("Jan-2023")
    st.markdown(
        "<div style='text-align: justify'>"
        "I picked the Bollinger Bands strategy, using the version that Rayner Teo ( famous youtuber in the trading community) used. Using the yfinance library to get data from Yahoo Finance. Implemented the strategy with some tweakble paramteres. I used the plotly library to visualize the trade signals. Then I used backtesting library to further viusalize the results and the statistics. At last I made a table with all the different paramteres I tweaked to optimize the strategy "
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div style='text-align: justify'>"
        "<br>"
        "<a href='https://github.com/shirdarec/Said-Portfolio/blob/main/Project_I-main/BollingerBand_optimized.ipynb'><img src='https://upload.wikimedia.org/wikipedia/commons/c/c2/GitHub_Invertocat_Logo.svg ' width='40'></a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown("----")
with right_column:
    st.markdown("----")
    st.image(
        r"images/project2.jpg",
    )
    st.markdown("### A simple tradingbot trading in Binance")
    st.markdown("March-2023")
    st.markdown(
        "<div style='text-align: justify'>"
        "Connected my binance account and built a clinet API to stream the BTCUSDT currency pair data. Made a dataframe from the live data and transferred it to a sqlite database.Built a simple trend-following strategy.Used the Binance client to execute live trades"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div style='text-align: justify'>"
        "<br>"
        "<a href='https://github.com/shirdarec?tab=repositories'><img src='https://upload.wikimedia.org/wikipedia/commons/a/ad/Link-dynamic-premium.png' width='40'></a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "<a href='https://github.com/shirdarec/Said-Portfolio/blob/main/Project_II-main/tradinbotTest2.ipynb'><img src='https://upload.wikimedia.org/wikipedia/commons/c/c2/GitHub_Invertocat_Logo.svg' width='40'></a>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown("----")

    st.image(r"images/clusters.jpg", use_column_width=True)
    st.markdown("### Modeling Electricity Consumption with Mobility Data : Identifying Opportunities for Localized Energy Markets")
    st.markdown("Dec-2022")
    st.markdown(
        "<div style='text-align: justify'>"
        "Designed and hosted a CTF where players use encryption, hashing, and validation to solve challenges. Participants are provided with RoE and scope, requiring them to apply OSINT, critical thinking, forensic analysis, and cryptographic operations to uncover the key."
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div style='text-align: justify'>"
        "<br>"
        "<a href=' https://drive.google.com/file/d/1022YDSE-Aji2VxyFIEYrtXspFunTDeS-/view?usp=drive_link '><img src='https://upload.wikimedia.org/wikipedia/commons/a/ad/Link-dynamic-premium.png' width='40'></a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown("----")
