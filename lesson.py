from dataclasses import dataclass

@dataclass
class Lesson:
    course_id: int
    teacher_id: int
    classroom_number: str
    time: str