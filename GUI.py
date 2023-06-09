from guizero import *
import hashlib,base64
def strtobyte(str):
    return bytes(str,"utf-8")
def sha256hash(byte):
    return hashlib.sha256(byte).hexdigest()

def encryptit():
    outbox.clear()
    outbox.append(sha256hash(strtobyte(inpbox.value)))

app=App(title="Encryptor")
icon=Picture(app,image="maxresdefault.ico")
inpbox=TextBox(app,width=50,multiline=True,height=5)
convbutton=PushButton(app,text="Hash",command=encryptit)
outbox=TextBox(app,text="",width=50,multiline=True,height=5)
outbox.disable()
app.display()