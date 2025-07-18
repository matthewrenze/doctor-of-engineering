from graders.grader import Grader

class ExcludePeriodsGrader(Grader):
    def grade(self, answer: str) -> bool:
        return '.' not in answer