def newuser(n,slot,sassignu,sassign,allow,frame):
    x=input("Do you want to create a new user? (yes/no) :")
    if x=="yes":
        n+=1
        print("Enter time required for the user:")
        print("M"+str(n)+":",end="")
        y=input()
        tusers.append(y)
        print("Assign slot to user:")
        print("Slots left for assigning",end=":")
        for i in range(8):
            if allow[i]==0:
                print(str(i+1),end=" ")      
        print("\n")
        print("M"+str(n)+" is assigned slot:",end="")
        y=int(input())
        sassign.append(y)
        sassignu[y-1]=n
        allow[y-1]=int(1)
        slot[y-1]=float(tusers[n-1])
        calculate(n,slot,sassignu,sassign,allow,frame)
    calculate(n,slot,sassignu,sassign,allow,frame)

def checkslot():
    f=0
    for i in range(n):
        x=sassign[i]
        if slot[x-1]<0:
            f+=1
    
    if f==n:
        return 0
    return 1


frame=0
def calculate(n,slot,sassignu,sassign,allow,frame): 
    while (checkslot()!=0):
        frame+=1
        print("Frame ",frame)
        for i in range(n):
            x=sassign[i]
            if slot[x-1]>0:
                slot[x-1]=slot[x-1]-0.577
        for i in range(8):
            if slot[i]==0:
                print("Slot "+str(i+1)+" : Idle")
            else:
                print("Slot "+str(i+1)+" : M"+str(sassignu[i])+" transmits (left over time :"+str(slot[i])+" )")
            if slot[i]<0:
                allow[i]+=1
        for i in range(8):
            if allow[i]==2:
                newuser(n,slot,sassignu,sassign,allow,frame)

print("Note: 1 TDMA slot is of 0.577 ms and such 8 slots makes up one TDMA frame of 4.616 ms.")
n=int(input("Enter number of users:"))
print("Enter time required for each user:")
tusers=[]
for i in range(n):
    print("M"+str(i+1)+":",end="")
    x=input()
    tusers.append(x)
print("Assign slots to users:")
sassign=[]
for i in range(n):
    print("M"+str(i+1)+" is assigned slot:",end="")
    x=int(input())
    sassign.append(x)
slot=[0,0,0,0,0,0,0,0]
sassignu=[0,0,0,0,0,0,0,0]
allow=[0,0,0,0,0,0,0,0]
for i in range(n):
    x=sassign[i]
    sassignu[x-1]=i+1
    allow[x-1]=int(1)
    slot[x-1]=float(tusers[i])
frame=0
calculate(n,slot,sassignu,sassign,allow,frame)