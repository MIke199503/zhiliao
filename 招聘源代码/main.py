from tkinter import *
import pickfile
import os

try :
    import webbrowser
except:
    os.system("pip install webbrowser")

try :
    import openpyxl
except:
    os.system("pip install openpyxl")

try :
    import msoffcrypto
except:
    os.system("pip install msoffcrypto")

root  = Tk()
root.title('JD查询')
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
root.tk.call('source', os.path.join(dir_path, 'sun-valley.tcl'))
root.tk.call("set_theme", "dark")
root.geometry(("1920x1080"))
pickfile.PickFile(root)
root.mainloop()
