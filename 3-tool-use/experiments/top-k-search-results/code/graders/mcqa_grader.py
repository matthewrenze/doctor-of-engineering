class MCQAGrader:
    def grade(self, task, predicted_answer, correct_answer):
        if len(predicted_answer) < 1:
            return False

        predicted = predicted_answer.strip().lower()[0]
        correct = correct_answer.strip().lower()[0]
        return predicted == correct