# Generate graphic representation of the PCA for the dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

DATASET = 'male'

def createGraphic2D(feature_columns_scaled, target_column):
    pca = PCA(n_components=2)  # Reduce to 2 dimensions
    feature_columns_pca = pca.fit_transform(feature_columns_scaled)
    
    print(f"Variância explicada pelas 2 primeiras componentes principais: {pca.explained_variance_ratio_}")
    print(f"Variância total explicada pelo PCA 2D: {sum(pca.explained_variance_ratio_):.4f}")
    # Graphic representation of the PCA 2D
    plt.figure(figsize=(8, 6))
    for class_id in np.unique(target_column):
        plt.scatter(
            feature_columns_pca[target_column == class_id, 0],  # First principal component
            feature_columns_pca[target_column == class_id, 1],  # Second principal component
            label=f"Diagnosis {class_id}"
        )

    plt.legend(title="Classes")

    plt.xlabel("First principal component")
    plt.ylabel("Second principal component")
    plt.title(f"PCA - Dispersion by classes for {DATASET} dataset")
    plt.savefig(f'graphics/graphics_PCA/PCA(2D)-{DATASET}.png')  



def createGraphic3D(feature_columns_scaled, target_column):
    
    pca = PCA(n_components=3)
    feature_columns_pca = pca.fit_transform(feature_columns_scaled)

    # Graphic representation of the PCA 3D
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    for class_id in np.unique(target_column):
        ax.scatter(
            feature_columns_pca[target_column == class_id, 0],  # First principal component
            feature_columns_pca[target_column == class_id, 1],  # Second principal component
            feature_columns_pca[target_column == class_id, 2],  # Third principal component
            label=f"Diagnosis {class_id}"  
        )

    # Rótulos dos eixos
    ax.set_xlabel("First Principal Component")
    ax.set_ylabel("Second Principal Component")
    ax.set_zlabel("Third Principal Component")

    ax.set_title(f"PCA - 3D Dispersion by Classes for {DATASET} dataset")
    ax.legend(title="Classes")
    ax.view_init(elev=30, azim=70)
    plt.savefig(f'graphics/graphics_PCA/PCA(3D)-{DATASET}.png')


# Load the dataset
dataset = pd.read_csv(f"datasets/{DATASET}-discretized.csv")

target_column = dataset.iloc[:, -1].values  # Last column (target)
feature_columns = dataset.iloc[:, :-1].values  # All columns except last (features)

# Standardize the features to have mean 0 and variance 1.
scaler = StandardScaler()
feature_columns_scaled = scaler.fit_transform(feature_columns)

createGraphic2D(feature_columns_scaled, target_column)
#createGraphic3D(feature_columns_scaled, target_column)




