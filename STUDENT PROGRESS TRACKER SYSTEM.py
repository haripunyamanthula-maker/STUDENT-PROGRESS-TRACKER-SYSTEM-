print("-------------------------------------------")
print("     STUDENT PROGRESS TRACKER SYSTEM")
print("-------------------------------------------")
STUDENT=(input(" ENTER YOUR NAME  : "))
CLASS=(input(  " ENTER YOUR CLASS : "))
ROLL_NUMBER=(input( " ENTER YOUR ROLL NUMBER   : "))
SUBJECTS=(int(input(" ENTER NUMBER OF SUBJECTS : ")))
TOTAL=0
failed_subjects=[]
for sub in range(1, SUBJECTS+1):
    MARKS=(float(input(f" ENTER YOUR SUBJECT {sub} MARKS :")))
    if MARKS<35:
        print(f" FAILED IN :[{sub}]")
        failed_subjects.append(sub)
    TOTAL += MARKS
AVERAGE=TOTAL/SUBJECTS
print(" TOTAL MARKS       :",TOTAL)
print(" AVERAGE MARKS     :",AVERAGE)
if AVERAGE>=90:
    GRADE ="A"
elif AVERAGE>=75:
    GRADE ="B"
elif AVERAGE>=50:
    GRADE ="C"
elif AVERAGE>=35:
    GRADE ="D"
else:
    GRADE ="fail"

if (len(failed_subjects)==0):
    print(" YOU ARE PASSED ALL SUBJECTS")
else:
    print(" YOU ARE FAIL")
    print(f" YOU ARE FAILED IN :{failed_subjects}")

#student report card
print("")
print("=-----------------------------------------=")
print("          STUDENT REPORT CARD")
print("=-----------------------------------------=")
print("NAME          :",STUDENT)
print("CLASS NAME    :",CLASS)
print("ROLL NUMBER   :",ROLL_NUMBER)
print("TOTAL MARKS   :",TOTAL)
print("AVERAGE MARKS :",AVERAGE)
print("GRADE         :",GRADE)
if (len(failed_subjects)!=0):
    print( "RESULT        : FAIL ")
else:
    print( "RESULT        : PASS ")

#MAIN MENU SYSTEM
print("")
print("==========================================")
print("          MAIN MENU SYSTEM ")
print("==========================================")
print("")
print("WHAT DO WANT TO DO NEXT")
print("1 = VIEW TOTAL MARKS")
print("2 =VIEW AVERAGE MARKS ")
print("3 = VIEW REPORT AGAIN")
print("4= EXIT ")
choice=input("Enter your choice :")
while choice!="4":
    if choice=="1":

        print(f"The Total Marks: {TOTAL}")
        print("---------------------------------------------")
        choice=input("Enter your choice :")
    elif choice=="2":
        print(f"The Student Average: {AVERAGE}")
        print("---------------------------------------------")
        choice=input("Enter your choice :")

    elif choice=="3":
        print("          STUDENT PROGRESS REPORT            ")
        print("---------------------------------------------")
        print(f"STUDENT NAME    :{STUDENT}")
        print(f"STUDENT CLASS   :{CLASS}")
        print(f"STUDENT ROLL NO :{ROLL_NUMBER}")
        print(f"STUDENT AVERAGE :{AVERAGE}")
        print(f"STUDENT GRADE   :{GRADE}")
        print(f"MARKS         :{MARKS}")
        if (len(failed_subjects)!=0):
           print( "RESULT        : FAIL ")
        else:
           print( "RESULT        : PASS ")
        print("---------------------------------------------")
        choice=input("Enter your choice :")
        print("---------------------------------------------")
    elif choice=="4":
        exit
print(" THANK YOU_ ")
print("---------------------------------------------")
