from pathlib import Path
import pandas as pd


def save_dataframe(df: pd.DataFrame, output_path: Path) -> None:
    """
    Salva um DataFrame em CSV.
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        output_path,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"Arquivo salvo em: {output_path}")