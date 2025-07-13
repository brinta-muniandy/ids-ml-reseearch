from sklearn.model_selection import cross_val_predict
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def train_model(model, X, y, cv, model_name="Model"):
    y_pred = cross_val_predict(model, X, y, cv=cv)
    cm = confusion_matrix(y, y_pred)
    print(f"=== {model_name} ===")
    print("Confusion Matrix:")
    print(cm)
    print("Classification Report:")
    print(classification_report(y, y_pred))
    print("ROC AUC Score:", roc_auc_score(y, y_pred))
    plot_confusion_matrix(cm, model_name)

def plot_confusion_matrix(cm, title):
    group_counts = ["{0:0.0f}".format(value) for value in cm.flatten()]
    group_percentages = ["{0:.2%}".format(value) for value in cm.flatten()/cm.sum()]
    labels = [f"{v1}\n{v2}" for v1, v2 in zip(group_counts, group_percentages)]
    labels = np.asarray(labels).reshape(cm.shape)
    sns.heatmap(cm, annot=labels, fmt='', cmap='Blues', cbar=False,
                xticklabels=['Benign', 'Malicious'], yticklabels=['Benign', 'Malicious'])
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title(title)
    plt.show()
