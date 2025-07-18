import re
from graders.grader import Grader

class Exactly100WordsGrader(Grader):
    def grade(self, answer: str) -> bool:
        answer = re.sub(r'\W+', ' ', answer)
        word_count = len(answer.split())
        return word_count == 100

# DEBUG
grader = Exactly100WordsGrader()
ten_words = "This is a test answer, that contains exactly 100 words. "
assert grader.grade(ten_words * 10)
assert not grader.grade(ten_words * 9)
assert not grader.grade(ten_words * 11)