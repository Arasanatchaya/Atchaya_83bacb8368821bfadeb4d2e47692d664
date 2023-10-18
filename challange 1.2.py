year=int(input("enter the number:"))
if((year%400==0)or(year%100!=0)):   print("the year is a leap")
if(year%4==0):
 print("the year is not a leap year")