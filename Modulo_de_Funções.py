from yellowbrick.classifier import ROCAUC
import numpy as np
import pandas as pd
import time
from scipy import stats 

# Bibliotecas gráficas
import matplotlib.pyplot as plt
import seaborn as sns

#Bibliotecas para modelos e predições
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split

# Modelo KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier

#Individual scores
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
#Complete tables
from sklearn.metrics import classification_report
#Confusion matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
#ROC Curve
from sklearn.metrics import roc_curve, auc

# Funções utilizadas para a melhor plotagem e vizualização de valores:

def correlacao_numerica(df):
    '''Com o auxílio do Seaborn, plota uma matriz com todos os valores de correlação
    entre as variavéis numéricas do dataframe escolhido'''
    
    corr = df.corr()
    plot , ax = plt.subplots( figsize =( 12 , 10 ) )
    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )
    plot = sns.heatmap(corr, cmap = cmap,square=True, 
        cbar_kws={ 'shrink' : .9 }, ax=ax, annot = True, 
        annot_kws = { 'fontsize' : 12 })

def plot_ROC_curve(model, xtrain, ytrain, xtest, ytest):

    # Criando visualização da ROC curve para multilabels
    visualizer = ROCAUC(model, encoder={0: 'Funcional', 
                                        1: 'Precisa de ajustes', 
                                        2: 'Abaixo dos padrões',
                                        3:'Não Funcional'},kwargs={'size':20})
                                        
    # Adaptando para termos de teste e treino                               
    visualizer.fit(xtrain, ytrain)
    visualizer.score(xtest, ytest)
    visualizer.show()
    
    return visualizer