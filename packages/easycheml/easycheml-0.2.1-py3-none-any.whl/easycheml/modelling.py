####### DATA MANIPULATION LIBRARIES
import pandas as pd
import numpy as np
import statsmodels.api as sm
import smogn
import pickle
# import dill as pickle

######### SYSTEM #############
import datetime
import sys
import copy
import os

###### DATA VISUALIZATION LIBRARIES
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
# %matplotlib inline

############ ML LIBRARIES ###########
from sklearn import impute,metrics,model_selection,linear_model,ensemble,svm,kernel_ridge,tree,experimental,neighbors
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,MinMaxScaler,StandardScaler
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV
from xgboost import XGBRegressor
from scipy import stats,special

############### EASYCHEML LIBRARIES ############
from easycheml.preprocessing import PreProcessing as pre

############## tensorflow ##################
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.callbacks import History
from tensorflow import keras
from tensorflow.keras import layers
import keras_tuner
from keras_tuner.tuners import RandomSearch
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.utils import to_categorical


global timestamp_var
value = datetime.datetime.fromtimestamp(datetime.datetime.now().timestamp())
timestamp_var=f"{value:%Y-%m-%d-%H-%M-%S}"


def build_ml_model():
    """
    This module helps in fitting to all the ml and dl algorithms that are available in Scikit-learn
    and other opensource packages

    Parameters
    ----------
    task_type : str, compulsory (regression, classification, clustering)

    algorithm : type of ml/dl model used to model data (linear_regression)
                # regression_models:all, linear, ridge, Lasso, ElasticNet, randomforest, gradientboosting
                # classification_models: 
                # clustering_models:
    
    cross_validation_method : KFold, LeaveOneOut, StratifiedKFold

    ignore_warnings : bool, optional (default=True)
        When set to True, the warning related to algorigms that are not able to run are ignored.
    custom_metric : function, optional (default=None)
        When function is provided, models are evaluated based on the custom evaluation metric provided.
    prediction : bool, optional (default=False)
        When set to True, the predictions of all the models models are returned as dataframe.
    classifiers : list, optional (default="all")
        When function is provided, trains the chosen classifier(s).
    """
    pass

class FeatureEngineering:

    def __init__(self,pandas_dataframe,target_name,additional_cols_list):
        self.dataset = pandas_dataframe
        self.targetname = target_name
        self.additional_cols_list = additional_cols_list

        additional_cols=self.dataset.loc[:, self.additional_cols_list]
        additional_cols=additional_cols.reset_index()
        self.additional_cols= additional_cols[additional_cols.columns.drop((additional_cols.filter(regex='ndex')))]

        self.df_without_additional_cols=self.dataset.drop(additional_cols_list, axis = 1)
        
    def feature_thru_correlation(self, lower_threshold, corr_method):
        """
        corr_method = pearson, kendall, spearman

        """
        print("#######################################")
        print(f"FEATURE SELECTION THROUGH CORRELATION")
        print("#######################################")
        
        # self.data=self.dataset
        print("\nShape of dataset: ", self.dataset.shape)
        self.dataset=self.dataset.reset_index()
        self.dataset = self.dataset[self.dataset.columns.drop((self.dataset.filter(regex='ndex')))]
        
        self.dataset=self.dataset._get_numeric_data()
        matrix = abs(self.dataset.corr(method=corr_method,numeric_only = True))[self.targetname].sort_values(kind="quicksort", ascending=False)
        matrix = matrix[matrix > lower_threshold]
        
        Relevant_Features =self.dataset.loc[:, abs(self.dataset.corr(method=corr_method,numeric_only = True)[self.targetname]) > lower_threshold]
        Relevant_Features = Relevant_Features[Relevant_Features.columns.drop((Relevant_Features.filter(regex='ndex')))]
        Relevant_Features = Relevant_Features[Relevant_Features.columns.drop((Relevant_Features.filter(regex='unnamed')))]

        print("\nTarget : ", self.targetname)
        print("\nCorrelation Method : ", corr_method)
        print("\nCorrelation with Target\n", matrix)

        return Relevant_Features
        
    def feature_thru_wrapper(dataset:str,target_name:str,feat_selc_dirn:str,num_min_features:int,num_max_features:int,model:callable,score_param:str,cross_val:int):
        """
        Function to select features through feature selection method

        Parameter
        ---------
        dataset : training dataset
        target_name: name of the target variable
        feat_selc_dirn: SFS, SFFS, SBS,SBFS
        num_features: number_features_to_keep
        model: model to fit to select features
        score_param: neg_mean_squared_error, r2, accuracy
        cross_val: KFold(n_splits=5,shuffle=True, random_state=False))

        """
        
        from mlxtend.feature_selection import SequentialFeatureSelector as SFS
        from mlxtend.feature_selection import ExhaustiveFeatureSelector as EFS


        dataset=dataset._get_numeric_data()
        features=dataset.drop([target_name], axis = 1)
        target = dataset.loc[:,target_name]

        if feat_selc_dirn=='EFS':
        #   fs =EFS(model, 
        #   min_features=num_min_features,
        #   max_features=num_max_features,
        #   scoring=score_param,
        #   cv=cross_val)
        # #   print("\nfeature_pred_score :",fs.best_score_*(-1))
        #   print('Selected features:', fs.best_idx_)
            pass


        else:
            if feat_selc_dirn=='SFS':
                forward_param=True
                floating_param=False

            elif feat_selc_dirn=='SBS':
                forward_param=False
                floating_param=False
                
            elif feat_selc_dirn=='SFFS':
                forward_param=True
                floating_param=True
                
            elif feat_selc_dirn=='SBFS':
                forward_param=False
                floating_param=True

            sfs = SFS(model, 
            k_features=num_max_features, 
            forward=forward_param, 
            floating=floating_param, 
            scoring=score_param,
            cv=cross_val)

            fs = sfs.fit(features, target)

            print("\nfeature_pred_score :",fs.k_score_)
            print("\nfeatures_name :",fs.k_feature_idx_)
            print("\nfeatures_name :",fs.k_feature_names_)

            Relevant_Features =dataset.loc[:, fs.k_feature_names_]

        return Relevant_Features
    
    def feature_thru_anova(self,num_features):
        from sklearn.feature_selection import SelectKBest, f_classif

        """
        Perform feature selection using ANOVA F-measure.

        Args:
            X_train (DataFrame or array-like): Input features for training.
            y_train (Series or array-like): Target variable for training.
            num_features (int): Number of top features to select.

        Returns:
            selected_features (list): List of selected feature column names.
        """
        dataset = self.df_without_additional_cols
        # Initialize SelectKBest with f_classif scoring function
        selector = SelectKBest(score_func=f_classif, k=num_features)

        target = dataset.loc[:,self.targetname]
        features_data=dataset.drop(self.targetname, axis = 1)
        
        # Fit selector to the training data
        selector.fit(features_data, target)

        # Get indices of selected features
        selected_indices = selector.get_support(indices=True)

        # Get selected feature column names
        selected_features = features_data.columns[selected_indices].tolist()

        # selected_features_list=selected_features.tolist()

        # Assuming you have imported necessary libraries and loaded your data into X_train and y_train

        # Call the select_features function to select top features
        # selected_features = select_features(features_data, target, num_features=20)  # Change num_features as needed

        # Use selected features for training
        features_data_selected = features_data[selected_features]

        feature_dataset = pd.concat([target,features_data_selected], axis=1)

        feature_dataset=feature_dataset.reset_index()


        Relevant_Features = pd.concat([self.additional_cols, feature_dataset], axis=1)

        Relevant_Features= Relevant_Features[Relevant_Features.columns.drop((Relevant_Features.filter(regex='ndex')))]




        return Relevant_Features
        
    def generate_synthetic_data(dataset, target, k_value, samp, thres, rel, rel_type,coef):
    
        df = smogn.smoter(

            data = dataset,             ## pandas dataframe
            y = target,                 ## string ('header name')
            k = k_value,                ## positive integer (k < n)
            samp_method = samp,         ## string ('balance' or 'extreme')
            rel_thres = thres,          ## positive real number (0 < R < 1)
            rel_method = rel,           ## string ('auto' or 'manual')
            rel_xtrm_type = rel_type,   ## string ('low' or 'both' or 'high')
            rel_coef = coef             ## positive real number (0 < R)

        )
        sns.kdeplot(dataset[target], label = "Original")
        sns.kdeplot(df[target], label = "SMOGN")        
        return df

    def categorize_target(data,oldtargetname:str,newtargetnname:str,bins:list, labels:list):
        df_Categorical = data.copy()

        category = pd.cut(df_Categorical[oldtargetname],bins=bins,labels=labels)

        df_Categorical.insert(2,newtargetnname, category)
        df_Categorical = df_Categorical[[newtargetnname]]
        df_Dataset_cat= pd.concat([df_Categorical,data],axis =1 )

        # dropping useless columns

        df_Dataset_cat = df_Dataset_cat.drop([oldtargetname], axis = 1)
        print('Category counts: ',df_Dataset_cat[newtargetnname].value_counts())


    
        return df_Dataset_cat

