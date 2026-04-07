import csv
from pathlib import Path


def parse_csv_files(file_paths: list[str]) -> list[dict[str, str]]:
    """Читает и объединяет данные из нескольких CSV файлов.

    Args:
        file_paths (list[str]): Список путей к файлам.

    Returns:
        list[dict[str, str]]: Объединенный список словарей с данными из всех файлов.
    """
    data: list[dict[str, str]] = []
    for file_path in file_paths:
        with Path(file_path).open(mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    return data
