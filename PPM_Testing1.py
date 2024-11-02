New = "sk-rV0oma4o-84YG58iWwgJakp4tnybIL5FW3AOfdtyMFT3BlbkFJK0gifhaVUtfF5I9rg6XZjrcnmFQCy51eR0vI15PvQA"
from httpx import URL, Proxy, Timeout, Response, BaseTransport, AsyncBaseTransport
import streamlit as st
st.set_page_config(layout="wide")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
# background-image: url("https://github.com/Aishamdawood/images/blob/main/2.jpg?raw=true");
# background-size: cover;
# background-position: center center;
# background-repeat: no-repeat;
# background-attachment: local;
background: rgba(0,0,0,0);


}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
content: "Development Environment";

}}

[data-testid="stSidebarNav"] {{
background-image: url("https://github.com/Aishamdawood/images/blob/main/expro%20logo.PNG?raw=true");
content: "Development Environment";
background-repeat: no-repeat;
padding-top: 120px;
background-position: 20px 20px;
background-size: 90% auto;
background-color: dark grey;


            }}
[data-testid="stSidebarNav"]::before {{
content: "Development Environment";
margin-left: 20px;
margin-top: 20px;
font-size: 20px;
position: relative;
top: 100px;
background-color: red;


}}
</style>
"""
import os
import pandas as pd
import streamlit as st
import plotly.express as px
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
import numpy as np
from PIL import Image
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("حالة استخدام: أتمتة التقارير -المتحدث الذكي")

df = pd.DataFrame()
# Create a chat box
chat_input = st.text_input("أكتب استفسارك ليتم الإجابة من بيانات منصة مشروعات")
import os
import pandas as pd

folder_path = '/workspaces/hc-usecase/Data_PPM/'
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

dfs = {}

for i, file in enumerate(files):
    df = pd.read_excel(os.path.join(folder_path, file), header=0, na_values=['NA', 'None'])
    dfs[f'df{i}'] = df
    # st.write(dfs[f'df{i}'])
flag = False
if st.button("Ask"):
    flag = True
import pandas as pd
from pandasai import SmartDatalake
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
file_path = '/contracts.xlsx'

Contracts = pd.read_excel(folder_path+file_path, header=0, na_values=['NA', 'None'])
file_path = '/projects.xlsx'

projects = pd.read_excel(folder_path+file_path, header=0, na_values=['NA', 'None'])

file_path = '/Project_change_requests.xlsx'

Project_change_requests = pd.read_excel(folder_path+file_path, header=0, na_values=['NA', 'None'])

file_path = '/Project_Payment_Plan.xlsx'

Project_Payment_Plan = pd.read_excel(folder_path+file_path, header=0, na_values=['NA', 'None'])

file_path = '/Workflow_schedule.xlsx'

Workflow_schedule = pd.read_excel(folder_path+file_path, header=0, na_values=['NA', 'None'])

file_path = '/programs.xlsx'

programs = pd.read_excel(folder_path+file_path, header=0, na_values=['NA', 'None'])

from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from pandasai.responses.response_parser import ResponseParser
from pandasai.responses.streamlit_response import StreamlitResponse
import matplotlib.pyplot as plt
openai_llm = OpenAI(
api_token=New,
temperature=0.9
)
# Concatenate the DataFrames in the dfs dictionary into a single DataFrame
df_concat = pd.concat(dfs.values(), ignore_index=True)
lake = SmartDatalake([Contracts, projects, Project_change_requests, Project_Payment_Plan, Workflow_schedule, programs], config={"llm": openai_llm})

from deep_translator import GoogleTranslator

# Text to be translated
text = chat_input

# Translate text from English to Arabic
chat_input = GoogleTranslator(source='ar', target='en').translate(text)
# st.write(chat_input)

def translate_text(text):
    try:
        return GoogleTranslator(source='en', target='ar').translate(text)
    except Exception as e:
        return str(e)  # Handle exceptions (e.g., API limits)

# Translate each cell in the DataFrame
# #//////////////////////////////////////
response = lake.chat(chat_input+" as a dataframe")
# response = str(response)
st.subheader("أسئلة مقترحة حسب المعطيات ")

x = lake.chat("generate 5 in Arabic questions similar to : "+chat_input +" as a dataframe")
# x = str(x)
# y = GoogleTranslator(source='en', target='ar').translate(x)
st.write(x)
from pandasai import Agent
# agent = Agent([Contracts, projects, Project_change_requests, Project_Payment_Plan, Workflow_schedule, programs])
# m = agent.explain(chat_input)
# st.write(m)
# response = df.applymap(translate_text)
st.subheader("خطوات ومصادر البيانات لإستخراج النتيجة ")
z = lake.chat("In arabic, list names of columns and how they were used to answer the question: "+chat_input )
st.write(z)
st.subheader("الإجابة إعتمادا على بيانات منصة مشروعات ")

# st.write(response)
column_names = response.columns.tolist()
column_names = [GoogleTranslator(source='en', target='ar').translate(text) for text in column_names]
# st.write(column_names)
response.columns = column_names
st.write(response)
# flag = True
i=0
st.subheader("الرسم البياني التوضيحي ")

with st.form("my_form"):
    # if flag == True:
        i= i+1
        column_names = response.columns.tolist()
        response.columns = column_names
        # Create a selectbox to choose the x-axis column
        x_axis_column = st.selectbox("Select x-axis column", column_names)
        # Create a multiselect to choose the y-axis columns
        y_axis_columns = st.multiselect("Select y-axis columns", column_names, default=column_names[1:])
        # Create a list of chart types
        chart_types = ["Line", "Scatter", "Bar", "Histogram"]
        # Create a selectbox to choose the chart type
        chart_type = st.selectbox("Select chart type", chart_types)
        # Create a Plotly figure based on the selected chart type
        # Display the figure in Streamlit
        st.form_submit_button()
        submitted = st.form_submit_button("Submit"+str(i))
        if submitted:
            if chart_type == "Line":
                fig = px.line(response, x=x_axis_column, y=y_axis_columns)
            elif chart_type == "Scatter":
                fig = px.scatter(response, x=x_axis_column, y=y_axis_columns)
            elif chart_type == "Bar":
                fig = px.bar(response, x=x_axis_column, y=y_axis_columns)
            elif chart_type == "Histogram":
                fig = px.histogram(response, x=x_axis_column)
            st.plotly_chart(fig)


    

