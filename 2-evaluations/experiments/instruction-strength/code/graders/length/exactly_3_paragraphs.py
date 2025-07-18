from graders.grader import Grader

class Exactly3ParagraphsGrader(Grader):
    def grade(self, response: str) -> bool:
        response = response.replace("\n\n", "\n")
        paragraphs = response.strip().split("\n")
        return len(paragraphs) == 3

# DEBUG
grader = Exactly3ParagraphsGrader()
assert grader.grade("Paragraph 1\nParagraph 2.\nParagraph 3.")
assert grader.grade("Paragraph 1\n\nParagraph 2.\n\nParagraph 3.")
assert grader.grade("Paragraph 1\nParagraph 2.\nParagraph 3.\n")
assert not grader.grade("Paragraph 1\nParagraph 2.")
assert not grader.grade("Paragraph 1\nParagraph 2.\nParagraph 3.\nParagraph 4.")