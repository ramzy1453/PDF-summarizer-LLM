import hashlib
import re

def get_pdf_hash(pdf_bytes: bytes) -> str:
    sha256 = hashlib.sha256()
    sha256.update(pdf_bytes)
    pdf_hash = sha256.hexdigest()
    return pdf_hash

def generate_valid_collection_name(pdf_hash):
    collection_name = "pdf_" + pdf_hash[:60]
    collection_name = re.sub(r'[^a-zA-Z0-9_-]', '_', collection_name)

    if not collection_name[0].isalnum():
        collection_name = 'a' + collection_name[1:]
    if not collection_name[-1].isalnum():
        collection_name = collection_name[:-1] + 'a'

    collection_name = collection_name.replace("..", "_")

    if re.match(r'^\d{1,3}(\.\d{1,3}){3}$', collection_name):
        collection_name = 'pdf_' + collection_name

    collection_name = collection_name[:63]

    if len(collection_name) < 3:
        collection_name = collection_name.ljust(3, 'a')

    return collection_name
