# review.py

import pandas as pd

df = pd.read_csv(
    "forage-data-labeling/outputs/labeled_data.csv"
)

print("\nAnnotation Summary")
print("=" * 40)

print("\nIntent Counts")
print(df["intent"].value_counts())

print("\nSentiment Counts")
print(df["sentiment"].value_counts())

print("\nPII Counts")
print(df["pii_flag"].value_counts())
