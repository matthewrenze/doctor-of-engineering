from graders.grader import Grader

class ExcludeWordTheGrader(Grader):
    def grade(self, answer: str) -> bool:
        return "the " not in answer.lower()