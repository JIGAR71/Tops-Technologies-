import random

class busreservation:
    def __init__(self):
        self.routes = {"mumbai to pune":500,"delhi to jaipur":600,"bangalore to chennai":700,"ahmedabad to surat":400,"kolkata to digha":350}
        self.tickets = {}
        self.seats = {}

    def showroutes(self):
        for r,p in self.routes.items():
            print(r,"- ₹",p)

    def bookticket(self):
        n=input("name:")
        a=int(input("age:"))
        m=input("mobile:")
        self.showroutes()
        r=input("route:")
        if r not in self.routes:
            print("invalid route")
            return
        if self.seats.get(r,0)>=40:
            print("full")
            return
        tid="T"+str(random.randint(10000,99999))
        sn=self.seats.get(r,0)+1
        self.seats[r]=sn
        self.tickets[tid]={"name":n,"age":a,"mobile":m,"route":r,"seat":sn,"price":self.routes[r]}
        print("ticket booked id:",tid," seat:",sn)

    def viewticket(self):
        tid=input("ticket id:")
        if tid in self.tickets:
            t=self.tickets[tid]
            for k,v in t.items():
                print(k,":",v)
        else:
            print("not found")

    def cancelticket(self):
        tid=input("ticket id:")
        if tid in self.tickets:
            r=self.tickets[tid]["route"]
            del self.tickets[tid]
            self.seats[r]-=1
            print("ticket cancelled")
        else:
            print("not found")

    def run(self):
        while True:
            print("1.show routes")
            print("2.book ticket")
            print("3.view ticket")
            print("4.cancel ticket")
            print("5.exit")
            ch=input("choice:")
            if ch=="1":
                self.showroutes()
            elif ch=="2":
                self.bookticket()
            elif ch=="3":
                self.viewticket()
            elif ch=="4":
                self.cancelticket()
            elif ch=="5":
                break
            else:
                print("wrong choice")

br=busreservation()
br.run()
