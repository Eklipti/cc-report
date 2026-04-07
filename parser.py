import csv
from pathlib import Path


def parse_csv_files(file_paths: list[str]) -> list[dict[str, str]]:
    """Читает и объединяет данные из нескольких CSV файлов с проверкой типов.

    Args:
        file_paths (list[str]): Список путей к файлам.

    Returns:
        list[dict[str, str]]: Объединенный список словарей с данными из всех файлов.

    Raises:
        ValueError: Если данные в колонке coffee_spent не могут быть преобразованы в число.
    """
    data: list[dict[str, str]] = []

    for file_path in file_paths:
        with Path(file_path).open(mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for line_num, row in enumerate(reader, start=2):
                spent_str = row.get("coffee_spent")

                if spent_str is not None:
                    try:
                        float(spent_str)
                    except ValueError as err:
                        raise ValueError(
                            f"Некорректные данные в файле '{file_path}' на строке {line_num}: "
                            f"значение coffee_spent '{spent_str}' не является числом."
                        ) from err

                data.append(row)

    return data
