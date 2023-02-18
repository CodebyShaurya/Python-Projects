import math
SIMPLECALCUL ==0
T=0https://www.tvseriesnmovies.com/links/view/UicFUr4A8O
xs=[]
while T==0:
z=int(input(' Enter 1 for NORMAL CALCULATOR\n Enter 2 for SCIENTIFIC CALCULATOR \n Enter any other number to EXIT :\n' ))
if z==1:
    

#sIMPLE CALCULATOR




    while SIMPLECALCUL ==0:      
    result=int(input(' Enter the number:\n'))
    xs.append(result)
    while True:
        abz=int(input(' Enter 1 for addition\n Enter 2 for subtaction\n Enter 3 for multiplication\n Eneter 4 for division \n Enter any other number to get the result :\n' ))
        if abz==1:
           xs.append('+')
        elif abz==2:
           xs.append('-')
        elif abz==3:
           xs.append('x')
        elif abz==4:
            xs.append('/')
        else:
            break 
      a=int(input(' Enter the number:\n'))
      xs.append(a)
      if abz==1:
            result=result+a
        elif abz==2:
            result=result-a
        elif abz==3:
            result=result*a
        elif abz==4:
        result=result/a

    for x in range(len(xs)):  
        print(xs[x],end="")
    print('=',result)        
    Fz=int(input(' Enter 1 TO exit\n Enter 2 for SCIENTIFIC CALCULATOR \n Enter any other number to contuinue the same :\n' ))
    if Fz==1:
        SIMPLECALCUL=1

#SCIENTIFIC CALCULATOR

if z==2 :


    while SCICALCUL ==0:      
    result=int(input(' Enter the number:\n'))
    xs.append(result)
    while True:
        abz=int(input(' Enter 1 for addition\n Enter 2 for subtaction\n Enter 3 for multiplication\n Eneter 4 for division \n Enter any other number to get the result :\n' ))
        if abz==1:
           xs.append('+')
        elif abz==2:
           xs.append('-')
        elif abz==3:
           xs.append('x')
        elif abz==4:
            xs.append('/')
        else:
            break 
      a=int(input(' Enter the number:\n'))
      xs.append(a)
      if abz==1:
            result=result+a
        elif abz==2:
            result=result-a
        elif abz==3:
            result=result*a
        elif abz==4:
        result=result/a

    for x in range(len(xs)):  
        print(xs[x],end="")
    print('=',result)        
    Fz=int(input(' Enter 1 TO exit\n Enter 2 for SCIENTIFIC CALCULATOR \n Enter any other number to contuinue the same :\n' ))
    if Fz==1:
        SIMPLECALCUL=1    
