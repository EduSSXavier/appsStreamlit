import streamlit as st

class ControleFinanceiro:
    def __init__(self):
        '''
        Controle Financeiro usando Streamlit
        ====================================
        Esta é a classe principal que inicia a aplicação de controle financeiro.
        Ela define a estrutura básica de armazenamento de dados e inicializa a 
        interface do usuário.
        '''
        # --- Armazenamento de dados ---
        # Lista contendo lançamentos de receitas e despesas;
        # Cada item da lista é um dicionário com detalhes de um lançamento financeiro.
        # Exemplo de estrutura de um lançamento:
        #   {'data': '2023-06-01', 
        #    'tipo': 'receita', 
        #    'descricao': 'Salário', 
        #   'valor': 5000}
        self.lancamentos = []

        # --- Interface do usuário ---
        st.title("Controle Financeiro")
        st.write("Gerenciamento de receitas e despesas usando Streamlit.")

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

        # --- Funções e métodos ---
        def adicionar_lancamento(self, lancamento):
            self.lancamentos.append(lancamento)
        def calcular_saldo(self):
            saldo = 0
            for lancamento in self.lancamentos:
                if lancamento['tipo'] == 'receita':
                    saldo += lancamento['valor']
                elif lancamento['tipo'] == 'despesa':
                    saldo -= lancamento['valor']
            return saldo
        def listar_lancamentos(self):
            return self.lancamentos 
        



# --- Iniciar a aplicação ---
app = ControleFinanceiro()
