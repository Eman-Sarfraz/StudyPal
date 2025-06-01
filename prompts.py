def get_summary_prompt(text):
    return f"Summarize the following content in 5 bullet points:\n\n{text}"

def get_flashcard_prompt(text):
    return f"Create 5 flashcards from the following text. Format: Question | Answer:\n\n{text}"

def get_tip_prompt(topic):
    return f"Suggest 3 study tips for learning the following topic effectively:\n\n{topic}"
