from tkinter import *
from tkinter import messagebox

popup = Tk()
popup.eval('tk::PlaceWindow %s center' % popup.winfo_toplevel())
popup.withdraw()
#popup.mainloop()
messagebox.showinfo('Info', 'Test')
popup.deiconify()
popup.destroy()
popup.quit()
