
def freedompay ():
    try:
        total_hours = None
        hours = None
        minutes = None
        grand_total_basic_40 = 0
        grand_total_OT_40 = 0
        grand_total_basic_80 = 0
        grand_total_OT_80 = 0
        great_grand_total = 0
        base_pay = None
        base_pay_incl_OT_40 =0
        base_pay_incl_OT_80 =0
        rate = None
        user_input = None
        while True:
            prompt_1 = input ("Enter Worked Hours and Minutes\nFormat (00:00): ")
            if (prompt_1 == "done") and (hours is None or minutes is None) :
                print ("Uh uh uh! Add numbers to calculate")
                continue
            elif (prompt_1 == "done") and (base_pay != None):
                print ("You are Done, Amigo!")
                break
            try:
                user_input = prompt_1
                (hours, minutes) = user_input.split(":")
                hours = float (hours)
                minutes = float (minutes)
                if hours<0.0 or minutes< 0.0:
                    print ("Uh uh uh! Negative Numbers are not accepted!")
                    continue
            except:
                print ("Uh uh uh! You didn't say the magic word!")
                continue
            print ("Hours:",int (hours), "\nMinutes:", int (minutes))
            minutes = (minutes/60)
            total_hours = hours + minutes

            rate = input ("Enter Pay Rate: ")
            try:
                rate = float (rate)
            except:
                print ("Uh uh uh! You didn't add a valid rate!")
                continue

            prompt_2 = input ("Weekly hrs?: ")
            base_pay = total_hours * rate
            
            if prompt_2 == "yes":
                if total_hours <= 40:
                    grand_total_basic_40 = base_pay + grand_total_basic_40
                    print ( "Pay: ", base_pay)   
                elif total_hours > 40:
                    base_pay_incl_OT_40 = ((hours - 40) * rate * 0.5) + base_pay
                    grand_total_OT_40 = base_pay_incl_OT_40 + grand_total_OT_40
                    print ("Pay with OT: ", base_pay_incl_OT_40)

            else:
                prompt_3 = input ("Bi-weekly hrs?: ")
                if prompt_3 == "yes":
                    if total_hours <= 80:
                        grand_total_basic_80 = base_pay + grand_total_basic_80
                        print ( "Pay: ", base_pay)   
                    elif total_hours > 80:
                        base_pay_incl_OT_80 = ((hours - 80) * rate * 0.5) + base_pay
                        grand_total_OT_80 = (base_pay_incl_OT_80 + grand_total_OT_80)
                        print ("Pay with OT: ", base_pay_incl_OT_80)
                else:
                    print ("Uh uh uh! You did not say Weekly or Bi-Weekly")

        great_grand_total = grand_total_basic_40 + grand_total_OT_40 + grand_total_basic_80 + grand_total_OT_80
        print ("Great Grand Total:", round (great_grand_total,2))
    except: 
        print ("Uh uh uh!")

freedompay ()

# Test 40hrs
# 45 hrs
# 10.50 rate
# output = 498.75

#Test 80 hrs
# 85 hrs
# 10.50 rate
# output = 918.75