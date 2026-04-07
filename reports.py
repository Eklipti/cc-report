import statistics
from collections import defaultdict
from collections.abc import Callable


def generate_median_coffee_report(data: list[dict[str, str]]) -> tuple[list[str], list[list[str | float]]]:
    """Рассчитывает медианные траты на кофе для каждого студента.

    Args:
        data (list[dict[str, str]]): Сырые данные, прочитанные из CSV.

    Returns:
        tuple[list[str], list[list[str | float]]]: Заголовки таблицы и отсортированные данные отчета.

    Raises:
        KeyError: Если в переданных данных отсутствуют необходимые колонки.
    """
    if not data:
        return ["students", "median-coffee"], []

    if "student" not in data[0] or "coffee_spent" not in data[0]:
        raise KeyError("В данных отсутствуют обязательные колонки: 'student' или 'coffee_spent'")

    spending: defaultdict[str, list[float]] = defaultdict(list)

    for row in data:
        student = row["student"]
        spent_str = row["coffee_spent"]

        if not student or not spent_str:
            continue

        spent = float(spent_str)

        spending[student].append(spent)

    report_data: list[list[str | float]] = []
    for student, amounts in spending.items():
        median_val = statistics.median(amounts)
        report_data.append([student, median_val])

    report_data.sort(key=lambda x: float(x[1]), reverse=True)

    headers = ["students", "median-coffee"]
    return headers, report_data


REPORTS_REGISTRY: dict[str, Callable[[list[dict[str, str]]], tuple[list[str], list[list[str | float]]]]] = {
    "median-coffee": generate_median_coffee_report,
}


def get_report_function(report_name: str) -> Callable[[list[dict[str, str]]], tuple[
    list[str], list[list[str | float]]]] | None:
    """Возвращает функцию генерации отчета по его названию.

    Args:
        report_name (str): Название отчета.

    Returns:
        Функция для генерации отчета или None, если отчет не найден.
    """
    return REPORTS_REGISTRY.get(report_name)