import os
import time
import platform
import binascii
import toru
import sys
class encryptf:
    def encrypt(self,s):
        s=s.encode('utf-8')   
        s = binascii.hexlify(s).decode('utf-8')
        return s 
    def decrypt(self,s):
        s = bytes.fromhex(s).decode()
        return s
class setvip(encryptf):   
     
    def __init__(self, times,password): 
        self.password=password
        name=platform.node()+'-'+str(password)
        name=self.encrypt(name)
        if(os.path.exists(f"{name}lock.vip")==False):
            name=platform.node()+'-'+str(password)
            name=self.encrypt(name)
            f=open(f"{name}lock.vip","w")
            os.path.getmtime(f"{name}lock.vip")
            s= str(times)+"-"+str(time.time())+"-"+str(self.password)
            s=self.encrypt(s)
            # s=s.encode('utf-8')   
            # s = binascii.hexlify(s).decode('utf-8')

            f.write(str(s))
    def help(self):
        print("""
setvip(times,password)
viplock(model,password)
---------------------------------------------------------
times=int The number of times you allow other users to use it.
model=0 Do not output prompt information   .
model=1 output prompt information   .
password=int the password.
--------------------------------------------ysw.2024.6---         
              """)
class viplock(setvip,):
    
    def ifvip(self):
        
        name=platform.node()+'-'+str(self.password)
        name=self.encrypt(name)
        f=open(f"{name}lock.vip")
        
        times=(f.read())
        times = self.decrypt(times)
        names=(times.split("-")[2])
        times=(times.split("-")[1])
                # print(str(os.path.getmtime(f"{platform.node()}lock.vip"))[0:13])
        # print(str(times[0:13]))
        if(str(os.path.getmtime(f"{name}lock.vip"))[0:10] ==str(times[0:10]) and names==str(self.password) ):
            return 1
        else:
            return 0
    def __init__(self,model,password):
        self.password=password
        name=platform.node()+'-'+str(self.password)
        name=self.encrypt(name)
        self.y=toru.model(model)
        
        if(os.path.exists(f"{name}lock.vip")):
            f=open(f"{name}lock.vip")
            s=(f.read())
            times=self.decrypt(s)
            times=int(times.split("-")[0])
            if(self.ifvip()==1 and times>=1) :
                times=times-1
                s= str(times)+"-"+str(time.time())+"-"+str(self.password)
                s=self.encrypt(s)
                # s=s.encode('utf-8') 
                # s = binascii.hexlify(s).decode('utf-8')
                f=open(f"{name}lock.vip","w")
                os.path.getmtime(f"{name}lock.vip")  

                f.write(str(s))
            elif(self.ifvip()==0):
                self.y.print("Dont chenge lock.vip!")
                sys.exit()
        else:
            self.y.print(" no vip filex")
            sys.exit()
        if(times<=0):
            self.y.print("no vip times")
            sys.exit()

    

