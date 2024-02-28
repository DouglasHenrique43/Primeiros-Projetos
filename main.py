# Bibliotecas para machine learning e deep learning
import tensorflow as tf
import requests
import tensorflow
from tensorflow.python.keras.layers import Input, Dense
from keras.layers import Dense
import catboost
import xgboost
import lightgbm
from sklearn import datasets, model_selection, metrics
import numpy as np
import pandas as pd
# Visualização de dados
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
# Biblioteca financeira para obter dados de mercado
import yfinance as yf
import scipy
from scipy.stats import norm
import statsmodels.api as sm

# 1º Passo - Importar as bibliotecas (E ENTENDER O QUE CADA UMA VAI FAZER NO PROJETO)
# 2º Passo - juntar o Database Financeiro de dados em tempo real e datasets públicos para dados históricos e macroeconômicos.
# 3º Passo - Importar o Database e tratar ele. (scripts para tratar os dados?).
# 4º Passo - Utilizar os dados para criar tabelas que representam diferentes tipos de dados financeiros.
# 5º Passo - Modelagem e Treinamento da IA:
    # -> Escolha um modelo adequado (por exemplo, LSTM para séries temporais).
    # -> Divida os dados em conjunto de treinamento e teste.
    # -> Alimente os dados no modelo e ajuste os hiperparâmetros.
    # -> Monitore a perda e a precisão durante o treinamento.
# 6º Passo - Avaliação do Modelo:
    # -> Use dados de teste para avaliar o desempenho.
    # -> Calcule métricas como MAE, MSE ou R².
# 7º Passo - Ajustes e Otimização:
    # -> Com base nos resultados da avaliação, ajuste hiperparâmetros e otimize o modelo.
    # -> Experimente diferentes arquiteturas e técnicas.
# 8º Passo - Previsões e Uso em Produção:
    # -> Após treinar o modelo, faça previsões com novos dados.
    # -> Integre o modelo em seu aplicativo ou sistema de produção para uso contínuo.
# 9º Passo - Feedback.




