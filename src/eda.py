import matplotlib.pyplot as plt
import seaborn as sns

def data_properties(df, name="Dataset"):
    print(f"{name}")
    print('Shape:', df.shape)
    print('Info:')
    print(df.info())
    print('Label distribution:')
    print(df['Label'].value_counts())
    print("\n" + "-"*50 + "\n")

def visualize_bar(df, title_suffix=""):
    if 'Label' not in df.columns:
        return
    label_counts = df['Label'].value_counts()
    colors = plt.cm.tab10(range(len(label_counts)))
    plt.figure(figsize=(10,6))
    plt.bar(label_counts.index, label_counts.values, color=colors)
    plt.title(f'Label Distribution - {title_suffix}')
    plt.xlabel('Label')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualize_pie(df, title_suffix=""):
    if 'Label' not in df.columns:
        return
    plt.figure(figsize=(8,8))
    plt.title(f'Label Distribution - {title_suffix}')
    plt.pie(df['Label'].value_counts(), labels=df['Label'].unique(), autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.show()
