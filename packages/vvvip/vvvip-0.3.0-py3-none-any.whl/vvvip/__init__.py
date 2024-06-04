import os
import time
import platform
import binascii
import toru
import sys
class setvip:     
    def __init__(self, times): 
        
        if(os.path.exists(f"{platform.node()}lock.vip")==False):
            f=open(f"{platform.node()}lock.vip","w")
            os.path.getmtime(f"{platform.node()}lock.vip")
            s= str(times)+"-"+str(time.time()) 
            s=s.encode('utf-8')   
            s = binascii.hexlify(s).decode('utf-8')

            f.write(str(s))
    def help():
        print("""
setvip(x)
viplock(y)
---------------------------------------------------------
x=n The number of times you allow other users to use it
y=0 Do not output prompt information   
y=1 output prompt information   
--------------------------------------------ysw.2024.6---         
              """)
class viplock:
    def ifvip(self):
        f=open(f"{platform.node()}lock.vip")
        
        times=(f.read())
        times = bytes.fromhex(times).decode()
        times=(times.split("-")[1])
        # print(str(os.path.getmtime(f"{platform.node()}lock.vip"))[0:13])
        # print(str(times[0:13]))
        if(str(os.path.getmtime(f"{platform.node()}lock.vip"))[0:13] ==str(times[0:13]) ):
            return 1
        else:
            return 0
    def __init__(self,model):
        self.y=toru.model(model)
        if(os.path.exists(f"{platform.node()}lock.vip")):
            f=open(f"{platform.node()}lock.vip")
            times=(f.read())
            times = bytes.fromhex(times).decode()
            times=int(times.split("-")[0])
            if(self.ifvip()==1 and times>=1) :
                times=times-1
                s= str(times)+"-"+str(time.time()) 
                s=s.encode('utf-8') 
                s = binascii.hexlify(s).decode('utf-8')
                f=open(f"{platform.node()}lock.vip","w")
                os.path.getmtime(f"{platform.node()}lock.vip")  
  
                f.write(str(s))
            elif(self.ifvip()==0):
                self.y.print("Dont chenge lock.vip!")
                sys.exit()
        else:
            self.y.print("vip filex")
            sys.exit()
        if(times<=0):
            self.y.print("no vip times")
            sys.exit()

    

