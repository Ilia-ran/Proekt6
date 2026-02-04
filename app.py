import streamlit as st

st.title("Мини формуляр – Тест")

q1 = st.text_input("Коя е столицата на България?")
q2 = st.text_input("В кой континент е България?")
q3 = st.text_input("През коя година е Освобождението на България?")
q4 = st.text_input("Коя река минава през Русе?")
q5 = st.text_input("Кой е авторът на 'Под игото'?")

if st.button("Провери"):
    correct = 0

    if q1.strip().lower() == "софия":
        correct += 1

    if q2.strip().lower() == "европа":
        correct += 1

    if q3.strip().lower() == "1878":
        correct += 1

    if q4.strip().lower() == "дунав":
        correct += 1

    if q5.strip().lower() == "иван вазов":
        correct += 1

    if correct == 5:
        st.success("Всички отговори са верни.")
    else:
        st.error(f"Верни отговори: {correct} от 5")
