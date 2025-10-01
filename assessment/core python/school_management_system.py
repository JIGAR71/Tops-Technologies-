class schoolmanagement:
    def __init__(self):
        self.students = {}
        self.next_id = 1

    def newadmission(self, name, age, std, mobile):
        if age < 5 or age > 18:
            return "age must be 5 to 18"
        if std < 1 or std > 12:
            return "class must be 1 to 12"
        if len(mobile)!=10 or not mobile.isdigit():
            return "mobile must be 10 digit"
        sid = self.next_id
        self.next_id += 1
        self.students[sid] = {"name":name,"age":age,"class":std,"mobile":mobile}
        return f"admission done id {sid}"

    def viewstudent(self, sid):
        if sid in self.students:
            s = self.students[sid]
            return f"id:{sid} name:{s['name']} age:{s['age']} class:{s['class']} mobile:{s['mobile']}"
        return "not found"

    def updatestudent(self, sid, mobile=None, std=None):
        if sid not in self.students:
            return "not found"
        if mobile:
            if len(mobile)==10 and mobile.isdigit():
                self.students[sid]["mobile"]=mobile
            else:
                return "mobile must be 10 digit"
        if std:
            if 1<=std<=12:
                self.students[sid]["class"]=std
            else:
                return "class must be 1 to 12"
        return f"id {sid} updated"

    def removestudent(self, sid):
        if sid in self.students:
            del self.students[sid]
            return f"id {sid} deleted"
        return "not found"

    def run(self):
        while True:
            print("1.new admission")
            print("2.view student")
            print("3.update student")
            print("4.remove student")
            print("5.exit")
            ch = input("enter choice:")
            if ch=="1":
                n=input("name:")
                a=int(input("age:"))
                c=int(input("class:"))
                m=input("mobile:")
                print(self.newadmission(n,a,c,m))
            elif ch=="2":
                sid=int(input("id:"))
                print(self.viewstudent(sid))
            elif ch=="3":
                sid=int(input("id:"))
                m=input("new mobile blank if no change:")
                c=input("new class blank if no change:")
                m = m if m.strip()!="" else None
                c = int(c) if c.strip().isdigit() else None
                print(self.updatestudent(sid,m,c))
            elif ch=="4":
                sid=int(input("id:"))
                print(self.removestudent(sid))
            elif ch=="5":
                break
            else:
                print("wrong choice")

sm = schoolmanagement()
sm.run()