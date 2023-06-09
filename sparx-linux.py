from guizero import *
import os
os.chdir("/home")
print(os.getcwd())
print("1")
try:
  os.mkdir("/home/code")
  print("2")
except:
  print("lols")
finally:
  os.chdir("/home/code")
  print("3")
def clara():
  no.clear()
  
  for x in os.listdir():
      if x.endswith(".txt"):
          os.system(f"rm {x}")
  no.append("Answers Cleared")

def ok():
  no.clear()
  code = in1.value
  code += ".txt"
  ans = in2.value
  os.system(f"echo {ans} >> {code}")
  in1.clear()
  in2.clear()

def check():
  no.clear()
  code=in1.value
  code+=".txt"
  try:
    fd = os.open(code, os.O_RDONLY)
  #print(fd)
  
  
    n = 100
    g=(os.read(fd, n))
    g=str(g)
    print("g is" +g)
    print(g)
    g=str(g)
    print(g)
    g=g[2:]
    g=g[:-3]
    print(g)
    in2.clear()
    in1.clear()
    no.append(g)
  except:
    g="Code Not Found"
    in2.clear()
    in1.clear()
    no.append(g)
app=App(title="Sparx")
t1=Text(app,text="What is the bookwork code?")
in1 = TextBox(app,width=50)
t2 = Text(app,text="What is the answer?")
in2 = TextBox(app,width=50)
send=PushButton(app,text="Ok",command=ok)
clar=PushButton(app,text="Clear all answers",command=clara)
check=PushButton(app,text="Check",command=check)
no=Text(app,size=12)
app.display()
