from guizero import *
def login():
    user=in1.value
    passw=in2.value
    if len(passw) <8 or len(passw) >12:
        no.visible = True
        no.clear()
        no.append("The password must be greater than 8 but less than 12")
    else:
        no.visible = True
        no.clear()
        no.append(f"Thanks for logging in,{user}")

app = App(title = "Login Terminal")
t1=Text(app,text="What is your username?")
in1=TextBox(app)
t2=Text(app,text="What is your password?")
in2=TextBox(app,hide_text=True)
no=Text(app,visible=False,text="")
button1=PushButton(app,text="Login",command=login)

app.display()