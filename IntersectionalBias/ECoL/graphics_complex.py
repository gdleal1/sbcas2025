# Create a graphic with the complexity measures for a dataset
import pandas as pd
import matplotlib.pyplot as plt

NAME_DATASET = 'female'
TITLE = f'Complexity measures of the {NAME_DATASET} dataset'

def create():
    
    file_path = f'outputs/outputs_complex/output-{NAME_DATASET}.csv'  
    data = pd.read_csv(file_path)

    # Bar graphic
    plt.figure(figsize=(10, 6))
    plt.bar(data['Complexity Measure'], data['Value'], color='cornflowerblue')

    # Line graphic
    plt.plot(data['Complexity Measure'], data['Value'], color='darkorange', label='Linha')

    plt.title(TITLE)
    plt.xlabel('Complexity Measure')
    plt.ylabel('Value')
    plt.xticks(rotation=45)  
    plt.tight_layout()  

    graphic_path = f"graphics/graphics_complex/{NAME_DATASET}_graphic.png"
    plt.savefig(graphic_path, dpi=300)

if __name__ == "__main__":
    create()
