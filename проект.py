from tkinter import *
from tkinter.colorchooser import askcolor

class MiniPaint:
    def __init__(self, root):
        self.root = root
        self.root.title("Мини-Пейнт")

        self.color = "black"
        self.eraser = False
        self.old_x = None
        self.old_y = None

        # Изначальный цвет фона
        self.bg_color = "white"
        
        # Холст
        self.canvas = Canvas(root, bg=self.bg_color, width=600, height=400)
        self.canvas.pack()

        self.frame = Frame(root)
        self.frame.pack()

        # Кнопки для изменения цвета кисти
        Button(self.frame, text="Черный", command=self.set_black).pack(side=LEFT)
        Button(self.frame, text="Красный", command=self.set_red).pack(side=LEFT)
        Button(self.frame, text="Синий", command=self.set_blue).pack(side=LEFT)
        Button(self.frame, text="Выбрать цвет", command=self.choose_color).pack(side=LEFT)
        Button(self.frame, text="Ластик", command=self.use_eraser).pack(side=LEFT)
        Button(self.frame, text="Очистить", command=self.clear).pack(side=LEFT)

        # Кнопка для смены фона
        Button(self.frame, text="Сменить фон", command=self.change_bg).pack(side=LEFT)

        # Ползунок для изменения толщины линии
        self.size_slider = Scale(root, from_=1, to=20, orient=HORIZONTAL)
        self.size_slider.set(5)
        self.size_slider.pack()

        # Привязка событий рисования
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def paint(self, event):
        c = "white" if self.eraser else self.color
        s = self.size_slider.get()
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                    fill=c, width=s, capstyle=ROUND, smooth=True)
        self.old_x, self.old_y = event.x, event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def set_black(self):
        self.color = "black"
        self.eraser = False

    def set_red(self):
        self.color = "red"
        self.eraser = False

    def set_blue(self):
        self.color = "blue"
        self.eraser = False

    def choose_color(self):
        clr = askcolor()[1]
        if clr:
            self.color = clr
            self.eraser = False

    def use_eraser(self):
        self.eraser = True

    def clear(self):
        self.canvas.delete("all")

    # Метод для смены фона
    def change_bg(self):
        color = askcolor()[1]
        if color:
            self.bg_color = color
            self.canvas.config(bg=self.bg_color)

if __name__ == "__main__":
    root = Tk()
    app = MiniPaint(root)
    root.mainloop()
