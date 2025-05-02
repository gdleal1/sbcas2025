# Create a graphic with the complexity measures for a dataset

import pandas as pd
import matplotlib.pyplot as plt

TITLE = "Pre-training metrics for measuring bias"


def create():
    
    file_path = 'metrics-diabetes.csv'
    data = pd.read_csv(file_path)

    # Different colors for positive and negative values
    colors = ['cornflowerblue' if value > 0 else 'lightcoral' for value in data['Value']]

    # Bar graphic
    plt.figure(figsize=(10, 6))
    plt.bar(data['Metric'], data['Value'], color=colors)

    # Line graphic
    plt.plot(data['Metric'], data['Value'], color='darkorange', label='Linha')

    plt.title(TITLE)
    plt.xlabel('Metric')
    plt.ylabel('Value')
    plt.xticks(rotation=45)  
    plt.tight_layout()  

    graphic_path = f"metrics_diabetes_graphic.png"
    plt.savefig(graphic_path, dpi=300)

if __name__ == "__main__":
    create()
