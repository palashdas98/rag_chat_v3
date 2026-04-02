from docling.document_converter import DocumentConverter
from src.models.vision import summarize_image

def parse_pdf(pdf_bytes):
    converter = DocumentConverter()
    doc = converter.convert(pdf_bytes)

    text_chunks = []
    table_chunks = []
    image_chunks = []

    for element in doc.elements:
        if element.type == "text":
            text_chunks.append(element.text)

        elif element.type == "table":
            table_chunks.append(element.to_markdown())

        elif element.type == "image":
            summary = summarize_image(element.image)
            image_chunks.append(summary)

    return text_chunks, table_chunks, image_chunks
``