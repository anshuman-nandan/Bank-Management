import time
from getpass import getpass
import os
from datetime import date
date=date.today().strftime("%B %d; %Y")
def tim():
    return time.strftime("%H:%M:%S")
#BANK MANAGEMENT PATTERN
def pattern():
    for i in range(1,2):
        for j in range(61):
            print('*',end=' ')
        print()
    for i in range(1,2):
        print(' ',end=' ')
        print()
    for i in range(1,8):
        for j in range(1,16):
            print(' ',end=' ')
        for j in range(1,8):#B
            if i==1 or i==7 or j==2 or j==7 or i==4 and j!=1:
                print('$',end=' ')
            else:
                print(' ',end=' ')
        for j in range(1,2):
            print(' ',end=' ')
        for j in range(1,8):#A
            if i==1 or j==1 or j==7 or i==4:
                print('$',end=' ')
            else:
                print(' ',end=' ')
        for j in range(1,2):
            print(' ',end=' ')
        for j in range(1,8):#N
            if j==1 or j==7 or i==j:
                print('$',end=' ')
            else:
                print(' ',end=' ')
        for j in range(1,2):
            print(' ',end=' ')
        for j in range(1,8):#K
            if j==1 or i==8-j-3 or i==j+3:
                print('$',end=' ')
            else:
                print(' ',end=' ')      
        print()
    for i in range(1,2):
        print(' ',end=' ')
        print()
    for i in range(1,6):#MANAGEMENT
        for j in range(1,2):
            print(' ',end=' ')
        for j in range(1,6):#M
            if j==1 or j==5 or i==j and j<3 or j==6-i and j>2:
                print('$',end=' ')
            else:
                print(' ',end=' ')
        for j in range(1,2):
            print(' ',end=' ')
        for j in range(1,6):#A
            if i==1 or j==1 or j==5 or i==3:
                print('$',end=' ')
            else:
                print(' ',end=' ')
        for j in range(1,2):
            print(' ',end=' ')
        for j in range(1,6):#N
            if j==1 or j==5 or i==j:
                print('$',end=' ')
            else:
                print(' ',end=' ')
        for j in range(1,2):
            print(' ',end=' ')
        for j in range(1,6):#A
            if i==1 or j==1 or j==5 or i==3:
                print('$',end=' ')
            else:
                print(' ',end=' ')
        for j in range(1,2):
            print(' ',end=' ')
        for j in range(1,6):#G
            if i==1 or j==1 or i==5 or j==5 and i>3 or j>3 and i==3:
                print('$',end=' ')
            else:
                print(' ',end=' ')    
        for j in range(1,2):
            print(' ',end=' ')
        for j in range(1,6):#E
            if i==1 or j==1 or i==5 or i==3:
                print('$',end=' ')
            else:
                print(' ',end=' ')
        for j in range(1,2):
            print(' ',end=' ')
        for j in range(1,6):#M
            if j==1 or j==5 or i==j and j<3 or j==6-i and j>2:
                print('$',end=' ')
            else:
                print(' ',end=' ')
        for j in range(1,2):
            print(' ',end=' ')
        for j in range(1,6):#E
            if i==1 or j==1 or i==5 or i==3:
                print('$',end=' ')
            else:
                print(' ',end=' ')
        for j in range(1,2):
            print(' ',end=' ')
        for j in range(1,6):#N
            if j==1 or j==5 or i==j:
                print('$',end=' ')
            else:
                print(' ',end=' ')
        for j in range(1,2):
            print(' ',end=' ')
        for j in range(1,6):#T
            if i==1 or j==3:
                print('$',end=' ')
            else:
                print(' ',end=' ')
        for j in range(1,2):
            print(' ',end=' ')
        print()
    for i in range(1,3):
        print(' ',end=' ')
        print()
    for i in range(1,2):
        for j in range(61):
            print('*',end=' ')
        print()
#############################################################
#USER LOGIN
#input usernme and acc.no. USER
def user_login(r=0):
    for i in range(5):
        username=input('enter user\'s name::')
        if len(username)>4:
            accno=error('enter last 4 digits of account number::',4)
            if accno=='_':
                break
            else:
                if r==1:
                    return uname_attempt(username,accno,1)
                else:
                    uname_attempt(username,accno)
                break
        else:
            print('INVALID INPUT\n')
