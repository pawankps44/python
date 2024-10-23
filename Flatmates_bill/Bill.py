from flatmate_bill import Flatmates, Flat_Bill

from generate import Pdf

flatmate1 = input("enter flatmate1 name:")
flatmate2 = input("enter flatmate2 name:")
flatmate1_days_stayed = int(input(f"No of days {flatmate1} stayed:"))
flatmate2_days_stayed = int(input(f"No of days {flatmate2} stayed:"))

total_bill = input("the total bill rent =")
time_period = input("time period of rent is:")

f1 = Flatmates(flatmate1, flatmate1_days_stayed)
f2 = Flatmates(flatmate2, flatmate2_days_stayed)
bill = Flat_Bill(total_bill, time_period)
pdf = Pdf('Flatamates_Bill.pdf')
pdf.generate_pdf(f1,f2,bill)
print(f"Total bill of {flatmate1} =", bill.flatmate_bill(f1,f2))
print(f"Total bill of {flatmate2}=",bill.flatmate_bill(f2,f1))

