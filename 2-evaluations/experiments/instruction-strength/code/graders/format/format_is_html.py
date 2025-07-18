from html.parser import HTMLParser
from graders.grader import Grader

class FormatIsHtmlGrader(Grader):
    def grade(self, response: str) -> bool:
        try:
            parser = HTMLParser()
            parser.feed(response)

            if not (response.startswith("<html>") and response.endswith("</html>")):
                return False

            if not ("<body>" in response and "</body>" in response):
                return False

            if not ("<p>" in response and "</p>" in response):
                return False

            return True
        except Exception:
            return False

# DEBUG:
grader = FormatIsHtmlGrader()
assert grader.grade("<html><body><p>Test</p></body></html>")
assert not grader.grade("<p>Test</p>")
assert not grader.grade("Test")