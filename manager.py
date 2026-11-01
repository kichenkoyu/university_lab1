import json
import xml.etree.ElementTree as ET
from dataclasses import asdict
from typing import Dict, Optional

from student import Student
from exceptions import UniversityError, EntityNotFoundError

class UniversityManager:
    def __init__(self):
        self.students: Dict[int, Student] = {}

    def create_student(self, student_id: int, name: str, group: str) -> Student:
        if student_id in self.students:
            raise UniversityError(f"Студент {student_id} уже существует.")
        student = Student(student_id, name, group)
        self.students[student_id] = student
        return student

    def read_student(self, student_id: int) -> Student:
        try:
            return self.students[student_id]
        except KeyError:
            raise EntityNotFoundError(f"Студент {student_id} не найден.")

    def update_student(self, student_id: int, name: Optional[str] = None, group: Optional[str] = None) -> Student:
        student = self.read_student(student_id)
        if name:
            student.name = name
        if group:
            student.group_name = group
        return student

    def delete_student(self, student_id: int) -> None:
        if student_id not in self.students:
            raise EntityNotFoundError(f"Студент {student_id} не найден.")
        del self.students[student_id]

    def export_to_json(self, filename: str) -> None:
        data = {"students": [asdict(s) for s in self.students.values()]}
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def import_from_json(self, filename: str) -> None:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.students = {s['id']: Student(**s) for s in data.get("students", [])}
        except FileNotFoundError:
            print(f"Ошибка: Файл {filename} не найден.")

    def export_to_xml(self, filename: str) -> None:
        root = ET.Element("UniversityData")
        students_element = ET.SubElement(root, "Students")
        for student in self.students.values():
            s_elem = ET.SubElement(students_element, "Student", id=str(student.id))
            ET.SubElement(s_elem, "Name").text = student.name
            ET.SubElement(s_elem, "GroupName").text = student.group_name
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)

    def import_from_xml(self, filename: str) -> None:
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            self.students.clear()
            for s_elem in root.find("Students"):
                s_id = int(s_elem.attrib['id'])
                name = s_elem.find("Name").text
                group = s_elem.find("GroupName").text
                self.students[s_id] = Student(s_id, name, group)
        except FileNotFoundError:
            print(f"Ошибка: Файл {filename} не найден.")