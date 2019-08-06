from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection

# function to drop feature and plot cross validation accuracy
def drop_feature(tree_model, sorted_importance, X, y, start):
    """
    Drop least important feautures one by one until there is only one feature.
    Calculate 5 folds cross validation scores and then plot them.
    
    Parameters:
    - start: int, number of features to be trimmed right away (Save computational time)
    — tree_model: tree model object from sk-learn
    — sorted_importance: sorted dataframe containing feauture, importance score, and standard error of feature imporance
    — X, y: data sets for cross validation scores (will be applied 80/20 train/test split with random_state = 0)
    
    Returns: 
    — cross_vals: list of 5 folds cross validation scores after removing features
    — std_cross_vals: list of corresponding standard deviations
    """
    #Resort importance (ascending = True)
    sorted_importance = sorted_importance.sort_values(by=['Importance'], ascending = True)
    
    #Holders for plots
    cross_vals = []
    std_cross_vals = []
    num_trimmed = [x for x in range(start,sorted_importance.shape[0])]
    
    #Add to cross_vals
    for trimmed in num_trimmed:
        
        #Select trimmed training data 
        remaining = sorted_importance.shape[0] - trimmed
        trimmed_X = X[sorted_importance.iloc[-remaining:,:]["Feature"]]
        
        #Divide train and test set
        X_train, X_test, y_train, y_test = model_selection.train_test_split(trimmed_X, y, test_size = 0.2, random_state=0)
        
        #Add to cross_vals list
        cross_val = cross_val_score(tree_model, X_train, y_train, cv = 5)
        cross_vals.append(np.average(cross_val))
        std_cross_vals.append(np.std(cross_val))
        
    
    return cross_vals, std_cross_vals, num_trimmed