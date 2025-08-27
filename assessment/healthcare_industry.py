class clinicappointment:
    def __init__(self):
        self.doctors=["dr a","dr b","dr c"]
        self.slots=["10am","11am","12pm","2pm","3pm"]
        self.app={}
        for d in self.doctors:
            self.app[d]={}
            for s in self.slots:
                self.app[d][s]=[]
        self.lookup={}

    def book(self,n,a,m,d,s):
        if d not in self.doctors:
            return "no doctor"
        if s not in self.slots:
            return "no slot"
        if m in self.lookup:
            return "already booked"
        if len(self.app[d][s])>=3:
            return "slot full"
        p={"name":n,"age":a,"mobile":m}
        self.app[d][s].append(p)
        self.lookup[m]=(d,s,p)
        return "booked with "+d+" at "+s

    def view(self,m):
        if m in self.lookup:
            d,s,p=self.lookup[m]
            return f"{p['name']} {p['age']}y {d} {s}"
        return "not found"

    def cancel(self,m):
        if m in self.lookup:
            d,s,p=self.lookup[m]
            self.app[d][s]=[x for x in self.app[d][s] if x["mobile"]!=m]
            del self.lookup[m]
            return "cancelled"
        return "not found"

    def showschedule(self,d):
        if d not in self.doctors:
            return "no doctor"
        for s in self.slots:
            print(s,":",len(self.app[d][s]),"/3")

clinic=clinicappointment()
while True:
    print("1.book")
    print("2.view")
    print("3.cancel")
    print("4.schedule")
    print("5.exit")
    ch=input("choice:")
    if ch=="1":
        n=input("name:")
        a=input("age:")
        m=input("mobile:")
        print("doctors:",clinic.doctors)
        d=input("doctor:")
        print("slots:",clinic.slots)
        s=input("slot:")
        print(clinic.book(n,a,m,d,s))
    elif ch=="2":
        m=input("mobile:")
        print(clinic.view(m))
    elif ch=="3":
        m=input("mobile:")
        print(clinic.cancel(m))
    elif ch=="4":
        d=input("doctor:")
        clinic.showschedule(d)
    elif ch=="5":
        break
    else:
        print("wrong choice")
