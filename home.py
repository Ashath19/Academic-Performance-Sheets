import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import os
import openpyxl
import warnings
warnings.filterwarnings("ignore")
st.set_page_config(page_title="21 Scheme Dashboard", page_icon=":mortar_board:", layout="wide")
st.title(":mortar_board: Welcome to the Academic Performence Sheets of AI&DS Department")
st.sidebar.title("Welcome")
wb = openpyxl.load_workbook(f'pages/DataDump/2022/Datasheet_main.xlsx')
sheets=wb.sheetnames
for i in sheets:
  pd.read_excel(f'pages/DataDump/2022/Datasheet_main.xlsx', sheet_name=i).to_csv(f'pages/DataDump/2022/{i}.csv', index=False)

st.write("Select the batch:")
batch = st.selectbox("Select the Batch",['2021','2022','2023','2024'])
# Read the CSV files
df = pd.read_csv(f'pages/DataDump/{batch}/sgpas.csv')

# Create columns for the layout
col1, col2 = st.columns(2)

# CGPA Section
with col1:
    usns = df['USN'].tolist()
    df['CGPA'] = pd.to_numeric(df['CGPA'], errors='coerce')
    st.subheader("CGPA Graph")
    fig = px.bar(df, x='USN', y='CGPA')
    fig.update_layout(xaxis_title='USN', yaxis_title='CGPA')
    st.plotly_chart(fig, use_container_width=True, height=500)

with col2:
    st.subheader("CGPA Details")
    reference_value = st.selectbox("USN:", usns, key='usn_cgpa_selectbox')
    filtered_data = df[df['USN'] == reference_value]
    st.write("USN: ", filtered_data['USN'].values[0])
    st.write("Name: ", filtered_data['Name'].values[0])
    cgpa_value = filtered_data[f'CGPA'].values[0]
    st.write("CGPA: ", str(round(cgpa_value, 2)))
    

# Subject Details Section
df1 = pd.read_csv(f'pages/DataDump/{batch}/Subjects.csv')
sems = [1, 2, 3, 4, 5, 6, 7, 8]
st.subheader("Semester Details:")
reference_value1 = st.selectbox("Sem:", sems, key='sem_selectbox')
co1, co2 = st.columns(2)

with co1:
    filtered_data1 = df1[df1['Sem'] == reference_value1]
    st.write("Sem: ", str(filtered_data1['Sem'].values[0]))
    df_html = filtered_data1.to_html(index=False)
    st.markdown(df_html, unsafe_allow_html=True)

with co2:
    st.markdown('''SGPA Details''', unsafe_allow_html=True)
    st.write("Sem: ", str(filtered_data1['Sem'].values[0]))
    USN1 = st.selectbox("USN:", usns, key='usn_subject_selectbox')
    filtered_data2 = df[df['USN'] == USN1]
    st.write("Name: ", filtered_data2['Name'].values[0])
    sgpa_value = filtered_data2[f'SGPA.{reference_value1}'].values[0]
    st.write("SGPA: ", str(round(sgpa_value, 2)))
df2=pd.read_csv(f'pages/DataDump/{batch}/Toppers_List.csv')
st.subheader("Topper Details")
c1,c2=st.columns(2)
with c1:
    st.markdown("Semester Topper Details", unsafe_allow_html=True)
    sem1=[1, 2, 3, 4, 5, 6, 7, 8]
    reference_value2 = st.selectbox("Sem:", sem1, key='semtop_selectbox')
    filtered_data3 = df2[df2['Sem'] == reference_value2]
    df_html1 = filtered_data3.to_html(index=False)
    st.markdown(df_html1, unsafe_allow_html=True)
with c2:
    df3=pd.read_csv('pages/DataDump/2022/Year_Toppers.csv')
    st.markdown("Year Topper Details", unsafe_allow_html=True)
    year=[1, 2, 3, 4]
    reference_value3 = st.selectbox("Year:", year, key='yeartop_selectbox')
    filtered_data4 = df3[df3['Year'] == reference_value3]
    df_html2 = filtered_data4.to_html(index=False)
    st.markdown(df_html2, unsafe_allow_html=True)
st.subheader('Backlogs Details:')
c1,c2=st.columns(2)
with c1:
    # Sem selection
    sem2 = [1, 2, 3, 4, 5, 6, 7, 8]
    reference_value4 = st.selectbox("Sem:", sem2, key='semback_selectbox')
    path = f'pages/DataDump/{batch}/{reference_value4}sem.csv'

    # Load the CSV file
    try:
        df4 = pd.read_csv(path)
    except FileNotFoundError:
        st.error(f"File not found: {path}")
        st.stop()

    # USN selection
    USN2 = st.selectbox("USN:", usns, key='usnback_selectbox')

    # Filter data based on USN
    filtered_data5 = df4[df4['USN'] == USN2]


    if not filtered_data5.empty:
        # Get the backlogs column value for the selected USN
        backlogs = filtered_data5['list of backlogs'].values[0]
        st.markdown("Backlogs:", unsafe_allow_html=True)
        
        if pd.isna(backlogs) or backlogs.strip() == '':
            st.write("No Backlogs")
        else:
            st.write(backlogs)
    else:
        st.write("No data available")

with c2:
    st.write("Present Backlogs:")
    
    # Load your DataFrame from CSV
    df5 = pd.read_csv(f'pages/DataDump/{batch}/Backlogs.csv')

    # Convert DataFrame to HTML without the index and add CSS for styling
    df_html3 = df5.to_html(index=False)

    # CSS to ensure the table has a fixed height and enables scrolling
    css = """
    <style>
        .scrollable-table {
            max-height: 400px; /* Adjust the height as needed */
            overflow-y: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
    </style>
    """
    # Combine CSS and HTML and display in Streamlit with a scrollable div
    st.markdown(f'<div class="scrollable-table">{css + df_html3}</div>', unsafe_allow_html=True)
a1,a2=st.columns(2)

with a1:
    st.subheader('CET Details:')
    df6=pd.read_csv(f'pages/DataDump/{batch}/kea.csv')
    srank=str(df6['starting rank'].values[0])
    erank=str(df6['end rank'].values[0])
    st.markdown(f'Max rank accepted: <b>{srank}</b> ', unsafe_allow_html=True)
    st.markdown(f'Lowest rank accepted: <b>{erank}</b> ', unsafe_allow_html=True)

st.caption('''<small>Basic Academic Performance Analyser v1.0  | Jul 2024 </small>''', unsafe_allow_html=True)
st.stop()