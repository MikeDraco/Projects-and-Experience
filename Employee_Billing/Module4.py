def readHourlyRate():
    while True:
        try:
            hourlyRate=float(input("Hourly Rate: "))
        except Exception:
            hourlyRate=1
        if hourlyRate<20:
            print("Invalid Hourly Rate, must be at least $20.00/hour.\n")
        else:
            break
    return hourlyRate
            
def readEmployeeName():
    while True:
        employeeName=input("Employee Name: ")
        if employeeName=='':
            print("Employee name must be entered.\n")
        else:
            return employeeName
            break

def readWeeklyHours(val):
    val=str(val)
    while True:
        try:
            hoursWeek=float(input("Enter hours worked for week "+val+": "))
        except Exception:
            hoursWeek=1
        if hoursWeek>80 or hoursWeek<35:
            print("Invaild number of hours, must be between 35 and 80.\n")
        else:
            break
    return hoursWeek

def resetBillingFile():
    billing=open('Billing.txt','w')
    billing.close()

def writeBillingRecord(val1,val2,val3,val4,val5,val6):
    billing=open('Billing.txt','a')
    billing.write(val1+'\n'+str(val2)+'\n'+str(val3)+'\n'+str(val4)+'\n'+str(val5)+'\n'+str(val6)+'\n')
    
    

        


