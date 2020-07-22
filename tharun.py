import re
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
global count
count = [0,0]
class Front:
    def __init__(self, master):
        self.master = master
        self.login()
    def login(self):
        global i
        i = 0
        self.master.geometry('640x360+250+150')
        self.master.title('Postinter Bank')

        self.logo = PhotoImage(file = 'python_logo.gif').subsample(3,3)

        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()

        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0,rowspan =3)
        ttk.Label(self.frame_header, text = 'Welcome to postinter Bank!').grid(row = 0, column = 1,columnspan = 2)


        self.frame_body = ttk.Frame(self.master)
        self.frame_body.pack()
        self.frame_body.config(relief = RIDGE, padding = (30,15))
        ttk.Label(self.frame_body, text = 'UserName:').grid(row = 0, column = 1, padx = 10,pady = 10, sticky = 'sw')
        ttk.Label(self.frame_body, text = 'Password:').grid(row = 1, column = 1, padx = 10, pady = 10, sticky = 'sw')
        self.user = ttk.Entry(self.frame_body,width = 24, font = ('Arial', 10))
        self.psd = ttk.Entry(self.frame_body, width = 24, font = ('Arial', 10))
        self.user.grid(row = 0,column = 2)
        self.psd.grid(row = 1,column = 2)
        self.user.insert(0,'Enter your name')
        self.psd.insert(0,'Enter your pass')
        self.user.config(foreground = 'grey')
        self.psd.config(foreground = 'grey')
        self.user.bind('<ButtonPress>', self.mouse_press1)
        self.psd.bind('<ButtonPress>', self.mouse_press2)

        def temp_action():
            self.log_name = self.user.get()
            messagebox.showinfo(title = 'Welcome to Postinter', message = 'Welcome {}'.format(self.log_name))
            self.home()
        ttk.Button(self.frame_body, text = "Submit",command = temp_action).grid(row = 2, column = 0,padx=10, pady=10,columnspan = 2)
        ttk.Button(self.frame_body, text = "Create account",command = self.create).grid(row = 2, padx=10, pady=10, column = 2, stick = 'se')
    def menu_ini(self):

        self.frame_menu = ttk.Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(relief = RIDGE)
        self.homebut = ttk.Button(self.frame_menu, text = "Home",command = self.home)
        self.homebut.grid(row = 0, column = 0)
        self.probut = ttk.Button(self.frame_menu, text = "Profile",command = self.profile)
        self.probut.grid(row = 0, column = 1)
        self.fribut = ttk.Button(self.frame_menu, text = "Friends",command = self.friends)
        self.fribut.grid(row = 0, column = 2)
        self.tranbut = ttk.Button(self.frame_menu, text = "Transfer amount",command = self.transfer)
        self.tranbut.grid(row = 0, column = 3)
        self.seabut = ttk.Button(self.frame_menu, text = "Search",command = self.search)
        self.seabut.grid(row = 0, column = 4)
    def home(self):
        global i
        if i == 0:
            self.menu_ini()
            i += 1
        self.master.geometry('640x390+250+150')
        self.frame_body.pack_forget()

        self.frame_body = ttk.Frame(self.master)
        self.frame_body.pack()
        self.frame_body.config(relief = RIDGE, padding = (30,15))
        ttk.Button(self.frame_body, text = "Check Account Balance",command = self.check_balance).grid(row = 1,padx = 30, pady=10, column = 1)
        ttk.Button(self.frame_body, text = "View Recent Transactions",command = self.transaction_history).grid(row = 2,padx = 30, pady=10, column = 1)
        ttk.Label(self.frame_body,wraplength = 300,text = "Welcome to postinter bank. This is a simple, fast and elegant way of transferring money to anyone swiftly. Explore for more features.").grid(row = 0, padx=20, pady=50, column = 1)

    def create(self):

        global i
        i = 0
        self.master.geometry('680x410+250+150')
        self.frame_body.pack_forget()
        self.frame_body = ttk.Frame(self.master)
        self.frame_body.pack()
        self.frame_body.config(relief = RIDGE, padding = (30,15))
        ttk.Label(self.frame_body, text = "Name: ").grid(row = 0, padx=5, pady=5, column = 0)
        ttk.Label(self.frame_body, text = "Email: ").grid(row = 1, padx=5, pady=5, column = 0)
        ttk.Label(self.frame_body, text = "DOB: ").grid(row = 2, padx=5, pady=5, column = 0)
        ttk.Label(self.frame_body, text = "Mobile: ").grid(row = 3, padx=5, pady=5, column = 0)
        ttk.Label(self.frame_body, text = "Address: ").grid(row = 4, padx=5, pady=5, column = 0)
        ttk.Label(self.frame_body, text = "Enter a password: ").grid(row = 5, padx=5, pady=5, column = 0)
        ttk.Label(self.frame_body, text = "Re-enter password: ").grid(row = 6, padx=5, pady=5, column = 0)
        ttk.Label(self.frame_body, text = "Bank: ").grid(row = 0, padx=5, pady=5, column = 2)
        ttk.Label(self.frame_body, text = "Account Number: ").grid(row = 1, padx=5, pady=5, column = 2)
        ttk.Label(self.frame_body, text = "Enter a UPI key: ").grid(row = 2, padx=5, pady=5, column = 2)
        ttk.Label(self.frame_body, text = "Re-enter UPI key: ").grid(row = 3, padx=5, pady=5, column = 2)

        self.name = ttk.Entry(self.frame_body, text = "Name: ")
        self.name.grid(row = 0, padx=5, pady=5, column = 1)
        self.email = ttk.Entry(self.frame_body, text = "Email: ")
        self.email.grid(row = 1, padx=5, pady=5, column = 1)
        self.dob = DateEntry(self.frame_body,width = 18, background='lightblue',foreground='black', borderwidth=2,year=2000, month=1, day=1, date_pattern='dd/MM/yyyy')
        # self.dob = ttk.Entry(self.frame_body, text = "DOB: ")
        self.dob.grid(row = 2, padx=5, pady=5, column = 1)

        self.phone = ttk.Entry(self.frame_body, text = "Phone: ")
        self.phone.grid(row = 3, padx=5, pady=5, column = 1)
        self.address = ttk.Entry(self.frame_body, text = "Address: ")
        self.address.grid(row = 4, padx=5, pady=5, column = 1)
        self.pswd = ttk.Entry(self.frame_body, text = "Enter a password: ")
        self.pswd.grid(row = 5, padx=5, pady=5, column = 1)
        self.pswd.config(show = '*')
        self.repswd = ttk.Entry(self.frame_body, text = "Re-enter password: ")
        self.repswd.grid(row = 6, padx=5, pady=5, column = 1)
        self.repswd.config(show = '*')
        self.bank = ttk.Combobox(self.frame_body, text = "Bank: ", width = 18)
        self.bank.grid(row = 0, padx=5, pady=5, column = 3)
        self.bank.set('Select your bank')
        self.bankoptions = ['State Bank Of India','ICICI','Indian Overseas Bank','Canara Bank']
        self.bank.config(values = self.bankoptions)
        self.acc = ttk.Entry(self.frame_body, text = "Account Number: ")
        self.acc.grid(row = 1, padx=5, pady=5, column = 3)
        self.upi = ttk.Entry(self.frame_body, text = "Enter a UPI key: ")
        self.upi.grid(row = 2, padx=5, pady=5, column = 3)
        self.upi.config(show = '*')
        self.reupi = ttk.Entry(self.frame_body, text = "Re-enter UPI key: ")
        self.reupi.grid(row = 3, padx=5, pady=5, column = 3)
        self.reupi.config(show = '*')

        ttk.Button(self.frame_body, text = 'Create',command = self.temp_action2).grid(row = 7, padx=5, pady=5, column = 1, sticky = 'ne')
        ttk.Button(self.frame_body, text = 'Cancel',command = self.edit_cancel_create).grid(row = 7, padx=5, pady=5, column = 2, sticky = 'nw')
        ttk.Label(self.frame_body, text = 'Already have an account?').grid(row = 8, padx=5, pady=5, column = 1, columnspan = 2)
        ttk.Button(self.frame_body, text = 'Sign-in',command = self.login).grid(row = 9, padx=5, pady=5, column = 1, columnspan = 2)
    def temp_action2(self):
        self.vname = self.name.get()
        self.vemail = self.email.get()
        self.vdob = self.dob.get()
        self.vphone = self.phone.get()
        self.vaddress = self.address.get()
        self.vfirstpass = self.pswd.get()
        self.vsecondpass = self.repswd.get()
        self.vupi = self.upi.get()
        self.vreupi = self.reupi.get()
        self.vbank = self.bank.get()
        self.vacc = self.acc.get()
        print(self.vdob)
        pattern = re.match(r'[a-zA-Z0-9.-]+@[a-zA-z-]+\.(com|edu|net)',self.vemail)
        if not self.vname.isalpha():
            messagebox.showerror(title='Invalid name', message = 'Please enter a valid name')
            self.create()
        if not pattern:
            messagebox.showerror(title='Invalid email', message = 'Please enter a valid email')
            self.create()
        elif not self.vphone.isnumeric():
            messagebox.showerror(title='Invalid number', message = 'Please enter a valid phone number')
            self.create()

        elif self.vfirstpass != self.vsecondpass:
            messagebox.showerror(title='Invalid password', message = "Passwords didn't match")
            self.create()
        elif self.vbank not in self.bankoptions:
            messagebox.showerror(title='Invalid Bank', message = "Please select a valid bank")
            self.create()

        elif not self.vacc.isnumeric():
            messagebox.showerror(title='Invalid Account Number', message = 'Please enter a valid Account Number')
            self.create()
        elif self.vreupi != self.vupi:
            messagebox.showerror(title='Invalid UPI keys', message = "UPI Keys didn't match")
            self.create()

        else:
            messagebox.showinfo(title = 'Welcome to Postinter', message = 'Welcome {}'.format(self.vname))
            self.home()


    def profile(self):
        self.master.geometry('640x440+250+150')
        self.frame_body.pack_forget()
        self.frame_body = ttk.Frame(self.master)
        self.frame_body.pack()
        self.frame_body.config(relief = RIDGE, padding = (30,15))
        ttk.Button(self.frame_body, text = 'Edit Profile',command = self.edit).grid(row = 7, padx=10, pady=20, column = 0, columnspan = 2)
        ttk.Label(self.frame_body, text = 'Name: ').grid(row = 0, padx=10, pady=10, column = 0, sticky = 'nw')
        ttk.Label(self.frame_body, text = self.vname).grid(row = 0, padx=10, pady=10, column = 1,sticky = 'nw')
        ttk.Label(self.frame_body, text = 'Email Address: ').grid(row = 1, padx=10, pady=10, column = 0,sticky = 'nw')
        ttk.Label(self.frame_body, text = self.vemail).grid(row = 1, padx=10, pady=10, column = 1,sticky = 'nw')
        ttk.Label(self.frame_body, text = 'Date of Birth: ').grid(row = 2, padx=10, pady=10, column = 0,sticky = 'nw')
        ttk.Label(self.frame_body, text = self.vdob).grid(row = 2, padx=10, pady=10, column = 1,sticky = 'nw')
        ttk.Label(self.frame_body, text = 'Mobile: ').grid(row = 3, padx=10, pady=10, column = 0,sticky = 'nw')
        ttk.Label(self.frame_body, text = self.vphone).grid(row =3, padx=10, pady=10, column = 1,sticky = 'nw')
        ttk.Label(self.frame_body, text = 'Address: ').grid(row = 4, padx=10, pady=10, column = 0,sticky = 'nw')
        ttk.Label(self.frame_body, text = self.vaddress).grid(row = 4, padx=10, pady=10, column = 1,sticky = 'nw')
        ttk.Label(self.frame_body, text = 'Bank: ').grid(row = 5, padx=10, pady=10, column = 0,sticky = 'nw')
        ttk.Label(self.frame_body, text = self.vbank).grid(row = 5, padx=10, pady=10, column = 1,sticky = 'nw')
        ttk.Label(self.frame_body, text = 'Account Number: ').grid(row = 6, padx=10, pady=10, column = 0,sticky = 'nw')
        ttk.Label(self.frame_body, text = self.vacc).grid(row = 6, padx=10, pady=10, column = 1,sticky = 'nw')



    def edit(self):
        self.master.geometry('640x440+250+150')
        self.frame_body.pack_forget()
        self.frame_body = ttk.Frame(self.master)
        self.frame_body.pack()
        self.frame_body.config(relief = RIDGE, padding = (30,15))
        ttk.Button(self.frame_body, text = 'Back',command = self.profile).grid(row = 0, padx=10, pady=10, column = 0, sticky = 'nw')

        ttk.Label(self.frame_body, text = 'Email: ').grid(row = 1, padx=10, pady=10, column = 0)
        self.edit_mail = ttk.Entry(self.frame_body)
        self.edit_mail.grid(row = 1, column = 1)
        self.edit_mail.insert(0, self.vemail)
        ttk.Label(self.frame_body, text = 'Mobile: ').grid(row = 2, padx=10, pady=10, column = 0)
        self.edit_mob = ttk.Entry(self.frame_body)
        self.edit_mob.grid(row = 2, column = 1)
        self.edit_mob.insert(0, self.vphone)
        ttk.Label(self.frame_body, text = 'Address: ').grid(row =3, padx=10, pady=10, column = 0)
        self.edit_add = ttk.Entry(self.frame_body)
        self.edit_add.grid(row = 3, column = 1)
        self.edit_add.insert(0, self.vaddress)


        ttk.Button(self.frame_body, text = 'Save',command = self.save_changes).grid(row = 4, padx=10, pady=10, column = 0,sticky = 'ne')
        ttk.Button(self.frame_body, text = 'Cancel',command = self.edit_cancel).grid(row = 4, padx=10, pady=10, column = 1  )
    def save_changes(self):
        temp = messagebox.askyesno(title = 'Pay Money', message = 'Are you sure you want to save the changes')
        if temp == True:
            self.vemail = self.edit_mail.get()
            self.vphone = self.edit_mob.get()
            self.vaddress = self.edit_add.get()
            messagebox.showinfo(title = 'Success', message = 'Profile information changed successfully')
            self.profile()
    def edit_cancel2(self):
        value = messagebox.askyesno(title = 'Cancel Changes?', message = 'Are you sure you want to cancel your changes?')
        if value == True:
            self.acc_tran.delete(0,END)
            self.money_tran.delete(0,END)
    def edit_cancel_create(self):
        value = messagebox.askyesno(title = 'Cancel Changes?', message = 'Are you sure you want to cancel your changes?')
        if value == True:
            self.name.delete(0,END);self.email.delete(0,END);self.dob.delete(0,END);self.phone.delete(0,END); self.address.delete(0,END); self.pswd.delete(0,END); self.repswd.delete(0,END);self.upi.delete(0,END); self.reupi.delete(0,END)



    def edit_cancel(self):
        newedit_mail = self.edit_mail.get()
        newedit_mob = self.edit_mob.get()
        newedit_add = self.edit_add.get()
        value = messagebox.askyesno(title = 'Cancel Changes?', message = 'Are you sure you want to cancel your changes?')
        if value == True and newedit_mail!=self.vemail:
            self.edit_mail.delete(0,END)
            self.edit_mail.insert(0,self.vemail)
            if newedit_mob!=self.vphone:
                self.edit_mob.delete(0,END)
                self.edit_mob.insert(0,self.vphone)
            if newedit_add!=self.vaddress:
                self.edit_add.delete(0,END)
                self.edit_add.insert(0,self.vaddress)



    def friends(self):
        self.frame_body.pack_forget()
    def check_balance(self):
        self.frame_body.pack_forget()
    def transaction_history(self):
        self.frame_body.pack_forget()
    def transfer(self):
        self.frame_body.pack_forget()
        self.frame_body = ttk.Frame(self.master)
        self.frame_body.pack()
        self.frame_body.config(relief = RIDGE, padding = (30,15))
        ttk.Label(self.frame_body, text = "Enter the Account Number").grid(row = 0, padx=10, pady=10, column = 0)
        ttk.Label(self.frame_body, text = "Enter the Amount").grid(row = 1, padx=10, pady=10, column = 0)
        self.acc_tran = ttk.Entry(self.frame_body)
        self.acc_tran.grid(row = 0, padx=10, pady=10,column = 1)
        self.money_tran = ttk.Entry(self.frame_body)
        self.money_tran.grid(row = 1, padx=10, pady=10,column = 1)
        ttk.Button(self.frame_body, text = 'Pay',command = self.pay_tran).grid(row = 2, padx=10, pady=10, column = 0, sticky = 'ne')
        ttk.Button(self.frame_body, text = 'Cancel',command = self.edit_cancel2).grid(row = 2, padx=10, pady=10, column = 1)

    def pay_tran(self):
        self.money_tr = self.money_tran.get()
        self.acc_tr = self.acc_tran.get()
        if not self.money_tr.isnumeric():
            messagebox.showerror(title='Invalid Cash', message = 'Please enter a valid Cash')
        elif not self.acc_tr.isnumeric():
            messagebox.showerror(title='Invalid Account Number', message = 'Please enter a valid account number')

        else:
            temp = messagebox.askyesno(title = 'Pay Money', message = 'Are you sure you want to pay {} to Account:["{}"]'.format(self.money_tr,self.acc_tr))
            if temp == True:
                messagebox.showinfo(title = 'Success', message = 'Transaction Successful')
    def search(self):
        self.frame_body.pack_forget()
        self.frame_body = ttk.Frame(self.master)
        self.frame_body.pack()
        self.frame_body.config(relief = RIDGE, padding = (30,15))
        self.search_var = StringVar()
        self.search_var.set('Select your search operation')
        ttk.Label(self.frame_body, textvariable = self.search_var).grid(row = 1, padx=10, pady=10, column = 0)
        search_combo = ttk.Combobox(self.frame_body, textvariable = self.search_var)
        search_combo.grid(row = 0, padx=10, pady=10, column = 1)
        search_combo.set('Specify How to Search: ')
        search_combo.config(values = ('Search by Name: ', 'Search by Phone: '))
        self.search_friend = ttk.Entry(self.frame_body)
        self.search_friend.grid(row = 1, padx=10, pady=10, column = 1)
        ttk.Button(self.frame_body, text = "search",command = self.search_list).grid(row = 2, padx=10, pady=10, column = 1)

    def search_list(self):
        pass
    def mouse_press1(self,event):
        global count
        if count[0] == 0:
            self.user.delete(0,'end')
            count[0] += 1
            self.user.config(foreground = 'black')
    def mouse_press2(self,event):
        global count
        if count[1] == 0:
            self.psd.delete(0,'end')
            count[1] += 1
            self.psd.config(foreground = 'black',show = '*')



root = Tk()
app = Front(root)
root.mainloop()

