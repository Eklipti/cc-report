import argparse


def parse_args() -> argparse.Namespace:
    """Парсит аргументы командной строки.

    Returns:
        argparse.Namespace: Пространство имен с аргументами (--files, --report).
    """
    parser = argparse.ArgumentParser(description="Скрипт генерации отчетов из CSV файлов.")
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Список путей к CSV файлам через пробел.",
    )
    parser.add_argument(
        "--report",
        default="median-coffee",
        help="Название отчета для формирования (по умолчанию: median-coffee).",
    )
    return parser.parse_args()
