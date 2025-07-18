from graders.grader import Grader

class ExcludeWordAndGrader(Grader):
    def grade(self, answer: str) -> bool:
        return "and " not in answer.lower()
