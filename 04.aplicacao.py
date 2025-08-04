import streamlit as st
import pandas as pd
import joblib
import numpy as np


# --- FUNÇÃO PARA CARREGAR OS ARTEFATOS DE OUTROS NOTEBOOKS ---
# Usamos @st.cache_resource para garantir que o modelo seja carregado apenas uma vez
@st.cache_resource
def load_artifacts():
    print("Carregando artefatos...")
    model = joblib.load('modelo_random_forest.joblib')
    model_columns = joblib.load('model_columns.joblib')
    print("Artefatos carregados.")
    return model, model_columns

# Carrega os artefatos
rf_model, model_columns = load_artifacts()

# Assumindo que a referência era 'Aldeota'. Mude se for outra.
bairros_disponiveis = [col.replace('Bairro_', '') for col in model_columns if 'Bairro_' in col]
bairro_referencia = 'Mondubim' # IMPORTANTE: Coloque aqui o seu bairro de referência real
bairros_disponiveis.insert(0, bairro_referencia)

# --- INTERFACE DO USUÁRIO (UI) COM STREAMLIT ---
st.title('Previsão de Preços de Imóveis em Fortaleza')
st.markdown('---')

# Criação dos inputs na barra lateral
st.sidebar.header('Preencha as Características do Imóvel:')

bairro = st.sidebar.selectbox('Bairro', options=bairros_disponiveis)
tamanho = st.sidebar.slider('Área (m²)', min_value=30, max_value=500, value=100, step=5)
vagas = st.sidebar.selectbox('Vagas de Garagem', options=[0, 1, 2, 3, 4, 5, 6])

# Botão para fazer a previsão
if st.sidebar.button('Estimar Preço'):
    
    # --- PROCESSAMENTO DOS DADOS DE ENTRADA ---
    # 1. Cria um dicionário com os dados do usuário
    user_data = {
        'tamanho (m²)': [tamanho],
        'qtd_vagas': [vagas]
    }
    
    # 2. Converte para DataFrame
    input_df = pd.DataFrame(user_data)
    
    # 3. Adiciona as colunas dummy dos bairros
    # Primeiro, cria uma coluna para o bairro selecionado com o valor 1
    coluna_bairro = f'Bairro_{bairro}'
    if coluna_bairro in model_columns:
        input_df[coluna_bairro] = 1


    # 4. Garante que o DataFrame de entrada tenha exatamente as mesmas colunas que o modelo espera
    #    As colunas que não foram preenchidas (os outros bairros) receberão o valor 0
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    # 5 . Calculando previsão e incerteza

        # --- INCERTEZA ---
    predictions_por_arvore = [tree.predict(input_df) for tree in rf_model.estimators_]
    predictions_array = np.array(predictions_por_arvore)
    media_previsao = np.mean(predictions_array)
    std_previsao = np.std(predictions_array)
    lim_inf = media_previsao - (1.96 * std_previsao)
    lim_sup = media_previsao + (1.96 * std_previsao)
   
    # --- EXIBINDO O RESULTADO ---
    # Valor mais provavel do imóvel
    st.subheader('Valor Estimado do Imóvel:')
    st.markdown(f'# R$ {media_previsao:,.2f}')

    # Intervalo de confiança
    st.subheader('Intervalo de preço do Imóvel:')
    st.markdown(f'O valor do imóvel está entre RS {lim_inf:,.2f} e RS {lim_sup:,.2f}.')

    #Desvio Padrão
    st.info(f'Nível de incerteza:  R$ {std_previsao:,.2f}')
else:
    st.write('Por favor, preencha as características do imóvel na barra lateral e clique em "Estimar Preço".')
