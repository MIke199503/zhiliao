
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
import DataEnd
import tkinter.filedialog as fp
from LoginPage import *

class PickFile:
    '''
    This is view for user to pick a Data.xlsx file from themselves  computer
    '''
    def __init__(self,master):
        '''
        initialize the basicView, need the father view.
        '''
        self.root = master
        self.root.geometry("1920x1080") # set Screen size
        self.filePath = ""
        self.create_page()  # go built View
 
    def create_page(self):
        '''
        built views by automatic 
        '''
        self.page = ttk.Frame(self.root)
        self.page.place(relx=0.45,rely = 0.3)
        self.pageImage = ttk.Frame(self.root)  
        
        self.button = ttk.Button(self.page,text = '点击你的数据源Excel',command= self.callbacks)
        self.button.pack()

        #company logo use as water point.
        global x
        x = tk.PhotoImage(file = "资源1.png")
        ttk.Label(self.pageImage,image = x).pack()
                
        self.pageImage.pack(side=tk.BOTTOM) 


    def callbacks(self):
        '''
        open askopenfilename for let user choose a Data.xlsx
        '''
        self.filePath = fp.askopenfilename(title = "请选择数据源Excel文件",filetypes=[("Excel文件",".xlsx")])
        try:
            self.DataSource = DataEnd.DataDeal(filePath=self.filePath)
        except:
            showerror(title="很可惜，发生了一点错误。:",message = "你所选择的文件不符合要求，请仔细核对并重新选择。")
        else:
            self.page.destroy() ## shut down this view
            #start the next view ,we need resource beacuse want to economize the internal memory. 
            #it's not need to open file twice .
            LoginPage(master = self.root,resource = self.DataSource) 
            
            

