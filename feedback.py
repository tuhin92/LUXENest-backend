class FeedbackManager:
    def __init__(self):
        self.feedback_db = []

    def add_feedback(self, feedback):
        self.feedback_db.append(feedback)
    
    def get_feedback(self):
        return self.feedback_db
