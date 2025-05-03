# Calculates a score for each complexity measure group
import pandas as pd

# Calculates the average magnitude of the variation in the group.
def mean_absolute(data):
    return data['Value'].abs().mean()

# Calculates the highest individual value in the group
def max_absolute(data):
    return data['Value'].abs().max()

# Calculates the standard deviation of the group
def std_dev(data):
    return data['Value'].std()

# Calculates the score for the group
def score(data):
    return round((mean_absolute(data) + max_absolute(data) + std_dev(data)),2)



NAME_OUTPUT = 'nonWhite'
output_path = f'outputs/outputs_complex/output-{NAME_OUTPUT}.csv'  
data = pd.read_csv(output_path)

# Feature-Based Measures
F_measures = data.iloc[0:5]

# Neighborhood Measures
N_measures = data.iloc[5:11]

# Linearity Measures
L_measures = data.iloc[11:14]


# Calculate scores
scores = {
    'Measure Group': ['Feature-Based', 'Neighborhood', 'Linearity'],
    'Score': [
        score(F_measures),
        score(N_measures),
        score(L_measures),
    ]
}

# Create a DataFrame for the scores
scores_df = pd.DataFrame(scores)

# Save to CSV
output_csv_path = f'outputs/outputs_score/score-{NAME_OUTPUT}-output.csv'
scores_df.to_csv(output_csv_path, index=False)