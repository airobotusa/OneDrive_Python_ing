from tkinter import*
import webbrowser

    
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator =""
    text_Input.set(operator)

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
    
def btnY1Display():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator =""
    print("Y1 is presed")

"""
    print("Enter URL : ")
    url_input = input()
    new = 2
#    url="https://mail.google.com/mail/u/1/#inbox"
    print("You entered url is : ", url)
    url = url_input
"""

def btnOpenurlDisplay1():
    import webbrowser

    new = 2
    url="https://mail.google.com/mail/u/1/#inbox"
    webbrowser.open(url,new=new)

    url="https://www.monster.com/jobs/search/?q=flat-panel-display-software-engineer&brd=1&brd=2&nosal=true&cy=US&geo=Santa%2520Clara%252c%2520CA%2c32.18688%2c1273541%2c580447%2c356&agentId=149516873&stp=JP9&useCloudJobSearch=true&Exp=JP9&MaxExpLevel=PowerSearchRequisitionMatch&MinScore=0&WT.mc_n=PSAAHG09_agentbamlite_p_jp9_0721&acnts=T:1_D:1_A:0_P:0&client=power"
    webbrowser.open(url,new=new)

    url="https://www.orbotech.com/careers/jobs-orbotech"
    webbrowser.open(url,new=new)

    url="https://www.monster.com/profile/profile?intcid=skr_navigation_confirmation_profile"
    webbrowser.open(url,new=new)

    url="http://google.com"
    webbrowser.open(url,new=new)
    print("btnOpenurlDisplay1_1 is pressed")

    url="https://www.bing.com"
    webbrowser.open(url,new=new)
    print("btnOpenurlDisplay1_2 is pressed")

    url="https://www.appliedmaterials.com"
    webbrowser.open(url,new=new)

    url="http://careers.kla-tencor.com/jobs/search?q=software+engineer&location=ca"
    webbrowser.open(url,new=new)

    url="http://www.intevac.com/company/careers/united-states/equipment-santa-clara-ca/software-engineer/"
    webbrowser.open(url,new=new)

    url="https://careers.lamresearch.com/job/Fremont-Global-Product-Support-Engineer-3-CA-94538/442434900/"
    webbrowser.open(url,new=new)

    url="https://www.naver.com"
    webbrowser.open(url,new=new)
    
    url="http://www.intevac.com/company/careers/united-states/equipment-santa-clara-ca/software-engineer/"
    webbrowser.open(url,new=new)
    url="https://highvolsubs-amazon.icims.com/jobs/search?amp%3Bhashed=124496045&mobile=false&width=890&height=1200&bga=true&needsRedirect=false&jan1offset=-300&jun1offset=-240"
    webbrowser.open(url,new=new)
    url="https://appliedmat.taleo.net/careersection/careersection/10020/mysubmissions.ftl?lang=en"
    webbrowser.open(url,new=new)
    url="https://mail.google.com/mail/u/2/#inbox"
    webbrowser.open(url,new=new)
    url="https://plus.google.com/u/2/116001877706224318104"
    webbrowser.open(url,new=new)
    url="https://www.glassdoor.com/Job/santa-clara-program-manager-jobs-SRCH_IL.0,11_IC1147439_KO12,27.htm"
    webbrowser.open(url,new=new)
    url="https://www.linkedin.com/jobs/search/?keywords=intevac&locationId=us%3A0"
    webbrowser.open(url,new=new)
    url="https://www.linkedin.com/learning/me"
    webbrowser.open(url,new=new)
    url="http://www.komanusa.com/irobot/index.html"
    webbrowser.open(url,new=new)
    url="https://cloud.docker.com/swarm/airobotusa/dashboard/onboarding/cloud-registry"
    webbrowser.open(url,new=new)
    url="https://www.w3schools.com/"
    webbrowser.open(url,new=new)
    url="http://www.learnpython.org/en/Modules_and_Packages"
    webbrowser.open(url,new=new)
    url="https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-3-functions-and-packages?ex=9"
    webbrowser.open(url,new=new)
    url="http://lexfridman.com/"
    webbrowser.open(url,new=new)
    url="https://www.youtube.com/watch?v=S5t6K9iwcdw"
    webbrowser.open(url,new=new)
    url="https://www.glassdoor.com/Job/santa-clara-applied-materials-jobs-SRCH_IL.0,11_IC1147439_KE12,29.htm"
    webbrowser.open(url,new=new)
    url="https://www.facebook.com/worldtrips100"
    webbrowser.open(url,new=new)
    url="https://en.savefrom.net/"
    webbrowser.open(url,new=new)
    url="https://translate.google.com/#auto/ko/tuple"
    webbrowser.open(url,new=new)
    url="https://www.udemy.com/home/teaching/"
    webbrowser.open(url,new=new)
    url="http://www.jetbrains.com/"
    webbrowser.open(url,new=new)

