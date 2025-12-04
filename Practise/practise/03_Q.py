from datetime import *

issue_date_str = input("Enter the date of issue(dd-mm-yyyy):")
return_date_str = input("Enter the date of return(dd-mm-yyyy):")

issue_date = datetime.strptime(issue_date_str, "%d-%m-%Y")
return_date = datetime.strptime(return_date_str, "%d-%m-%Y")

due_date = issue_date + timedelta(days=15)
delay_days = (return_date - due_date).days

if delay_days <= 5:
  fine = delay_days * 0.50
  print(f"Fine is:{fine}")
elif delay_days < 30:
  print(f"Membership cancelled")
elif delay_days <= 10:
  fine = delay_days * 1
  print(f"Fine is:{fine}")
else:
  fine = delay_days * 5
  print(f"Fine:{fine}")