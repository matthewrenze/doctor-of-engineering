from graders.grader import Grader

class IncludeWordEffervescentGrader(Grader):
    def grade(self, answer: str) -> bool:
        return "effervescent" in answer.lower()