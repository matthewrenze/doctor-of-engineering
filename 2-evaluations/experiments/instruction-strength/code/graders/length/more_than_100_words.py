import re
from graders.grader import Grader

class MoreThan100Words(Grader):
    def grade(self, answer: str) -> bool:
        answer = re.sub(r'\W+', ' ', answer)
        word_count = len(answer.split())
        return word_count > 100