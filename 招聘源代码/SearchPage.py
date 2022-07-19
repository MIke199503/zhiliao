import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import webbrowser

class SearchPage:
    '''
    built a Search view on root view
    '''
    def __init__(self,master,resource) -> None:
        #define a basic tree view style.Actually, we only need to limit row height equal 150
        s = ttk.Style()
        s.configure('Treeview', rowheight=150)

        #basic  settings
        self.root = master
        self.data = resource
        self.root.geometry("1920x1080")

        #save the choose 
        self.pickchoose = tk.StringVar() 
        self.pickplats = tk.StringVar() 

        #get job detail data.
        self.jbData = self.data.generateData()

        #get locations from data ,it's ready for combobox
        self.locations = self.data.locationlist

        #go !!   go ahead!!!
        self.createPage()

        # create a frame to take other views in 
        self.page4 = ttk.Frame(self.page3,width =  1000)
        self.page4.grid(row=3,column=0,columnspan=20,stick= tk.W,padx=10,pady=10) 

        #create x\y scroll to help user slide the page 
        self.xscroll = ttk.Scrollbar(self.page4, orient=tk.HORIZONTAL) # Don't Work
        self.yscroll = ttk.Scrollbar(self.page4, orient=tk.VERTICAL) # Working Now
        
        #initialize the tree view
        self.tree = ttk.Treeview(
            master = self.page4, #root view
            show='headings', #dont show the first column 
            height=5, #how many row need to showing 
            xscrollcommand=self.xscroll.set,  # bind the x scroll command to xscrol data set 
            yscrollcommand=self.yscroll.set,  # bind the y scroll command to yscrol data set 
            style="Treeview"
            )     

        #for show info easy, dont care.
        self.columnsa = ["岗位", "公司", "工作描述", "任职需求","薪资待遇","直达链接"] 

        #define the column 
        self.tree["columns"] = ("岗位", "公司", "工作描述", "任职需求","薪资待遇","直达链接")    

        #set the column 
        self.tree.column("岗位", width=100,anchor=tk.CENTER)         
        self.tree.column("公司", width=200,anchor=tk.CENTER)
        self.tree.column("工作描述", width=500,anchor=tk.W)
        self.tree.column("任职需求", width=500,anchor=tk.W)
        self.tree.column("薪资待遇", width=100,anchor=tk.W)
        self.tree.column("直达链接", width=300,anchor=tk.CENTER)
        self.tree.heading("岗位",text = "岗位",anchor=tk.CENTER)
        self.tree.heading("公司",text = "公司",anchor=tk.CENTER)
        self.tree.heading("工作描述",text = "工作描述",anchor=tk.CENTER)
        self.tree.heading("任职需求",text = "任职需求",anchor=tk.CENTER)
        self.tree.heading("薪资待遇",text = "薪资待遇",anchor=tk.CENTER)
        self.tree.heading("直达链接",text = "直达链接",anchor=tk.CENTER)

        #bind the mouse - 1(left)  behavior
        self.tree.bind('<ButtonRelease-1>', self.selectItem)
        
        #let scroll  widget control tree.xview.
        # self.xscroll.config(command=self.tree.xview)
        self.yscroll.config(command=self.tree.yview)

        #place the widget 
        # self.xscroll.pack(side= tk.BOTTOM,fill = tk.X)
        self.yscroll.pack(side = tk.RIGHT,fill = tk.Y)
        
        #place the tree view
        self.tree.pack(fill = tk.BOTH,expand=True)
  
    def createPage(self): 
        '''
        create the search view 
        '''
        #for separate the search view and tree view ,so. let's create a new Frame.
        self.page3 = ttk.Frame(self.root) #创建Frame 
        self.page3.pack() 

        #Tell the user what you're selecting ----location 
        ttk.Label(self.page3).grid(row=0, stick=tk.W) 
        ttk.Label(self.page3, text = '请选择你的地区：').grid(row=1,column=4, stick=tk.E, pady=10) 
        
        #list the options 
        a = ttk.Combobox(self.page3,textvariable=self.pickchoose, value=tuple(sorted(list(self.locations))))
        a.current(0)
        a.grid(row=1, column=5, stick=tk.E,padx=10)

        #Tell the user what you're selecting ----platform
        ttk.Label(self.page3, text = '请选择查询的平台：').grid(row=1,column=7, stick=tk.E, pady=10) 
        b = ttk.Combobox(self.page3,textvariable=self.pickplats, value=('BOSS直聘', '猎聘', '前程无忧', '智联招聘', '中华英才网'))
        b.current(0)
        b.grid(row=1, column=9, stick=tk.E,padx=10)  

        #Button ,let go search !,width=15
        ttk.Button(self.page3, text='查询', command=self.poring).grid(row=1, column=10, stick=tk.E,padx=10) 


    def poring(self):
        #get and delete all the Tree item.
        obk = self.tree.get_children()
        for x in obk:
            self.tree.delete(x)

        #get all the data what we're searching.
        result = self.data.getItem(self.pickplats.get(),self.pickchoose.get())
        
        #if get data ,show it .
        if isinstance(result,list):
            for x in result:
                item  = tuple([x["岗位"],x["公司"],x["工作描述"],x["任职需求"],x["薪资待遇"],x["直达链接"]])
                self.tree.insert("","end",values=item,open= True)
        else:
            showinfo(title='发生了一点意外哦～',message=result)
    

    def selectItem(self, event):
        '''
        In order to look easily and clearly ,
        when you use mouse-1 to click the Tree cell, 
        there will have a message box pop out 

        '''

        #which item is focus on 
        curItem = self.tree.item(self.tree.focus())
        #which cell 
        col = self.tree.identify_column(event.x)

        #if you foucs the #0 column *(it doesn't work , because we make heading undisplay)

        if col == '#0':
            cell_value = curItem['text']
        elif col == '#1':
            cell_value = curItem['values'][0]
            showinfo(title= self.columnsa[0] ,message=cell_value)
        elif col == '#2':
            cell_value = curItem['values'][1]
            showinfo(title= self.columnsa[1] ,message=cell_value)
        elif col == '#3':
            cell_value = curItem['values'][2]
            showinfo(title= self.columnsa[2] ,message=cell_value)
        elif col == '#4':
            cell_value = curItem['values'][3]
            showinfo(title= self.columnsa[3] ,message=cell_value)
        elif col == '#5':
            cell_value = curItem['values'][4]
            showinfo(title= self.columnsa[4] ,message=cell_value)
        #if you are focus on the link ,this code will open the url by your default web browser.
        elif col == '#6':
            cell_value = curItem['values'][5]
            webbrowser.open(cell_value)