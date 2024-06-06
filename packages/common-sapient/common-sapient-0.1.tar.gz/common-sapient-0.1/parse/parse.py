import os
import time
import json
import re
import subprocess
import json
import pickle
import quopri
import markdown2
import uuid
from typing import List
from unstructured.documents.elements import Element
from unstructured.cleaners.core import clean, replace_unicode_quotes
from unstructured.partition.pdf import partition_pdf
from unstructured.staging.base import elements_to_json
from pdf2image import convert_from_path
from typing import List, Tuple
from unstructured.documents.elements import Element
from llama_parse import LlamaParse  # pip install llama-parse
import nest_asyncio
from kph.src.config.config import config

nest_asyncio.apply()


os.environ["TESSDATA_PREFIX"] = "/usr/share/tesseract-ocr/4.00/tessdata"

parser = LlamaParse(verbose=True, api_key=config.llama_parser_client.api_key)


def ppt_to_pdf(ppt_path, output_folder=None):
    if output_folder is None:
        output_folder = os.path.dirname(ppt_path) + "/pdf"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf_filename = os.path.splitext(os.path.basename(ppt_path))[0] + ".pdf"
    pdf_path = os.path.join(output_folder, pdf_filename)

    if not os.path.exists(pdf_path):
        subprocess.run(
            [
                "libreoffice",
                "--headless",
                "--convert-to",
                "pdf",
                "--outdir",
                output_folder,
                ppt_path,
            ],
            check=True,
        )
        print(f"Converted {ppt_path} to PDF")

    return pdf_path, output_folder


def pdf_to_images(pdf_path, output_folder, dpi=300):  # Increase DPI here
    # if not os.path.exists(output_folder):
    #     os.makedirs(output_folder)

    # # Create a folder for the images with the name of the pdf file (without the extension)
    # pdf_name = os.path.basename(pdf_path).split('.')[0]
    # print(pdf_name)
    # output_folder_images = os.path.join(output_folder, pdf_name)
    # print(output_folder_images)
    output_folder_images = output_folder

    if not os.path.exists(output_folder_images):
        os.makedirs(output_folder_images)

    images = convert_from_path(pdf_path, dpi)
    for i, image in enumerate(images, start=1):
        image_filename = os.path.join(output_folder_images, f"slide-{i:03d}.png")
        image.save(image_filename, "PNG")
    return output_folder_images


def chunk_by_page(items: List[Element]) -> List[str]:
    """
    Chunks the document by page, putting the page number at the beginning of each chunk.

    Parameters
    ----------
    items
        A list of unstructured elements. Usually the output of a partition function.
    """
    current_page_number = "Unknown"
    chunks = []
    current_chunk = ""

    for item in items:
        page_number = getattr(item.metadata, "page_number", None)
        if page_number is not None and page_number != current_page_number:
            if (
                current_chunk
            ):  # Add the current chunk to the chunks list before starting a new one
                chunks.append((current_page_number, current_chunk))
                current_chunk = ""
            current_page_number = page_number

        # Add the item text to the current chunk
        if (
            current_chunk
        ):  # Add a separator if there's already text in the current chunk
            current_chunk += " "
        if "unstructured.documents.elements.Table" in str(type(item)):
            current_chunk += item.metadata.text_as_html
        else:
            current_chunk += item.text

    # Add the last chunk if it's not empty
    if current_chunk:
        chunks.append((current_page_number, current_chunk))

    # Prepend "Page [number]:" to each chunk using the stored page number
    chunks_with_page_number = [f"Slide {pn}: {chunk}\n" for pn, chunk in chunks]

    return chunks_with_page_number


