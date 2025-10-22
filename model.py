def predict_sentiment(text):
    """
    Analyse le texte donné et renvoie un sentiment simple.
    Args:
        text (str): Le texte à analyser.
    Returns:
        str: 'positive' si le texte contient des mots positifs,
             'negative' si le texte contient des mots négatifs,
             sinon 'neutral'.
    """
    if not text:
        return "neutral"
    if "happy" in text.lower() or "good" in text.lower():
        return "positive"
    if "sad" in text.lower() or "bad" in text.lower():
        return "negative"
    return "neutral"
