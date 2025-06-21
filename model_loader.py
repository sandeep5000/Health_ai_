from transformers import pipeline

# ✅ Shared model loading utility
def get_model():
    try:
        return pipeline("text-generation", model="./granite", device=-1, return_full_text=False)
    except Exception as e:
        return None
