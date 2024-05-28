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

st.markdown(page_bg_img, unsafe_allow_html=True)

# Rest of your Streamlit code
form1 = st.form("Job Description Form")




# Title of the form
st.header("Enter The Job Description")

# Create a form and each form element inside the form
with st.form(key='job_description_form'):
    uploaded_files = st.file_uploader("Upload CVs", accept_multiple_files=True, type=['pdf', 'doc', 'docx'])
    # Create columns for the input fields and the sliders
    col1, col2= st.columns([30, 7])
    
    # Input fields in the first column
    with col1:
        degree = st.selectbox("Degree:", ["Bachelor", "Master", "PhD"])
        main_skills = st.multiselect("Main Skills:", ["Programming", "Project Management", "Design", "Analysis"])
        certifications = st.selectbox("Certifications:", ["SAS","IFCE","PMP", "CompTIA", "AWS Certified", "Scrum Master"])
        years_of_experience = st.selectbox("Years of Experience:", ["0 to 1", "2 to 5", "6 to 10", "10+"])
        govt_experience = st.radio("Government Experience:", ["Yes", "No"])
        job_title = st.text_input("Job Title:")
        search_term = st.text_input("Search:")

    # Sliders for priority score in the second column
    with col2:
        priority_options = [1, 2, 3, 4, 5]
        degree_priority = st.selectbox("Degree Priority:", priority_options, index=2)
        skills_priority = st.selectbox("Skills Priority:", priority_options, index=2)
        cert_priority = st.selectbox("Certifications Priority:", priority_options, index=2)
        experience_priority = st.selectbox("Experience Priority:", priority_options, index=2)
        govt_exp_priority = st.selectbox("Govt. Experience Priority:", priority_options, index=2)
        title_priority = st.selectbox("Job Title Priority:", priority_options, index=2)

    # Display the value of each slider in the third column
   # File uploader in the fourth column

    # Submit button for the form
    submit_button = st.form_submit_button(label='Submit')

# Check if the form has been submitted
if submit_button:
    st.success("Form Submitted!")
    if uploaded_files:
        st.write(f"Uploaded {len(uploaded_files)} files.")
    # Process the input data or store it as needed

if submit_button:
    st.success("Form Submitted!")

    # Display the content of the Excel file
    try:
        # Read the Excel file
        import pandas as pd
        df = pd.read_excel('Output new3.xlsx', engine='openpyxl')

        # Sort the DataFrame by the 'Score' column (assuming 'Score' is stored as a string like '70%' and needs conversion to float)
        df = df.sort_values(by='Score', ascending=False) # Sort in descend
        df['Score'] = df['Score'] * 100
        df['Score'] = df['Score'].astype(str) + '%'

        st.dataframe(df)
    except Exception as e:
        st.error(f"Failed to read the Excel file: {str(e)}")