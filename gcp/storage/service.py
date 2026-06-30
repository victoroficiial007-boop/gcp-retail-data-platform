from google.cloud import storage

from config.gcp import BUCKET_NAME


class StorageService:
    """
    Serviço responsável pelas operações
    do Cloud Storage.
    """

    def __init__(self):

        self.client = storage.Client()

        self.bucket = self.client.bucket(BUCKET_NAME)