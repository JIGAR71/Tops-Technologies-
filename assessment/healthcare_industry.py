class ClinicAppointment:
    def __init__(self):
        self.doctors = ["Dr. A", "Dr. B", "Dr. C"]
        self.slots = ["10 AM", "11 AM", "12 PM", "2 PM", "3 PM"]
        self.bookings = {}
        for d in self.doctors:
            self.bookings[d] = {}
            for s in self.slots:
                self.bookings[d][s] = []
        self.lookup = {}

    def book(self, name, age, mobile, doctor, slot):
        if doctor not in self.doctors:
            return "Doctor not available"
        if slot not in self.slots:
            return "Invalid slot"
        if mobile in self.lookup:
            return "You already have an appointment"
        if len(self.bookings[doctor][slot]) >= 3:
            return f"{doctor} at {slot} is full"

        p = {"name": name, "age": age, "mobile": mobile}
        self.bookings[doctor][slot].append(p)
        self.lookup[mobile] = (doctor, slot, p)
        return f"Booked with {doctor} at {slot}"

    def view(self, mobile):
        if mobile not in self.lookup:
            return "No appointment found"
        d, s, p = self.lookup[mobile]
        return f"{p['name']} ({p['age']} yrs) with {d} at {s}"

    def cancel(self, mobile):
        if mobile not in self.lookup:
            return "No appointment found"
        d, s, p = self.lookup[mobile]
        self.bookings[d][s] = [x for x in self.bookings[d][s] if x["mobile"] != mobile]
        del self.lookup[mobile]
        return f"Cancelled for {p['name']}"

    def schedule(self, doctor):
        if doctor not in self.doctors:
            return "Doctor not available"
        out = f"Schedule for {doctor}\n"
        for s in self.slots:
            c = len(self.bookings[doctor][s])
            out += f"{s}: {c}/3 booked\n"
        return out

if __name__ == "__main__":
    c = ClinicAppointment()
    while True:
        print("\n--- Clinic Appointment ---")
        print("1. Book Appointment")
        print("2. View Appointment")
        print("3. Cancel Appointment")
        print("4. Doctor Schedule")
        print("5. Exit")
        ch = input("Choice: ")
        if ch == "1":
            n = input("Name: ")
            a = input("Age: ")
            m = input("Mobile: ")
            print("Doctors:", c.doctors)
            d = input("Doctor: ")
            print("Slots:", c.slots)
            s = input("Slot: ")
            print(c.book(n, a, m, d, s))
        elif ch == "2":
            m = input("Mobile: ")
            print(c.view(m))
        elif ch == "3":
            m = input("Mobile: ")
            print(c.cancel(m))
        elif ch == "4":
            d = input("Doctor: ")
            print(c.schedule(d))
        elif ch == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice")
