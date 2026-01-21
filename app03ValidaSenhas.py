# Versão 1: Sem uso de expressões regulares (regex)

import streamlit as st
import random
import string
import re

class AvaliadorSenhas:
    def __init__(self):
        self.tamanho_minimo = 8
        self.tamanho_maximo = 32
        self.tipos = {
            'maiusculas': string.ascii_uppercase,
            'minusculas': string.ascii_lowercase,
            'digitos': string.digits,
            'simbolos': string.punctuation
        }

    def gera_senha_aleatoria(self, tamanho, usaMaiusculas, usaMinusculas, usaDigitos, usaSimbolos): 
        if tamanho < self.tamanho_minimo or tamanho > self.tamanho_maximo:
            raise ValueError(f"Comprimento deve estar entre {self.tamanho_minimo} e {self.tamanho_maximo} caracteres.")
        
        caracteres_validos = ''
        if usaMaiusculas:
            caracteres_validos += self.tipos['maiusculas']
        if usaMinusculas:    
            caracteres_validos += self.tipos['minusculas']
        if usaDigitos:
            caracteres_validos += self.tipos['digitos']
        if usaSimbolos:
            caracteres_validos += self.tipos['simbolos']
        
        if not caracteres_validos:
            raise ValueError("Pelo menos um tipo de caractere deve ser selecionado.")
        
        senha = ''.join(random.choice(caracteres_validos) for _ in range(tamanho))
        return senha

    def valida_senha_informada(self, senha, tamanho, usaMaiusculas, usaMinusculas, usaDigitos, usaSimbolos):
        pontuacao = 0
        
        # Checar comprimento
        if len(senha) >= tamanho:
            pontuacao += 1
            st.success("Comprimento de senha adequado.")
        else:
            st.error(f"A senha deve ter pelo menos {tamanho} caracteres.")
        
        # Checar tipos (sem usar regex)
        if usaMaiusculas:
            # Valida letras maiúsculas COM regex
            if re.search(r'[A-Z]', senha):
            # Valida letras maiúsculas SEM regex    
            # if any(c.isupper() for c in senha):
                pontuacao += 1
                st.success("Senha contém letras maiúsculas.")
            else:
                st.error("A senha deve conter letras maiúsculas.")
        if usaMinusculas:
            # Valida letras minúsculas COM regex
            if re.search(r'[a-z]', senha):
            # Valida letras minúsculas SEM regex    
            # if any(c.islower() for c in senha):
                pontuacao += 1
                st.success("Senha contém letras minúsculas.")
            else:
                st.error("A senha deve conter letras minúsculas.")
        if usaDigitos:
            # Valida digitos numéricos COM regex
            if re.search(r'[\d]', senha):
            # Valida digitos numéricos SEM regex    
            # if any(c.isdigit() for c in senha):
                pontuacao += 1
                st.success("Senha contém números.")
            else:
                st.error("A senha deve conter números.")
        if usaSimbolos:
            # Valida símbolos COM regex
            if re.search(r'[' + re.escape(string.punctuation) + r']', senha):
            # Valida símbolos SEM regex    
            # if any(c in string.punctuation for c in senha):
                pontuacao += 1
                st.success("Senha contém símbolos.")
            else:
                st.error("A senha deve conter símbolos.")

        # Avaliar força da senha
        requisitos = sum([usaMaiusculas, usaMinusculas, usaDigitos, usaSimbolos]) + 1  # +1 para comprimento
        
        if pontuacao == requisitos:
            return "Forte"
        elif pontuacao >= requisitos/2:
            return "Média"
        else:
            return "Fraca"

def main():
    st.title("Gerador e Validador de Senhas")
    
    avaliador = AvaliadorSenhas()
    
    # Opções de configuração
    config = st.container(border=True)
    config.subheader("Critérios de Verificação")
    tamanhoSelecionado = config.slider("Comprimento da senha", 
                                   min_value=avaliador.tamanho_minimo, 
                                   max_value=avaliador.tamanho_maximo, 
                                   value=12)
    col1, col2 = config.columns(2)
    maiusculas = col1.checkbox("Incluir letras maiúsculas", value=True)
    minusculas = col1.checkbox("Incluir letras minúsculas", value=True)
    digitos = col2.checkbox("Incluir números", value=True)
    simbolos = col2.checkbox("Incluir símbolos", value=True)
    
    # Gerador e Validador
    colGerar, colValidar = st.columns(2,border=True)
    # Geração de nova senha
    with colGerar:
        colGerar.subheader("Gerar Nova Senha")
        if colGerar.button("Gerar Senha"):
            try:
                nova_senha = avaliador.gera_senha_aleatoria(tamanhoSelecionado, 
                                                            maiusculas, 
                                                            minusculas, 
                                                            digitos, 
                                                            simbolos)
                colGerar.success(f"Senha gerada: {nova_senha}")
                strength = avaliador.valida_senha_informada(nova_senha, 
                                                            tamanhoSelecionado, 
                                                            maiusculas, 
                                                            minusculas, 
                                                            digitos, 
                                                            simbolos)
                colGerar.info(f"Força da senha: {strength}")
            except ValueError as e:
                colGerar.error(str(e))
    # Validação de senha existente
    with colValidar:
        st.subheader("Validar Senha Informada")
        senha_informada = st.text_input("Insira uma senha para validar")
        if st.button("Validar Senha"):
            if senha_informada:
                strength = avaliador.valida_senha_informada(senha_informada, 
                                                            tamanhoSelecionado, 
                                                            maiusculas, 
                                                            minusculas, 
                                                            digitos, 
                                                            simbolos)
                st.info(f"Força da senha: {strength}")
            else:
                st.error("Por favor, insira uma senha.")

if __name__ == "__main__":
    main()