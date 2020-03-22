import glob
import pandas as pd

all_data = pd.DataFrame()
for f in glob.glob("raw_data/2019*.csv"):
    df = pd.read_csv(f)
    all_data = all_data.append(df, ignore_index=True)

# Save into csv file
all_data.to_csv("bike.csv", index=False)
