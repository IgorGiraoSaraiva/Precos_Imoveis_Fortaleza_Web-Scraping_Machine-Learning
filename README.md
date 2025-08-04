# Projeto de Previsão de Preços de Imóveis - Fortaleza
Este projeto realiza uma análise completa do mercado imobiliário de apartamentos na cidade de Fortaleza-CE, construindo um pipeline de ponta a ponta que vai desde a coleta de dados brutos até a criação de uma aplicação web interativa para previsão de preços.

## Objetivo
O objetivo principal é desenvolver um modelo de Machine Learning preciso e interpretável para estimar o valor de venda de um imóvel com base em suas características, como tamanho, localização e número de quartos/banheiros.

## Metodologia e Ferramentas
O projeto foi dividido em 5 etapas principais:
* Web Scraping: Diante da ausência de datasets públicos, os dados foram coletados de um grande portal imobiliário através de automação de navegador com Selenium, superando barreiras de segurança e conteúdo dinâmico.
* Análise Exploratória e Limpeza: Com os dados em mãos, a biblioteca Pandas foi utilizada para um rigoroso processo de limpeza e tratamento. Em seguida, Matplotlib e Seaborn foram usados para visualizar os dados e extrair insights sobre a estrutura do mercado, como a hierarquia de preços dos bairros e as correlações entre as variáveis.
* Engenharia de Features: Para enriquecer o modelo, foram criadas features geoespaciais usando a biblioteca Geopy para calcular a distância de cada imóvel a pontos de interesse da cidade (praias, shoppings, etc.).
* Modelagem e Interpretabilidade: Foram treinados, otimizados (GridSearchCV) e comparados quatro diferentes famílias de modelos de regressão: Regressão Linear, Random Forest, XGBoost e Rede Neural. O modelo campeão (Random Forest Regressor) foi então analisado com a biblioteca SHAP para entender os fatores por trás de suas previsões.
* Aplicação Web: Como produto final, foi desenvolvida uma aplicação interativa com Streamlit, onde o usuário pode inserir as características de um imóvel e receber uma estimativa de preço em tempo real, incluindo uma análise da incerteza da previsão.

## Tecnologias Utilizadas
* Coleta de Dados: Selenium, BeautifulSoup
* Análise de Dados: Pandas, Matplotlib, Seaborn, Geopy
* Modelagem de ML: Scikit-learn, XGBoost, Statsmodels
* Interpretabilidade: SHAP
* Aplicação Web: Streamlit
* Gerenciamento de Dependências: Poetry