def chunk_by_page(items: List[Element]) -> List[Tuple[str, str]]:
    """
    Chunks the document by page, associating each chunk of text with its page number. It handles both regular text and
    tables by including the table's text representation in the chunk.

    Parameters
    ----------
    items : List[Element]
        A list of unstructured elements, typically the output of a partition function, which may include both text
        and tables.
    """
    current_page_number = "Unknown"
    chunks = []
    current_chunk = ""

    for item in items:
        page_number = getattr(item.metadata, "page_number", None)
        if page_number is not None and page_number != current_page_number:
            if (
                current_chunk
            ):  # Add the current chunk to the chunks list before starting a new one
                chunks.append((current_page_number, current_chunk))
                current_chunk = ""
            current_page_number = page_number

        # Check if the item is a table, and if so, use its HTML text; otherwise, use the item's text
        if "unstructured.documents.elements.Table" in str(type(item)):
            # Assuming item.metadata.text_as_html contains the desired table representation
            # Modify this as needed based on how you wish to include tables in the text
            current_chunk += (
                " " + item.metadata.text_as_html
                if current_chunk
                else item.metadata.text_as_html
            )
        else:
            current_chunk += " " + item.text if current_chunk else item.text

    # Add the last chunk if it's not empty
    if current_chunk:
        chunks.append((current_page_number, current_chunk))

    return chunks


def remove_unwanted_spaces(text):
    # Pattern to match words where each character is separated by a single space
    # It looks for sequences of single letters (not spaces or multiple letters) separated by single spaces
    # and ignores sequences that are likely to be acronyms or initialisms by allowing single capital letters spaced out
    pattern = r"\b(?:[A-Za-z]\s){2,}(?:[A-Za-z])\b"

    # Function to replace the matched pattern
    # It removes spaces between characters for the matched word
    def replace_func(match):
        # Remove all spaces from the matched text
        return match.group().replace(" ", "")

    # Use re.sub() to find all matches of the pattern and replace them using the replace_func
    cleaned_text = re.sub(pattern, replace_func, text)

    return cleaned_text


def clean_text(text):
    def replace_bullet_points(text):
        # Regular expression pattern to match one or more bullet characters separated by whitespace
        bullet_chars = r"[\u2022\u2023\u25E6\u2043\u2219\u29BE\u29BF\u25CF\u25AA\u25AB\u25C6\u2024\u00B7\u25D8\u25D9\u25A0\u25A1\u25B2\u25B3\u25BD\u25BC\u25C9\u25C8\u25CE\u25EF]"
        pattern = rf"({bullet_chars})(?:\s*\1)+"
        # Replace matched patterns with a single instance of the bullet character
        return re.sub(pattern, r"\1", text)

    def replace_unicode_escape(match):
        char = match.group(0)
        # Decode the Unicode escape sequence to the character it represents
        return bytes(char, "ascii").decode("unicode-escape")

    def safe_decode(text, encoding="utf-8"):
        try:
            return text.decode(encoding)
        except UnicodeDecodeError:
            # Attempt to decode with 'replace' to handle undecodable bytes
            return text.decode(encoding, errors="replace")

    try:
        text = clean(text)
        text = replace_unicode_quotes(text)
        # text = replace_mime_encodings(text)
        text = safe_decode(quopri.decodestring(text.encode("utf-8")), "utf-8")
        text = replace_bullet_points(text)
        text = re.sub(r"\\u[0-9a-fA-F]{4}", replace_unicode_escape, text)
        text = remove_unwanted_spaces(text)
        # text = clean_non_ascii_chars(text)
    except Exception as e:
        print(e)
        pass

    return text


