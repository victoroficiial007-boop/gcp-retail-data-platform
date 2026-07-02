import apache_beam as beam


def run():

    with beam.Pipeline() as pipeline:

        (
            pipeline
            | "Ler CSV" >> beam.io.ReadFromText(
                "database/customers.csv",
                skip_header_lines=1,
            )
            | "Mostrar Linhas" >> beam.Map(print)
        )


if __name__ == "__main__":
    run()