class Regressors:
    """
    Parameter

    dataset: 
    target_name: name of the target in the dataset
    train_size: splitsize of the training dataset
    val_size: splitsize of the validation dataset
    """
    
    def __init__(self, dataset,target_name,train_size:float, val_size:float,additional_cols_list=None):
        self.dataset = dataset
        self.target = target_name
        self.val_size = val_size
        self.train_size = train_size
        self.additional_cols_list=additional_cols_list
        train, validate, test=pre.train_validate_test_split(dataset,train_size,val_size,0)

        # train=train._get_numeric_data()
        # validate=validate._get_numeric_data()
        # test=test._get_numeric_data()

        X_train=train.drop([target_name], axis = 1)
        self.y_train = train.loc[:,target_name]
        X_val=validate.drop([target_name], axis = 1)
        self.y_val = validate.loc[:,target_name]
        X_test=test.drop([target_name], axis = 1)
        self.y_test = test.loc[:,target_name]

        self.X_train_add_cols=X_train.loc[:,additional_cols_list]
        self.X_test_add_cols=X_test.loc[:,additional_cols_list]
        self.X_val_add_cols=X_val.loc[:,additional_cols_list]

        self.X_val=X_val.drop(additional_cols_list, axis = 1)
        self.X_train=X_train.drop(additional_cols_list, axis = 1)
        self.X_test=X_test.drop(additional_cols_list, axis = 1)

        self.log_dir_path = "logfiles"
        isExist = os.path.exists(self.log_dir_path)
        if not isExist:
            os.makedirs(self.log_dir_path)
        
        self.model_dir_path = "models"
        isExist = os.path.exists(self.model_dir_path)
        if not isExist:
            os.makedirs(self.model_dir_path)

    def linear_models(self,select_model:str,tuner_parameters=None):
        timestamp = copy.copy(timestamp_var)
        sys.stdout = Logger(f"{self.log_dir_path}/linear_model-{select_model}-logfile-{timestamp}.log")

        if select_model=='LR':        
            model=linear_model.LinearRegression()
        if select_model=='Ridge':        
            model=linear_model.Ridge()
        
        pass
    
    def ensemble_models(self,select_model:str,tuner_parameters=None):
        """
        
        Args:
            select_model (str): _description_
            tuner_parameters (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_

        Example

        parameters = {
                        'n_estimators' :[50,100,200,300,400,500,600,700,800,900,1000],
                        'criterion' : ["squared_error", "friedman_mse", "absolute_error"],
                        'max_depth' : [3,5,7,9,11,13,15,17,19,21,23,25,27,29,31],
                        'min_samples_split' : [5,10,20,30,40,50,60,70,80,90,100],

                        'min_samples_leaf':[5,10,20,30,40,50,60,70,80,90,100],
                        }
        # model.ensemble_models("RF",parameters)
        # model.compare_ml_models(None,None)
        """
        
        timestamp = copy.copy(timestamp_var)
        sys.stdout = Logger(f"{self.log_dir_path}/ensemble_model-{select_model}-logfile-{timestamp}.log")
        
        if select_model=='RF':        
            model=ensemble.RandomForestRegressor(random_state=6)
        if select_model=='GBR':        
            model=ensemble.GradientBoostingRegressor(random_state=0)
        if select_model=='hGBR':        
            model=ensemble.HistGradientBoostingRegressor(random_state=6)
        if select_model=='AdaBoost':        
            model=ensemble.AdaBoostRegressor(random_state=6)
        if select_model=='ETree':        
            model=ensemble.ExtraTreesRegressor(random_state=6)
                
        if tuner_parameters==None:
            model.fit(self.X_train, self.y_train.values)
            y_pred = model.predict(self.X_test)
        else:                
            RF_cv = RandomizedSearchCV(estimator=model,param_distributions=tuner_parameters,n_iter=30,cv=5,n_jobs=-1)
            RF_cv.fit(self.X_train,self.y_train.values.ravel())
            model=RF_cv.best_estimator_
            model.fit(self.X_train, self.y_train.values)
            y_pred = model.predict(self.X_test)

        print("\n#########################################")
        print("         ENSEMBLE MODEL SELECTED")
        print("#########################################\n")

        print("\nModel :", model)
        print("\nTuner Parameters :", tuner_parameters)            
        print(f"\nModel Metrics\n")
        
        r2_score_test=round(metrics.r2_score(self.y_test, y_pred),2)*100
        mse_test=round(metrics.mean_squared_error(self.y_test, y_pred,squared=False),3)
        mae_test=round(metrics.mean_absolute_error(self.y_test, y_pred),3)

        print('R2 score of training data : {0} %'.format(round(metrics.r2_score(self.y_train, model.predict(self.X_train)),2)*100))
        print('R2 score of Testing data : {0} %'.format(round(metrics.r2_score(self.y_test, y_pred),2)*100))
        print('RMSE of of Testing data : {0}'.format(round(metrics.mean_squared_error(self.y_test, y_pred,squared=False),3)))
        print('MAE of Testing data : {0}'.format(round(metrics.mean_absolute_error(self.y_test, y_pred),3)))
        print("#########################################\n")
        
        filename=f'{self.models}/{select_model}-{timestamp}.pickle'
        # filename=f'{model}/{select_model}-{timestamp}.pickle'

        pickle.dump(model, open(filename, "wb"))

        return select_model, r2_score_test,mse_test, mae_test

    def mixed_ensemble_models(self,select_model,estimator_models,tuner_parameters):
    
        if select_model=='bagging':        
            model=ensemble.BaggingRegressor(estimator_models,random_state=6)
        
        if select_model=='voting':        
            model=ensemble.VotingRegressor(estimator_models)

        if select_model=='adaBoost_dtree':
            print('not implemented yet')
        if select_model=='stacking':
            print('not implemented yet')
                
        if tuner_parameters==None:
            model.fit(self.X_train, self.y_train.values)
            y_pred = model.predict(self.X_test)
        else:                
            RF_cv = RandomizedSearchCV(estimator=model,param_distributions=tuner_parameters,n_iter=30,cv=5,n_jobs=-1)
            RF_cv.fit(self.X_train,self.y_train.values.ravel())
            model=RF_cv.best_estimator_
            model.fit(self.X_train, self.y_train.values)
            y_pred = model.predict(self.X_test)
            
        print(f"\n############ {select_model} MODEL METRICS #############")
        print('R2 score of training data : {0} %'.format(round(metrics.r2_score(self.y_train, model.predict(self.X_train)),2)*100))
        print('R2 score of Testing data : {0} %'.format(round(metrics.r2_score(self.y_test, y_pred),2)*100))
        print('RMSE of of Testing data : {0}'.format(round(metrics.mean_squared_error(self.y_test, y_pred,squared=False),3)))
        print('MAE of Testing data : {0}'.format(round(metrics.mean_absolute_error(self.y_test, y_pred),3)))
        print("#########################################\n")
        filename=f'{select_model}.pickle'
        pickle.dump(model, open(filename, "wb"))


    def tree_models(self,select_model:str,tuner_parameters=None):
        
        if select_model=='DTREE':        
            model=tree.DecisionTreeRegressor(random_state=6)
        
        if tuner_parameters==None:
            model.fit(self.X_train, self.y_train.values)
            y_pred = model.predict(self.X_test)
        else:                
            RF_cv = RandomizedSearchCV(estimator=model,param_distributions=tuner_parameters,n_iter=30,cv=5,n_jobs=-1)
            RF_cv.fit(self.X_train,self.y_train.values.ravel())
            model=RF_cv.best_estimator_
            model.fit(self.X_train, self.y_train.values)
            y_pred = model.predict(self.X_test)
            
        print(f"\n############ {select_model} MODEL METRICS #############")
        print('R2 score of training data : {0} %'.format(round(metrics.r2_score(self.y_train, model.predict(self.X_train)),2)*100))
        print('R2 score of Testing data : {0} %'.format(round(metrics.r2_score(self.y_test, y_pred),2)*100))
        print('RMSE of of Testing data : {0}'.format(round(metrics.mean_squared_error(self.y_test, y_pred,squared=False),3)))
        print('MAE of Testing data : {0}'.format(round(metrics.mean_absolute_error(self.y_test, y_pred),3)))
        print("#########################################\n")
        filename=f'{select_model}.pickle'
        pickle.dump(model, open(filename, "wb"))

    def compare_ml_models(self,list_ensemble_models,tuner_parameters):

        if list_ensemble_models==None:
            list_ensemble_models=['RF','GBR','hGBR','AdaBoost','ETree']
        
        metrics = pd.DataFrame()

        for model in list_ensemble_models:
            modelname,r2_score_test, mse_test, mae_test=self.ensemble_models(model, tuner_parameters)
            temp ={
            'Model': model,
            'R2':r2_score_test,
            'MSE': mse_test,
            'MAE': mae_test
            }
            
            metrics=metrics.append(temp,ignore_index=True)            
            metrics = metrics.sort_values(['R2'], ascending=False)

        print(f"\n############ MODELS PERFORMANCE #############")
        print(metrics)
        print(f"#############################################\n")

    
    def build_model(self,hp):
        model = models.Sequential()
        for i in range(hp.Int('num_layers', 2, 30)):
            model.add(layers.Dense(units=hp.Int('units_' + str(i),
                                                min_value=2,
                                                max_value=20,
                                                step=4),
                                                activation='relu'))
        model.add(layers.Dense(1, activation='linear'))
        model.compile(
            optimizer=keras.optimizers.Adam(
            hp.Choice('learning_rate', [1e-2, 1e-3, 1e-4,1e-4,1e-5,1e-6])),
            loss='mean_absolute_error',
            metrics='mean_absolute_error')
        return model

    def dnn_sequential_model_opt(self,num_max_trials,num_executions_per_trial,num_epochs,num_batch_size):
        """

        Example

        # model.dnn_sequential_model_opt(num_max_trials=5,num_executions_per_trial=3,num_epochs=1,num_batch_size=64)
        """       
                
        self.timestamp = copy.copy(timestamp_var)
        sys.stdout = Logger(f"{self.log_dir_path}/DNN-{self.timestamp}.log")
        LOG_DIR = f'{self.log_dir_path}/DNN-LOG-DIR-{self.timestamp}'
        tensorboard = TensorBoard(log_dir=LOG_DIR)    
        
        self.tuner = RandomSearch(
            self.build_model,
            objective=keras_tuner.Objective("val_mean_absolute_error", direction="min"),        
            max_trials=num_max_trials,
            executions_per_trial=num_executions_per_trial,
            overwrite=True,
            directory=f'{self.log_dir_path}/DNN-TUNER-DIR-{self.timestamp}',
            project_name=LOG_DIR)

        print("\n########################")
        print(" Search for best model")    
        print("########################\n")

        self.tuner.search(x=self.X_train,
                    y=self.y_train,
                    epochs=num_epochs,
                    batch_size=num_batch_size,
                    callbacks=[tensorboard],
                    validation_data=(self.X_val, self.y_val))

        print("\n########################")
        print("Search Space Summary")    
        print("########################\n")
        self.tuner.search_space_summary()

        print("\n########################")
        print("Results Summary")    
        print("########################\n")
        
        self.tuner.results_summary()

        self.dnn_filename=f'{self.model_dir_path}/DNN-MODEL-{self.timestamp}.pickle'
        
        # with open(self.dnn_filename, "wb") as f:
            # pickle.dump(self.tuner, f)

    def dnn_compile_evaluate_model(self,epoch,batchsize):
        """_summary_

        Args:
            epoch (_type_): _description_
            batchsize (_type_): _description_

        Example
        # model.dnn_compile_evaluate_model(epoch=20,batchsize=64)
        """
        self.timestamp = copy.copy(timestamp_var)

        history = History()

        model=self.model
        #Configure the model
        # model.compile(optimizer='adam',loss="mean_squared_error",metrics=["mean_absolute_error"])
        model.compile(optimizer='adam',loss="mean_squared_error",metrics=["mean_absolute_percentage_error"])

        history = model.fit(self.X_train,self.y_train, validation_data=(self.X_val, self.y_val),epochs=epoch,batch_size=batchsize)
        result = model.evaluate(self.X_test,self.y_test)

        for i in range(len(model.metrics_names)):
            print("Metric ",model.metrics_names[i],":",str(round(result[i],2)))

        # list all data in history
        print(history.history.keys())

        figure,axes = plt.subplots(nrows=1, ncols=2, figsize=(8,3))
        # axes[0].plot(history.history['mean_absolute_error'])
        # axes[0].plot(history.history['val_mean_absolute_error'],color='b')

        axes[0].plot(history.history['mean_absolute_percentage_error'])
        axes[0].plot(history.history['val_mean_absolute_percentage_error'],color='b')

        axes[0].set_title('Model Training & Validation loss a/cross epochs')
        axes[0].set_ylabel('Loss')
        # axes[0].set_ylim([0, 1])
        axes[0].set_xlabel('epoch')
        axes[0].legend(['train', 'test'], loc='upper left')

        # summarize history for loss
        axes[1].plot(history.history['val_loss'])
        axes[1].plot(history.history['loss'],color='b')
        axes[1].set_title('model loss')
        axes[1].set_ylabel('loss')
        # axes[1].set_ylim([0, 1])
        axes[1].set_xlabel('epoch')
        axes[1].legend([ 'validation loss', 'train'], loc='upper left')
        plt.show()

        # model.save(f'{self.model_dir_path}/DNN-bestmodel-{self.timestamp}')
        result=model.evaluate(np.array(self.X_test), np.array(self.y_test))

        #Print the results
        for i in range(len(model.metrics_names)):
            print("Metric ",model.metrics_names[i],":",str(round(result[i],2)))
        
        y_prediction = model.predict(self.X_test)
        self.predicted=y_prediction
        self.actual=self.y_test
        # self.predicted = np.argmax (y_prediction, axis = 1)
        # self.actual=np.argmax(self.y_test, axis=1)
    
    def dnn_best_model(self,num_top_model:int,select_model_num:int):
        """

        Example
        # model.dnn_best_model(num_top_model=5,select_model_num=1)

        """
        
        with open(self.dnn_filename, 'rb') as file:
            tuner=pickle.load(file)

        tuner.results_summary()

        models = tuner.get_best_models(num_models=num_top_model)
        model = models[select_model_num]
        model.build(self.X_train.shape)
        model.summary()

        # history = History()

        # #Configure the model
        # model.compile(optimizer='adam',loss="mean_squared_error",metrics=["mean_absolute_error"])
        # history = model.fit(self.X_train,self.y_train, validation_data=(self.X_val, self.y_val),epochs=epoch,batch_size=batchsize)
        # result = model.evaluate(self.X_test,self.y_test)

        # for i in range(len(model.metrics_names)):
        #     print("Metric ",model.metrics_names[i],":",str(round(result[i],2)))

        # # list all data in history
        # print(history.history.keys())

        # figure,axes = plt.subplots(nrows=1, ncols=2, figsize=(8,3))
        # axes[0].plot(history.history['mean_absolute_error'])
        # axes[0].plot(history.history['val_mean_absolute_error'],color='b')
        # axes[0].set_title('Model Training & Validation loss a/cross epochs')
        # axes[0].set_ylabel('Loss')
        # # axes[0].set_ylim([0, 1])
        # axes[0].set_xlabel('epoch')
        # axes[0].legend(['train', 'test'], loc='upper left')

        # # summarize history for loss
        # axes[1].plot(history.history['val_loss'])
        # axes[1].plot(history.history['loss'],color='b')
        # axes[1].set_title('model loss')
        # axes[1].set_ylabel('loss')
        # # axes[1].set_ylim([0, 1])
        # axes[1].set_xlabel('epoch')
        # axes[1].legend([ 'validation loss', 'train'], loc='upper left')
        # plt.show()

        # model.save(f'{self.model_dir_path}/DNN-bestmodel-{self.timestamp}')
        # score=model.evaluate(np.array(self.X_test), np.array(self.y_test))
        
        # y_prediction = model.predict(self.X_test)
        # self.predicted=y_prediction
        # self.actual=self.y_test
        # # self.predicted = np.argmax (y_prediction, axis = 1)
        # self.actual=np.argmax(self.y_test, axis=1)

        self.model=model
    
    # def dnn_custom_model(self):
    #     model = models.Sequential()
    #     print(self.X_train.shape)
    #     model.add(layers.Dense(150,input_dim = self.X_train.shape[1],activation="relu"))
    #     model.add(layers.Dense(350,activation="relu"))
    #     model.add(layers.Dense(350,activation="relu"))
    #     model.add(layers.Dense(350,activation="relu"))
    #     model.add(layers.Dense(350,activation="relu"))
        
    #     model.add(layers.Dense(1,activation = "linear"))    

    #     #Configure the model
    #     # model.compile(optimizer='adam',loss="mean_absolute_error",
    #     # metrics=["mean_absolute_error"])
    #     #Train the model
    #     # model.fit(self.X_train,self.y_train, validation_data= (self.X_val,self.y_val),epochs=num_epoch,batch_size=num_batch_size)
    #     self.model=model

    def dnn_custom_model(self, params):
        """
        Constructs a custom deep neural network (DNN) model based on the provided parameters.

        Args:
            params (dict): A dictionary containing the parameters for constructing the DNN model.
                - 'input_dim' (int): Input dimensionality of the first layer.
                - 'layer_sizes' (list of int): List containing the number of neurons for each hidden layer.
                - 'activations' (list of str): List containing the activation functions for each hidden layer.
                - 'dropout_rates' (optional, list of float): List containing the dropout rates for each hidden layer.

        Example:
            To construct a DNN model with the following parameters:
            - Input dimension: 10
            - Hidden layer sizes: [150, 350, 350, 350, 350]
            - Activation functions: ["relu", "relu", "relu", "relu", "relu"]
            - Dropout rates: [0.2, 0.3, 0.4, 0.5]

            >>> dnn_params = {
            ...     'input_dim': 10,
            ...     'layer_sizes': [150, 350, 350, 350, 350],
            ...     'activations': ["relu", "relu", "relu", "relu", "relu"],
            ...     'dropout_rates': [0.2, 0.3, 0.4, 0.5]
            ... }
            >>> self.dnn_custom_model(dnn_params)
        """
        model = models.Sequential()
        model.add(layers.Dense(params['layer_sizes'][0], input_dim=self.X_train.shape[1], activation=params['activations'][0]))
        for size, activation, dropout_rate in zip(params['layer_sizes'][1:], params['activations'][1:], params.get('dropout_rates', [])):
            model.add(layers.Dense(size, activation=activation))
            if dropout_rate:
                model.add(layers.Dropout(dropout_rate))
        model.add(layers.Dense(1, activation="linear"))
        
        self.model = model
    
    def mean_baseline(self):
        """
        Calculate the mean baseline prediction and evaluate its performance using Mean Absolute Error (MAE).

        Args:
            y_train (array-like): Array containing the target variable (dependent variable) values in the training set.
            y_test (array-like): Array containing the target variable (dependent variable) values in the test set.

        Returns:
            float: Mean Absolute Error (MAE) of the mean baseline predictions.
        """
        # Calculate the mean of the target variable in the training set
        mean_prediction = np.mean(self.y_train)
        
        # Use the mean prediction as the prediction for all samples in the test set
        mean_predictions = np.full_like(self.y_test, fill_value=mean_prediction)
        
        # Calculate the Mean Absolute Error (MAE) between the mean predictions and actual values in the test set
        mae_baseline = metrics.mean_absolute_error(self.y_test, mean_predictions)
        
        return mae_baseline

    def model_metrics(self):
        
        print('\n')
        # print("r2_Score: ", metrics.r2_score(self.actual, self.predicted))
        print("Model Baseline:", self.mean_baseline())

        MAPE=(metrics.mean_absolute_percentage_error(self.actual, self.predicted))*100
        MAE = metrics.mean_absolute_error(self.actual, self.predicted)

        print("MAPE: ", MAPE)
        print("MAE",MAE)


        print('\n')
        
        pred_table = pd.DataFrame()
        pred_table['actual'] = self.actual
        pred_table['predicted'] = self.predicted

        self.pred_table=pred_table.reset_index()
        self.pred_table = self.pred_table[self.pred_table.columns.drop((self.pred_table.filter(regex='ndex')))]
        
        self.X_test_add_cols=self.X_test_add_cols.reset_index()
        self.X_test_add_cols = self.X_test_add_cols[self.X_test_add_cols.columns.drop((self.X_test_add_cols.filter(regex='ndex')))]
        
        prediction_dataset = pd.concat([self.X_test_add_cols,self.pred_table], axis=1)
        prediction_dataset.to_csv('IntTesting-prediction-dataset.csv')

        return prediction_dataset

    def ext_testing(self,ext_testing_dataset):

        self.ext_X_test=ext_testing_dataset.drop([self.target], axis = 1)
        self.ext_y_test = ext_testing_dataset.loc[:,self.target]

        # self.ext_X_test_add_cols=self.ext_X_test.loc[:,self.additional_cols_list]
        self.ext_X_test_add_cols=self.ext_X_test.loc[:,list(set(self.additional_cols_list) & set(self.ext_X_test.columns))]

        self.ext_X_test=self.ext_X_test.drop(self.additional_cols_list, axis = 1)
        
        # print("self.ext_X_test",self.ext_X_test.shape)
        # print("self.ext_y_test",self.ext_y_test.shape)

        score=self.model.evaluate(np.array(self.ext_X_test), np.array(self.ext_y_test))
        y_prediction = self.model.predict(self.ext_X_test)

        MAPE=(metrics.mean_absolute_percentage_error(self.ext_y_test, y_prediction))*100
        print("MAPE", MAPE)
        
        pred_table = pd.DataFrame()
        pred_table['actual'] = self.ext_y_test
        pred_table['predicted'] = y_prediction
        
        self.ext_X_test_add_cols=self.ext_X_test_add_cols.reset_index()
        self.ext_X_test_add_cols = self.ext_X_test_add_cols[self.ext_X_test_add_cols.columns.drop((self.ext_X_test_add_cols.filter(regex='ndex')))]
        
        prediction_dataset = pd.concat([self.ext_X_test_add_cols,pred_table], axis=1)
        prediction_dataset=prediction_dataset.T.drop_duplicates().T    

        prediction_dataset.to_csv('ExtTesting-prediction-dataset.csv')
        return prediction_dataset, MAPE

