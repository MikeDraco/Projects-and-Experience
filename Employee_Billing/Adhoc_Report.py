def main():
    billing=open('Billing.txt','r')

    print('Employee'+'\tRate'+'\tWeek 1'+'\tWeek 2'+'\tWeek 3'+'\tWeek 4'+'\tHours'+'\tTotal')

    name= 'sean'
    iteration=0
    totalBillableDue=0
    totalBillableHours=0

    while name!='':
        name=str(billing.readline().rstrip('\n'))
        if name=='':
            break
        rate=float(billing.readline().rstrip('\n'))
        week1=float(billing.readline().rstrip('\n'))
        week2=float(billing.readline().rstrip('\n'))
        week3=float(billing.readline().rstrip('\n'))
        week4=float(billing.readline().rstrip('\n'))
        

        iteration+=1
        employeeHours= week1+week2+week3+week4
        overtimeHours=employeeHours-160
        overtimeRate=rate*1.05
        if employeeHours>160:
            totalPaid=(overtimeHours*overtimeRate)+(160*rate)
        else:
            totalPaid=employeeHours*rate
        totalBillableDue+=totalPaid
        totalBillableHours+=employeeHours
        averageBillableHours=totalBillableHours/iteration
        

        print(name,'\t$'+format(rate,'.2f')+'\t'+format(week1,'.2f')+'\t'+format(week2,'.2f')+'\t'+format(week3,'.2f')+'\t'+format(week4,'.2f')+'\t'+format(employeeHours,'.2f')+'\t$'+format(totalPaid,',.2f'))
      
    billing.close
    print("Total Billable Due: $"+format(totalBillableDue,',.2f'))
    print("Total Billable Hours: "+format(totalBillableHours,',.2f'))
    print("Average Billable Hours: "+format(averageBillableHours,',.2f'))

     
    
main()
        
    
