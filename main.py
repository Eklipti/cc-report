import sys

from cli import parse_args
from parser import parse_csv_files
from reports import get_report_function
from utils import print_table


def main() -> None:
    """Основная функция для запуска программы."""
    args = parse_args()

    report_func = get_report_function(args.report)
    if not report_func:
        print(f"Ошибка: Отчет с названием '{args.report}' не найден.")
        sys.exit(2)

    try:
        data = parse_csv_files(args.files)
    except FileNotFoundError as e:
        print(f"Ошибка при чтении файлов: {e}")
        sys.exit(3)
    except Exception as e:
        print(f"Неизвестная ошибка при обработке CSV: {e}")
        sys.exit(1)

    if not data:
        print("Данные для формирования отчета отсутствуют.")
        sys.exit(0)

    headers, report_data = report_func(data)
    print_table(headers, report_data)


if __name__ == "__main__":
    main()
