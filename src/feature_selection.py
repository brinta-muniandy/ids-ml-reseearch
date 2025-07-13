import pandas as pd
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.tree import DecisionTreeClassifier

def drop_constant_columns(df):
    return df.loc[:, df.nunique() > 1]

def drop_duplicate_columns(df):
    duplicates = set()
    columns = df.columns
    for i in range(len(columns)):
        for j in range(i+1, len(columns)):
            if df[columns[i]].equals(df[columns[j]]):
                duplicates.add(columns[j])
    return df.drop(columns=list(duplicates))

def apply_feature_selection(df, n_features=30):
    X = df.drop("Label", axis=1)
    y = df["Label"]
    model = DecisionTreeClassifier()
    sfs = SequentialFeatureSelector(model, n_features_to_select=n_features, direction="backward").fit(X, y)
    selected = X.columns[sfs.get_support()].tolist()
    selected.append("Label")
    return df[selected]
