from guizero import *
import base64
app=App(title="Messager")

def go():
   if choie.value == "Encrypt":
      string=encrypt(inpbox.value)
      outbox.clear()
      outbox.append(string)
   else:
      string=decrypt(inpbox.value)
      outbox.clear()
      outbox.append(string)
def encrypt(string):
    for times in range(12):
        string=base64.b64encode(string.encode('utf-8')).decode('utf-8')
    return string
def decrypt(string):
  for i in range(12):
    string = base64.b64decode(string).decode("utf-8")
  return string

inpbox=TextBox(app,height=5,width=50,multiline=True)
choie=ButtonGroup(app,horizontal=True,options=["Encrypt","Decrypt"])
outbox=TextBox(app,height=5,width=50,multiline=True)
gobutton=PushButton(app,text="Go!",command=go)
outbox.disable()
app.display()
