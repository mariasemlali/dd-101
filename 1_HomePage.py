import streamlit as st
st.set_page_config(
    page_title="multipage app",
)
st.title("Main Page")
st.sidebar.success("select a page above.")
st.write("google sheet/gethub with streamlit")
my_input = st.text_input("Input a text here", key="my_input")
if st.button("Submit"):
    st.write('You have entered:', my_input)