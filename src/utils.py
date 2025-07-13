from imblearn.under_sampling import RandomUnderSampler
import pandas as pd

def balance_data(df):
    X = df.drop("Label", axis=1)
    y = df["Label"]
    rus = RandomUnderSampler()
    X_bal, y_bal = rus.fit_resample(X, y)
    return pd.concat([pd.DataFrame(X_bal, columns=X.columns), pd.DataFrame(y_bal, columns=["Label"])], axis=1)