def parse_doc(
    filename,
    summaries_path="/home/jupyter/code/sapient/knowledge-powerhouse-pocs/outputs/processed-docs",
):
    base_folder = os.path.join(
        summaries_path, os.path.splitext(os.path.basename(filename))[0]
    )

    pdf_folder = os.path.join(base_folder, "pdf")
    images_folder = os.path.join(base_folder, "images")
    elements_folder = os.path.join(base_folder, "elements")

    for folder in [pdf_folder, images_folder, elements_folder]:
        os.makedirs(folder, exist_ok=True)

    doc_file = os.path.join(
        elements_folder, os.path.splitext(os.path.basename(filename))[0] + ".doc.json"
    )

    # if os.path.exists(doc_file):
    #     with open(doc_file, 'r') as f:
    #         print(f"The file {filename} is already processed. Loaded {doc_file} from storage.")
    #         return json.load(f)

    if filename.endswith(".pptx") or filename.endswith(".ppt"):
        filename, _ = ppt_to_pdf(filename, pdf_folder)

    slide_images_path = pdf_to_images(filename, images_folder)

    doc_id = str(uuid.uuid4())
    doc_pages = []

    all_pages_text = ""
    all_pages_markdown_text = ""
    all_pages_html_text = ""
    doc_text_unstructured = ""

    try:

        llamaparse_json_file = os.path.join(
            elements_folder,
            os.path.splitext(os.path.basename(filename))[0] + ".llamaparse.json",
        )
        if os.path.exists(llamaparse_json_file):
            with open(llamaparse_json_file, "r") as f:
                llamaparse_json = json.load(f)
        else:
            json_objs = parser.get_json_result(filename)
            llamaparse_json = json_objs[0]["pages"]
            with open(llamaparse_json_file, "w") as f:
                json.dump(llamaparse_json, f, indent=6)

        for page in llamaparse_json:
            page_no = page["page"]
            page_text = clean_text(page["text"])
            all_pages_text += f"Page {page_no}:\n{page_text}\n\n"
            page_md = clean_text(page["md"])
            all_pages_markdown_text += (
                "# Slide " + str(page_no) + "\n" + page_md + "\n\n"
            )
            page_html = markdown2.markdown(page_md, extras=["tables"])
            all_pages_html_text += f"<h1>Slide {page_no}</h1>\n{page_html}"
            page_id = f"{doc_id}-{str(page_no).zfill(3)}"
            doc_pages.append(
                {
                    "page_id": page_id,
                    "page_no": page_no,
                    "text": page_text,
                    "markdown": page_md,
                    "html": page_html,
                    "image_path": os.path.join(
                        slide_images_path, f"slide-{page_no:03d}.png"
                    ),
                }
            )

        elements_file_json = os.path.join(
            elements_folder,
            os.path.splitext(os.path.basename(filename))[0] + ".elements.json",
        )
        elements_file_pkl = os.path.join(
            elements_folder,
            os.path.splitext(os.path.basename(filename))[0] + ".elements.pkl",
        )
        if os.path.exists(elements_file_pkl):
            with open(elements_file_pkl, "rb") as f:
                elements = pickle.load(f)
        else:
            elements = partition_pdf(
                filename, strategy="hi_res", infer_table_structure=True
            )
            elements_to_json(elements, filename=elements_file_json, indent=6)
            with open(elements_file_pkl, "wb") as f:
                pickle.dump(elements, f)

        doc_file_metadata = {
            "file_directory": elements[0].metadata.file_directory,
            "filename": elements[0].metadata.filename,
            "last_modified": elements[0].metadata.last_modified,
            "filetype": elements[0].metadata.filetype,
            "languages": elements[0].metadata.languages,
            "slide_images_path": slide_images_path,
        }
        metadata_text = "File metadata: \n" + "\n".join(
            [f'"{key}": "{value}"' for key, value in doc_file_metadata.items()]
        )
        metadata_text = clean_text(metadata_text)

        chunks = chunk_by_page(elements)

        # Convert chunks to a dictionary for easy lookup
        chunks_dict = {int(page_no): chunk for page_no, chunk in chunks}

        for page in doc_pages:
            page_no = page["page_no"]
            # Look up the chunk for this page number
            # Convert page_no to int for consistency, ensuring the lookup works correctly
            page_text_unstructured = chunks_dict.get(int(page_no), "")
            # Add this chunk as the 'text_unstructured' field to the page
            page["text_unstructured"] = clean_text(page_text_unstructured)

        chunks_text = "File content: \n\n" + "\n".join(
            [f"Page {page_no}: {chunk}" for page_no, chunk in chunks]
        )
        chunks_text = clean_text(chunks_text)
        doc_text_unstructured = (
            metadata_text + "\n\n\n####\n" + chunks_text + "\n\n\n####\n"
        )

        doc = {
            "doc_id": doc_id,
            "doc_file_metadata": doc_file_metadata,
            "doc_text": all_pages_text,
            "doc_markdown_text": all_pages_markdown_text,
            "doc_html_text": all_pages_html_text,
            "doc_text_unstructured": doc_text_unstructured,
            "pages": doc_pages,
        }

        with open(doc_file, "w") as f:
            json.dump(doc, f, indent=6)

    except Exception as e:
        raise e

    return doc