#check if exist USER
def uname_attempt(username,accno,r=0):
    f=open('accounts.txt','r')
    check=f.readline()
    while check:
        a,b,c,d=check.split(',')
        if a==username and b[-4:]==accno:
            if r==0:
                f.close()
                pass_attempt(username,c,d.rstrip())
            else:
                return d
            f.close()
            break
        else:
            check=f.readline()
    else:
        print(username,'with account number','********'+accno,'NOT FOUND!!\n')
        if r==0:
            user_login()
        else:
            user_login(1)
#password input USER
def pass_attempt(username,password,d,r=0):
    z=5
    for i in range(4):
      _pass=getpass('ENTER PASSWORD::')
      if password==_pass:
          if r==0:
            user_account(d)
          else:
            return True
          break
      else:
          print('ACCESS DENIED\nWRONG PASSWORD!!!\n')
          z-=1
          print(z,'attempts left')
    else:
        print('wait for 10 seconds\nDON\'T PRESS ANY KEY OR YOUR ACCOUNT MIGHT GET BLOCKED!!!\n')
        time.sleep(10)
        _pass=getpass('ENTER PASSWORD::')
        if password==_pass:
            if r==0:
                user_account(d)
            else:
                return True
        else:
            print ('WRONG PASSWORD!!!\nACCOUNT BLOCKED\nCONTACT BANK EMPLOYEE\n')
            acc_status(d,'blocked')
            log_act('blocked',d)
            if r==1:
                return False
#USER FUNCTIONS
def user_account(accdetail):
    f=open(accdetail,'r')
    status=f.readline()
    if status.rstrip()=='blocked':
        print('YOUR ACCOUNT HAS BEEN BLOCKED\nCONTACT BANK EMPLOYEE')
        f.close()
    else:
        print('WELCOME',accdetail[:-8],'\n')
        print('CURRENT ACCOUNT BALANCE IS :',f.readline())
        f.close()
        log_act('logged in',accdetail)
        while True:
            f=open(accdetail,'r')
            f.seek(0)
            f.readline()
            cur=int(f.readline())
            print()
            choice=input('Press\n1 to TRANSFER AMOUNT\n2 to ACCESS TRANSACTION HISTORY\n3 to SEE LOGIN ACTIVITY\n4 to SEE USER INFORMATION\n5 to CHANGE PASSWORD\n6 to CLEAR TRANSACTION HISTORY\n7 to CLEAR LOGIN ACTIVITY\n0 to SIGN OUT\n::')
            print()
            if choice=='1':
                print('RECEIVER\'S')
                rec=user_login(1)
                if rec is not None:
                    rec=rec.rstrip()
                    if accdetail==rec:
                        print('Can\'t perform this action!!')
                    else:
                        t=in_amt(cur)
                        if t!=0:
                            f.close()
                            transfer(accdetail,t,'-',rec)
                            transfer(rec,t,'+',accdetail)
                            f=open(accdetail,'r')
                            f.readline()
                            print('BALANCELEFT::',f.readline())
                            f.close()
                else:
                    print('\ncan not perform this action right now\nplease try again later!!\n')
            elif choice=='2':
                f.readline()
                for i in f.readline().split(','):
                    if i!='':
                        print(i.rstrip())
            elif choice=='3':
                f.readline()
                f.readline()
                for i in f.readline().split(','):
                    if i!='':
                        print(i.rstrip())
            elif choice=='4':
                for i in f.readline().rstrip().split(','):
                    print(i)
            elif choice=='5':
                c=change_pass(accdetail)
                if c==1:
                    print('PASSWORD CHANGED SUCCESSFULLY')
                else:
                    break
            elif choice=='6':
                f.close()
                clear_this(accdetail)
                f=open(accdetail,'r')
            elif choice=='7':
                f.close()
                clear_lact(accdetail)
                f=open(accdetail,'r')   
            elif choice=='0':
                print('LOGGED OUT\nTHANK YOU FOR VISITING US')
                f.close()
                break
            else:
                print('invalid input')
            
#CHECKS LENGTH AND INTEGER TYPE CASTING
def error(arg,l,r=5):
    if r==0:
        return '_'
    else:
        temp=input(arg)
        if len(temp)!=l:
            print('INVALID INPUT')
            return error(arg,l,r-1)
        else:
            try:
                a=int(temp)
                if a>=0:
                    return temp
                else:
                    print('INVALID INPUT')
                    return error(arg,l,r-1)
            except:
                print('INVALID INPUT')
                return error(arg,l,r-1)
   
#CHANGING ACCOUNT STATUS
def acc_status(file,status):
    f=open('anonymous.txt','w')
    g=open(file,'r')
    f.write(status+'\n')
    g.readline()
    f.writelines(g.readlines())
    f.close()
    os.remove(file)
    os.rename('anonymous.txt',file)
   
