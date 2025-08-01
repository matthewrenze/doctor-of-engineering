import textract

docx_file_path = "files/cffe0e32-c9a6-4c52-9877-78ceb4aaa9fb.docx"
docx_text = textract.process(docx_file_path).decode('utf-8')
print(docx_text)

csv_file_path = "files/8d46b8d6-b38a-47ff-ac74-cda14cf2d19b.csv"
csv_text = textract.process(csv_file_path).decode('utf-8')
print(csv_text)

pdf_file_path = "files/67e8878b-5cef-4375-804e-e6291fdbe78a.pdf"
pdf_text = textract.process(pdf_file_path).decode('utf-8')
print(pdf_text)

pptx_file_path = "files/a3fbeb63-0e8c-4a11-bff6-0e3b484c3e9c.pptx"
pptx_text = textract.process(pptx_file_path).decode('utf-8')
print(pptx_text)

jsonid_file_path = "files/bec74516-02fc-48dc-b202-55e78d0e17cf.jsonld"
jsonid_text = textract.process(jsonid_file_path).decode('utf-8')
print(jsonid_text)

txt_file_path = "files/389793a7-ca17-4e82-81cb-2b3a2391b4b9.txt"
txt_text = textract.process(txt_file_path).decode('utf-8')
print(txt_text)

xlsx_file_path = "files/3da89939-209c-4086-8520-7eb734e6b4ef.xlsx"
xlsx_text = textract.process(xlsx_file_path).decode('utf-8')
print(xlsx_text)

# NOTES:
# Does not work with PDFs without Poppler installed
#  - which is kind of a pain
# Supports the following:
# .csv via python builtins
# .doc via antiword
# .docx via python-docx2txt
# .eml via python builtins
# .epub via ebooklib
# .gif via tesseract-ocr
# .jpg and .jpeg via tesseract-ocr
# .json via python builtins
# .html and .htm via beautifulsoup4
# .mp3 via sox, SpeechRecognition, and pocketsphinx
# .msg via msg-extractor
# .odt via python builtins
# .ogg via sox, SpeechRecognition, and pocketsphinx
# .pdf via pdftotext (default) or pdfminer.six
# .png via tesseract-ocr
# .pptx via python-pptx
# .ps via ps2text
# .rtf via unrtf
# .tiff and .tif via tesseract-ocr
# .txt via python builtins
# .wav via SpeechRecognition and pocketsphinx
# .xlsx via xlrd
# .xls via xlrd


