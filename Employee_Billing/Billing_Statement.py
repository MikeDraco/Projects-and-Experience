#input
import Module4

def main():

    runAgain='y'
    Module4.resetBillingFile()

    while runAgain=='y':
        employee_name=Module4.readEmployeeName()
        hourly_rate=Module4.readHourlyRate()
        hours_week1=Module4.readWeeklyHours(1)
        hours_week2=Module4.readWeeklyHours(2)
        hours_week3=Module4.readWeeklyHours(3)
        hours_week4=Module4.readWeeklyHours(4)

        Module4.writeBillingRecord(employee_name,hourly_rate,hours_week1,hours_week2,hours_week3,hours_week4)

#process
        total_hours=hours_week1+hours_week2+hours_week3+hours_week4
        average_weekly_hours=((total_hours)/4)
        overtime_hours=total_hours-160
        overtime_rate=hourly_rate*1.05
        overtime_pay=overtime_hours*overtime_rate
        regular_pay=(total_hours-overtime_hours)*hourly_rate
        amount_due=overtime_pay+regular_pay

#output
#checking to see if there is overtime
        if total_hours>160:
            print("\n"+employee_name,"worked",overtime_hours,"hours of overtime.")
        else:
            print("\n"+employee_name, "has worked no overtime.")
    
        print("\nInvoice")
        print("Resource:",employee_name,"\tAverage weekly hours:",format(average_weekly_hours,'.2f'))   
        print("\nTotal Billable Hours: ",format(total_hours,'.2f'),"\trate: $",format(hourly_rate,'.2f'),sep='')
        if total_hours>160:
            print("Overtime Hours:",format(overtime_hours,'.2f'),"@ $"+format(overtime_rate,'.2f'),"\t\t= $"+format(overtime_pay,',.2f'))
        print("Regular Hours:",format(total_hours-overtime_hours,'.2f'),"@ $"+format(hourly_rate,'.2f'),"\t\t= $"+format(regular_pay,',.2f'))
        print('Amount Due: $'+format(amount_due,',.2f'))

#Checking if the user would like to run the program again
        runAgain=str(input("\nEnter another employee?('y'=yes): "))

    print("\nProgram ended normally.")


main()


 
