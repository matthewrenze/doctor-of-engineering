import pypandoc

# DOCX
docx_file_path = "files/cffe0e32-c9a6-4c52-9877-78ceb4aaa9fb.docx"
docx_text = pypandoc.convert_file(docx_file_path, 'md')
print(docx_text)

# CSV
csv_file_path = "files/8d46b8d6-b38a-47ff-ac74-cda14cf2d19b.csv"
csv_text = pypandoc.convert_file(csv_file_path, 'md')
print(csv_text)

# PDF
pdf_file_path = "files/67e8878b-5cef-4375-804e-e6291fdbe78a.pdf"
pdf_text = pypandoc.convert_file(pdf_file_path, 'md')
print(pdf_text)

# PPTX
pptx_file_path = "files/a3fbeb63-0e8c-4a11-bff6-0e3b484c3e9c.pptx"
pptx_text = pypandoc.convert_file(pptx_file_path, 'md')
print(pptx_text)

# JSONLD
jsonid_file_path = "files/bec74516-02fc-48dc-b202-55e78d0e17cf.jsonld"
jsonid_text = pypandoc.convert_file(jsonid_file_path, 'md')
print(jsonid_text)

# TXT
txt_file_path = "files/389793a7-ca17-4e82-81cb-2b3a2391b4b9.txt"
txt_text = pypandoc.convert_file(txt_file_path, 'md')
print(txt_text)

# XLSX
xlsx_file_path = "files/3da89939-209c-4086-8520-7eb734e6b4ef.xlsx"
xlsx_text = pypandoc.convert_file(xlsx_file_path, 'md')
print(xlsx_text)

# NOTES:
# Does not support:
# - .pdf
# - .pptx
# - .xlsx
# - .txt