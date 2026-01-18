import streamlit as st

class Lancamento:
    def __init__(self, data, tipo, descricao, valor):
        self.data = data
        self.tipo = tipo
        self.descricao = descricao
        self.valor = float(valor)
        
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
        #   {'id':1,
        #    'data': '2023-06-01', 
        #    'tipo': 'receita', 
        #    'descricao': 'Salário', 
        #   'valor': 5000}
            
        # Inicializa dados no session_state (só na primeira execução)
        if 'lancamentos' not in st.session_state:
            #st.session_state.lancamentos = []
            st.session_state.lancamentos = [
                Lancamento('2024-01-05', 'receita', 'Salário', 6000),
                Lancamento('2024-01-10', 'despesa', 'Aluguel', 1500),
                Lancamento('2024-01-15', 'despesa', 'Supermercado', 800),
                Lancamento('2024-01-20', 'receita', 'Freela Projeto X', 1200),
                Lancamento('2024-01-25', 'despesa', 'Conta de Luz', 200)
            ]

        if 'total_receitas' not in st.session_state:
            st.session_state.total_receitas = 0
        if 'total_despesas' not in st.session_state:
            st.session_state.total_despesas = 0

        # configurações da página
        st.set_page_config(
            page_title="Controle Financeiro",
            page_icon="💰",
        )

        # --- Interface do usuário ---

        st.title("Controle Financeiro")
        st.write("Gerenciamento de receitas e despesas usando Streamlit.")

        # Cadastro de lançamentos
        st.subheader("Adicionar Novo Lançamento")
        with st.form(key='form_lancamento', clear_on_submit=True):
            colform1, colform2 = st.columns(2)
            data = colform1.date_input("Data do Lançamento")
            tipo = colform2.selectbox("Tipo de Lançamento", ["receita", "despesa"])
            colform3, colform4 = st.columns(2)
            descricao = colform3.text_input("Descrição")
            valor = colform4.number_input("Valor (R$)", min_value=0.0, format="%.2f")
            botao_submit = st.form_submit_button(label='Adicionar Lançamento')
            if botao_submit:
                st.session_state.lancamentos.append(
                    Lancamento(data.strftime("%Y-%m-%d"), tipo, descricao, valor))        
                st.success("Lançamento adicionado com sucesso!")
                # Atualiza totais
                self.atualizar_totais()
        
        # Métricas gerais
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Total de Receitas", 
                      value=f"R$ {st.session_state.total_receitas:.2f}",
                      border=True)
        with col2:
            st.metric(label="Total de Despesas", 
                      value=f"R$ {st.session_state.total_despesas:.2f}", 
                      border=True)
        with col3:
            st.metric(label="Saldo Atual", 
                      value=f"R$ {st.session_state.total_receitas - st.session_state.total_despesas:.2f}",
                      border=True)

        # exibe lançamentos cadastrados
        self.listar_lancamentos()

        # rodapé
        st.markdown("---")
        st.write("© 2026 Prof. Eduardo Xavier")

    # --- Funções e métodos ---7

    # Atualiza totais de lançamentos
    def atualizar_totais(self):
        st.session_state.total_receitas = 0
        st.session_state.total_despesas = 0
        for lanc in st.session_state.lancamentos:
            if lanc.tipo == 'receita':
                st.session_state.total_receitas += lanc.valor
            else:
                st.session_state.total_despesas += lanc.valor
        # Recarrega a página para atualizar métricas
        st.rerun()

    def listar_lancamentos(self):
        st.subheader("Lançamentos Registrados")
        if not st.session_state.lancamentos:
            st.info("Nenhum lançamento registrado.")
        else:
            st.write(f"Total de Lançamentos registrados: {len(st.session_state.lancamentos)}")
            # exibe lançamentos
            # Usamos enumerate para ter índice de cada item
            for indice, lanc in enumerate(st.session_state.lancamentos):
                colData, colTipo, colDescricao, colValor, colExcluir = st.columns([1, 1, 4, 1, 1])
                colData.write(lanc.data)
                colTipo.write(lanc.tipo.upper())
                colDescricao.write(lanc.descricao)
                colValor.write(f"R$ {lanc.valor:.2f}")
                btExcluir = (colExcluir.button("Excluir", key=f"excluir_{indice}"))
                if btExcluir:
                    # Remove o item pelo índice
                    st.session_state.lancamentos.pop(indice)
                    # Atualiza totais
                    self.atualizar_totais()
                    st.success("Lançamento excluído com sucesso!")

# --- Iniciar a aplicação ---
app = ControleFinanceiro()
