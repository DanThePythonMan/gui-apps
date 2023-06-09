from guizero import *
import os
os.chdir("C:/")
try:
    os.mkdir("codes")
except:
    print("Errors")
finally:
    os.chdir("C:/codes")
def clara():
    files=[]
    for x in os.listdir():
        if x.endswith(".txt"):
            os.system(f"del {x}")

def ok():
    code = in1.value
    code += ".txt"
    ans = in2.value
    os.system(f"echo {ans} >> {code}")
    in1.clear()
    in2.clear()

def check():
    code=in1.value
    in2.clear()
    in1.clear()
    code+=".txt"
    fd = os.open(code, os.O_RDONLY)
    print(fd)


    n = 100
    g=(os.read(fd, n))
    g=str(g)
    g=str(g)
    g=g[2:]
    g=g[:-3]
    in2.append(g)
    os.close(fd)
app=App(title="Sparx")
t1=Text(app,text="What is the bookwork code?")
in1 = TextBox(app,width=50)
t2 = Text(app,text="What is the answer?")
in2 = TextBox(app,width=50)
send=PushButton(app,text="Ok",command=ok)
clar=PushButton(app,text="Clear all answers",command=clara)
check=PushButton(app,text="Check",command=check)
app.display()
