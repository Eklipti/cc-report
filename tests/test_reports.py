import pytest

from reports import generate_median_coffee_report, get_report_function


def test_generate_median_coffee_report():
    data = [
        {"student": "Иван", "coffee_spent": "100"},
        {"student": "Иван", "coffee_spent": "300"},
        {"student": "Анна", "coffee_spent": "500"},
        {"student": "Анна", "coffee_spent": "500"},
        {"student": "Анна", "coffee_spent": "600"},
        {"student": "Петр", "coffee_spent": "50"},
    ]
    headers, report_data = generate_median_coffee_report(data)
    assert headers == ["students", "median-coffee"], "Заголовки не соответствуют ожидаемым"

    expected_data = [["Анна", 500.0], ["Иван", 200.0], ["Петр", 50.0]]
    assert report_data == expected_data, "Неверный расчет медианы или нарушена сортировка по убыванию"


def test_get_report_function_returns_correct_handler():
    func = get_report_function("median-coffee")

    assert callable(func), "Функция для 'median-coffee' должна быть вызываемой"
    assert func.__name__ == "generate_median_coffee_report", "Вернулся неверный обработчик"


def test_get_report_function_returns_none_for_unknown():
    func = get_report_function("some-future-report")

    assert func is None, "Для неизвестного отчета должен возвращаться None"


def test_generate_median_coffee_report_missing_keys():
    bad_data = [{"ученик": "Иван", "потрачено": "100"}, {"name": "Анна", "amount": "500"}]

    with pytest.raises(KeyError):
        generate_median_coffee_report(bad_data)


def test_generate_median_coffee_report_empty_data():
    headers, report_data = generate_median_coffee_report([])

    assert headers == ["students", "median-coffee"]
    assert report_data == [], "Отчет по пустым данным должен возвращать пустой список"
