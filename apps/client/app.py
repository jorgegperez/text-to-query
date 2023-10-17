from urllib import parse
import requests
import pandas as pd
import streamlit as st
from styles import css, bot_template

API_URL = "http://localhost:8000"


def genetateLlmResponse(query: str):
    response = requests.get(f"{API_URL}/?query={parse.quote(query, safe='')}", timeout=5000)
    return response.json()


def handle_user_input(query: str):
    st.session_state.chat_history.append(query)
    response = genetateLlmResponse(query)
    st.session_state.chat_history.append(response)
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(
                bot_template.replace("{{MSG}}", message),
                unsafe_allow_html=True,
            )
        else:
            message_type = message["type"]
            message_content = message["message"]
            if message_type == "LIST":
                csv = pd.DataFrame(message_content).to_csv()
                st.download_button(
                    label="Download data as CSV",
                    data=csv,
                    file_name='large_df.csv',
                    mime='text/csv',
                )
            st.write(
                message_content)


def clear_input():
    st.session_state["user_question"] = st.session_state["question_input"]
    st.session_state["question_input"] = ""


def main():
    st.set_page_config(page_title="Pregunta a tu BBDD!", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "question_input" not in st.session_state:
        st.session_state.question_input = ""
    if "user_question" not in st.session_state:
        st.session_state.user_question = ""

    st.header("Pregunta a tu BBDD!")

    st.text_input(
        "Escribe tu pregunta a continuación:",
        key="question_input",
        on_change=clear_input,
    )
    if st.session_state["user_question"]:
        handle_user_input(st.session_state["user_question"])


if __name__ == "__main__":
    main()
