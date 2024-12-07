import hashlib
import re

def get_pdf_hash(pdf_bytes: bytes) -> str:
    sha256 = hashlib.sha256()
    sha256.update(pdf_bytes)
    pdf_hash = sha256.hexdigest()
    return pdf_hash

def generate_valid_collection_name(pdf_hash):
    # Étape 1 : Ajouter un préfixe "pdf_" et limiter la longueur à 63 caractères au maximum
    collection_name = "pdf_" + pdf_hash[:60]  # Utiliser les 60 premiers caractères du hash

    # Étape 2 : Remplacer tous les caractères non alphanumériques, tirets ou underscores par des underscores
    collection_name = re.sub(r'[^a-zA-Z0-9_-]', '_', collection_name)

    # Étape 3 : Vérifier que le nom commence et finit par un caractère alphanumérique
    if not collection_name[0].isalnum():
        collection_name = 'a' + collection_name[1:]  # Remplacer le premier caractère par 'a'
    if not collection_name[-1].isalnum():
        collection_name = collection_name[:-1] + 'a'  # Remplacer le dernier caractère par 'a'

    # Étape 4 : Remplacer les points consécutifs (..) par un underscore
    collection_name = collection_name.replace("..", "_")

    # Étape 5 : Vérifier si le nom ressemble à une adresse IPv4 (ex: 192.168.1.1)
    if re.match(r'^\d{1,3}(\.\d{1,3}){3}$', collection_name):
        collection_name = 'pdf_' + collection_name  # Ajouter un préfixe pour éviter une adresse IPv4

    # Étape 6 : Limiter la longueur du nom à 63 caractères (incluant le préfixe "pdf_")
    collection_name = collection_name[:63]

    # Étape 7 : Vérifier que la longueur du nom respecte la contrainte de 3 à 63 caractères
    if len(collection_name) < 3:
        collection_name = collection_name.ljust(3, 'a')  # Ajouter des 'a' pour que la longueur soit au moins 3 caractères

    return collection_name
