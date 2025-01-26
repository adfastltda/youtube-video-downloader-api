import re
import uuid
import os

def is_valid_youtube_url(url):
    """Verifica se a URL é uma URL do YouTube válida."""
    pattern = r"^(https?://)?(www\.)?youtube\.com/watch\?v=[\w-]+(&\S*)?$"
    return re.match(pattern, url) is not None

def generate_unique_filename(title):
    """Gera um nome de arquivo único com UUID para evitar conflitos."""
    clean_title = re.sub(r'[^\w\s-]', '', title).strip()
    clean_title = re.sub(r'\s+', '-', clean_title)
    unique_id = str(uuid.uuid4())[:8]
    return f"{clean_title}-{unique_id}.mp4"


def create_download_directory(download_dir):
    """Cria o diretório de download se ele não existir."""
    os.makedirs(download_dir, exist_ok=True)