#BALANCE TRANSACTION HISTORY
def transfer(user,amount,oper,transhis):
    f=open(user,'r')
    f1=open('temp.txt','w')
    bt=open('banktransactions.txt','a')
    f1.write(f.readline())
    z=int(f.readline().rstrip())
    d=f.readline()
    l=f.readline().rstrip().split(',')
    if oper=='-':
        z-=amount
        l.insert(1,'Sent '+str(amount)+' to '+transhis[:-4]+' on '+date+' at '+tim())
        a=user[:-4]+' Sent '+str(amount)+' to '+transhis[:-4]+' on '+date+' at '+tim()+'\n'
        bt.write(a)
    elif oper=='+':
        z+=amount
        l.insert(1,'Recieved '+str(amount)+' from '+transhis[:-4]+' on '+date+' at '+tim())    
    elif oper=='++':
        z+=amount
        l.insert(1,str(amount)+' deposited on '+date+' at '+tim())
        a=str(amount)+' deposited on '+date+' at '+tim()+' in '+user[:-4]+'\n'
        bt.write(a)
    elif oper=='--':
        z-=amount
        l.insert(1,str(amount)+' retrieved on '+date+' at '+tim())
        a=str(amount)+' retrieved on '+date+' at '+tim()+' in '+user[:-4]+'\n'
        bt.write(a)
    f1.write(str(z)+'\n')
    f1.write(d)
    for i in l:
        i+=','
        f1.write(i)
    f1.write('\n')
    f1.write(f.readline())
    f.close()
    f1.close()
    bt.close()
    os.remove(user)
    os.rename('temp.txt',user)
#LOGIN ACTIVITY
def log_act(act,user):
    f=open(user,'r')
    g=open('temp.txt','w')
    for i in range(4):
        g.write(f.readline())
    l=f.readline().split(',')
    l.insert(1,act+' on '+date+' at '+tim())
    for i in l:
        g.write(i+',')
    f.close()
    g.close()
    os.remove(user)
    os.rename('temp.txt',user)

#AMOUNT RETRIEVAL ALLOWANCE
def in_amt(lim):
    print('\nAVAILABLLE BALANCE::',lim,'\n')
    try:
        t=int(input('enter amount::'))
        if t<=int(lim):
            return t
        else:
            print('NOT ALLOWED')
            return in_amt(lim)
    except:
        print('INVALID INPUT')
        return in_amt(lim)
           
                                     
#CLEAR TRANSACTION HISTORY
def clear_this(user):
        f=open(user)
        g=open('temp.txt','w')
        for i in range(3):
            g.write(f.readline())
        g.write('TRANSACTION HISTORY::\n')
        f.readline()
        g.write(f.readline())
        g.close()
        f.close()
        os.remove(user)
        os.rename('temp.txt',user)
        print('TRANSACTION HISTORY CLEARED')
       
#CLEAR LOGIN ACTIVITY
def clear_lact(user):
        f=open(user)
        g=open('temp.txt','w')
        for i in range(4):
            g.write(f.readline())
        g.write('LOGIN ACTIVITY::\n')
        g.close()
        f.close()
        os.remove(user)
        os.rename('temp.txt',user)
        print('LOGIN ACTIVITY CLEARED')
       
#CHANGE PASSWORD
def change_pass(user):
    f=open('accounts.txt','r')
    g=open('passtemp.txt','w')
    check=f.readline()
    while check:
           a,b,c,d=check.split(',')
           if d.rstrip()==user:
            print('ENTER OLD PASSWORD BELOW')
            if pass_attempt('no#use',c,user,1) is True:
                print('password should be atleast 5 characters long')
                c=input('ENTER NEW PASSWORD::')
                while len(c)<5:
                    c=input('ENTER NEW PASSWORD::')
                e=1
            else:
                e=0
            g.write(a+','+str(b)+','+c+','+d)
           else:
            g.write(check)
           check=f.readline()
    f.close()
    g.close()
    os.remove('accounts.txt')
    os.rename('passtemp.txt','accounts.txt')
    return e
##############################################################
            
