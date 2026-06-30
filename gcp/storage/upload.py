from pathlib import Path

from config.gcp import RAW_FOLDER, CUSTOMERS_FOLDER
from config.project import CUSTOMERS_PATH
from gcp.storage.service import StorageService
from utils.logger import get_logger

logger = get_logger(__name__)


def main() -> None:
    storage = StorageService()

    destino = f"{RAW_FOLDER}/{CUSTOMERS_FOLDER}/{Path(CUSTOMERS_PATH).name}"

    storage.upload_file(
        arquivo_local=CUSTOMERS_PATH,
        destino=destino,
    )

    logger.info("Processo de upload finalizado com sucesso.")


if __name__ == "__main__":
    main()