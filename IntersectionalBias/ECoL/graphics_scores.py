# Create a graphic with the scores by measure group for a dataset

import pandas as pd
import matplotlib.pyplot as plt

NAME_DATASET = 'nonWhite'
TITLE = f'Score by measure group for {NAME_DATASET} dataset'

def create():
    
    file_path = f'outputs/outputs_score/score-{NAME_DATASET}-output.csv'  
    scores_df = pd.read_csv(file_path)

    # Bar graphic
    plt.figure(figsize=(8, 6))
    plt.bar(scores_df['Measure Group'], scores_df['Score'], color=['blue', 'orange', 'green'])
    plt.title(TITLE, fontsize=16)
    plt.ylim(0, 0.7)
    plt.xticks(rotation=45, fontsize=12)
    plt.tight_layout()

    graphic_path = f"graphics/graphics_scores/score-{NAME_DATASET}_graphic.png"
    plt.savefig(graphic_path, dpi=300)
    

if __name__ == "__main__":
    create()
