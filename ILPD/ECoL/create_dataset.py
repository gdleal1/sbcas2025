# Create datasets for experiments, separing them acording to a sensitive attribute
import pandas as pd

# Function to discretize the non-numeric columns of the dataset (binary attribute)
def discretize(x,attr1,attr2=None):
    if x == attr1:
        return 0
    elif attr2 == None or x == attr2:
        return 1
    else:
        raise

# Discretize the non-numeric columns of the dataset
original_dataset = pd.read_csv('datasets/ILPD.csv')
original_dataset['Sex'] = original_dataset['Sex'].apply(lambda x: discretize(x,'Female','Male'))

original_dataset['Diagnosis'] = original_dataset['Diagnosis'].apply(lambda x: discretize(x,2,1))

# Separate the original dataset  according to a sensitive attribute
male_dataset= original_dataset[original_dataset['Sex'] == 1]
female_dataset = original_dataset[original_dataset['Sex'] == 0]

# Remove the sensitive attribute column of the datasets
male_dataset = male_dataset.drop(columns=['Sex'])
female_dataset = female_dataset.drop(columns=['Sex'])

# Save the datasets
male_dataset.to_csv('datasets/male-discretized.csv', index=False)
female_dataset.to_csv('datasets/female-discretized.csv', index=False)
original_dataset.to_csv('datasets/ILPD-discretized.csv', index=False)
