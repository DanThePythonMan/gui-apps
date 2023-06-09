from guizero import *
import sys
import webbrowser

def open_scp():
    num = formatnum(int(inpbox.value))
    webbrowser.open_new_tab(f"https://scp-wiki.wikidot.com/scp-{num}")

def formatnum(num):
    if num < 10:
        return "00" + str(num)
    elif 10 <= num < 100:
        return "0" + str(num)
    else:
        return str(num)

app = App(title="Scp Opener")

inpbox = TextBox(app, width="50", multiline=False)
pushbut = PushButton(app, width="25", text="Open", command=open_scp)

app.display()