#CREATE USER ACCOUNT
def cracc():
    username=input('enter username(atleast 5 characters)\n::')
    password=input('enter password(atleast 5 characters)\n::')
    while (len(username)<=4 or len(password)<=4):
            print('username and password should be of atlest 5 characters')
            username=input('enter username::')
            password=input('enter password::')
    with open('accounts.txt','r+') as f:
                l=f.readlines()[-1].split(',')[1]
                accno=str(int(l)+1)
                userfile=username+accno[-4:]+'.txt'
                f.write(username+','+accno+','+password+','+userfile+'\n')
    with open(userfile,'w') as g:
                name=input('enter name::')
                print('enter date of birth::')
                date=error('date::',2,100000)
                month=error('month::',2,100000)
                year=error('year::',4,100000)
                c=input('care of::')
                adn=error('enter adhar no.::',12,10000)
                adr=input('enter address::')
                phone=error('enter mobile number(without code)::',10)
                accdetail='name:'+name+','+'dob:'+date+'\\'+month+'\\'+year+','+'c/o:'+c+','+'aadhar no.:'+str(adn)+','+'account no.:'+accno+','+'address:'+adr+','+'mobile no.:'+str(phone)
                g.write('unblocked'+'\n'+'10000'+'\n'+accdetail+'\n'+'TRANSACTION HISTORY::,'+'\n'+'LOGIN ACTIVITY::,')
                print('\nACCOUNT CREATED::\nusername::'+username+'\npassword::'+password+'\naccount number::'+accno)
#SHOW DETAILS OF PARTICULAR CUSTOMER    
def show_det():
            rec=user_login(1)
            if rec is not None:
                        rec=rec.rstrip()
                        f=open(rec)
                        cur=f.readline()
                        cur=f.readline()
                        cur=f.readline()
                        l=cur.rstrip().split(',')
                        for i in l:
                            print(i)                        
                        f.close()
                        return rec
            else:
                print('\ncan not perform this action right now\nplease try again later!!\n')
                return 0    
#EMPLOYEE LOGIN
def emp_login():
        username=input('enter username::')
        password=getpass('enter password::')
        with open('employees.txt','r') as f:
            while True:
                try:
                    a,b=f.readline().rstrip().split(',')
                    if a==username and b==password:
                        emp_loggedin()
                        break
                except:
                    print('\nINVALID USERNAME OR PASSWORD\n')
                    break
                   
#RETRIEVE MONEY FROM ACCOUNT TO EMPLOYEE
def ret_mon():
                rec=user_login(1)
                if rec is not None:
                            rec=rec.rstrip()
                            f=open(rec)
                            cur=f.readline()
                            cur=f.readline()
                            f.close()
                            t=in_amt(cur)
                            if t!=0:
                                transfer(rec,t,'--','transhis')
                                f=open(rec,'r')
                                f.readline()
                                print('BALANCE LEFT::',f.readline())
                                f.close()
                                print('SUCCESSFULLY RETRIEVED!!')
                else:
                    print('\ncan not perform this action right now\nplease try again later!!\n')
#MONEY DEPOSIT BY EMPLOYEE
def dep_money():
            try:
                ah=user_login(1).rstrip()
                for i in range(2):
                    try:
                        a=input('enter amount::')
                        amount=abs(int(a))
                        transfer(ah,amount,'++','transhis')
                        print('SUCCESSFULLY DEPOSITED!!')
                        break
                    except:
                        print('INVALID INPUT')
            except:
                print('\ncan not perform this action right now\nplease try again later!!\n')
#UPDATE DETAILS OF ACCOUNT HOLDER
def upd_det(user):
    print('press enter on details that is not to be changed or enter new details::')
    with open(user) as f:
        with open('temp.txt','w') as g:
                g.write(f.readline())
                g.write(f.readline())
                lst=f.readline().rstrip().split(',')
                news=''
                for i in lst:
                    if i[:3]=='acc' or i[:3]=='aad' or i[:3]=='dob' or i[:3]=='name':
                        news+=(i+',')
                    else:
                        print(i,end=':::new:::')
                        a=input()
                        if a.rstrip()=='':
                            news+=(i+',')
                        else:
                            j=i.split(':')
                            k=j[0]+':'+a+','
                            news+=k
                g.write(news.rstrip(',')+'\n')
                g.writelines(f.readlines())                
    os.remove(user)
    os.rename('temp.txt',user)            
    print('DETAILS UPDATED SUCCESFULLY')
