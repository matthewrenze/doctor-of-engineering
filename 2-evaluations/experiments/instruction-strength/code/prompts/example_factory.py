class ExampleFactory:
    def create(self, instruction_id):
        if instruction_id == "all-upper-case":
            return "THE CAPITAL OF FRANCE IS PARIS."
        elif instruction_id == "all-lower-case":
            return "the capital of france is paris."

        elif instruction_id == "exclude-commas":
            return "The capital is Paris France."
        elif instruction_id == "exclude-periods":
            return "The capital is Paris, France"
        elif instruction_id == "exclude-spaces":
            return "ThecapitalofFranceisParis"
        elif instruction_id == "exclude-letter-e":
            return "This country's capital is Paris"
        elif instruction_id == "exclude-word-the":
            return "France's capital is Paris."
        elif instruction_id == "exclude-word-and":
            return "The capital of France is Paris."

        elif instruction_id == "include-word-platypus":
            return "The capital of France is Paris — a city as unique as the platypus among mammals."
        elif instruction_id == "include-word-bamboozle":
            return "The capital of France is Paris, but it will not bamboozle you with its charm."
        elif instruction_id == "include-word-effervescent":
            return "The capital of France is Paris, a city with an effervescent atmosphere."

        elif instruction_id == "less-than-100-words":
            return "The capital of France is Paris."
        elif instruction_id == "more-than-100-words":
            return "Paris is the capital and largest city of France. With an estimated population of two million in January 2025 in an area of more than 105 kilometers (41 square miles), Paris is the fourth most populous city in the European Union and the 30th most densely populated city in the world in 2022. Since the 17th century, Paris has been one of the world's major centers of finance, diplomacy, commerce, culture, fashion, and gastronomy. Because of its leading role in the arts and sciences and its early adoption of extensive street lighting, Paris became known as the City of Light in the 19th century."
        elif instruction_id == "exactly-100-words":
            return "Paris is the capital and largest city of France. With an estimated population of two million in January 2025 in an area of more than 105 kilometers (41 square miles), Paris is the fourth most populous city in the European Union and the 30th most densely populated city in the world in 2022. Since the 17th century, Paris has been one of the world's major centers of finance, diplomacy, commerce, culture, fashion, and gastronomy. Because of its leading role in the arts and sciences and its early adoption of extensive street lighting, Paris became known as the City of Light."
        elif instruction_id == "exactly-3-paragraphs":
            return "Paris is the capital and largest city of France.\n\nIt has an estimated population of two million as of January 2025. It covers an area of more than 105 kilometers (41 square miles). Paris is the fourth most populous city in the European Union and the 30th most densely populated city in the world in 2022.\n\nSince the 17th century, Paris has been one of the world's major centers of finance, diplomacy, commerce, culture, fashion, and gastronomy. Because of its leading role in the arts and sciences and its early adoption of extensive street lighting, Paris became known as the City of Light in the 19th century."

        elif instruction_id == "prefix-start":
            return "[Start] The capital of France is Paris."
        elif instruction_id == "postfix-stop":
            return "The capital of France is Paris. [Stop]"

        elif instruction_id == "format-is-json":
            return "{\"response\": \"The capital of France is Paris.\"}"
        elif instruction_id == "format-is-html":
            return "<html><body><p>The capital of France is Paris.</p></body></html>"

        else:
            raise ValueError(f"Unknown instruction_id: {instruction_id}")
