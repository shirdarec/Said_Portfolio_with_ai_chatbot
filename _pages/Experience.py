import reveal_slides as rs

sample_markdown = r"""
# EXPERIENCE
Brief overview of my experience till date.
---


## Equinor
`Data scientist internship - master thesis writing`
</br>
``august 2023 - august 2024``
<div style='text-align: justify'><b>
<li> Used unconventional data sources like Oslo bysykkel data as well as electricty demand data from Statnett and Elvia to model energy consumption.</li><br> 
<li>Did clustering analysis to map out electricty demand and bikeride activity in various zipcodes in Oslo. </li><br> 
<li> Anti-correlation analysis was then performed on clusters and indivdual zipcodes to identify zipcode candiates for a localized energy market and investment opportunties.</li><br>
</b>
</div>
Technologies Used
--
<b>Technologies Used</b><br>
<!-- .slide: data-background-color="#bfc4c9"-->
<div style='text-align: justify'>
Geospatial Analysis,Time-Series Analysis, Energy Systems Knowledge, Data Visualization, Statistical Analysis, machine learning,Large Language Model (LLM), Python,JSON, geoJSON,Jupyter Notebook, Excel
</div>
---
## RITMO and TV2 (UiO)
`Student`
</br>
`Aug-Dec 2023`
<div style='text-align: justify'><b>
<li>Wrote a paper about using machine learning to identify a competitive-edge in elite beach volleyball players in cooperation with RITMO and TV2 </li><br>
<li>Transformed movement data that was gathered by RITMO from time to frequency domain.</li><br> 
<li>Utilizes a CNN model to identify which movements that mostly distingushed elite vs non elite beach volleyabll players. We also used LIME as explainablity tool.</li><br> 
<li>Presented the results in SCAI Symposium 2024 at Jönköping University.</li><br>
</b>
</div>
Technologies Used
--
<b>Technologies Used</b><br>
<!-- .slide: data-background-color="#bfc4c9"-->
<div style='text-align: justify'>
Machine learning, Neural networks, python, LIME, teamwork, reporting

</div>
---
## Digna AS
`Data scienitst/ AI developer volunteer`
</br>
`2023 - now`
<div style='text-align: justify'><b>
<li>Collaborated with the team to implement various automation tools, chatbots and services in a 13-step platform that helps newcomers integrate into Norway.</li><br>
<li>Using various langchain tools to gather analytics on unti testing through agile methodology. </li><br> 
<li> Leading insight meetings with various partners to gather insights about focus groups and brainstorming product ideas.</li><br> 
<br>
</b>
</div>
Technologies Used
--
<b>Technologies Used</b><br>
<!-- .slide: data-background-color="#bfc4c9"-->
<div style='text-align: justify'>
Data Mining, Data Analytics, Langsmith, Langchain, Trubrics, Streamlit, Python/R, Data Visualization, Machine learning algorithms, Automation, AWS Bedrock, API.

</div>

"""
st.title("Experience")
currState = rs.slides(
    sample_markdown,
    theme="",
    height=600,
    config={
        "transition": "slide",
        "width": 400,
        "height": 400,
        "center": True,
        "margin": 0.10,
        "scale_range": [0.1, 3.0],
    },
    initial_state={
        "indexf": -1,
    },
    markdown_props={"data-separator-vertical": "^--$"},
    key="foo",
)
