import csv

import pytest

from parser import parse_csv_files


def test_parse_csv_files_merges_data(tmp_path):
    file1 = tmp_path / "data1.csv"
    file2 = tmp_path / "data2.csv"

    with file1.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["student", "coffee spent"])
        writer.writerow(["Иван", "100"])

    with file2.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["student", "coffee spent"])
        writer.writerow(["Анна", "500"])

    result = parse_csv_files([str(file1), str(file2)])

    expected_result = [{"student": "Иван", "coffee spent": "100"}, {"student": "Анна", "coffee spent": "500"}]
    assert result == expected_result, "Данные из нескольких файлов не объединились в общий набор"


def test_parse_csv_files_raises_error_on_non_numeric_data(tmp_path):
    bad_file = tmp_path / "bad_data.csv"
    with bad_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["student", "coffee_spent"])
        writer.writerow(["Иван", "сто рублей"])

    with pytest.raises(ValueError):
        parse_csv_files([str(bad_file)])
