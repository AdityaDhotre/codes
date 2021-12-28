i=1
while(i==1):
    print("Medical Diagnosis")
    print("Do you have fever(y/n):")
    ch=input()
    if(ch=='y'):
        print("Do you have headache(y/n)")
        ch=input()
        if(ch=='y'):
            print("Do you have weakness(y/n)")
            ch=input()
            if(ch=='y'):
                print("You may have swineflue")
                print("Please Take Care")
            else:
                print("You have vommiting Problem")
                print("Please Take following Drug 1.ABC")
        elif(ch=='n'):
            print("You have muscle pain(y/n)")
            ch=input()
            print("Please take following drug for 2 days 1.Paracetamol")
            if(ch=='y'):
                print("You may have chickenpox")
                print("Please take the drug Antibiotic")
            else:
                print("You may have high temp")
                print("Please drink cold water and eat healthy food")

    elif(ch=='n'):
        print("You have normal(y/n)")
        ch=input()

        if(ch=='y'):
            print("you have breathing problem(y/n)")
            ch=input()
            if(ch=='y'):
                print("You may have asthma")
            else:
                print("you may have acidity")
                print("Please take ENO get well soon")
        else:
            print("you have cold(y/n)")
            ch=input()
            if(ch=='y'):
                print("you have coughing(y/n)")
                ch=input()
                if(ch=='y'):
                    print("you have itching problem(y/n)")
                    ch=input()
                    if(ch=='y'):
                        print("you may have infection")
                    else:
                        print("you may have cough")
                else:
                    print("you may have cold")
            else:
                print("you may have normal")
    print("Pleae refer Expert Doctor")
    print("for continue(1)")
    i=int(input())
