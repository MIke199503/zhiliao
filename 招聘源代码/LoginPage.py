import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
import SearchPage


class LoginPage(): 
    '''
    this object is aim for creat login view ,include verify the acount is still work .
    
    '''
    def __init__(self, master,resource): 
        self.root1 = master 
        self.data = resource
        self.root1.geometry("1920x1080")

        #save the user input 
        self.username = tk.StringVar() 
        self.password = tk.StringVar() 

        #go!built it!!!
        self.createPage() 
  

    def createPage(self): 
        '''
        create basic entry view and label
        
        '''
        self.page2 = ttk.Frame(self.root1) #创建Frame 


        ttk.Label(self.page2).grid(row=0, sticky="nsew")
        ttk.Label(self.page2, text = '账户: ').grid(row=1, sticky="nsew", pady=10) 
        ttk.Entry(self.page2, textvariable=self.username).grid(row=1, column=1, sticky="nsew") 
        ttk.Label(self.page2, text = '密码: ').grid(row=2, sticky="nsew", pady=10) 
        ttk.Entry(self.page2, textvariable=self.password, show='*').grid(row=2, column=1, stick="nsew") 
        ttk.Button(self.page2, text='登陆', command=self.loginCheck).grid(row=3, sticky="nsew", pady=10) 
        ttk.Button(self.page2, text='退出', command=self.quitapp).grid(row=3, column= 1,sticky="e")

        self.page2.place(relx=0.4,rely=0.2)


    def quitapp(self):
        '''
        shut down the app
        '''
        self.root1.quit()
    
    def loginCheck(self): 
        '''
        compara the acount and password is right
        you can ignore the space before or after the string .
        '''
        name = str(self.username.get()).strip()
        secret = str(self.password.get() ).strip()
        UserList = self.data.getUserData()
        if name not in UserList.keys() : 
            showerror(title='账号错误', message='账号不存在！！请联系你的助教老师。') 
        elif secret != str(UserList[name]["password"]) :
            showerror(title='密码错误', message='账号密码错误！！再想想吧～') 
        elif  not UserList[name]["quality"] :
            showerror(title='有效期错误',message="该账号已无对应权限，请联系你的助教老师。")
        else: 
            showinfo(title='恭喜', message='请稍等，登陆成功。')
            self.page2.destroy()
            SearchPage.SearchPage(self.root1,self.data) 