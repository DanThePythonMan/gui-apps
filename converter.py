from guizero import *
def decBin(num):
  num=int(num)
  startnum=bin(num)
  finnum=""
  for char in range(len(startnum)):
    if char == 0 or char == 1: 
        continue
    else:
      finnum = finnum + startnum[char]
  return (finnum)
def hexBin(num):
  #num="0x"+num
  #print(num)
  num=int(num,16)
  #print(num)
  num=bin(num)
  #print(num)
  finnum=""
  for char in range(0, len(num)):
      #print(hexpre[char])
      if char == 0 or char == 1: 
          continue
      else:
        finnum = finnum + num[char]
  return(finnum)
def binHex(num):
  num=str(num)
  num=int(num,2)
  hexpre=hex(num)
  finalhex=""
  for char in range(0, len(hexpre)):
    #print(hexpre[char])
    if char == 0 or char == 1: 
        continue
    else:
      finalhex = finalhex + hexpre[char]
  return(finalhex)
def binDec(num):
  num=int(str(num),2)
  return num
def hexDec(num):
  return(binDec(hexBin(num)))
def decHex(num):
  hexpre=hex(num)
  hexfin=""
  for i in range (len(hexpre)):
    if i ==0 or i ==1:
      continue
    else:
      hexfin+=hexpre[i]
  return hexfin

def outputit():
  out.disable()
  out.show()
  out.clear()
  if inp2.value == "Decimal":
    if inp3.value == "Decimal":
      out.append("The same, idiot")
    elif inp3.value == "Binary":
      out.append(decBin(int(inp1.value)))
    else:
      out.append(decHex(int(inp1.value)))
  elif inp2.value == "Binary":
    if inp3.value == "Binary":
      out.append("The same, idiot")
    elif inp3.value == "Decimal":
      out.append(binDec(inp1.value))
    else:
      out.append(binHex(int(inp1.value)))
  else:
    if inp3.value == "Hexadecimal":
      out.append("The same, idiot")
    elif inp3.value == "Decimal":
      out.append(hexDec(inp1.value))
    else:
      out.append(hexBin(inp1.value))
    
app=App(title="Converter")
text1=Text(app,text="What is the number?")
inp1=TextBox(app)
text2=Text(app,text="What is the base?")
inp2=ButtonGroup(app,options=["Decimal","Binary","Hexadecimal"],horizontal=True)
text3=Text(app,text="What is the desired base?")
inp3 = ButtonGroup(app,options=["Decimal","Binary","Hexadecimal"],horizontal=True)
button=PushButton(app,text="Convert!",command=outputit)
out=Text(app,text="")
out.hide()
app.display()