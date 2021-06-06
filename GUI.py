from tkinter import *
from Engine.Metrics import MineMap


class MineCell:
    def __init__(self, host, width, text, x, y):
        self.obj = Button(host,
                          width=width,
                          height=width//2,
                          text='',
                          font=('Times New Roman', 10, 'bold'),
                          command=self.pressed_left_button)
        self.obj.grid(row=x, column=y)
        self.x = x
        self.y = y
        self.hidden = text

    def pressed_left_button(self):
        self.obj['state'] = ACTIVE
        self.obj['bg'] = 'grey'
        map_colour = {'1': 'blue',
                      '2': 'green',
                      '3': 'darkblue',
                      '4': 'purple',
                      '5': 'yellow',
                      '6': 'pink',
                      '7': 'darkgreen',
                      '8': 'red'}
        if self.hidden != '*':
            if self.hidden != '0':
                self.obj['text'] = self.hidden
                self.obj['fg'] = map_colour[self.hidden]
            else:
                pass
        else:
            self.obj['text'] = 'M'


class MineField:
    def __init__(self):
        self.w = 360
        self.h = self.w
        self.map_size = 1
        self.difficulty = 3
        self.amount_of_cells = [9, 15, 18]
        self.mine_coefficients = [0.1, 0.3, 0.5, 0.7]
        self.mine_map = MineMap(self.amount_of_cells[self.map_size],
                                self.mine_coefficients[self.difficulty])
        self.metric = self.mine_map.checking()
        self.root = Tk()
        self.root.title('Minesweeper')
        self.field = Frame()
        self.field.pack()
        self.cells = []
        self.size = 4
        for idx1 in range(self.amount_of_cells[self.map_size]):
            for idx2 in range(self.amount_of_cells[self.map_size]):
                self.cells.append(MineCell(self.field,
                                           self.size,
                                           f'{self.metric[idx1][idx2]}',
                                           idx1,
                                           idx2))
        self.root.mainloop()


new_game = MineField()
print(new_game.mine_map)
