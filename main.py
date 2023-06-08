from utils import open_zip_file
from classes.operations import Operations


def main():
    """
    Основная функция программы.
    Открывает ZIP-архив 'operations.zip' и выводит информацию о 5 последних операциях.
    """
    operations = open_zip_file('operations.zip')
    operations = Operations(operations)
    operations.output_last_operations()


if __name__ == '__main__':
    main()