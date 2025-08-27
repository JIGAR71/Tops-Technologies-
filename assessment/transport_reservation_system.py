class SchoolManagement:
    def __init__(self):
        self.students = {}
        self.next_id = 1

    def new_admission(self, name, age, student_class, mobile):
        if age < 5 or age > 18:
            return "Age must be between 5 and 18!"
        if student_class < 1 or student_class > 12:
            return "Class must be between 1 and 12!"
        if len(mobile) != 10 or not mobile.isdigit():
            return "Mobile number must be 10 digits!"

        sid = self.next_id
        self.students[sid] = [name, age, student_class, mobile]
        self.next_id += 1
        return f"Student admitted successfully! ID: {sid}"

    def view_student(self, sid):
        if sid in self.students:
            d = self.students[sid]
            return f"ID: {sid}, Name: {d[0]}, Age: {d[1]}, Class: {d[2]}, Mobile: {d[3]}"
        else:
            return "No record found!"

    def update_student(self, sid, mobile=None, student_class=None):
        if sid not in self.students:
            return "No record found!"
        if mobile:
            if len(mobile) == 10 and mobile.isdigit():
                self.students[sid][3] = mobile
            else:
                return "Mobile must be 10 digits!"
        if student_class:
            if 1 <= student_class <= 12:
                self.students[sid][2] = student_class
            else:
                return "Class must be between 1 and 12!"
        return f"Student ID {sid} updated!"

    def remove_student(self, sid):
        if sid in self.students:
            del self.students[sid]
            return f"Student ID {sid} removed!"
        else:
            return "No record found!"

    def run(self):
        while True:
            print("\n--- School Management ---")
            print("1. New Admission")
            print("2. View Student")
            print("3. Update Student")
            print("4. Remove Student")
            print("5. Exit")
            ch = input("Enter choice: ")

            if ch == "1":
                name = input("Name: ")
                age = int(input("Age: "))
                cls = int(input("Class (1-12): "))
                mob = input("Guardian Mobile: ")
                print(self.new_admission(name, age, cls, mob))
            elif ch == "2":
                sid = int(input("Student ID: "))
                print(self.view_student(sid))
            elif ch == "3":
                sid = int(input("Student ID: "))
                mob = input("New Mobile (leave blank to skip): ")
                cls = input("New Class (leave blank to skip): ")
                mob = mob if mob.strip() != "" else None
                cls = int(cls) if cls.strip().isdigit() else None
                print(self.update_student(sid, mob, cls))
            elif ch == "4":
                sid = int(input("Student ID: "))
                print(self.remove_student(sid))
            elif ch == "5":
                print("Exiting system...")
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    sm = SchoolManagement()
    sm.run()
