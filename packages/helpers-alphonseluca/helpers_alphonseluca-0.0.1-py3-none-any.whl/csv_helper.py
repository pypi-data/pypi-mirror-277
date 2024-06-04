import csv
from .path_helper import ensurePathExist


def save(path: str, data: list[dict], header: list[str] = None):
    # create and save csv
    ensurePathExist(path)
    with open(path, "w+", encoding="utf-8", newline="") as csvfile:
        fieldnames = header if header is not None else data[0].keys()
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writeheader()
        csvwriter.writerows(data)


def create(path: str, header: list):
    """
    Purpose: path:str
    """
    ensurePathExist(path)
    with open(path, "w+", encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=header)
        csvwriter.writeheader()


def appendRow(path: str, data: dict):
    with open(path, "a+", encoding="utf-8", newline="") as csvfile:
        fieldnames = data.keys()
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writerow(data)
    # end open file


def appendRows(path: str, data: list[dict], header: list[str] = None):
    with open(path, "a+", encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=header)
        csvwriter.writerows(data)


__all__ = ["save", "create", "appendRow", "appendRows"]
