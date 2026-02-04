import streamlit as st

st.title("Мини формуляр")

question = "Коя е столицата на България?"
correct_answer = "София"

user_answer = st.text_input(question)

if st.button("Провери"):
    if user_answer.strip().lower() == correct_answer.lower():
        st.success("Верен отговор.")
    else:
        st.error("Грешен отговор.")
