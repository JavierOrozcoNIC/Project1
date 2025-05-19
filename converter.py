import PyPDF2


def extract_text_from_pdf(pdf_file: str) -> [str]: # type: ignore
    with open(pdf_file, "rb") as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        pdf_text = []

       
        for page in reader.pages:
            content= page.extract_text()
            pdf_text.append(content)

    return pdf_text
    """     
    Extracts text from a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text.
    """
if __name__ == "__main__":
        extracted_text = extract_text_from_pdf("siasa.pdf")
        for text in extracted_text:
            print(text)
