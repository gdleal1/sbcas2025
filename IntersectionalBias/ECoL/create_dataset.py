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
original_dataset = pd.read_csv('datasets/intersectional-bias.csv')
original_dataset['Sex'] = original_dataset['Sex'].apply(lambda x: discretize(x,'Female','Male'))
original_dataset['Race'] = original_dataset['Race'].apply(lambda x: discretize(x,'White'))
original_dataset['Housing'] = original_dataset['Housing'].apply(lambda x: discretize(x,'Stable','Unstable'))
original_dataset['Delay'] = original_dataset['Delay'].apply(lambda x: discretize(x,'No','Yes'))

# Separate the original dataset  according to a sensitive attribute
male_dataset= original_dataset[original_dataset['Sex'] == 1]
female_dataset = original_dataset[original_dataset['Sex'] == 0]
nonWhite_dataset = original_dataset[original_dataset['Race'] == 1]
white_dataset = original_dataset[original_dataset['Race'] == 0]

# Remove the sensitive attribute column of the datasets
male_dataset = male_dataset.drop(columns=['Sex'])
female_dataset = female_dataset.drop(columns=['Sex'])
white_dataset = white_dataset.drop(columns=['Race'])
nonWhite_dataset = nonWhite_dataset.drop(columns=['Race'])

# Save the datasets
male_dataset.to_csv('datasets/male-discretized.csv', index=False)
female_dataset.to_csv('datasets/female-discretized.csv', index=False)
white_dataset.to_csv('datasets/white-discretized.csv', index=False)
nonWhite_dataset.to_csv('datasets/nonWhite-discretized.csv', index=False)
original_dataset.to_csv('datasets/intersectional-bias-discretized.csv', index=False)