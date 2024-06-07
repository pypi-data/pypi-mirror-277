# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:44:39 2021

@author: User
"""
#import core_helper.helper_general as hg
#hg.set_base_path()

from data_science_helper import helper_general as hg
import shutil
import statistics
import json
import os
import math
import sys
import math
import os
import pandas as pd
import numpy as np
import time
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import lightgbm as lgb 
#import core_helper.helper_plot as hp
#import src.Prj_Core.core_helper.helper_plot as hp
from data_science_helper import helper_plot as hp
import data_science_helper.helper_dataframe as hd

#import model.general as g
#import src.Prj_Core.core_helper.model.general as g
from data_science_helper.model import general as g
from data_science_helper.model import neg_bagging_fraction__lgb_model as nbf_lgb_model
from data_science_helper.model import scale_pos_weight__lgb_model as spw_lgb_model
from data_science_helper.model import custom_bagging__lgb_model as cb_lgb_model
from sklearn.model_selection import StratifiedKFold   
from sklearn.metrics import f1_score

from data_science_helper.model import lgb_model as l

from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score, auc, average_precision_score, confusion_matrix, roc_curve, precision_recall_curve
from numpy import interp
from sklearn.metrics import  roc_auc_score, average_precision_score 
from sklearn.model_selection import  StratifiedShuffleSplit
import seaborn as sns
import shutil
#import src.Prj_Core.core_helper.model.neg_bagging_fraction__lgb_model as nbf_lgb_model
#import src.Prj_Core.core_helper.model.scale_pos_weight__lgb_model as spw_lgb_model
#import src.Prj_Core.core_helper.model.custom_bagging__lgb_model as cb_lgb_model

#import model.neg_bagging_fraction__lgb_model as nbf_lgb_model
#import model.scale_pos_weight__lgb_model as spw_lgb_model
#import model.custom_bagging__lgb_model as cb_lgb_model

def modelar_clasificacion_binaria(strategy="", X_train=None,y_train=None,X_test=None,y_test=None,params=None,max_iter_cls=None,
                                  cls_ini_opt=[] ,enable_cls_opt = False, enable_umbral_opt=False,metric='average_precision',
                                  num_rounds=10000,early_stop=400,log=0,api="train_api",sesgo=0.15,random_state=42,url=None, 
                                  cv=False,cv_n_split=None, print_consola=True,   shuffle_cv=False,  shuffle_cv_test_size=None):
    start = time.time()
    
    if url is not None:        
        #shutil.rmtree(url)
        hg.validar_directorio(url)      
    
    params.update({"metric":metric})
    params.update({"seed":random_state})
    params.update({"objective":'binary'})
            
    args = {'X_train':X_train, 'y_train': y_train, 'X_test': X_test, 'y_test': y_test, 'params':params,
            "metric":metric,"num_rounds":num_rounds,"early_stop":early_stop,"log":log,"random_state":random_state,"api":api ,"strategy":strategy,
            "url":url }     
    
    list_cls_ini = None
    
    if (enable_cls_opt):
        print("----------- INICIO enable_cls_opt = True ---------------------")
        
        list_cls_ini = cls_ini_opt 
        
        list_cls_ini = list(dict.fromkeys(list_cls_ini)) # removiendo duplicados  

        list_cl_to_delete = []
        for COL in list_cls_ini:
     
            if COL not in X_train:   
                print(f" se eliminara la columna {COL} que no existe")                
                list_cl_to_delete.append(COL)
        
                
        list_cls_ini = hd.Diff(list_cls_ini, list_cl_to_delete) 
        
        list_cls = hd.Diff(X_train.columns.tolist(),list_cls_ini) 
        
        #print("list_cls: ", list_cls)
        list_sesgo = []
        last_best_value = 0
        
        for COLUMN in list_cls:            

            
            if max_iter_cls is not None:
            
                if len(list_sesgo)>=max_iter_cls:
                    break
            
            list_cls_ini.append(COLUMN)
            
            X_train_ = X_train.copy()     
            #print("X_train_ : ", X_train_.columns.tolist())
            #print("COLUMN : ", COLUMN)
            #print("list_cls_ini : ", list_cls_ini)
            
            X_train_ = X_train_[list_cls_ini]
            
            X_test_ = X_test.copy()             
            X_test_ = X_test_[list_cls_ini]
            
                    
            args["X_train"]=X_train_
            args["X_test"]=X_test_
            args["url"]=None
    
            model ,  y_prob_uno_train, y_prob_uno_test    = l.modelar(**args)
            
            kpis_train = generar_reporte(model,y_prob_uno_train,X_train,y_train,None,None,print_consola)
        
            kpis_test = generar_reporte(model,y_prob_uno_test,X_test,y_test,None,None,print_consola)
            
            
            f1_train = kpis_train[2]
            f1_test  = kpis_test[2] 
                
            SESGO = f1_train  - f1_test
            
            sesgo_var = {"COLUMN":COLUMN,"DIFF":SESGO,"F1_TRAIN":f1_train,"F1_TEST":f1_test }
            
            if SESGO > sesgo:
                list_cls_ini.remove(COLUMN)
                sesgo_var["SESGO"]=True
                sesgo_var["IMPROVEMENT"]=False
            else:
                sesgo_var["SESGO"]=False
                if f1_test > last_best_value:
                    last_best_value = f1_test
                    sesgo_var["IMPROVEMENT"]=True
                else:
                    list_cls_ini.remove(COLUMN)
                    sesgo_var["IMPROVEMENT"]=False
            print(sesgo_var)     
            list_sesgo.append(sesgo_var)
            
        
        g.save_json(list_sesgo,url+"/resumen_cls_sesgo.json")
        g.save_json(list_cls_ini,url+"/list_cls_sin_sesgo.json")           

                        
        args["X_train"]=X_train[list_cls_ini]
        args["X_test"]=X_test[list_cls_ini]
        args["url"]=url
        
        print("----------- FIN enable_cls_opt = True ---------------------")
        
        
    model ,  y_prob_uno_train, y_prob_uno_test    = l.modelar(**args)
    
    if early_stop is None:
        num_rounds_cv = num_rounds 
    else:
        num_rounds_cv = model.best_iteration
        
  
    if cv : 
        
        if url is None:
            print ("SE NECESITA UNA URL PARA PROCESAR CROSS VALIDATION")
            
        else:
            print("INICIO CROSS VALIDATION: ")
            print(params)
            args_cv = { 'X_train':X_train, 'y_train': y_train, 'X_test': X_test, 'y_test': y_test, 'params':params,
                        "metric":metric,"num_rounds":num_rounds_cv,"random_state":random_state,
                        "api":api , "url":url , "cv_n_split" :cv_n_split, "shuffle_cv" :shuffle_cv,
                        "shuffle_cv_test_size" :shuffle_cv_test_size,
                        }      
            
            generate_cv_result(**args_cv)    

    else:
        path_cv = os.path.join(url,"cv")  
        if os.path.isdir(path_cv)==True:
            shutil.rmtree(path_cv) 

    kpis_train = generar_reporte(model,y_prob_uno_train,X_train,y_train,None,None,print_consola)
    
    kpis_test = generar_reporte(model,y_prob_uno_test,X_test,y_test,None,url,print_consola)
    
        

    umbral_opt=0
    kpis_opt = (0,0,0,0,0,0,0,0)
    
    if enable_umbral_opt:
        umbral_opt = g.get_opt_threshold(y_test,y_prob_uno_test)   
        kpis_opt = generar_reporte(model,y_prob_uno_test,X_test,y_test,umbral_opt,None,print_consola)
    
    print("Time elapsed: ", time.time() - start)
    
    return model ,  kpis_train, kpis_test , kpis_opt , umbral_opt , list_cls_ini



def generate_cv_result(X_train=None,y_train=None,X_test=None,y_test=None,api=None, num_rounds = None , metric=None, 
                       params =None ,  url=None, shuffle_cv = False ,shuffle_cv_test_size=None, cv_n_split=None,
                       random_state=42):
    
   print(X_train.shape)
   X_t_ = X_train.append(X_test)
   y_ = y_train.append(y_test)
   
   if shuffle_cv:
       folds = StratifiedShuffleSplit(n_splits=cv_n_split, test_size=shuffle_cv_test_size, random_state=random_state)
       print("StratifiedShuffleSplit")
   else:
   
       if cv_n_split is None:
           test_size = get_test_size(X_t_)
           n_s = round(1/test_size)
       else:
           n_s = cv_n_split      
         
       print("StratifiedKFold")
       folds = StratifiedKFold(n_splits=n_s, shuffle=True, random_state=random_state) 
   print("##########################################")
   print("params: : ", params)
   print("num_rounds_cv : ",num_rounds)
   print("##########################################")

   path_cv = os.path.join(url,"cv")  
   hg.validar_directorio(path_cv)  
   
   i = 0   
   for train_idx, valid_idx in folds.split(X_t_, y_):
       
       X_train_cv, y_train_cv  = X_t_.iloc[train_idx], y_.iloc[train_idx]
       X_valid_cv , y_valid_cv = X_t_.iloc[valid_idx], y_.iloc[valid_idx]
       
       args_cv = { 'X_train':X_train_cv, 'y_train': y_train_cv, 'X_test': X_valid_cv, 'y_test': y_valid_cv, 'params':params,
                   "metric":metric,"num_rounds":num_rounds,"early_stop":None,"log":0,"random_state":random_state,"api":api ,
                   "strategy":None, "url":None }  
       
       model_cv ,  y_prob_uno_train_cv, y_prob_uno_test_cv    = l.modelar(**args_cv)
       
       path_cv_test_filename = os.path.join(path_cv, f"y_test_cv_{i}.csv")      
       df_ = pd.DataFrame()
       df_["y_test_cv"] = y_valid_cv
       df_["y_prob_uno_test_cv"] = y_prob_uno_test_cv  
       df_.to_csv(path_cv_test_filename,index=False)  
       
   
       path_cv_train_filename = os.path.join(path_cv, f"y_train_cv_{i}.csv") 
       df_ = pd.DataFrame()
       df_["y_train_cv"] = y_train_cv
       df_["y_prob_uno_train_cv"] = y_prob_uno_train_cv       
       df_.to_csv(path_cv_train_filename,index=False)     
          
       i += 1 
       
             

def kpis_cross_validation(list_path=[], n_splits=5,url_out=None,postfix=""):
  
     

    list_train_filtracion = [] 
    list_train_subcobertura = [] 
    
    list_train_specificity = []    
    list_train_precision = []
    list_train_recall = []
    list_train_f1 = []
    list_train_average_precision = []
    list_train_roc_auc = []
    
    list_valid_filtracion = [] 
    list_valid_subcobertura = [] 
    
    list_valid_specificity = []
    list_valid_precision = []
    list_valid_recall = []
    list_valid_f1 = []
    list_valid_average_precision = []
    list_valid_roc_auc = []
    
    
    

    
    for i in range(n_splits):
        
       df_cv_fold = pd.DataFrame()           
       for path_ in list_path:
           print(" path_ :  ", path_)   
           df_cv_fold_ = pd.read_csv(f"{path_}/y_train_cv_{i}.csv", index_col=False)
           df_cv_fold = df_cv_fold.append(df_cv_fold_)
           
       y_train_cv = df_cv_fold.y_train_cv
       y_prob_uno_train_cv = df_cv_fold.y_prob_uno_train_cv       
       y_pred_train_cv = np.round(y_prob_uno_train_cv, 0)
       
       precision_train, recall_train, f1_train, support_train = precision_recall_fscore_support(y_train_cv, y_pred_train_cv ,average="binary",pos_label=1)
       train_average_precision = average_precision_score(y_train_cv, y_prob_uno_train_cv)      
       roc_auc_train = roc_auc_score(y_train_cv, y_prob_uno_train_cv) 
       
       filtracion_train = 1 - precision_train
       list_train_filtracion.append(filtracion_train)
       subcobertura_train = 1 - recall_train
       list_train_subcobertura.append(subcobertura_train)
       
       cm1 = confusion_matrix(y_train_cv,y_pred_train_cv)
       #total1=sum(sum(cm1))
       specificity_train = cm1[0,0]/(cm1[0,0]+cm1[0,1])       
    
       list_train_specificity.append(specificity_train)
        
       list_train_precision.append(precision_train)
       list_train_recall.append(recall_train)
       list_train_f1.append(f1_train)
       list_train_average_precision.append(train_average_precision)
       list_train_roc_auc.append(roc_auc_train)
       
       
       df_cv_fold = pd.DataFrame()           
       for path_ in list_path:
           print(" path_ :  ", path_)   
           df_cv_fold_ = pd.read_csv(f"{path_}/y_test_cv_{i}.csv", index_col=False)
           df_cv_fold = df_cv_fold.append(df_cv_fold_)      
        
       y_test_cv = df_cv_fold.y_test_cv
       y_prob_uno_test_cv = df_cv_fold.y_prob_uno_test_cv       
       y_pred_valid_cv = np.round(y_prob_uno_test_cv, 0)
       
       precision_test, recall_test, f1_test, support_test = precision_recall_fscore_support(y_test_cv, y_pred_valid_cv ,average="binary",pos_label=1)
       valid_average_precision = average_precision_score(y_test_cv, y_prob_uno_test_cv)      
       roc_auc_valid = roc_auc_score(y_test_cv, y_prob_uno_test_cv) 
       
              
       filtracion_valid = 1 - precision_test
       list_valid_filtracion.append(filtracion_valid)
       subcobertura_valid = 1 - recall_test
       list_valid_subcobertura.append(subcobertura_valid)
       
       cm11 = confusion_matrix(y_test_cv,y_pred_valid_cv)
       specificity_valid = cm11[0,0]/(cm11[0,0]+cm11[0,1])
       
       list_valid_specificity.append(specificity_valid)
               
       list_valid_precision.append(precision_test)
       list_valid_recall.append(recall_test)
       list_valid_f1.append(f1_test)
       list_valid_average_precision.append(valid_average_precision)
       list_valid_roc_auc.append(roc_auc_valid)
       
          
    mean_valid_subcobertura = statistics.mean(list_valid_subcobertura) 
    std_valid_subcobertura = statistics.pstdev(list_valid_subcobertura)
    min_valid_subcobertura = min(list_valid_subcobertura)           
    max_valid_subcobertura = max(list_valid_subcobertura)      
    mean_train_subcobertura = statistics.mean(list_train_subcobertura) 
    std_train_subcobertura = statistics.pstdev(list_train_subcobertura)
    min_train_subcobertura = min(list_train_subcobertura)           
    max_train_subcobertura = max(list_train_subcobertura)      
   
    mean_valid_filtracion = statistics.mean(list_valid_filtracion) 
    std_valid_filtracion = statistics.pstdev(list_valid_filtracion)
    min_valid_filtracion = min(list_valid_filtracion)           
    max_valid_filtracion = max(list_valid_filtracion)      
    mean_train_filtracion = statistics.mean(list_train_filtracion) 
    std_train_filtracion = statistics.pstdev(list_train_filtracion)
    min_train_filtracion = min(list_train_filtracion)           
    max_train_filtracion = max(list_train_filtracion)     

    mean_valid_specificity = statistics.mean(list_valid_specificity) 
    std_valid_specificity = statistics.pstdev(list_valid_specificity)
    min_valid_specificity = min(list_valid_specificity)           
    max_valid_specificity = max(list_valid_specificity)      
    mean_train_specificity = statistics.mean(list_train_specificity) 
    std_train_specificity = statistics.pstdev(list_train_specificity)
    min_train_specificity = min(list_train_specificity)           
    max_train_specificity = max(list_train_specificity)     

    mean_valid_precision = statistics.mean(list_valid_precision)           
    std_valid_precision = statistics.pstdev(list_valid_precision)
    min_valid_precision = min(list_valid_precision)           
    max_valid_precision = max(list_valid_precision)      
    mean_train_precision = statistics.mean(list_train_precision)           
    std_train_precision = statistics.pstdev(list_train_precision)
    min_train_precision = min(list_train_precision)           
    max_train_precision = max(list_train_precision)  
    
    
    mean_valid_recall = statistics.mean(list_valid_recall)           
    std_valid_recall = statistics.pstdev(list_valid_recall)
    min_valid_recall = min(list_valid_recall)           
    max_valid_recall = max(list_valid_recall)    
    mean_train_recall = statistics.mean(list_train_recall)           
    std_train_recall = statistics.pstdev(list_train_recall)
    min_train_recall = min(list_train_recall)           
    max_train_recall = max(list_train_recall) 
    
    
    mean_valid_f1 = statistics.mean(list_valid_f1)           
    std_valid_f1 = statistics.pstdev(list_valid_f1)
    min_valid_f1 = min(list_valid_f1)           
    max_valid_f1 = max(list_valid_f1)       
    mean_train_f1 = statistics.mean(list_train_f1)           
    std_train_f1 = statistics.pstdev(list_train_f1)   
    min_train_f1 = min(list_train_f1)           
    max_train_f1 = max(list_train_f1)   
    

    mean_valid_average_precision = statistics.mean(list_valid_average_precision) 
    std_valid_average_precision = statistics.pstdev(list_valid_average_precision)
    min_valid_average_precision = min(list_valid_average_precision)           
    max_valid_average_precision = max(list_valid_average_precision)     
    mean_train_average_precision = statistics.mean(list_train_average_precision) 
    std_train_average_precision = statistics.pstdev(list_train_average_precision) 
    min_train_average_precision = min(list_train_average_precision)           
    max_train_average_precision = max(list_train_average_precision)     
    
    
    mean_valid_roc_auc = statistics.mean(list_valid_roc_auc)           
    std_valid_roc_auc = statistics.pstdev(list_valid_roc_auc)
    min_valid_roc_auc = min(list_valid_roc_auc)           
    max_valid_roc_auc = max(list_valid_roc_auc)    
    mean_train_roc_auc = statistics.mean(list_train_roc_auc)           
    std_train_roc_auc = statistics.pstdev(list_train_roc_auc)
    min_train_roc_auc = min(list_train_roc_auc)           
    max_train_roc_auc = max(list_train_roc_auc)  

    
    result_kpis = [
                   {"Métrica":"Precisión","Splits":n_splits,"Datos":"Validación","Promedio":mean_valid_precision,"SD":std_valid_precision,"Min":min_valid_precision,"Max":max_valid_precision},
                   {"Métrica":"Precisión","Splits":n_splits,"Datos":"Entrenamiento","Promedio":mean_train_precision,"SD":std_train_precision,"Min":min_train_precision,"Max":max_train_precision},
                   
                   {"Métrica":"Sensibilidad","Splits":n_splits,"Datos":"Validación","Promedio":mean_valid_recall,"SD":std_valid_recall,"Min":min_valid_recall,"Max":max_valid_recall},
                   {"Métrica":"Sensibilidad","Splits":n_splits,"Datos":"Entrenamiento","Promedio":mean_train_recall,"SD":std_train_recall,"Min":min_train_recall,"Max":max_train_recall},
    
                   {"Métrica":"Especificidad","Splits":n_splits,"Datos":"Validación","Promedio":mean_valid_specificity,"SD":std_valid_specificity,"Min":min_valid_specificity,"Max":max_valid_specificity},               
                   {"Métrica":"Especificidad","Splits":n_splits,"Datos":"Entrenamiento","Promedio":mean_train_specificity,"SD":std_train_specificity,"Min":min_train_specificity,"Max":max_train_specificity},               
                                       
                   {"Métrica":"F1","Splits":n_splits,"Datos":"Validación","Promedio":mean_valid_f1,"SD":std_valid_f1,"Min":min_valid_f1,"Max":max_valid_f1},
                   {"Métrica":"F1","Splits":n_splits,"Datos":"Entrenamiento","Promedio":mean_train_f1,"SD":std_train_f1,"Min":min_train_f1,"Max":max_train_f1},
    
                   {"Métrica":"PR AUC","Splits":n_splits,"Datos":"Validación","Promedio":mean_valid_average_precision,"SD":std_valid_average_precision,"Min":min_valid_average_precision,"Max":max_valid_average_precision},
                   {"Métrica":"PR AUC","Splits":n_splits,"Datos":"Entrenamiento","Promedio":mean_train_average_precision,"SD":std_train_average_precision,"Min":min_train_average_precision,"Max":max_train_average_precision},
    
                   {"Métrica":"ROC AUC","Splits":n_splits,"Datos":"Validación","Promedio":mean_valid_roc_auc,"SD":std_valid_roc_auc,"Min":min_valid_roc_auc,"Max":max_valid_roc_auc},
                   {"Métrica":"ROC AUC","Splits":n_splits,"Datos":"Entrenamiento","Promedio":mean_train_roc_auc,"SD":std_train_roc_auc,"Min":min_train_roc_auc,"Max":max_train_roc_auc},               
                  
                   {"Métrica":"Filtración ","Splits":n_splits,"Datos":"Validación","Promedio":mean_valid_filtracion,"SD":std_valid_filtracion,"Min":min_valid_filtracion,"Max":max_valid_filtracion},
                   {"Métrica":"Filtración ","Splits":n_splits,"Datos":"Entrenamiento","Promedio":mean_train_filtracion,"SD":std_train_filtracion,"Min":min_train_filtracion,"Max":max_train_filtracion},               
                 
                   {"Métrica":"Subcobertura  ","Splits":n_splits,"Datos":"Validación","Promedio":mean_valid_subcobertura,"SD":std_valid_subcobertura,"Min":min_valid_subcobertura,"Max":max_valid_subcobertura},
                   {"Métrica":"Subcobertura ","Splits":n_splits,"Datos":"Entrenamiento","Promedio":mean_train_subcobertura,"SD":std_train_subcobertura,"Min":min_train_subcobertura,"Max":max_train_subcobertura},               
                  
                  ]
    
    df = pd.DataFrame(result_kpis)
    
    if url_out is None:
        return df
    else:
        df.to_excel(url_out+f"kpis_cross_validation_{postfix}.xlsx")  
 
 

def roc_curva_cross_validation(list_path=[], n_splits=5,url_out=None,postfix=""):
    
    tprs = []
    aucs = []
    mean_fpr = np.linspace(0, 1, 100)

    #list_path = ["CV","CV2"]
    
       
    for i in range(n_splits):   
        
       df_cv_fold = pd.DataFrame()   
        
       for path_ in list_path:
           #print(" path_ :  ", path_)
           df_cv_fold_ = pd.read_csv(f"{path_}/y_test_cv_{i}.csv", index_col=False)
           df_cv_fold = df_cv_fold.append(df_cv_fold_)
           
       y_test_cv = df_cv_fold.y_test_cv
       y_prob_uno_test_cv = df_cv_fold.y_prob_uno_test_cv
       
       fpr, tpr, thresholds = roc_curve(y_test_cv, y_prob_uno_test_cv)
       tprs.append(interp(mean_fpr, fpr, tpr))
       tprs[-1][0] = 0.0
       roc_auc = auc(fpr, tpr)
       aucs.append(roc_auc)
       #plt.plot(fpr, tpr, lw=1, alpha=0.3, label='ROC fold %d (AUC = %0.2f)' % (i, roc_auc))
       i += 1  
    
    #print("df_cv_fold.shape: ", df_cv_fold.shape)
    plt.plot([0, 1], [0, 1], linestyle='--', lw=1, color='r', label='Línea de base', alpha=.8)  
   
    mean_tpr = np.mean(tprs, axis=0)
    mean_tpr[-1] = 1.0
    mean_auc = auc(mean_fpr, mean_tpr)
    std_auc = np.std(aucs)
    plt.plot(mean_fpr, mean_tpr, color='b',label=r'Media ROC (AUC = %0.2f $\pm$ %0.2f)' % (mean_auc, std_auc),lw=1, alpha=.8)
   
    std_tpr = np.std(tprs, axis=0)
    tprs_upper = np.minimum(mean_tpr + std_tpr, 1)
    tprs_lower = np.maximum(mean_tpr - std_tpr, 0)
    plt.fill_between(mean_fpr, tprs_lower, tprs_upper, color='grey', alpha=.5, label=r' std. dev.')

    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('Tasa de falsos positivos')
    plt.ylabel('Tasa de verdaderos positivos')  
    plt.title(f"Curva ROC (n_splits:{n_splits})")
    plt.legend(loc="lower right")
    #plt.show()
    
    if url_out is None:
        plt.show()
    else:
        hg.validar_directorio(url_out)  
        plt.savefig(url_out+f'roc_curva_cv_{postfix}.png', bbox_inches='tight')
        plt.close()





def pr_curva_cross_validation(list_path=[], n_splits=5,url_out=None,postfix=""):

    
    y_real = []
    y_proba = []
       
    for i in range(n_splits):   
        
       df_cv_fold = pd.DataFrame()   
        
       for path_ in list_path:
           #print(" path_ :  ", path_)
           df_cv_fold_ = pd.read_csv(f"{path_}/y_test_cv_{i}.csv", index_col=False)
           df_cv_fold = df_cv_fold.append(df_cv_fold_)
                  
           
       y_test_cv = df_cv_fold.y_test_cv
       y_prob_uno_test_cv = df_cv_fold.y_prob_uno_test_cv       
       
       precision, recall, _ = precision_recall_curve(y_test_cv, y_prob_uno_test_cv)
             
       
       #plt.plot(recall, precision, lw=1, alpha=0.3,  label='PR fold %d (AUC = %0.2f)' % (i, average_precision_score(y_test_cv, y_prob_uno_test_cv)))
       plt.plot(recall, precision, lw=1, alpha=0.3)
       
       #plt.legend(loc="lower right")
       #plt.gca().get_legend().remove()
       
       y_real.append(y_test_cv)
       y_proba.append(y_prob_uno_test_cv)
       

       i += 1  
    
    y_real = np.concatenate(y_real)
    y_proba = np.concatenate(y_proba)    
    
    precision, recall, _ = precision_recall_curve(y_real, y_proba)
    plt.plot(recall, precision, color='b',label=r'Precisión-Recall (AUC = %0.2f)' % (average_precision_score(y_real, y_proba)), lw=2, alpha=.8)
    
    baseline = len(y_real[y_real==1]) / len(y_real)
    #baseline = 0.2
    #print(baseline)
    plt.plot([0, 1], [baseline, baseline], linestyle='--', label=r'Línea de base = %0.2f' %(baseline))
    
    #https://stats.stackexchange.com/questions/34611/meanscores-vs-scoreconcatenation-in-cross-validation

    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('Recall (Sensibilidad) ')
    plt.ylabel('Precisión')  
    plt.title(f"Curva Precisión-Recall (n_splits:{n_splits})")
    plt.legend(loc="upper right")
    #plt.gca().get_legend().remove()
    #plt.show()
    
    if url_out is None:
        plt.show()
    else:
        hg.validar_directorio(url_out)  
        plt.savefig(url_out+f'pr_curva_cv_{postfix}.png', bbox_inches='tight')
        plt.close()






def get_umbral_opt(list_path=[], n_splits=5,url_out=None,postfix="",intervalo = 0.001):

    
    y_real = []
    y_proba = []
       
    #opt_list = []
    
    for i in range(n_splits):   
        
       df_cv_fold = pd.DataFrame()   
        
       for path_ in list_path:
           #print(" path_ :  ", path_)
           df_cv_fold_ = pd.read_csv(f"{path_}/y_test_cv_{i}.csv", index_col=False)
           df_cv_fold = df_cv_fold.append(df_cv_fold_)
                  
           
       y_test_cv = df_cv_fold.y_test_cv
       y_prob_uno_test_cv = df_cv_fold.y_prob_uno_test_cv       
       
       
       y_real.append(y_test_cv)
       y_proba.append(y_prob_uno_test_cv)
       
       #umbral_opt = g.get_opt_threshold(y_test_cv,y_prob_uno_test_cv,intervalo=intervalo) 
       #print(umbral_opt)
       #opt_list.append(umbral_opt)
       

       i += 1  
    
    y_real = np.concatenate(y_real)
    y_proba = np.concatenate(y_proba)    
    
    umbral_opt = g.get_opt_threshold(y_real,y_proba,intervalo=intervalo)  
    
    #return umbral_opt , opt_list
    return umbral_opt




def distribucion_cross_validation(list_path=[], n_splits=5,url_out=None,postfix=""):

    
    y_real = []
    y_proba = []
       
    for i in range(n_splits):   
        
       df_cv_fold = pd.DataFrame()   
        
       for path_ in list_path:
           print(" path_ :  ", path_)
           df_cv_fold_ = pd.read_csv(f"{path_}/y_test_cv_{i}.csv", index_col=False)
           df_cv_fold = df_cv_fold.append(df_cv_fold_)
                  
           
       y_test_cv = df_cv_fold.y_test_cv
       y_prob_uno_test_cv = df_cv_fold.y_prob_uno_test_cv       
       

       y_real.append(y_test_cv)
       y_proba.append(y_prob_uno_test_cv)       

       i += 1  
       
    

    
    y_real = np.concatenate(y_real)
    y_proba = np.concatenate(y_proba)   
    
    
    sns.distplot(y_proba , hist = False, kde = True, 
                 color = 'darkblue', 
                 kde_kws={'linewidth': 3},
                 rug_kws={'color': 'black'})
    

    #plt.xlim([-0.05, 1.05])
    #plt.ylim([-0.05, 1.05])

    
    
    plt.title('Densidad de Kernel de la probabilidad estimada')
    plt.xlabel('Probabilidad Estimada')
    plt.ylabel('Densidad')
    
    #plt.gca().get_legend().remove()
    #plt.show()
    
    if url_out is None:
        plt.show()
    else:
        hg.validar_directorio(url_out)  
        plt.savefig(url_out+f'pr_curva_cv_{postfix}.png', bbox_inches='tight')
        plt.close()


def modelar_clasificacion_binaria_rscv(strategy, X_train,y_train=None,X_test=None,y_test=None,score_rs=None,params=None,param_dist=None, n_iter=None,n_jobs=None,url=None,print_consola=True):
    if url is not None:
        hg.validar_directorio(url)     

    if (strategy=="neg_bagging_fraction__lgb_model"):
        results, model , predicted_probas, params, best_params = nbf_lgb_model.modelar_rscv(X_train,y_train,X_test,y_test,score_rs,params,param_dist,n_iter,n_jobs,url)
        
    if (strategy=="scale_pos_weight__lgb_model"):
        results, model , predicted_probas, params, best_params = spw_lgb_model.modelar_rscv(X_train,y_train,X_test,y_test,score_rs,params,param_dist,n_iter,n_jobs,url)
       
    if (strategy=="custom_bagging__lgb_model"):
        results, model , predicted_probas, params, best_params = spw_lgb_model.modelar_rscv(X_train,y_train,X_test,y_test,score_rs,params,param_dist,n_iter,n_jobs,url)
       
    kpis = generar_reporte(model,predicted_probas,X_test,y_test,url,print_consola)
    
    return results, model , predicted_probas, params, best_params ,kpis
    

def generar_reporte(model,y_prob_uno, X_test, y_test,umbral_opt,url,print_consola): 
    
     
    kpis = hp.print_kpis_rendimiento_modelo(y_test,y_prob_uno,umbral_opt,url,print_consola)   
    '''
    if  isinstance(model, list)==False:
        if (print_consola):
            hp.print_shap_plot(model, X_test, url)   
    '''
    g.generate_summary_evaluation(X_test,y_prob_uno,y_test,url) 
    
    
    
    return kpis



    
    
def predecir_clasificacion_binaria(model, X=None, umbral=0.5):
    print("inicio predecir_clasificacion_binaria")
    
    if type(model)==lgb.basic.Booster:
        y_prob_uno = model.predict(X, num_iteration=model.best_iteration)      
        
    elif  isinstance(model, list)==False:    
        predicted_probas = model.predict_proba(X)
        y_prob_uno = predicted_probas[:,1]
    else:
        print("modelo es una lista")
        y_pred,y_prob_uno , predicted_probas = cb_lgb_model.predict_proba(model, X)
    
    y_pred_uno = np.where(y_prob_uno >= umbral, 1, 0).tolist()
    print("fin  predecir_clasificacion_binaria")
    return y_pred_uno, y_prob_uno



def get_result_df(KPIs_list,decimal=3):
    
    df = pd.DataFrame(columns=["Agrupación","Modelo","Total(E)","Total(E) Pos.","Total(V)","Total(V) Pos.",
                               'Precisión(E)', 'Sensibilidad(E)', 'Especificidad(E)','F1(E)','PR AUC(E)','ROC AUC(E)', 'Filtración(E)', 'Subcobertura(E)', 
                               'Precisión(V)', 'Sensibilidad(V)', 'Especificidad(V)','F1(V)','PR AUC(V)','ROC AUC(V)', 'Filtración(V)', 'Subcobertura(V)',
                               "umbral_opt",
                               'Precisión(Opt)','Sensibilidad(Opt)','Especificidad(Opt)','F1(Opt)','PR AUC(Opt)','ROC AUC(Opt)', 'Filtración(Opt)', 'Subcobertura(Opt)'])
    
    for idx, result  in enumerate(KPIs_list):
        mr = result[0]
        
        mod = result[1]
        
        t_train = result[2]
        
        t_train_class_1 = result[3]
        
        t_test = result[4]
        
        t_test_class_1 = result[5]
        
        Ks_train = result[6]
        
        Ks = result[7]
        umbral_opt = result[8]
        Ks_opt = result[9]
        
        result_rd = [mr,mod,t_train,t_train_class_1,t_test,t_test_class_1]+[round(num, decimal) for num in list(Ks_train)]+[round(num, decimal) for num in list(Ks)]+[umbral_opt]+[round(num_opt, decimal) for num_opt in list(Ks_opt)]
        df.loc[idx] = result_rd

        #df.loc[i] = list(KPIs)

    return df

def get_kpi_df_nacional(PATH_RESULT="resultado",grupos_grados=None,lista_mr=None):
    df_resumen = None
    #grupos_grados = {"1 prim": [4],"2 prim": [5], "3-5 prim": [6,7,8], "6 prim": [9], "1-4 sec": [10,11,12,13],"5 sec": [14]}
    #lista_mr = ["centro","norte","sur","oriente","lima"]
    
    list_df = []
    for key, grupo_grado  in grupos_grados.items():
        path = "{}/{}/{}".format(PATH_RESULT,key,"resultados.xlsx")
    
        df = pd.read_excel (path,index_col=0)
        idx = df.groupby(['Macro Región'])['Average Precision'].transform(max) == df['Average Precision']
        df = df[idx].copy()
        df["key_grupo_grado"] = key
        list_df.append(df)
    
    df_resumen = pd.concat(list_df)
    return df_resumen


def get_test_size(X_t=None,log=None):
    Total_X_t =  X_t.shape[0]
    Total_Test = 20000 # Cantidad minima de Test
    test_size = round(Total_Test/Total_X_t,5)
    
    min_test_size = 0.20
    if(test_size > min_test_size):
        test_size = 0.20 
    if  log is not None and log>0 :
        print("test_size : ", test_size)
    return test_size

def export_resultado_final_nacional(alto=0.75,medio=0.5,grupos_grados=None,lista_mr=None,path="resultado",
                                    delta_path=None,modelos=[]):
    if (grupos_grados is None):
        msg = "ERROR: No se ha especificado el parametro 'grupos_grados'"      
        raise Exception(msg)   
        
    if (lista_mr is None):
        msg = "ERROR: No se ha especificado el parametro 'lista_mr', que contiene la lista de macro regiones"      
        raise Exception(msg)   

    hg.validar_directorio(path)    
    if delta_path is not None:
        hg.validar_directorio(delta_path) 
        
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d%m%Y_%H%M%S")
    #"norte","sur"
    #grupos_grados = { "3-5 prim": [6,7,8]}
    #lista_mr = ["norte"]
    df_resumen = get_kpi_df_nacional(path+"/02.Modelo",grupos_grados)
        
    dt = {'COD_MOD':str,'COD_MOD_T':str,'ANEXO':int,'ANEXO_T':int,'EDAD':int,
      'N_DOC':str,'COD_MOD_T_MENOS_1':str,
      'ANEXO_T_MENOS_1':int,'NUMERO_DOCUMENTO_APOD':str,'ID_PERSONA':int}
    
    list_result = []
    
    if len(modelos)==0:
        modelos = ["neg_bagging_fraction__lgb_model","scale_pos_weight__lgb_model"] 
    
    columns = ['ID_PERSONA'] + modelos
    
    for key, grupo_grado  in grupos_grados.items():
        
        for macro_region in lista_mr:
            #print("obteniendo best model : ",macro_region," - ",key)
            best_model = df_resumen[(df_resumen.key_grupo_grado==key) & (df_resumen['Macro Región']==macro_region)]
            if best_model.shape[0]==0:
                msg = "ERROR: El archivo resultados.xlsx para el grupo de grados '"+key+"' no tiene resultados para la macro region: "+macro_region      
                raise Exception(msg)   
                
            best_model = best_model.Modelo.iloc[0]
            print(best_model," - ",macro_region," - ",key)
            if delta_path is None:
                specific_url = '{}/{}/{}/{}/{}'.format(path,"01.data_input",key,macro_region,"X_t_mas_1.csv")
            else:
                specific_url = '{}/{}/{}/{}/{}'.format(delta_path,"01.data_input",key,macro_region,"X_t_mas_1.csv")
                
            df=pd.read_csv(specific_url,dtype=dt, encoding="utf-8",usecols=columns) 
            df['RISK_SCORE'] = df[best_model] 
            list_result.append(df)
            
          
    df_nacional = pd.concat(list_result)
    df_nacional.drop_duplicates(subset ="ID_PERSONA",  keep = "first", inplace = True)
      
    df_nacional['PREDICCION']=None
    df_nacional.loc[(df_nacional['RISK_SCORE']>=alto) & (df_nacional['RISK_SCORE']<=1), 'PREDICCION'] = 3
    df_nacional.loc[(df_nacional['RISK_SCORE']>=medio) & (df_nacional['RISK_SCORE']<alto), 'PREDICCION'] = 2
    df_nacional.loc[df_nacional['RISK_SCORE']<medio, 'PREDICCION'] = 1
    df_nacional.PREDICCION = df_nacional.PREDICCION.astype(int)      
    
    cls_export = ["ID_PERSONA","RISK_SCORE",'PREDICCION']
    print("Total de registros : ",df_nacional.shape)
    if delta_path is None:
        url = "{}/{}/".format(path,"03.data_output")
        hg.validar_directorio(url)  
        filename = "nacional_{}.dta".format(dt_string)
        df_nacional[cls_export].to_stata(url+filename) 
    else:
        url = "{}/{}/".format(delta_path,"02.data_output")
        hg.validar_directorio(url) 
        filename = "nacional_{}.dta".format(dt_string)         
        df_nacional[cls_export].to_stata(url+filename)
    return df_nacional




def show_barplot_resultado_final_nacional(grupos_grados=None, lista_mr = None, scores = [] ,path = None,show=False):
    df_resumen = get_kpi_df_nacional(PATH_RESULT=path,grupos_grados=grupos_grados,lista_mr=lista_mr)
    
    list_result_total = []
    for macro_region in lista_mr:
        list_mr = []
        for score in scores:
            for key, grupo_grado  in grupos_grados.items():
                directory = path+"/"+str(key)
                hg.validar_directorio(directory) 
                final_path = directory+ "/resultados.xlsx"
                
                df = pd.read_excel(final_path, index_col=0)  
               
                best_model = df_resumen[(df_resumen.key_grupo_grado==key) & (df_resumen['Macro Región']==macro_region)]
                if best_model.shape[0]==0:
                    msg = "ERROR: El archivo resultados.xlsx para el grupo de grados '"+key+"' no tiene resultados para la macro region: "+macro_region      
                    raise Exception(msg)   
    
                valor = best_model[score].values[0]
                
                df_mr_grado = pd.DataFrame() 
                df_mr_grado['Valor'] = [valor] 
                df_mr_grado['Indicador'] = [score] 
                df_mr_grado['Grados'] = [key]        
                df_mr_grado['MR'] = [macro_region]
    
                list_mr.append(df_mr_grado)
        df_mr = pd.concat(list_mr)
        show_barplot_rf_n(df_mr,macro_region,path,show)
        list_result_total.append(df_mr)
    
    df_result_total = pd.concat(list_result_total)
    show_barplot_rf_n(df_result_total,"Nacional",path,show)
    return df_result_total

def show_barplot_rf_n(df,titulo_top_left="",dir_name=None,show=False):
    fig = plt.figure(figsize=(15, 6))
    ax = sns.barplot(x='Grados',y='Valor',data=df, hue='Indicador')
    
    for p in ax.patches:    
        height = p.get_height()
        #print(height)
        if math.isnan(height):
            height = 0
        #height = round(height,0)
        ax.text(p.get_x()+p.get_width()/2.,
                height ,
                '{:0.2f}'.format(height),
                ha="center") 
    plt.suptitle(titulo_top_left.upper()+' - Robustez por Grado', fontsize=20)
    ax.legend(ncol = 3, loc = 'best', bbox_to_anchor=(0.65, -0.1))
    
    
    if show :
        plt.show()
       
    filename =titulo_top_left+'_barplot.png'
    if len(dir_name.strip())==0 :
        full_dirname = filename
    else:
        if os.path.isdir(dir_name)==False:
            os.makedirs(dir_name)
        full_dirname = os.path.join(dir_name, filename)         
            
    plt.savefig(full_dirname, bbox_inches='tight')
    plt.close()

'''            
def split_x_y(ID_GRADO,macro_region,modalidad="EBR"):

    lista_regiones = get_macro_region(macro_region)
    list_join_n=[]
    list_join_n_mas_1=[]
    for region in lista_regiones:

        url_dir = "{}/{}/".format(region,ID_GRADO)
        print(url_dir)
        try:
            df_join_n , df_join_n_mas_1 = get_saved_join_data(url_dir,modalidad=modalidad)
        except:
            continue
        
        #df_join_n , df_join_n_mas_1 = get_saved_join_data(url_dir,modalidad=modalidad)
        df_join_n['REGION']= region
        df_join_n_mas_1['REGION']= region
        
        ############tempEEE#######
        df_join_n['D_REGION']= region
        df_join_n_mas_1['D_REGION']= region
        ########################
        
        
        print(region)
        print(df_join_n.DESERCION.value_counts())
        list_join_n.append(df_join_n)
        list_join_n_mas_1.append(df_join_n_mas_1)

    df_join_n = pd.concat(list_join_n)
    df_join_n_mas_1 = pd.concat(list_join_n_mas_1)

    fe_df(df_join_n,df_join_n_mas_1)

    X_train, X_test, y_train, y_test , X_t, X_t_eval, y_eval , ID_P_T,ID_P_T_MAS_1, y = tranform_data(df_join_n,df_join_n_mas_1,False)
    

    return X_train, X_test, y_train, y_test , X_t, X_t_eval, y_eval ,  ID_P_T,ID_P_T_MAS_1 , y
   

def get_saved_join_data(url_dir,sub_dir="data",modalidad="EBR"):
    
    if not url_dir:
        url_dir="../02.PreparacionDatos/03.Fusion/reporte_modelo/"+sub_dir+"/"
    else:
        url_dir = '{}/{}'.format("../02.PreparacionDatos/03.Fusion/reporte_modelo/"+sub_dir,url_dir)
        if not os.path.exists(url_dir):
            os.makedirs(url_dir)
        print("reporte generado en : "+url_dir)
    
    if (modalidad=="EBR"):
        specific_url = url_dir+"data.csv"
        specific_url_eval = url_dir+"data_eval.csv"
    else:
        specific_url = url_dir+"data_{}.csv".format(modalidad)
        specific_url_eval = url_dir+"data_eval_{}.csv".format(modalidad)        
    
    dt = {'COD_MOD':str,'COD_MOD_T':str,'ANEXO':int,'ANEXO_T':int,'EDAD':int,
          'N_DOC':str,'COD_MOD_T_MENOS_1':str,
          'ANEXO_T_MENOS_1':int,'NUMERO_DOCUMENTO_APOD':str,'ID_PERSONA':int}

    df=pd.read_csv(specific_url,dtype=dt, encoding="utf-8") 
    df_eval=pd.read_csv(specific_url_eval,dtype=dt, encoding="utf-8") 
    
    return df,df_eval

 ''' 