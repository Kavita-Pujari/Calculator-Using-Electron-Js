import eel
from os import path
import bottle_websocket

eel.init(path.dirname(__file__) + "/web")

@eel.expose
def total(Value1, Value2,Id):
    print(Value1)
    print(Value2)
   

    if(str(Id)=="1"):
        Ans1=int(Value1)+int(Value2)

    elif(str(Id)=="2"):
        Ans1=int(Value1)-int(Value2)

    elif(str(Id)=="3"):
        Ans1=int(Value1)*int(Value2)    
    elif(str(Id)=="4"):
        Ans1=int(Value1)/int(Value2)
   
    
    
    
    #total=int(log_email)+int(log_password)
    #return total
        
    
    eel.error_alert("please enter the integer value")


eel.start('gk.html', size=(2000, 2000),block=False)

#eel.my_javascript_function('main.html', ' test')

while True:
    eel.sleep(10)
