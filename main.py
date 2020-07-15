#-----MODULES-----#
import tkinter
import tkinter.messagebox as box
import os
import pickle
import tkinter.tix
#-----CLASSES-----#

class frame_title(tkinter.Frame):  #Frame class
    
    def __init__(self,parent):
        frame=tkinter.Frame(parent)
        frame.pack()
                           
class login_frame(frame_title):  #The Login Frame
    
    def __init__(self,parent):
        
        frame_title.__init__(self,parent)
        self.parent = parent
        self.parent.title("Login")
        self.parent.configure(background='#44B3C2')
        self.centerWindow()

        self.frame=tkinter.Frame(parent)
        self.frame.configure(height=600,width=600,bg='#44B3C2')
        self.frame.pack()
        
        self.login_label=tkinter.Label(self.frame, text='LOGIN SCREEN', font=('Lato', 20), fg='white', background='#44B3C2')
        self.login_label.place(x=200,y=120)

        self.user_label=tkinter.Label(self.frame, text="Enter/Choose your\nusername: ", font=("Lato", 18), fg='white', background='grey', width=20)
        self.user_label.place(x=0,y=190)

        self.pass_label=tkinter.Label(self.frame, text="Enter/Choose your\npassword: ", font=("Lato", 18), fg='grey', background='white', width=20)
        self.pass_label.place(x=0,y=250)

        self.entry_user = tkinter.Entry(self.frame, width = 25, borderwidth=0, font=("Calibri Light", 35), background='grey', fg='white')
        self.entry_user.place(x=286, y=190)
        
        self.entry_pass = tkinter.Entry(self.frame, width = 25, borderwidth=0, font=("Calibri Light", 35), background='white', fg='black')
        self.entry_pass.place(x=286, y=250)

        self.login = tkinter.Button(self.frame, text="Log In", font=("Lato", 18), borderwidth=0, command=self.login, background='white', fg='black', height=1, width=10)
        self.login.place(x= 140, y = 339)

        self.signup = tkinter.Button(self.frame, text="Sign Up", font=("Lato", 18), borderwidth=0, command=self.signup, background='white', fg='black', height=1, width=10)
        self.signup.place(x= 300, y =340)


    def centerWindow(self):     # Function to center window
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - 490)/2
        y = (sh - 550)/2
            
        self.parent.geometry("%dx%d+%d+%d" %(600,500,x,y))
        
    def quit(self):
        self.parent.destroy()

    def login(self):
        global a
        self.username=self.entry_user.get().lower()
        self.password=self.entry_pass.get()
        f=open('user.dat','rb')
        try:
            while True:
                a=pickle.load(f)
                self.usernames=a.keys()
                if len(self.usernames)==1:
                    self.entry_pass.delete(0,'end')
        except EOFError:
            pass
        if self.password=='':
            box.showerror('ERROR','Please enter a password before trying to login')
        else:
            if self.username.strip() not in self.usernames:
                box.showerror('ERROR',"That username wasn't found in our directory.\nPlease sign up first")
        if self.username.strip() in self.usernames:
            if self.password==a[self.username.strip()]:
                self.frame.destroy()
                self.parent.destroy()


                self.timeframe=tkinter.Frame(root, bg='white', height=1500, width=1500)
                self.timeframe.pack()
                canvas=tkinter.Canvas(self.timeframe, height=900, width=500, background='white')
                canvas.place(x=110,y=0)

                self.tm=tkinter.Label(self.timeframe, text='TM', font=('Avantagesmall', 10), bg='white')
                self.tm.place(x=290,y=28)
                
                self.ask=tkinter.Label(self.timeframe, text='A S K', font=('Avantagesmall', 60), bg='white')
                self.ask.place(x=190,y=15)
                
                self.shoppers=tkinter.Label(self.timeframe, text='S     H     O     P     P     E     R     S ', font=('Avantagesmall', 8), bg='white')
                self.shoppers.place(x=188,y=110)

                self.tagline=tkinter.Label(self.timeframe, text="Shop", font=('Avantagesmall', 30), bg='white')
                self.tagline.place(x=188,y=240)

                self.tagline2=tkinter.Label(self.timeframe, text="the", font=('Avantagesmall', 20), bg='white')
                self.tagline2.place(x=188,y=290)

                self.tagline3=tkinter.Label(self.timeframe, text="Desire", font=('Avantagesmall', 60), bg='white')
                self.tagline3.place(x=188,y=318)

                self.tagline4=tkinter.Label(self.timeframe, text="Loading...", font=('Avantagesmall', 20), bg='white')
                self.tagline4.place(x=220,y=410)

                self.timeframe.after(3000,lambda:self.timeframe.destroy())            

                
            else:
                box.showerror('ERROR','Incorrect username/password entered.\nPlease enter valid details')
                self.entry_pass.delete(0,'end')

    def signup(self):
        global a
        self.username=self.entry_user.get().lower()
        self.password=self.entry_pass.get()
        f=open('user.dat','rb')
        self.collection=dict()
        try:
            while True:
                self.collection=pickle.load(f)
                self.usernames=self.collection.keys()
        except EOFError:
            pass
        f.close()
        if len(self.password.strip())==0:
                box.showerror('ERROR','Please enter a password') 
        else:
            if self.username.strip() in self.usernames:
                box.showerror('ERROR','The entered username has already been taken.\nPlease enter another one')
                self.entry_pass.delete(0,'end')
                self.entry_user.delete(0,'end')
            else:
                self.collection[self.username.strip()]=self.password
                f=open('user.dat','wb')
                g=open("Allsellersname.dat","ab")
                pickle.dump(self.username.strip(),g)
                g.close()
                pickle.dump(self.collection,f)
                f.close()
                box.showinfo('Success','Your details have been saved.')
                self.userdata='Username: '+self.username.strip()+'\nPassword: '+self.password
                box.showinfo('Your details',self.userdata)
                

#-----MAIN_SECTION-----#

#----MAKING THE USERNAME/PASSWORD FILE-----#

f=open('user.dat','ab').close()                        #Creating a file, if its doesn't exist.
f=open('user.dat','rb')
a=dict()
try:
    while True:
        a=pickle.load(f)
except EOFError:
    pass
if type(a)==dict:
    pass
else:
    a=dict()

f.close()
f=open('user.dat','wb')
pickle.dump(a,f)
f.close()


root = tkinter.tix.Tk( )
b=frame_title(root)
c=login_frame(root)
root.mainloop( )

#-----MAIN_SECTION-----#
