import streamlit as st
import pandas as pd
import openpyxl
st.title("Student Marks Details")
batch=st.selectbox("Select the Batch",['2021','2022','2023','2024'])
try:
    wb = openpyxl.load_workbook(f'pages/DataDump/{batch}/Datasheet_main.xlsx')
    sheets=wb.sheetnames
    for i in sheets:
        pd.read_excel(f'pages/DataDump/{batch}/Datasheet_main.xlsx', sheet_name=i).to_csv(f'pages/DataDump/{batch}/{i}.csv', index=False)
    semsub=pd.read_csv(f'pages/DataDump/{batch}/semsub.csv')
    hello=st.selectbox("Select the Semester",['1','2','3','4','5','6','7','8'])
    subname,cie,see,total,grade,gradepts,cleared=[],[],[],[],[],[],[]
    sub_df=pd.read_csv(f'pages/DataDump/{batch}/subjects.csv')
    subjects=sub_df[sub_df['Sem']==int(hello)]
    subject={}
    for i in range(0,len(subjects)):
        subject[(subjects.iloc[i,1])] = subjects.iloc[i,2]
    no=semsub[semsub['sem']==int(hello)]['no of subjects'].values[0]
    df=pd.read_csv(f'pages/DataDump/2022/{hello}sem.csv')
    usns=[x for x in df['USN']]# Get the value from the user as reference
    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    usnsel=st.selectbox("Enter or select an USN:",usns).upper()
    filtered_data = df[df['USN'] == usnsel]
    st.markdown(f"<p class='big-font'>Name of the student: {filtered_data['Name'].values[0]}</p>", unsafe_allow_html=True)
    subcode=filtered_data.iloc[0,(3+(no*6+5)):].tolist()
    for i in range(0,len(subcode)):
        subname.append(subject[subcode[i]])
        cie.append(int(filtered_data.iloc[0,(3+(i*6))]))
        see.append(int(filtered_data.iloc[0,(4+(i*6))]))
        total.append(int(filtered_data.iloc[0,(5+(i*6))]))
        gradepts.append(int(filtered_data.iloc[0,(6+(i*6))]))
        grade.append(filtered_data.iloc[0,(7+(i*6))])
        cleared.append(filtered_data.iloc[0,(8+(i*6))])
    final={'Subject Code':subcode,'Subject Name':subname,'CIE':cie,'SEE':see,'Total':total,'Grade':grade,'Grade Points':gradepts,'Cleared':cleared}
    finaldf=pd.DataFrame(final)
    st.markdown(finaldf.style.hide(axis="index").to_html(), unsafe_allow_html=True)
    sgpa=str(filtered_data['SGPA'].values[0])
    st.write("SGPA:",sgpa)
    if pd.isna(filtered_data['list of backlogs'].values[0]):
        st.write("Backlogs: None")
        
    else:
        st.write("Backlogs: ",filtered_data['list of backlogs'].values[0])
    st.write("Note: CIE - Continuous Internal Evaluation, SEE - Semester End Examination")

except FileNotFoundError:
    st.error("Data not found. Contact admin.")
    st.stop()
st.caption('''<small>Academic Performence Sheet v1.0  | Jul 2024 </small>''', unsafe_allow_html=True)
