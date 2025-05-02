# Generates graphs of dataset complexity measures for comparison according to the sensitive attributes 

import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

# Define the names of the CSV files and their respective labels
datasets = {
    "outputs/outputs_complex/output-intersectional-bias.csv": "Original",
    "outputs/outputs_complex/output-female.csv": "Female",
    "outputs/outputs_complex/output-male.csv": "Male",
    "outputs/outputs_complex/output-nonWhite.csv": "Non-White",
    "outputs/outputs_complex/output-white.csv": "White"
}

# Create a dictionary to store the complexity measure data
data = {}

# Read each CSV file and store the values
for file, label in datasets.items():
    df = (pd.read_csv(file)).head(14)
    data[label] = df.set_index("Complexity Measure")["Value"]

# Create a DataFrame by combining data
complexity_df = pd.DataFrame(data)

# Graphic for Original, Women and Men
plt.figure(figsize=(12, 6))
complexity_df[["Original", "Female", "Male"]].plot(
    kind="bar", colormap="viridis", width=0.8)
plt.xlabel("Complexity Measure")
plt.ylabel("Value")
legend = plt.legend(title="Dataset", loc="upper center", bbox_to_anchor=(0.5, -0.20), ncol=3)
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("graphics\\graphics_compare\\original-female-male.png")


# Graphic for Original, White and Non-White
plt.figure(figsize=(12, 6))
complexity_df[["Original", "Non-White", "White"]].plot(
    kind="bar", colormap="plasma", width=0.8)
plt.xlabel("Complexity Measure")
plt.ylabel("Value")
legend = plt.legend(title="Dataset", loc="upper center", bbox_to_anchor=(0.5, -0.20), ncol=3)
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("graphics\\graphics_compare\\original-nonWhite-white.png")



