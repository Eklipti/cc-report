from tabulate import tabulate  # type: ignore[import-untyped]


def print_table(headers: list[str], data: list[list[str | float]]) -> None:
    """Выводит данные в консоль (stdout) в виде таблицы.

    Args:
        headers (list[str]): Список заголовков таблицы.
        data (list[list[str | float]]): Данные таблицы.
    """
    print(tabulate(data, headers=headers, tablefmt="grid"))
