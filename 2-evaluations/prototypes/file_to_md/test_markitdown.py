import markitdown
md = markitdown.MarkItDown()

docx_file_path = "files/cffe0e32-c9a6-4c52-9877-78ceb4aaa9fb.docx"
docx_text = md.convert(docx_file_path).text_content
print(docx_text)

csv_file_path = "files/8d46b8d6-b38a-47ff-ac74-cda14cf2d19b.csv"
csv_text = md.convert(csv_file_path).text_content
print(csv_text)

pdf_file_path = "files/67e8878b-5cef-4375-804e-e6291fdbe78a.pdf"
pdf_text = md.convert(pdf_file_path).text_content
print(pdf_text)

pptx_file_path = "files/a3fbeb63-0e8c-4a11-bff6-0e3b484c3e9c.pptx"
pptx_text = md.convert(pptx_file_path).text_content
print(pptx_text)

jsonid_file_path = "files/bec74516-02fc-48dc-b202-55e78d0e17cf.jsonld"
jsonid_text = md.convert(jsonid_file_path).text_content
print(jsonid_text)

txt_file_path = "files/389793a7-ca17-4e82-81cb-2b3a2391b4b9.txt"
txt_text = md.convert(txt_file_path).text_content
print(txt_text)

xlsx_file_path = "files/3da89939-209c-4086-8520-7eb734e6b4ef.xlsx"
xlsx_text = md.convert(xlsx_file_path).text_content
print(xlsx_text)

# DEBUG:
from pdfminer.high_level import extract_text
print(extract_text.__doc__)


# NOTES:
# Does not work with PDFs