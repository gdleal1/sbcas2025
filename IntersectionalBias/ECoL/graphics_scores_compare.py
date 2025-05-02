# Generates graphs of score for groups of complexity measures for comparison according to the sensitive attributes 

import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

# Define the names of the CSV files and their respective labels
datasets = {
    "outputs/outputs_score/score-intersectional-bias-output.csv": "Original",
    "outputs/outputs_score/score-female-output.csv": "Female",
    "outputs/outputs_score/score-male-output.csv": "Male",
    "outputs/outputs_score/score-nonWhite-output.csv": "Non-White",
    "outputs/outputs_score/score-white-output.csv": "White"
}

# Create a dictionary to store the scores
data = {}

# Read each CSV file and store the values
for file, label in datasets.items():
    df = pd.read_csv(file)
    data[label] = df.set_index("Measure Group")["Score"]

# Create a DataFrame by combining data
score_df = pd.DataFrame(data)

# Graphic for Original, Women and Men
plt.figure(figsize=(12, 6))
score_df[["Original", "Female", "Male"]].plot(
    kind="bar", colormap="viridis", width=0.8)
plt.xlabel("")
plt.ylabel("Score")
legend = plt.legend(title="Dataset", loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=3)
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("graphics/graphics_scores/original-female-male-compare.png")


# Graphic for Original, White and Non-White
plt.figure(figsize=(12, 6))
score_df[["Original", "Non-White", "White"]].plot(
    kind="bar", colormap="plasma", width=0.8)
plt.xlabel("")
plt.ylabel("Score")
legend = plt.legend(title="Dataset", loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=3)
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("graphics/graphics_scores/original-nonWhite-white-compare.png")



