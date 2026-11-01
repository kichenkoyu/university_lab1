from university import University
from manager import UniversityManager
from exceptions import EntityNotFoundError, UniversityError

if __name__ == "__main__":
    manager = UniversityManager()
    stankin = University(name="МГТУ СТАНКИН", faculties=[])

    print("--- Демонстрация CRUD-операций ---")
    try:
        manager.create_student(1, "Юлия Киченко", "ИДБ-25-11")
        manager.create_student(2, "Влад", "ИДБ-25-11")
        print("Студенты добавлены.")

        print(f"Чтение студента 1: {manager.read_student(1)}")
        manager.update_student(2, group="ИИ-25-1")
        print(f"После обновления: {manager.read_student(2)}")

        manager.delete_student(2)
        print("Студент 2 успешно удален.")

        print("\n--- Экспорт данных ---")
        manager.export_to_json("university.json")
        manager.export_to_xml("university.xml")
        print("Файлы успешно созданы.")

        print("\n--- Обработка исключений ---")
        manager.read_student(999)

    except EntityNotFoundError as e:
        print(f"Перехвачено ожидаемое исключение EntityNotFoundError: {e}")
    except UniversityError as e:
        print(f"Ошибка бизнес-логики: {e}")