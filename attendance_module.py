class student:
    def __init__(
        self,
        sap_id: int,
        name: str,
        classroom_max: int,
        classroom_attended: int,
        sport_max: int,
        sport_attended: int,
        co_curricular_max: int,
        co_curricular_attended: int,
    ):
        self.sap_id = sap_id
        self.name = name
        self.classroom_max = classroom_max
        self.classroom_attended = classroom_attended
        self.sport_max = sport_max
        self.sport_attended = sport_attended
        self.co_curricular_max = co_curricular_max
        self.co_curricular_attended = co_curricular_attended

    def get_classroom_attendance(self) -> float:
        if self.classroom_max == 0:
            return 100.0
        if self.classroom_attended == 0:
            return 0.0
        return round(100 * (self.classroom_attended / self.classroom_max), 2)

    def get_sport_attendance(self) -> float:
        if self.sport_max == 0:
            return 100.0
        if self.sport_attended == 0:
            return 0.0
        return round(100 * (self.sport_attended / self.sport_max), 2)

    def get_co_curricular_attendance(self) -> float:
        if self.co_curricular_max == 0:
            return 100.0
        if self.co_curricular_attended == 0:
            return 0.0
        return round((self.co_curricular_attended / self.co_curricular_max) * 100, 2)

    def check_debar(self) -> bool:
        if (
            self.get_classroom_attendance() < 50.0
            or self.get_sport_attendance() < 20.0
            or self.get_co_curricular_attendance() < 10.0
        ):
            return True
        return False

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Sap ID: {self.sap_id}")
        print(f"Classroom Attendance: {self.get_classroom_attendance()}")
        print(f"Sport Attendance: {self.get_sport_attendance()}")
        print(f"Co-curricular Attendance: {self.get_co_curricular_attendance()}")


def search_student(students: list, sap_id: int):
    for student in students:
        if student.sap_id == sap_id:
            return student
    return None


def print_all_students(students: list):
    for student in students:
        student.print_info()
        print("\n")


def print_debarred_students(students: list):
    print("Debarred Students:".center(30, "-"))
    for student in students:
        if student.check_debar():
            print(f"Name: {student.name}")