#CHECKS SAME AADHAR NUMBER
def same_accno():
    with open('accounts.txt') as f:
        d={'account':'aadhar'}
        c=0
        h=[]
        df={}
        while True:
            try:
                a=f.readline().rstrip().split(',')[3]
                with open(a) as g:
                    a=a[:-4]
                    b=g.readlines()
                    b=b[2].rstrip().split(',')[3][-12:]
                    if b in d.values():
                        df.update({a:b})
                        h.append(a)
                        e=list(d.keys())[c]
                        if e not in h:
                            df.update({e:d[e]})
                d.update({a:b})
                c+=1
            except:
                break
    chl=0
    while df:
        chl=1
        dfe=[]
        b=list(df.keys())
        a=b[0]
        c=df[a]
        for i in b:
            if c==df[i]:
                dfe+=[i]
        for i in b:
            if c==df[i]:
                df.pop(i)
        print('users having aadhar number::',c)
        for i in dfe:
            print(i)
        print()
    if chl==0:
        print('NO USERS HAVE SAME AADHAR NUMBER')
#EMPLOYEE FUNCTIONS
def emp_loggedin():
    while True:
        print('\nPRESS::\n1 to CREATE an ACCOUNT\n2 for ACCOUNT DETAILS\n3 to DEPOSIT MONEY\n4 to RETRIEVE MONEY\n5 to UNBLOCK an ACCOUNT\n6 to CHECK if any USERS have same ACCOUNT NUMBER\n0 to MOVE BACK\n')
        c=input('::')
        if c=='1':
            cracc()
        elif c=='2':
            a=show_det()
            if a!=0:
                b=input('PRESS 0 to exit or 1 to update details\n::')
                while True:
                    if b=='0':
                        break
                    elif b=='1':
                        upd_det(a)
                    b=input('PRESS 0 to exit or 1 to update details\n::')
        elif c=='3':
            dep_money()
        elif c=='4':
            ret_mon()
        elif c=='5':
            try:
                ah=user_login(1).rstrip()
                acc_status(ah,'unblock')
                print('\nACCOUNT HAS BEEN UNBLOCLKED SUCCESSFULLY\n')
            except:
                print('\ncan not perform this action right now\nplease try again later!!\n')
        elif c=='6':
            same_accno()
        elif c=='0':
            break
            
#############################################################
#MANAGER LOGIN
def man_login():
        username=input('enter username::')
        password=getpass('enter password::')
        if username=='manager' and password=='pass':
            man_choice()
        else:
            print('INCORRECT USERNAME OR PASSSWORD')
            
#MANAGER FUNCTIONS
def man_choice():
    while True:
        print('Press\n1 to access bank transactions\n2 to create new employee account\n3 to access details of customer\'s accounts\n4 to access employee functions\n5 to access details of employees\' accounts\n0 to signout')
        mn=input('::')
        if mn=='1':
            with open('banktransactions.txt','r') as btl:
                bt=btl.readlines()
                for i in range(-1,-(len(bt)+1),-1):
                    print(bt[i])
        elif mn=='2':
            create_emp()
        elif mn=='3':
            with open('accounts.txt','r') as f:
                sno=1
                while True:
                    try:
                        a=f.readline().rstrip().split(',')
                        print('\n   ',sno,'.'," Account Holder's name:: ",a[0],'\n\t',"Password:: ",a[2],'\n\t',"Account number:: ",a[1])
                        sno+=1
                    except:
                        break
        elif mn=='4':
            emp_loggedin()
        elif mn=='5':
            with open('employees.txt','r') as f:
                sno=1
                while True:
                    try:
                        a=f.readline().rstrip().split(',')
                        print('\n   ',sno,'.'," Employee's name:: ",a[0],'\n\t',"Password:: ",a[1])
                        sno+=1
                    except:
                        break
        elif mn=='0':
            break
        
                                        
#CREATE EMPLOYEE ACCOUNT
def create_emp():
    with open('employees.txt','a') as empf:
        username=input('Enter New Username(atleast 5 characters)::')
        password=input('Enter New Password(atleast 5 characters)::')
        while len(username)<=4 or len(password)<=4:
            print('username and password should be of atlest 5 characters')
            username=input('Enter New Username::')
            password=input('Enter New Password::')
        a=username+','+password+'\n'
        empf.write(a)
        print('ACCOUNT CREATED')   
##############################################################
#MAIN PROGRAM
pattern()
try:
    f=open('accounts.txt')
    f.close()
except:
    with open('accounts.txt','a') as f:
        f.write('@#$%&,100000000000,&%$#@,@#$%&0000.txt'+'\n')
while True:
    print('\n\n','—'*60,'\n\n')
    c=input('PRESS::\n1 for MANAGER\n2 for EMPLOYEE\n3 for ACCOUNT HOLDER\n::')
    if c=='1':
        man_login()        
    elif c=='2':
        emp_login()
    elif c=='3':    
        user_login()
   