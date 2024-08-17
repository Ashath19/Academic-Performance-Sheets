import streamlit as st
import pandas as pd

st.title("Student Basic Details")
batch='2022'
try:
    df=pd.read_csv(f'pages/DataDump/{batch}/Students_details.csv')
except FileNotFoundError:
    st.error("Data not found. Contact admin.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.stop()
df=pd.read_csv(f'pages/DataDump/{batch}/Students_details.csv')
usns=[x for x in df['USN']]# Get the value from the user as reference
reference_value = st.selectbox("Enter or select an USN:",usns).upper()
# Filter the DataFrame based on the reference value
filtered_data = df[df['USN'] == reference_value]
col1, col2 = st.columns(2)
adar=str(filtered_data['Adhar Number'].values[0])
p_phone=str(filtered_data["Parent's Mobile Number"].values[0])
s_phone=str(filtered_data["Student's Mobile Number"].values[0])
sslc=str(filtered_data['SSLC Marks'].values[0])
puc=str(filtered_data['PUC Marks(PCM)'].values[0])
cet=str(filtered_data['CET Rank'].values[0])
with col1:
    st.write("Name:",filtered_data['Name'].values[0])
    st.write("USN:",filtered_data['USN'].values[0])
    st.write("Date of Birth:",filtered_data['Date of Birth'].values[0])
    st.write("Father's Name:",filtered_data["Father's Name"].values[0])
    if batch=='2022':
        st.write("Mother's Name:",filtered_data["Mother's Name"].values[0])
    st.write("Aadhaar Number:",adar)
    st.write("Address:",filtered_data['Address'].values[0])
    st.write("Parent's Phone Number:",p_phone)
    st.write("Student's Phone Number:",s_phone)
    st.write("Email ID:",filtered_data['Email ID 1'].values[0],",",filtered_data['Email ID 2'].values[0])

with col2:
    st.markdown(f"SSLC Percentage: **{sslc}** %")
    if puc=='nan':
        st.markdown("PUC Percentage (PCM)::red[Not Provided] ")
    else:
        st.markdown(f"PUC Percentage (PCM):**{puc}**%")
    if cet=='nan':
        st.write("CET Rank: **:red[Not Provided]**")
    else:
        st.markdown(f"CET Rank:**{cet}**")
    st.write("Category:",filtered_data['Category'].values[0])
    
st.caption('''<small>Academic Performence Sheet v1.0  | Jul 2024 </small>''', unsafe_allow_html=True)
