import streamlit as st

st.title("Formulário de cadastro")

with st.form(key="include_cliente"):
    input_name = st.text_input(label="Insira o seu nome")
    input_age = st.number_input(label="Insira a sua idade", format="%d", step=1)
    input_occupation = st.selectbox("Selecione sua profissao", options=["Desenvolvedor", "Designer", "Professor"])
    input_button_submit = st.form_submit_button("Enviar")

if input_button_submit: