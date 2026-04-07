from unittest.mock import patch

from cli import parse_args


def test_parse_args_default_report():
    with patch("sys.argv", ["main.py", "--files", "data1.csv", "data2.csv"]):
        args = parse_args()

        assert args.files == ["data1.csv", "data2.csv"], "Аргумент --files спарсился неверно"
        assert args.report == "median-coffee", "Не сработало значение по умолчанию для --report"


def test_parse_args_custom_report():
    with patch("sys.argv", ["main.py", "--files", "data1.csv", "--report", "new-report"]):
        args = parse_args()

        assert args.files == ["data1.csv"]
        assert args.report == "new-report", "Аргумент --report спарсился неверно"
