Flood Risk Prediction
1. Definição do Problema

Este projeto tem como objetivo prever o risco de enchentes com base em variáveis ambientais. A proposta é auxiliar na análise preventiva de áreas com maior probabilidade de inundação, utilizando técnicas de Machine Learning.

2. Dataset

O dataset utilizado é sintético, gerado com base em variáveis relevantes para a ocorrência de enchentes:

Chuva (mm)
Nível do rio (m)
Saturação do solo (%)
Capacidade de drenagem (%)
Altitude (m)
Urbanização (%)
Temperatura (°C)
Umidade (%)
Velocidade do vento
3. Tratamento e Preparação dos Dados

Os dados foram organizados em formato estruturado, garantindo consistência entre as variáveis de entrada. Foi realizada a separação entre variáveis independentes (features) e variável alvo (target), além da divisão entre dados de treino e teste.

4. Técnicas de Treinamento

Foi utilizado o algoritmo Random Forest Classifier, da biblioteca scikit-learn. O modelo foi treinado com dados rotulados e dividido em conjuntos de treino e teste utilizando train_test_split.

5. Avaliação do Modelo

O modelo foi avaliado utilizando as seguintes métricas:

Accuracy (Acurácia)
Classification Report
Matriz de Confusão

Essas métricas permitem avaliar o desempenho do modelo na classificação dos níveis de risco.

6. Avaliação Visual

Foi gerada uma matriz de confusão para análise visual do desempenho do modelo. Além disso, a aplicação em Streamlit apresenta um gráfico interativo com as variáveis de entrada fornecidas pelo usuário.

7. Tecnologias Utilizadas
Python
Streamlit
Scikit-learn
NumPy
Pandas
Matplotlib
Seaborn
Joblib
8. Como Executar o Projeto

Instalar dependências:

pip install -r requirements.txt

Executar aplicação:

streamlit run app.py

9. Deploy

A aplicação foi publicada utilizando Streamlit Cloud, permitindo acesso via navegador.
