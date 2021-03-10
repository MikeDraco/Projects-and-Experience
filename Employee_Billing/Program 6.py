
    
def main():
    
    runAgain=1

    while runAgain!=0:
        print("\nBilling System Menu:","\n\n\t0-end","\n\t1-Enter billing Data","\n\t2-Display adhoc billing report")
        try:
            runAgain=int(input("\nOption==>"))
        except Exception:
            print("\nPlease enter a valid integer")
        if runAgain==0:
            print("\nProgram terminated")
        elif runAgain<0 or runAgain>2:
            print("\nPlease enter a valid integer")
        elif runAgain==1:
            import Billing_Statement
        elif runAgain==2:
            import Adhoc_Report
            

main()
