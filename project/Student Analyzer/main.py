# SMART STUDENT EXPENSE & STUDY ALALYSER 
# Colsole Besed Python Project 
from datetime import datetime
print("SMART STUDENT ALALYSER")

#LOGIN SYSTEM

username = input("Enter Your Username: ")
password = input("Enter Your Password: ")
if username !="jigar" or password !="90012":
    print("Invlid Password and Username Plz Try Agin.")
    exit()
print("\n Susccesful Login. Welcome", username )

expenses = []
study_record = []

while True:
    print("\n MAIN MENU")
    print("1. Add Expense")
    print("2. Add Study Houre")
    print("3. View Summary ")
    print("4. View Expense History")
    print("5. Productivity Feedback")
    print("6. Exit")
    choice = input("Enter Your choice (1-6):").strip()
    
    if choice =="1":
        print("\n Add Expense")
        try:
            amount = float(input("Enter Amount: "))
            category = input("Enter category (Food/Travel/Study/Other):")
            date = datetime.now().strftime("%d-%m-%Y")
            
            expenses.append({
                "amount": amount,
                "category": category,
                "date": date
                
            })
            print("Expense added" , date)
        except ValueError:
            print("Amount must ba a number")
            
    elif choice =="2":
        print("\n Add Study Houre")
        try:
            subject = input("Enter a Subject: ")
            hours = float(input("Enter study houers: "))
            date = datetime.now().strftime("%d-%m-%Y")
            
            study_record.append({
                "subject" : subject,
                "hours": hours,
                "date" : date
            })
            print("Study hours added", date)
            
        except ValueError:
            print("Hours must be a number")
        
    elif choice =="3":
        print("\n Summary")
        
        total_expense = sum(e["amount"] for e in expenses)
        total_study = sum(s["hours"] for s in study_record)
        
        print("Total Expense: ", total_expense)
        print("Total Study Hours:", total_study)
        
    elif choice == "4":
        print("\n Expense History")
        
        if not expenses:
            print("No expenses Addes yet.")
        else:
            for i, e in enumerate(expenses, start=1):
                print(f"{i}. {e['date']} | {e['category']} | {e['amount']}")
        
    elif choice == "5":
        print("\n Productivity Feedback")
        
        total_study = sum(s["hours"] for s in study_record)
        
        if total_study >= 4:
            print(" Godd Job Study hours are Good.")
        elif total_study > 0:
            print(" Study more . Minimum 4 hours are need.")
        else:
            print("No Study data founf.")
            
    elif choice == "6":
        print("\n Thank You. ")
        break
    else:
        print("Invalid choice. Please enter 1 to 6.")