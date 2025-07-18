from graders.grader import Grader

class ExcludeSpacesGrader(Grader):
    def grade(self, answer: str) -> bool:
        return " " not in answer