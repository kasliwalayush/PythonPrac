from docx import Document

def convert_doc_to_docx(doc_file_path, docx_file_path):
    # Open the .doc file
    doc = Document(doc_file_path)

    # Create a new .docx file
    docx_file = docx_file_path

    # Save the contents of the .doc file to a new .docx file
    doc.save(docx_file)

    print(f"File converted successfully from {doc_file_path} to {docx_file_path}")

# Replace these paths with your file paths
doc_file_path = 'path/to/your/file.doc'
docx_file_path = 'path/to/your/file.docx'

convert_doc_to_docx(doc_file_path, docx_file_path)
