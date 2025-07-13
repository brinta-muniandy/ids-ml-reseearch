# 🚨 Intrusion Detection Using Machine Learning (CSE-CIC-IDS 2018)

This repository contains a complete ML pipeline applied to the [CSE-CIC-IDS2018 dataset](https://www.unb.ca/cic/datasets/ids-2018.html), aimed at detecting network intrusions and malicious packets using various traditional and ensemble machine learning classifiers.

---

## 📊 Dataset

- **Name:** CSE-CIC-IDS2018
- **Source:** Canadian Institute for Cybersecurity
- **Contains:** Realistic network traffic scenarios (e.g., DoS, DDoS, Botnet, Infiltration)

The dataset is not included in this repo. You can download it from the [official site](https://www.unb.ca/cic/datasets/ids-2018.html) and place it under the `data/` directory.

---

## 📁 Directory Structure

```bash
.
├── data/
│   ├── raw/                     # Instructions or placeholder for raw .csv files
│   └── processed/              # Cleaned + transformed file like `cleaned_features.csv`
├── notebooks/              # Google Colab notebook with research steps
├── src/                    # Modular Python scripts for reuse
├── requirements.txt        # All required packages
└── README.md               # You are here!
```

---

## 🧪 Methodology

The end-to-end process is implemented in Python using Jupyter/Colab:

### 1. 📥 Data Loading & Cleaning
- Merge CSVs
- Drop redundant headers
- Fix data types

### 2. 🧹 Preprocessing
- Drop NaNs/Infinities
- Drop constant & duplicate columns
- Encode target to binary (`Benign` = 0, `Malicious` = 1)
- Normalize features using `RobustScaler`

### 3. 📊 Exploratory Data Analysis (EDA)
- Label distributions via bar/pie charts
- Summary stats & imbalance check

### 4. 🎯 Feature Selection
- Backward Sequential Feature Selector
- Correlation matrix for multicollinearity removal

### 5. ⚖️ Data Balancing
- Using `RandomUnderSampler` to balance benign/malicious classes

### 6. 🤖 Model Training
Evaluated models using 10-fold Cross Validation:
- Decision Tree
- Random Forest
- LightGBM
- K-Nearest Neighbors
- Gaussian Naive Bayes
- Support Vector Machine

Confusion matrices and classification reports are generated for each.

---

## 📈 Sample Results (TBD)

Each classifier's results are visualized using heatmaps and metrics like:

- Accuracy
- Precision / Recall / F1
- ROC-AUC

Plots are auto-generated within the notebook.

---

## 🧰 Installation

To install required dependencies:

```bash
pip install -r requirements.txt
```

Make sure to use a Python 3.8+ environment with Jupyter or Google Colab support.

---

## 🧑‍💻 Run the Notebook

> Option 1: Google Colab  
Click to open in Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-UTyyaTjTggbmMN1jqcZ8oH0uIMbN2su)

> Option 2: Local Jupyter
```bash
jupyter notebook notebooks/main.ipynb
```

---

## 🪪 License

MIT License. See [`LICENSE`](./LICENSE) for more information.

---

## 🙌 Acknowledgements

- Dataset: [Canadian Institute for Cybersecurity (CIC)](https://www.unb.ca/cic/)
- Libraries: scikit-learn, LightGBM, CatBoost, matplotlib, seaborn, pandas, numpy, imbalanced-learn
