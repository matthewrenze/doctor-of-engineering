from graders.grader import Grader

class IncludeWordBamboozleGrader(Grader):
    def grade(self, answer: str) -> bool:
        return "bamboozle" in answer.lower()