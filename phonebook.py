import csv



    
while True:

   
    print('WELCOME TO PHONEBOOK')
    print('Some of your contacts have already been stored')

    next=int(input('\n   Press 1 to enter any entry in phonebook \n   Press 2 to delete any entry in phonebook \n   Press 3 to access any entry in phonebook \n      Press 4 to exit \n   '))
    if next==1 :
        name=input('Enter the Name : ')
        phone=input('Enter the Phone No. : ')
        conc=[name,phone]                
        a=open('contacts.csv','a')
        q=csv.writer(a)
        q.writerow(conc)
        a.close()

               
    if next==2:
        namae=input('Enter the Name of the contact you want to delete : ')
        a=open('contacts.csv','a')
        q=csv.reader(a)
        qqw=[]
        for row in q:
            print(row)
            
        er=0
        print(a)
        print('anything')
        for i in q:
            print('erer')
            
            if i[1]==namae:
                break
            else:
                er=er+1
        if er==0:
            er=er+1
        a.close()
        a=open('contacts.csv','w')
        qqw[er-1]=''
        qw.writerows(qqw) 
        print('Deleted')
        a.close()



    if next==3 :
        sname=input('Enter the name of contact you want to you see : ')
        a=open('contacts.csv','r')
        q=csv.reader(a)
        for row in q:
            for sname in row:
                print(row)
            break
                


    if next== 4 :
        break
                
