from tkinter import *
from tkinter.colorchooser import askcolor

class MyPaint:
    def __init__(self, root):
        self.root = root
    
        self.color = "black"
        self.eraser = False
        self.old_x = None
        self.old_y = None
        
        self.bg_color = "white"
        
        self.canvas = Canvas(root, bg=self.bg_color, width=600, height=400)
        self.canvas.pack()
        
        self.frame = Frame(root)
        self.frame.pack()
        
        
        Button(self.frame, text="Black", command=self.black).pack(side=LEFT)
        Button(self.frame, text="Red", command=self.red).pack(side=LEFT)
        Button(self.frame, text="Blue", command=self.blue).pack(side=LEFT)
        Button(self.frame, text="Choose color", command=self.choose_color).pack(side=LEFT)
        Button(self.frame, text="change background", command=self.change_bg).pack(side=LEFT)
        Button(self.frame, text="eraser", command=self.use_eraser).pack(side=LEFT)
        Button(self.frame, text="clear", command=self.clear).pack(side=LEFT)
        
        
        
    def paint (self, event):
        pass

    def reset (self,event):
        pass
    
    def black (self):
        self.color = "black"
        self.eraser = False
    
    def red (self):
        self.color = "red"
        self.eraser = False
    
    def blue (self):
        self.color = "blue"
        self.eraser = False
    
    def choose_color (self):
        pass
    
    def use_eraser (self):
        self.eraser = True
    
    def clear (self):
         self.canvas.delete("all")
    
    def change_bg (self):
        color = askcolor()[1]
        if color:
            self.bg_color = color
            self.canvas.config(bg=self.bg_color)



if __name__ == "__main__":
    root = Tk()
    app = MyPaint(root)
    root.title('paint')
    root.mainloop()
    
    
 