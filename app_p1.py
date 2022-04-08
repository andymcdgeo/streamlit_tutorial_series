import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Earthquake Data Explorer')
st.text('This is a web app to allow exploration of Earthquake Data')

upload_file = st.file_uploader('Upload a file containing earthquake data')

if upload_file is not None:
    df = pd.read_csv(upload_file)

    st.header('Statistics of Dataframe')
    st.write(df.describe())

    st.header('Header of Dataframe')
    st.write(df.head())

    st.header('Plot of Data')
    
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Depth'], y=df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')
    
    st.pyplot(fig)