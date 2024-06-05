#!/usr/bin/env python
# coding: utf-8

import nbformat
import codecs
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier, GradientBoostingRegressor, AdaBoostClassifier, AdaBoostRegressor
from xgboost import XGBClassifier, XGBRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.svm import SVC, SVR
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, mean_squared_error, r2_score
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from nbconvert import HTMLExporter

# Attempt to import ydata_profiling and handle the case where it is not installed
try:
    from ydata_profiling import ProfileReport
    profiling_available = True
except ModuleNotFoundError:
    print("Warning: ydata_profiling module not found. Profiling functionality will be disabled.")
    profiling_available = False

def func(file_loc, header_row_number=0):
    try:
        if header_row_number == 0:
            df = pd.read_csv(file_loc)
        else:
            df = pd.read_csv(file_loc, header=header_row_number)

        print(df.head(3))

        # Identify categorical and continuous variables
        categorical_vars = df.select_dtypes(include=['object']).columns
        continuous_vars = df.select_dtypes(exclude=['object']).columns

        # Encode categorical variables
        for col in categorical_vars:
            df[col] = LabelEncoder().fit_transform(df[col])

        print(df.dtypes)
        # Check for missing values in each column
        missing_values = df.isnull().sum()
        if missing_values.any():
            print("\nColumns with Missing Values:")
            print(missing_values[missing_values > 0])

        # Handle missing values
        df = df.fillna(df.mean())  # Fill numeric columns with mean
        df = df.fillna(df.mode().iloc[0])  # Fill categorical columns with mode

        # Statistical analysis
        print("\nStatistical Summary:\n", df.describe())

        # Plot distributions of numerical columns
        for col in continuous_vars:
            fig = px.histogram(df, x=col, nbins=20, title=f'Distribution of {col}')
            fig.show()

        # Plot counts of categorical columns
        for col in categorical_vars:
            fig = px.histogram(df, x=col, title=f'Count of Each Category in {col}')
            fig.show()

        # Correlation heatmap
        correlation_matrix = df.corr()
        fig = px.imshow(correlation_matrix, title='Correlation Heatmap', aspect='auto')
        fig.show()

        # Pairplot of all continuous variables
        fig = px.scatter_matrix(df, dimensions=continuous_vars, title='Scatter Matrix of Continuous Variables')
        fig.show()

        # Box plots for continuous variables
        for col in continuous_vars:
            fig = px.box(df, y=col, title=f'Box Plot of {col}')
            fig.show()

        # Violin plots for continuous variables
        for col in continuous_vars:
            fig = px.violin(df, y=col, title=f'Violin Plot of {col}')
            fig.show()

        # Bar plots for categorical variables
        for col in categorical_vars:
            fig = px.bar(df, x=col, title=f'Bar Plot of {col}')
            fig.show()

        # Data normalization
        scaler_choice = input('Choose a scaler: StandardScaler (S) or MinMaxScaler (M): ')
        if scaler_choice.upper() == 'S':
            scaler = StandardScaler()
        elif scaler_choice.upper() == 'M':
            scaler = MinMaxScaler()
        else:
            print("Invalid choice, proceeding without scaling.")
            scaler = None

        target = input(f'\nFrom the list of columns to choose from: {df.columns}\n Specify which column that you want to use as target variable: \n')
        id_col = input(' If there is an ID column you would like to exclude from analysis, please specify the ID column: If not, press Enter')

        if id_col in df.columns:
            X = df.drop([target], axis=1).drop(id_col, axis=1)
            y = df[target]
        else:
            X = df.drop(target, axis=1)
            y = df[target]

        # Apply scaling
        if scaler:
            X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

        # VIF dataframe
        vif_data = pd.DataFrame()
        vif_data["feature"] = X.columns
        vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
        print("\nVariance Inflation Factor (VIF):\n", vif_data)

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        print("Training set shape:", X_train.shape, y_train.shape)
        print("Testing set shape:", X_test.shape, y_test.shape)

        inp = input('Which ML model would you like to perform? Enter C for Classification, R for Regression, SR for OLS Regression, CL for Clustering, PCA for Dimensionality Reduction: ')
        y_pred = None

        if inp.upper() == 'C':
            model_choice = input('Choose a model: RF for RandomForest, LR for LogisticRegression, SVM for SupportVectorMachine, GB for GradientBoosting, AB for AdaBoost, XGB for XGBoost: ')
            if model_choice.upper() == 'RF':
                clf = RandomForestClassifier(n_estimators=100, random_state=42)
            elif model_choice.upper() == 'LR':
                clf = LogisticRegression(random_state=42)
            elif model_choice.upper() == 'SVM':
                clf = SVC(random_state=42)
            elif model_choice.upper() == 'GB':
                clf = GradientBoostingClassifier(n_estimators=100, random_state=42)
            elif model_choice.upper() == 'AB':
                clf = AdaBoostClassifier(n_estimators=100, random_state=42)
            elif model_choice.upper() == 'XGB':
                clf = XGBClassifier(n_estimators=100, random_state=42)
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            print("Accuracy:", accuracy)
            precision = precision_score(y_test, y_pred, average='micro')
            recall = recall_score(y_test, y_pred, average='micro')
            print("Precision:", precision)
            print("Recall:", recall)
            conf_matrix = confusion_matrix(y_test, y_pred)
            fig = px.imshow(conf_matrix, text_auto=True, title='Confusion Matrix')
            fig.show()

        elif inp.upper() == 'R':
            model_choice = input('Choose a model: RF for RandomForest, LR for LinearRegression, SVM for SupportVectorMachine, GB for GradientBoosting, AB for AdaBoost, XGB for XGBoost: ')
            if model_choice.upper() == 'RF':
                clf = RandomForestRegressor(random_state=42)
            elif model_choice.upper() == 'LR':
                clf = LinearRegression()
            elif model_choice.upper() == 'SVM':
                clf = SVR()
            elif model_choice.upper() == 'GB':
                clf = GradientBoostingRegressor(n_estimators=100, random_state=42)
            elif model_choice.upper() == 'AB':
                clf = AdaBoostRegressor(n_estimators=100, random_state=42)
            elif model_choice.upper() == 'XGB':
                clf = XGBRegressor(n_estimators=100, random_state=42)
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            print("Mean Squared Error:", mse)
            r2 = r2_score(y_test, y_pred)
            print("R ^2:", r2)

            # Scatter plot of actual vs predicted
            fig = px.scatter(x=y_test, y=y_pred, labels={'x': 'Actual', 'y': 'Predicted'}, title='Actual vs Predicted')
            fig.add_shape(type="line", line=dict(dash='dash'), x0=y_test.min(), y0=y_test.min(), x1=y_test.max(), y1=y_test.max())
            fig.show()

        elif inp.upper() == 'SR':
            clf = sm.OLS(y_train, X_train).fit()
            print(clf.summary())
            y_pred = clf.predict(X_test)

        elif inp.upper() == 'CL':
            model_choice = input('Choose a clustering model: KMeans for KMeans, DBSCAN for DBSCAN: ')
            if model_choice.upper() == 'KMEANS':
                n_clusters = int(input("Enter the number of clusters: "))
                clf = KMeans(n_clusters=n_clusters, random_state=42)
            elif model_choice.upper() == 'DBSCAN':
                eps = float(input("Enter the eps value: "))
                min_samples = int(input("Enter the min_samples value: "))
                clf = DBSCAN(eps=eps, min_samples=min_samples)
            cluster_labels = clf.fit_predict(X)
            fig = px.scatter_matrix(df, dimensions=continuous_vars, color=cluster_labels, title='Clustering Results')
            fig.show()
            y_pred = cluster_labels

        elif inp.upper() == 'PCA':
            n_components = int(input("Enter the number of components for PCA: "))
            pca = PCA(n_components=n_components)
            X_pca = pca.fit_transform(X)
            explained_variance = pca.explained_variance_ratio_
            print("Explained variance by each component:", explained_variance)
            fig = px.scatter_matrix(pd.DataFrame(X_pca), title='PCA Results')
            fig.show()
            y_pred = X_pca

        else:
            print("Invalid model type selected.")
            return

        if y_pred is not None:
            id_column = y_test.index if id_col in df.columns else pd.Series(range(len(y_test)))
            prediction_df = pd.DataFrame({'ID': id_column, 'prediction': y_pred})
            prediction_df.to_csv('prediction_result.csv', index=False)
            print("Prediction output is stored in prediction_result.csv")
        output_file_name = 'output.html'
        exporter = HTMLExporter()
        output_notebook = nbformat.v4.new_notebook()
        output_notebook.cells.append(nbformat.v4.new_code_cell(codecs.open(__file__, encoding='utf-8').read()))
        output, resources = exporter.from_notebook_node(output_notebook)
        codecs.open(output_file_name, 'w', encoding='utf-8').write(output)
        print("Your file containing the output is stored in output.html")

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except pd.errors.EmptyDataError as e:
        print(f"No data: {e}")
    except pd.errors.ParserError as e:
        print(f"Parsing error: {e}")
    except KeyError as e:
        print(f"Key error: {e}")
    except ValueError as e:
        print(f"Value error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")