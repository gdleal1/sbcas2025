# Create a graphic with the percentage of increase in complexity measures for a dataset in relation to another dataset
import pandas as pd
import matplotlib.pyplot as plt

NAME_DS1 = 'female'
NAME_DS2 = 'male'
TITLE = f'Increase in complexity measures of the {NAME_DS1} dataset in relation to the {NAME_DS2} dataset'

def create():
    
    file_path = f'outputs/outputs_increase/{NAME_DS1}-{NAME_DS2}-increase.csv'  
    df_result = pd.read_csv(file_path)

    # Order data by the increase percentage
    df_result = df_result.sort_values(by='Increase (%)', ascending=True)

    # Creating the bar graphic
    plt.figure(figsize=(10, 6))
    plt.barh(df_result['Complexity Measure'], df_result['Increase (%)'], color='cornflowerblue')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Linha no zero para referência

    # Personalizing the graphic
    plt.title(TITLE, fontsize=14)
    plt.xlabel('Increase (%)', fontsize=12)
    plt.ylabel('Complexity Measure', fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    plt.tight_layout()
    graphic_path = f"graphics/graphics_increase/{NAME_DS1}-{NAME_DS2}-increase_graphic.png"
    plt.savefig(graphic_path, dpi=300)
    

if __name__ == "__main__":
    create()