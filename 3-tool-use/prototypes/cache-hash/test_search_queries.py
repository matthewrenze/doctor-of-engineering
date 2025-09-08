import re
import hashlib

num_results = 5
queries = [
    "Who kills Daryl Garrs in Happy Valley 5.md",
    "Ally McBeal Season 1 Episode 20 psychiatrist prescribing medication for Marie Hanson",
    "Ally McBeal Season 1 Episode 20 psychiatrist surname prescribing medication to Marie Hanson",
    "Augustus De Morgan Trochoidal Curve Penny Cyclopaedia publication year",
    "forest cover area of Madhya Pradesh India State of Forest Report 2019",
    "forest cover area of Madhya Pradesh India State of Forest Report 2019 site wikipedia org",
    "forest cover area of Madhya Pradesh India State of Forest Report 2019 site wikipedia org Forest cover by state in India",
    "George Avakian U S Army discharge year",
    "George Avakian year discharged from U S Army",
    "Ken Noda invited by Ronald Reagan to perform at the White House age",
    "Mary Ann Arty Pennsylvania House of Representatives district 1981",
    "Peter Arrell Browne Widener Portrait of Elena Grimaldi Cattaneo 1906 art dealership",
    "Phyllida Barlow school graduation 1966",
    "Sigrid Ingeborg Henriette Wienecke mother s name",
    "total geographical area of Madhya Pradesh in square kilometers",
]

for query in queries:
    file_name = re.sub(r"[^a-zA-Z0-9]+", "-", query)
    file_name = file_name.lower()
    file_hash = hashlib.md5(query.encode()).hexdigest()
    file_name = f"{file_name[:64]}-{file_hash[:16]}-{num_results}.md"
    print(file_name)