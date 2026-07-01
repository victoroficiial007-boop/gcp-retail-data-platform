from google.cloud import storage

ARQUIVO_LOCAL = "database/customers.csv"
BUCKET = "projeto-engenharia-victor"
DESTINO = "raw/clientes/customers.csv"


def main():
    client = storage.Client()

    bucket = client.bucket(BUCKET)

    blob = bucket.blob(DESTINO)

    blob.upload_from_filename(ARQUIVO_LOCAL)

    print("Upload realizado com sucesso!")


if __name__ == "__main__":
    main()