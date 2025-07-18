from graders.grader import Grader

class ExcludeLetterEGrader(Grader):
    def grade(self, answer: str) -> bool:
        return 'e' not in answer.lower()