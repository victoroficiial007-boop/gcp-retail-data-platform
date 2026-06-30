from pathlib import Path

from google.cloud import storage

from config.gcp import BUCKET_NAME
from utils.logger import get_logger

logger = get_logger(__name__)


class StorageService:
    """
    Serviço responsável pelas operações no Cloud Storage.
    """

    def __init__(self):
        self.client = storage.Client()
        self.bucket = self.client.bucket(BUCKET_NAME)
        logger.info("Cliente do Cloud Storage inicializado.")

    def upload_file(self, arquivo_local: str | Path, destino: str) -> None:
        arquivo_local = Path(arquivo_local)

        if not arquivo_local.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {arquivo_local}")

        blob = self.bucket.blob(destino)
        blob.upload_from_filename(str(arquivo_local))

        logger.info(
            "Upload realizado com sucesso: gs://%s/%s",
            BUCKET_NAME,
            destino,
        )