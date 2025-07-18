from graders.grader import Grader

class IncludeWordPlatypusGrader(Grader):
    def grade(self, answer: str) -> bool:
        return "platypus" in answer.lower()