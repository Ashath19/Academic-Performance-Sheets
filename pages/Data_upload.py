import streamlit as st
import os
import shutil
def upload_form(file):
    path=os.path.join('pages/DataDump/2022/Datasheet_main.xlsx')
    os.remove(path)
    with open(path, 'wb') as f:
        f.write(file.getbuffer())
def rec():
    shutil.copy(f'pages/DataDump/2022/Datasheet_main.xlsx',f'pages/Recovery_zone/2022/Datasheet_main.xlsx')

st.title("Data Upload Zone")
st.write("Welcome to the uploading section.")

st.write("It is kindly requested thet the data uploading should be done in the predetermined format for the functioning of the website.")
st.markdown("""<p style='color:red;font-weight:bold;'>Download a copy and then edit it.</p>""", unsafe_allow_html=True)
st.markdown("""<p style='color:red;font-weight:bold;'>The uploaded document must be named as 'Datasheet_main.xlsx'.</p>""", unsafe_allow_html=True)
st.markdown("""<p style='color:red;font-weight:bold;'>Verify and submit.</p>""", unsafe_allow_html=True)

try:
    rec()

    with open(f'pages/DataDump/2022/Datasheet_main.xlsx', 'rb') as file:
        data = file.read()
    st.download_button(label="Download the template",data=data,file_name=f"Datasheet_main.xlsx")
    with st.form(key='upload_form'):    
        file = st.file_uploader("Upload file", type=["xlsx"],accept_multiple_files=False,key="file_uploader")   
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            if file is not None:
                upload_form(file)
                st.write("File uploaded successfully.")
            else:
                st.write("Please upload a file.")
    with st.expander("Recovery zone"):
        st.write("Looks like you messd up. No worries, we got you covered.")
        st.write("You can recover the previous version of the uploaded file.")
        with open(f'pages/Recovery_zone/2022/Datasheet_main.xlsx', 'rb') as file:
            data = file.read()
        st.download_button(label="Download the previous version",data=data,file_name=f"Datasheet_main.xlsx")
except FileNotFoundError:
    st.error("Data not found. Contact admin.")
    st.stop()
st.caption('''<small>Academic Performence Sheet v1.0  | Jul 2024 </small>''', unsafe_allow_html=True)
