import streamlit as st

st.title("Servidor Streamlit")
st.write("Este é um servidor simples usando Streamlit.")

# menu lateral
st.sidebar.title("Menu")
option = st.sidebar.selectbox("Escolha uma opção:", ["Página 1", "Página 2", "Página 3"])
st.sidebar.write(f"Você selecionou: {option}")
# conteúdo principal
if option == "Página 1":
    st.header("Bem-vindo à Página 1")
    st.write("Conteúdo da Página 1.")
elif option == "Página 2":
    st.header("Bem-vindo à Página 2")
    st.write("Conteúdo da Página 2.")
else:
    st.header("Bem-vindo à Página 3")
    st.write("Conteúdo da Página 3.")
# rodapé
st.markdown("---")
st.write("© 2024 Servidor Streamlit")