class Classifiers:
    """
    Parameter

    dataset: 
    target_name: name of the target in the dataset
    train_size: splitsize of the training dataset
    val_size: splitsize of the validation dataset
    """
    
    def __init__(self, dataset,target_name,train_size:float, val_size:float,encode_target=None,additional_cols_list=None):
        self.dataset = dataset
        self.target = target_name
        self.val_size = val_size
        self.train_size = train_size
        self.additional_cols_list=additional_cols_list
        train, validate, test=pre.train_validate_test_split(dataset,train_size,val_size,0)

        # train=train._get_numeric_data()
        # validate=validate._get_numeric_data()
        # test=test._get_numeric_data()

        self.X_train=train.drop([target_name], axis = 1)
        self.y_train = train.loc[:,target_name]
        self.X_val=validate.drop([target_name], axis = 1)
        self.y_val = validate.loc[:,target_name]
        self.X_test=test.drop([target_name], axis = 1)
        self.y_test = test.loc[:,target_name]
        
        self.X_train_add_cols=self.X_train.loc[:,additional_cols_list]
        self.X_test_add_cols=self.X_test.loc[:,additional_cols_list]
        self.X_val_add_cols=self.X_val.loc[:,additional_cols_list]

        self.X_val=self.X_val.drop(additional_cols_list, axis = 1)
        self.X_train=self.X_train.drop(additional_cols_list, axis = 1)
        self.X_test=self.X_test.drop(additional_cols_list, axis = 1)

        self.num_targets=self.y_train.nunique()

        if encode_target==None:
            # self.y_train=keras.utils.to_categorical(self.y_train, num_classes=num_classes)
            # self.y_val=keras.utils.to_categorical(y_train, num_classes=num_classes)
            # self.y_test=keras.utils.to_categorical(y_train, num_classes=num_classes)
            pass
        elif encode_target=='encode':
            self.y_train, self.y_val,self.y_test = self.target_encoder(self.y_train,self.y_val,self.y_test)

        self.log_dir_path = "logfiles"
        isExist = os.path.exists(self.log_dir_path)
        if not isExist:
            os.makedirs(self.log_dir_path)
        
        self.model_dir_path = "models"
        isExist = os.path.exists(self.model_dir_path)
        if not isExist:
            os.makedirs(self.model_dir_path)
        
        # self.model=
    
    def target_encoder(self,y_train,y_val, y_test):
        from tensorflow.keras.utils import to_categorical
        self.endocder = LabelEncoder()
        self.endocder.fit(y_train)
        
        y_train_enc = self.endocder.transform(y_train)
        y_val_enc = self.endocder.transform(y_val)
        y_test_enc = self.endocder.transform(y_test)

        y_train_enc = to_categorical(y_train_enc, num_classes=self.num_targets)
        y_val_enc = to_categorical(y_val_enc,num_classes=self.num_targets)
        y_test_enc = to_categorical(y_test_enc,num_classes=self.num_targets)
        return y_train_enc,y_val_enc, y_test_enc

    def linear_models(self,select_model:str,tuner_parameters=None):
        timestamp = copy.copy(timestamp_var)
        sys.stdout = Logger(f"{self.log_dir_path}/linear_model-{select_model}-logfile-{timestamp}.log")

        if select_model=='LR':        
            model=linear_model.LinearRegression()
        if select_model=='Ridge':        
            model=linear_model.Ridge()
            
        pass
    
    def ensemble_models(self,select_model:str,tuner_parameters=None):
        
        timestamp = copy.copy(timestamp_var)
        sys.stdout = Logger(f"{self.log_dir_path}/ensemble_model-{select_model}-logfile-{timestamp}.log")
        
        if select_model=='RF':        
            model=ensemble.RandomForestRegressor(random_state=6)
        if select_model=='GBR':        
            model=ensemble.GradientBoostingRegressor(random_state=0)
        if select_model=='hGBR':        
            model=ensemble.HistGradientBoostingRegressor(random_state=6)
        if select_model=='AdaBoost':        
            model=ensemble.AdaBoostRegressor(random_state=6)
        if select_model=='ETree':        
            model=ensemble.ExtraTreesRegressor(random_state=6)
                
        if tuner_parameters==None:
            model.fit(self.X_train, self.y_train.values)
            y_pred = model.predict(self.X_test)
        else:                
            RF_cv = RandomizedSearchCV(estimator=model,param_distributions=tuner_parameters,n_iter=30,cv=5,n_jobs=-1)
            RF_cv.fit(self.X_train,self.y_train.values.ravel())
            model=RF_cv.best_estimator_
            model.fit(self.X_train, self.y_train.values)
            y_pred = model.predict(self.X_test)

        print("\n#########################################")
        print("         ENSEMBLE MODEL SELECTED")
        print("#########################################\n")

        print("\nModel :", model)
        print("\nTuner Parameters :", tuner_parameters)            
        print(f"\nModel Metrics\n")
        
        r2_score_test=round(metrics.r2_score(self.y_test, y_pred),2)*100
        mse_test=round(metrics.mean_squared_error(self.y_test, y_pred,squared=False),3)
        mae_test=round(metrics.mean_absolute_error(self.y_test, y_pred),3)

        print('R2 score of training data : {0} %'.format(round(metrics.r2_score(self.y_train, model.predict(self.X_train)),2)*100))
        print('R2 score of Testing data : {0} %'.format(round(metrics.r2_score(self.y_test, y_pred),2)*100))
        print('RMSE of of Testing data : {0}'.format(round(metrics.mean_squared_error(self.y_test, y_pred,squared=False),3)))
        print('MAE of Testing data : {0}'.format(round(metrics.mean_absolute_error(self.y_test, y_pred),3)))
        print("#########################################\n")
        
        filename=f'{self.models}/{select_model}-{timestamp}.pickle'
        pickle.dump(model, open(filename, "wb"))

        return select_model, r2_score_test,mse_test, mae_test

    def mixed_ensemble_models(self,select_model,estimator_models,tuner_parameters):
    
        if select_model=='bagging':        
            model=ensemble.BaggingRegressor(estimator_models,random_state=6)
        
        if select_model=='voting':        
            model=ensemble.VotingRegressor(estimator_models)

        if select_model=='adaBoost_dtree':
            print('not implemented yet')
        if select_model=='stacking':
            print('not implemented yet')
                
        if tuner_parameters==None:
            model.fit(self.X_train, self.y_train.values)
            y_pred = model.predict(self.X_test)
        else:                
            RF_cv = RandomizedSearchCV(estimator=model,param_distributions=tuner_parameters,n_iter=30,cv=5,n_jobs=-1)
            RF_cv.fit(self.X_train,self.y_train.values.ravel())
            model=RF_cv.best_estimator_
            model.fit(self.X_train, self.y_train.values)
            y_pred = model.predict(self.X_test)
            
        print(f"\n############ {select_model} MODEL METRICS #############")
        print('R2 score of training data : {0} %'.format(round(metrics.r2_score(self.y_train, model.predict(self.X_train)),2)*100))
        print('R2 score of Testing data : {0} %'.format(round(metrics.r2_score(self.y_test, y_pred),2)*100))
        print('RMSE of of Testing data : {0}'.format(round(metrics.mean_squared_error(self.y_test, y_pred,squared=False),3)))
        print('MAE of Testing data : {0}'.format(round(metrics.mean_absolute_error(self.y_test, y_pred),3)))
        print("#########################################\n")
        filename=f'{select_model}.pickle'
        pickle.dump(model, open(filename, "wb"))

    def tree_models(self,select_model:str,tuner_parameters=None):
        
        if select_model=='DTREE':        
            model=tree.DecisionTreeRegressor(random_state=6)
        
        if tuner_parameters==None:
            model.fit(self.X_train, self.y_train.values)
            y_pred = model.predict(self.X_test)
        else:                
            RF_cv = RandomizedSearchCV(estimator=model,param_distributions=tuner_parameters,n_iter=30,cv=5,n_jobs=-1)
            RF_cv.fit(self.X_train,self.y_train.values.ravel())
            model=RF_cv.best_estimator_
            model.fit(self.X_train, self.y_train.values)
            y_pred = model.predict(self.X_test)
            
        print(f"\n############ {select_model} MODEL METRICS #############")
        print('R2 score of training data : {0} %'.format(round(metrics.r2_score(self.y_train, model.predict(self.X_train)),2)*100))
        print('R2 score of Testing data : {0} %'.format(round(metrics.r2_score(self.y_test, y_pred),2)*100))
        print('RMSE of of Testing data : {0}'.format(round(metrics.mean_squared_error(self.y_test, y_pred,squared=False),3)))
        print('MAE of Testing data : {0}'.format(round(metrics.mean_absolute_error(self.y_test, y_pred),3)))
        print("#########################################\n")
        filename=f'{select_model}.pickle'
        pickle.dump(model, open(filename, "wb"))

    def compare_ml_models(self,list_ensemble_models,tuner_parameters):

        if list_ensemble_models==None:
            list_ensemble_models=['RF','GBR','hGBR','AdaBoost','ETree']
        
        metrics = pd.DataFrame()

        for model in list_ensemble_models:
            modelname,r2_score_test, mse_test, mae_test=self.ensemble_models(model, tuner_parameters)
            temp ={
            'Model': model,
            'R2':r2_score_test,
            'MSE': mse_test,
            'MAE': mae_test
            }
            
            metrics=metrics.append(temp,ignore_index=True)            
            metrics = metrics.sort_values(['R2'], ascending=False)

        print(f"\n############ MODELS PERFORMANCE #############")
        print(metrics)
        print(f"#############################################\n")

    def build_model(self,hp):
        model = keras.Sequential()
        for i in range(hp.Int('num_layers', 2, 30)):
            model.add(layers.Dense(units=hp.Int('units_' + str(i),
                                                min_value=32,
                                                max_value=3072,
                                                step=32),
                                activation='relu'))
        model.add(layers.Dense(3, activation='softmax'))
        model.add(layers.Dense(self.num_targets, activation='softmax'))
        model.compile(
            optimizer=keras.optimizers.Adam(
                hp.Choice('learning_rate', [1e-2, 1e-3, 1e-4])),
            loss='categorical_crossentropy',
        metrics=['accuracy'])
        return model
    
    def dnn_sequential_model_opt(self,num_max_trials,num_executions_per_trial,num_epochs,num_batch_size):
        """

        """       
                
        self.timestamp = copy.copy(timestamp_var)
        sys.stdout = Logger(f"{self.log_dir_path}/DNN-{self.timestamp}.log")
        LOG_DIR = f'{self.log_dir_path}/DNN-LOG-DIR-{self.timestamp}'
        tensorboard = TensorBoard(log_dir=LOG_DIR)    
        
        self.tuner = RandomSearch(
            self.build_model,
            objective='val_accuracy',        
            max_trials=num_max_trials,
            executions_per_trial=num_executions_per_trial,
            overwrite=True,
            directory=f'{self.log_dir_path}/DNN-TUNER-DIR-{self.timestamp}',
            project_name=LOG_DIR)

        print("\n########################")
        print(" Search for best model")    
        print("########################\n")

        print("self.X_train:",self.X_train)
        print("self.X_train_add_cols:",self.X_train_add_cols)

        self.tuner.search(x=self.X_train,
                    y=self.y_train,
                    epochs=num_epochs,
                    batch_size=num_batch_size,
                    callbacks=[tensorboard],
                    validation_data=(self.X_val, self.y_val))

        print("\n########################")
        print("Search Space Summary")    
        print("########################\n")
        self.tuner.search_space_summary()

        print("\n########################")
        print("Results Summary")    
        print("########################\n")
        
        self.tuner.results_summary()

        self.dnn_filename=f'{self.model_dir_path}/DNN-MODEL-{self.timestamp}.pickle'
        
        with open(self.dnn_filename, "wb") as f:
            pickle.dump(self.tuner, f)
    
    def dnn_compile_evaluate_model(self,optimizer,loss,metrics,epoch,batchsize):
        """_summary_

        Args:
            epoch (_type_): _description_
            batchsize (_type_): _description_

        Example
        # model.dnn_compile_evaluate_model(epoch=20,batchsize=64)
        """
        self.timestamp = copy.copy(timestamp_var)

        history = History()

        print('y_train\n', self.y_train)
        # print("X_test",self.X_test.isnull().values.any())
        # print("X_test",self.y_test.isnull().values.any())


        model=self.model
        #Configure the model
        model.compile(optimizer=optimizer,loss=loss,metrics=[metrics])
        print("\nself.X_test",self.X_test.shape)
        print("\nself.X_test",self.X_test.columns)

        # print("\nself.y_test",self.y_test.shape)

        history = model.fit(self.X_train,self.y_train, validation_data=(self.X_val, self.y_val),epochs=epoch,batch_size=batchsize)
        result = model.evaluate(self.X_test,self.y_test)

        for i in range(len(model.metrics_names)):
            print("Metric ",model.metrics_names[i],":",str(round(result[i],2)))

        # list all data in history
        print(history.history.keys())

        figure,axes = plt.subplots(nrows=1, ncols=2, figsize=(8,3))
    
        axes[0].plot(history.history['accuracy'])
        axes[0].plot(history.history['val_accuracy'],color='b')

        axes[0].set_title('Model Training & Validation loss a/cross epochs')
        axes[0].set_ylabel('Loss')
        # axes[0].set_ylim([0, 1])
        axes[0].set_xlabel('epoch')
        axes[0].legend(['train', 'test'], loc='upper left')

        # summarize history for loss
        axes[1].plot(history.history['val_loss'])
        axes[1].plot(history.history['loss'],color='b')
        axes[1].set_title('model loss')
        axes[1].set_ylabel('loss')
        # axes[1].set_ylim([0, 1])
        axes[1].set_xlabel('epoch')
        axes[1].legend([ 'validation loss', 'train'], loc='upper left')
        plt.show()

        # model.save(f'{self.model_dir_path}/DNN-bestmodel-{self.timestamp}')
        model.save(f'model.h5')

        result=model.evaluate(np.array(self.X_test), np.array(self.y_test))

        #Print the results
        for i in range(len(model.metrics_names)):
            print("Metric ",model.metrics_names[i],":",str(round(result[i],2)))
        
        
        self.predicted = model.predict(self.X_test)


        self.predicted = np.argmax (self.predicted, axis = 1)
        # y_prediction = model.predict(self.X_test)
        # self.predicted=y_prediction
        self.actual=self.y_test
        print('\nself.predicted',self.predicted)
        print('\nself.actual',self.actual)


        # self.actual=np.argmax(self.y_test, axis=1)
    
    def dnn_best_model(self,num_top_model:int,select_model_num:int):
        # import dill as pickle
        # tuner = pickle.load(open(self.dnn_filename,"rb"))

        with open(self.dnn_filename, 'rb') as file:
            tuner=pickle.load(file)

        tuner.results_summary()

        models = tuner.get_best_models(num_models=num_top_model)
        model = models[select_model_num]
        model.build(self.X_train.shape)
        model.summary()

        # history = History()

        # self.y_train = keras.utils.to_categorical(self.y_train, num_classes=self.num_targets)
        # self.y_val = keras.utils.to_categorical(self.y_val, num_classes=self.num_targets)

        # #Configure the model
        # model.compile(optimizer='adam',loss="categorical_crossentropy",metrics=["accuracy"])
        # history = model.fit(self.X_train,self.y_train, validation_data=(self.X_val, self.y_val),epochs=epoch,batch_size=batchsize)
        # result = model.evaluate(self.X_test,self.y_test)

        # for i in range(len(model.metrics_names)):
        #     print("Metric ",model.metrics_names[i],":",str(round(result[i],2)))

        # # list all data in history
        # print(history.history.keys())

        # figure,axes = plt.subplots(nrows=1, ncols=2, figsize=(8,3))
        # axes[0].plot(history.history['accuracy'])
        # axes[0].plot(history.history['val_accuracy'],color='b')
        # axes[0].set_title('model accuracy')
        # axes[0].set_ylabel('accuracy')
        # axes[0].set_ylim([0, 1])
        # axes[0].set_xlabel('epoch')
        # axes[0].legend(['train', 'test'], loc='upper left')

        # # summarize history for loss
        # axes[1].plot(history.history['val_loss'])
        # axes[1].plot(history.history['loss'],color='b')
        # axes[1].set_title('model loss')
        # axes[1].set_ylabel('loss')
        # axes[1].set_ylim([0, 1])
        # axes[1].set_xlabel('epoch')
        # axes[1].legend([ 'validation loss', 'train'], loc='upper left')
        # plt.show()

        # model.save(f'{self.model_dir_path}/DNN-bestmodel-{self.timestamp}')
        # score=model.evaluate(np.array(self.X_test), np.array(self.y_test))
        
        # y_prediction = model.predict(self.X_test)
        
        # self.predicted = np.argmax (y_prediction, axis = 1)
        # self.actual=np.argmax(self.y_test, axis=1)

        self.model=model
    
    
    def dnn_custom_model(self, params):
        """
        Constructs a custom deep neural network (DNN) classification model based on the provided parameters.

        Args:
            params (dict): A dictionary containing the parameters for constructing the DNN model.
                - 'input_dim' (int): Input dimensionality of the first layer.
                - 'layer_sizes' (list of int): List containing the number of neurons for each hidden layer.
                - 'activations' (list of str): List containing the activation functions for each hidden layer.
                - 'dropout_rates' (optional, list of float): List containing the dropout rates for each hidden layer.

        Example:
            To construct a DNN classification model with the following parameters:
            - Input dimension: 10
            - Hidden layer sizes: [150, 350, 350, 350, 350]
            - Activation functions: ["relu", "relu", "relu", "relu", "relu"]
            - Dropout rates: [0.2, 0.3, 0.4, 0.5]

            >>> dnn_params = {
            ...     'input_dim': 10,
            ...     'layer_sizes': [150, 350, 350, 350, 350],
            ...     'activations': ["relu", "relu", "relu", "relu", "relu"],
            ...     'dropout_rates': [0.2, 0.3, 0.4, 0.5]
            ... }
            >>> self.dnn_custom_classification_model(dnn_params)
        """

        model = models.Sequential()
        model.add(layers.Dense(params['layer_sizes'][0], input_dim=self.X_train.shape[1], activation=params['activations'][0]))
        for size, activation, dropout_rate in zip(params['layer_sizes'][1:], params['activations'][1:], params.get('dropout_rates', [])):
            model.add(layers.Dense(size, activation=activation))
            if dropout_rate:
                model.add(layers.Dropout(dropout_rate))
        # Modify output layer for classification
        model.add(layers.Dense(self.num_targets, activation=params['output_layer_actvfunc']))  # Adjust 'num_classes' based on your classification problem
        self.model = model
        
    def accuracy_baseline(self, y_train, y_test):
        """
        Calculate the accuracy baseline prediction and evaluate its performance using accuracy score.

        Args:
            y_train (array-like): Array containing the target variable (dependent variable) values in the training set.
            y_test (array-like): Array containing the target variable (dependent variable) values in the test set.

        Returns:
            float: Accuracy score of the baseline predictions.
        """
        # Calculate the most frequent class in the training set
        most_frequent_class = np.argmax(np.bincount(y_train))
        
        # Use the most frequent class as the prediction for all samples in the test set
        baseline_predictions = np.full_like(y_test, fill_value=most_frequent_class)
        
        # Calculate the accuracy score between the baseline predictions and actual values in the test set
        accuracy_baseline = metrics.accuracy_score(y_test, baseline_predictions)
        
        return accuracy_baseline

    
    def model_metrics(self):
        
        print("Accuracy Score: ", metrics.accuracy_score(self.y_test, self.predicted))
        print('\n')
        print("Confusion Matrix \n \n",metrics.confusion_matrix(self.y_test, self.predicted))
        print('\n')
        print("Classification Report \n \n", metrics.classification_report(self.y_test, self.predicted))

        self.actual=self.endocder.inverse_transform(self.actual)
        self.predicted=self.endocder.inverse_transform(self.predicted)

        pred_table = pd.DataFrame()
        pred_table['actual'] = self.actual
        pred_table['predicted'] = self.predicted
        
        self.pred_table=pred_table.reset_index()
        self.pred_table = self.pred_table[self.pred_table.columns.drop((self.pred_table.filter(regex='ndex')))]
        
        self.X_test_add_cols=self.X_test_add_cols.reset_index()
        self.X_test_add_cols = self.X_test_add_cols[self.X_test_add_cols.columns.drop((self.X_test_add_cols.filter(regex='ndex')))]
        
        prediction_dataset = pd.concat([self.X_test_add_cols,self.pred_table], axis=1)
        prediction_dataset.to_csv('IntTesting-prediction-dataset.csv')

        return prediction_dataset

    def ext_testing(self,ext_testing_dataset):

        self.ext_X_test=ext_testing_dataset.drop([self.target], axis = 1)
        self.ext_y_test = ext_testing_dataset.loc[:,self.target]

        self.ext_X_test_add_cols=self.ext_X_test.loc[:,self.additional_cols_list]
        self.ext_X_test=self.ext_X_test.drop(self.additional_cols_list, axis = 1)
        
        ext_y_test_enc = self.endocder.transform(self.ext_y_test)        
        self.ext_y_test = to_categorical(ext_y_test_enc,num_classes=self.num_targets)

        print("\nself.ext_X_test",self.ext_X_test.shape)
        print("\nself.ext_y_test",self.ext_y_test.shape)

        result=self.model.evaluate(self.ext_X_test, self.ext_y_test)

        #Print the results
        for i in range(len(self.model.metrics_names)):
            print("Metric ",self.model.metrics_names[i],":",str(round(result[i],2)))

        self.ext_predicted = self.model.predict(self.ext_X_test)


        self.ext_predicted = np.argmax (self.predicted, axis = 1)
        
        


        # score=self.model.evaluate(np.array(self.ext_X_test), np.array(self.ext_y_test))
        # score = self.model.evaluate(self.ext_X_test,self.ext_y_test)
        # print('score',score)
        # self.ext_predicted  = np.argmax(self.model.predict(self.ext_X_test), axis=-1)

        return self.ext_y_test, self.ext_predicted

        
class Logger(object):
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "a")
    def __getattr__(self, attr):
        return getattr(self.terminal, attr)
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)      
    def flush(self):
        self.terminal.flush()
        self.log.flush()
