from zipfile import ZipFile
import json


def open_zip_file(path_zip):
    """
    Функция распаковывает файл внутри ZIP-архива и возвращает его содержимое в формате JSON.
    :param path_zip: Путь к ZIP-архиву.
    :return: Содержимое файла в формате JSON.
    """
    with ZipFile(path_zip, "r") as myzip:
        for item in myzip.infolist():
            if item.filename.endswith(".json"):
                with myzip.open(item.filename, "r") as file:
                    return json.load(file)
