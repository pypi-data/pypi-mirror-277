# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 00:44:58 2022

@author: User
"""

from sklearn.datasets import make_classification
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from data_science_helper import helper_general as hg
import lightgbm as lgb 
import scikitplot as skplt
import matplotlib.pyplot as plt
from data_science_helper.model import lgb_model as l
import data_science_helper.helper_classification_model as hcm
import math
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import SMOTE
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import RFECV

strategy = "neg_bagging_fraction__lgb_model_2" # Lista de modelo ,"scale_pos_weight__lgb_model" neg_bagging_fraction__lgb_model custom_bagging__lgb_model

metric = "f1" # precision  f1
num_rounds=9999999
early_stop=400 #200
log=0
api="train_api"
random_state=42
n_decimals = 6
max_iter_cls = None

cv= False    
cv_n_split=10 
shuffle_cv=False  # True: StratifiedShuffleSplit, False: StratifiedKFold

enable_umbral_opt = False


specific_url = "E:\\PROYECTOS\\BBVA-Data-Challenge-2023\\data\\processed\\_03_data_integrada\\prueba_2\\1\\X_t.csv"
X_t=pd.read_csv(specific_url, encoding="utf-8")   


#X_t.fillna(0, inplace=True)


ID_P_T = X_t['ID']
y  = X_t['attrition'] 

print(y.value_counts())
                
del X_t['ID'] 
del X_t['attrition']

test_size = hcm.get_test_size(X_t)
#X_t = X_t.round(decimals = n_decimals)

X_train, X_test, y_train, y_test= train_test_split(X_t, y, test_size=test_size,stratify=y,random_state=random_state)


N_p = y_train[y_train==1].count()
N_n = y_train[y_train==0].count()
#T_minimo= 43000
T_minimo = l.get_Total_min_to_train(N_p)
print(N_p)
print(N_n)

#smote = SMOTE(sampling_strategy='minority')
# Aplicar SMOTE a tus datos
#X_resampled, y_resampled = smote.fit_resample(X_train, y_train)



#smote = SMOTE(sampling_strategy='auto', random_state=42)
#X_resampled, y_resampled = smote.fit_resample(X_train, y_train)


params = {
    
        "bagging_fraction": 0.8,
        "feature_fraction": 0.8,
        "bagging_freq":1,
        "lambda_l1": 0,
        "lambda_l2": 0,
        "learning_rate": 0.005,
        "max_bin": 150,
        "max_depth": -1,
        "min_data_in_leaf": 20,
        "min_gain_to_split": 0,
        "num_leaves": 31, #60  proceso anterior
        "path_smooth": 0,
        "lambda_l1":0,
        "verbose":-1
    
}

params.update({"metric":metric})
params.update({"seed":random_state})
params.update({"objective":'binary'})


for T_minimo in [50000,51000,52000,53000,55000]:
        print(f"##################   T_minimo:  {T_minimo}       ############################")
        

        args = {'X_train':X_train, 'y_train': y_train, 'X_test': X_test, 'y_test': y_test, 'params':params,
                "metric":metric,"num_rounds":num_rounds,"early_stop":early_stop,"log":log,"random_state":random_state,"api":api ,"strategy":strategy,
                "url":None,"T_minimo":T_minimo }     

        model ,  y_prob_uno_train, y_prob_uno_test    = l.modelar(**args)

        print(f"##################   model.best_iteration :   {model.best_iteration}       ############################")

        kpis_test = hcm.generar_reporte(model,y_prob_uno_test,X_test,y_test,None,None,True)



#############################


feature_importance = model.feature_importance(importance_type='split')


print(feature_importance)

kpis_train = hcm.generar_reporte(model,y_prob_uno_train,X_train,y_train,None,None,True)

kpis_test = hcm.generar_reporte(model,y_prob_uno_test,X_test,y_test,None,None,True)



params_final = l.get_neg_bagging_fraction_params(y_train,params=params)
print(params_final)
model0 = lgb.LGBMClassifier(params)



# Aplicar SMOTE para generar ejemplos sintéticos
smote = SMOTE(sampling_strategy='auto', random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)



K = 1
N_p = y_train[y_train==1].count()
N_n = y_train[y_train==0].count()

MIN_N_TRAIN = l.get_Total_min_to_train(N_p)

#fn_eval = g.get_fn_eval(score_rs)
#fit_params = l.get_fit_params(X_train,y_train,X_test,y_test,fn_eval)

alpha=(MIN_N_TRAIN-N_p)/(N_n) 
N_n_res = int(round(alpha*N_n,0))

list_model = []

lambda_ = N_p/N_n

T = int(round(math.log(0.05)/math.log(1-K*alpha)))
T,K = l.get_T_reducido(K,alpha)
print("T: ",T,"k:",K)

for i in range(T):
        print("model :",i)

        rus = RandomUnderSampler(random_state=i,sampling_strategy={1:N_p ,0: N_n_res},replacement=False) #majority
        X_res, y_res = rus.fit_resample(X_train, y_train)
        print("total: ",len(y_res),", Class_1: ",y_res[y_res==1].count(),", Class_0: ",y_res[y_res==0].count())