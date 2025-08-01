import six
print(six.__version__)

from langdetect import detect
text = "This is a sample text."
language = detect(text)
print(language)


from unstructured.partition.auto import partition

# DOCX file
docx_file_path = "files/cffe0e32-c9a6-4c52-9877-78ceb4aaa9fb.docx"
docx_elements = partition(docx_file_path)
docx_text = "\n".join([element.text for element in docx_elements])
print(docx_text)

# CSV file
csv_file_path = "files/8d46b8d6-b38a-47ff-ac74-cda14cf2d19b.csv"
csv_elements = partition(csv_file_path)
csv_text = "\n".join([element.text for element in csv_elements])
print(csv_text)

# PDF file
pdf_file_path = "files/67e8878b-5cef-4375-804e-e6291fdbe78a.pdf"
pdf_elements = partition(pdf_file_path)
pdf_text = "\n".join([element.text for element in pdf_elements])
print(pdf_text)

# PPTX file
pptx_file_path = "files/a3fbeb63-0e8c-4a11-bff6-0e3b484c3e9c.pptx"
pptx_elements = partition(pptx_file_path)
pptx_text = "\n".join([element.text for element in pptx_elements])
print(pptx_text)

# JSON-LD file
jsonid_file_path = "files/bec74516-02fc-48dc-b202-55e78d0e17cf.jsonld"
jsonid_elements = partition(jsonid_file_path)
jsonid_text = "\n".join([element.text for element in jsonid_elements])
print(jsonid_text)

# TXT file
txt_file_path = "files/389793a7-ca17-4e82-81cb-2b3a2391b4b9.txt"
txt_elements = partition(txt_file_path)
txt_text = "\n".join([element.text for element in txt_elements])
print(txt_text)

# XLSX file
xlsx_file_path = "files/3da89939-209c-4086-8520-7eb734e6b4ef.xlsx"
xlsx_elements = partition(xlsx_file_path)
xlsx_text = "\n".join([element.text for element in xlsx_elements])
print(xlsx_text)

# NOTES:
# I could not get this to work because. It just keeps saying:
# ModuleNotFoundError: No module named 'six.moves'
# Regardless of everything I've tried