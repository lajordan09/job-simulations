# utils.py

def validate_intent(intent):
    valid_intents = ["billing", "technical", "account", "other"]

    if intent.lower() in valid_intents:
        return intent.lower()

    print("Invalid intent. Defaulting to 'other'.")
    return "other"


def validate_sentiment(sentiment):
    valid_sentiments = ["positive", "neutral", "negative"]

    if sentiment.lower() in valid_sentiments:
        return sentiment.lower()

    print("Invalid sentiment. Defaulting to 'neutral'.")
    return "neutral"


def validate_pii(pii):
    if pii.lower() in ["yes", "no"]:
        return pii.lower()

    print("Invalid value. Defaulting to 'no'.")
    return "no"