# make js html code beautiful
    url="http://jsbeautifier.org/"
    webbrowser.open(url,new=new)

    #Very useful site Youtube for python reading excel files and more.
    url="https://www.youtube.com/channel/UCKOOGcSN291BlQqC5rvLKSw?sub_confirmation=1"
    webbrowser.open(url,new=new)

    print("btnOpenurlDisplay1_3 is pressed")
    
def btnOpenurlDisplay2():
    new = 2
    url="http://www.komanusa.com/irobot"
    webbrowser.open(url,new=new)
    print("btnOpenurlDisplay2 is pressed")
def btnOpenurlDisplay3():
    new = 2
    url="http://www.gmail.com"
    webbrowser.open(url,new=new)
    print("btnOpenurlDisplay3 is pressed")
   
    
cal=Tk()
cal.title("Calculator")
operator=""
text_Input=StringVar()

txtDisplay = Entry(cal,font=('arial', 20,'bold'),textvariable=text_Input,bd=30, insertwidth=5,
                   bg="powder blue", justify='right').grid(columnspan=5)

btn7=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'),
            text="7", bg="powder blue",command=lambda:btnClick(7)).grid(row=1,column=0)

btn8=Button(cal,padx=16, pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="8", bg="powder blue",command=lambda:btnClick(8)).grid(row=1,column=1)

btn9=Button(cal,padx=16, pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="9", bg="powder blue",command=lambda:btnClick(9)).grid(row=1,column=2)

Addition=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'),
            text="+", bg="powder blue",command=lambda:btnClick("+")).grid(row=1,column=3)
# ======================================================================
btn4=Button(cal,padx=16, pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="4", bg="powder blue",command=lambda:btnClick(4)).grid(row=2,column=0)

btn5=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'),
            text="5", bg="powder blue",command=lambda:btnClick(5)).grid(row=2,column=1)

btn6=Button(cal,padx=16, pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="6", bg="powder blue",command=lambda:btnClick(6)).grid(row=2,column=2)

Substraction=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'),
            text="-", bg="powder blue",command=lambda:btnClick("-")).grid(row=2,column=3)
# ======================================================================
btn1=Button(cal,padx=16, pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="1", bg="powder blue",command=lambda:btnClick(1)).grid(row=3,column=0)

btn2=Button(cal,padx=16, pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="2", bg="powder blue",command=lambda:btnClick(2)).grid(row=3,column=1)

btn3=Button(cal,padx=16, pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="3", bg="powder blue",command=lambda:btnClick(3)).grid(row=3,column=2)

Multiply=Button(cal,padx=16, pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="*", bg="powder blue",command=lambda:btnClick("*")).grid(row=3,column=3)
# ======================================================================
btn0=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'),
            text="0", bg="powder blue",command=lambda:btnClick(0)).grid(row=4,column=0)

btnClear=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'),
            text="C", bg="powder blue",command=btnClearDisplay).grid(row=4,column=1)

btnEquals=Button(cal,padx=16, pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="=", bg="powder blue",command=btnEqualsInput).grid(row=4,column=2)

Division=Button(cal,padx=16, pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="/", bg="powder blue",command=lambda:btnClick("/")).grid(row=4,column=3)

# =My own button ==========================================================
btnp=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'),
            text="P", bg="powder blue",command=lambda:btnClick("**")).grid(row=5,column=0)

btnOpen1=Button(cal,padx=16,pady=16, bd=8, fg="black",font=('arial',20,'bold'),
            text="Op1", bg="powder blue",command=btnOpenurlDisplay1).grid(row=5,column=1)

btnOpen2=Button(cal,padx=16, pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="irobot", bg="powder blue",command=btnOpenurlDisplay2).grid(row=5,column=2)

btnOpen3=Button(cal,padx=16, pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="gmail", bg="powder blue",command=btnOpenurlDisplay3).grid(row=5,column=3)

cal.mainloop()
