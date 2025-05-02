# Create a graphic with the difference of the complexity measures between two datasets
import pandas as pd
import matplotlib.pyplot as plt

NAME_DS1 = 'female'
NAME_DS2 = 'male'
TITLE = f'Difference of the complexity measures between {NAME_DS1} and {NAME_DS2} datasets'


def create():
    
    file_path = f'outputs/outputs_diff/{NAME_DS1}-{NAME_DS2}-diff.csv'  
    data = (pd.read_csv(file_path)).head(14)

    # Different colors for positive and negative values
    colors = ['cornflowerblue' if value > 0 else 'lightcoral' for value in data['Value']]

    # Bar graphic
    plt.figure(figsize=(10, 6))
    plt.bar(data['Complexity Measure'], data['Value'], color=colors)

    # Line graphic
    plt.plot(data['Complexity Measure'], data['Value'], color='darkorange', label='Linha')

    # Set y-axis limits
    plt.ylim(-0.15, 0.3)

    plt.title(TITLE)
    plt.xlabel('Complexity Measure')
    plt.ylabel('Value')
    plt.xticks(rotation=45)  
    plt.tight_layout()  

    graphic_path = f"graphics/graphics_diff/{NAME_DS1}-{NAME_DS2}-diff_graphic.png"
    plt.savefig(graphic_path, dpi=300)

if __name__ == "__main__":
    create()
