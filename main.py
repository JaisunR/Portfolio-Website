import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1 , col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Jaisun Rattu")
    content = """Welcome to my portfolio! My name is Jaisun Rattu and I'm a computer science student. I have always 
    been passionate about technology and its ability to transform the world we live in. Through my coursework and 
    personal projects, I've developed skills in software development, including experience with programming languages 
    such as Python and Java. This portfolio showcases some of my best work and provides an overview of my skills and 
    experience. I'm excited to continue learning and growing in this field, and I look forward to 
    the opportunities that lie ahead. Thank you for visiting my portfolio!"
    """
    st.info(content)

content2 = """
Below you can find some apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])