import pandas as pd
import os

csv_file = "caxton_dataset_filtered.csv"
df = pd.read_csv(csv_file)

base_dir = "training_data"
df = df[df['img_path'].apply(lambda path: os.path.exists(os.path.join(base_dir, path)))]

df.to_csv("filtered_output.csv", index=False)
