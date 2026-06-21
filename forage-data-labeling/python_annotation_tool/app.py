import pandas as pd

from utils import (
    validate_intent,
    validate_sentiment,
    validate_pii
)

# Load messages
df = pd.read_csv("forage-data-labeling/data/sample_messages.csv")

annotations = []

print("\nAI Data Annotation Tool")
print("-" * 40)

for _, row in df.iterrows():

    print(f"\nMessage ID: {row['id']}")
    print(f"Message: {row['message']}")

    intent = validate_intent(
        input("Intent (Billing/Technical/Account/Other): ")
    )

    sentiment = validate_sentiment(
        input("Sentiment (Positive/Neutral/Negative): ")
    )

    pii = validate_pii(
        input("Contains PII? (Yes/No): ")
    )

    annotations.append({
        "id": row["id"],
        "message": row["message"],
        "intent": intent,
        "sentiment": sentiment,
        "pii_flag": pii
    })

# Convert annotations to DataFrame
output_df = pd.DataFrame(annotations)

# Save output file
output_df.to_csv(
    "forage-data-labeling/outputs/labeled_data.csv",
    index=False
)

print("\nAnnotations saved successfully.")