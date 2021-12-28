
#best first search
SuccList={"A":[["B",3],["C",2]],"B":[["A",5],["C",2],["D",2],["E",3]],"C":[["A",5],["B",3],["F",2],["G",4]],"D":[["H",1],["I",99]],"F":[["J",99]],"G":[["K",99],["L",3]]}
Start="A"
Goal="H"
Closed=list()
SUCCESS=True
FAILURE=False
State=FAILURE

def goal_test(n):
    if n==Goal:
        return True
    else:
        return False

def move_gen(n):
    new_list=list()
    if n in SuccList.keys():
        new_list=SuccList[n]
    return new_list

def Append(l1,l2):
    new_list=list(l1)+list(l2)
    return new_list

def Sort(l):
    l.sort(key=lambda x:x[1])  #['B'3]
    return l

def BestFirstSearch():
    OPEN=[[Start,5]]
    CLOSED=list()
    global State
    global Closed
    while(len(OPEN)!=0 and State != SUCCESS):
        print("----------")
        n=OPEN[0]
        print("N=",n)
        del OPEN[0]

        if goal_test(n[0])==True:
            State=SUCCESS
            CLOSED=Append(CLOSED,[n])
            print("CLOSED=",CLOSED)
        else:
            CLOSED=Append(CLOSED,[n])
            print("CLOSED=",CLOSED)
            CHILD=move_gen(n[0])
            print("CHILD=",CHILD)
            for val in OPEN:
                if val in CHILD:
                    CHILD.remove(val)
            for val in CLOSED:
                if val in CHILD:
                    CHILD.remove(val)
            OPEN=Append(CHILD,OPEN)
            print("Unsorted OPEN=",OPEN)
            Sort(OPEN)
            print("Sorted OPEN=",OPEN)
    Closed=CLOSED
    return State

print(BestFirstSearch())
