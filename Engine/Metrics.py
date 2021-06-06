from random import sample
n = 9


class MineMap:
    def __init__(self, size=9, mine_coefficient=0.1):
        self.size = size
        self.field = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.mines = int((self.size**2) * mine_coefficient)
        self.shuffle()

    def shuffle(self):
        counter = self.mines
        for idx1 in range(self.size):
            for idx2 in range(self.size):
                if counter > 0:
                    self.field[idx1][idx2] = '*'
                    counter -= 1
        epoch = 1000
        while epoch > 0:
            idx1, idx2, idx3, idx4 = sample([num for num in
                                             range(self.size)], 4)
            self.field[idx1][idx2], self.field[idx3][idx4] = \
                self.field[idx3][idx4], self.field[idx1][idx2]
            epoch -= 1

    def checking(self):
        idx1 = 0
        idx2 = 0
        # searching neighbours
        while idx1 in range(self.size) and idx2 in range(self.size):
            neighbours = []
            if idx1-1 >= 0:
                if idx2 - 1 >= 0:
                    neighbours.append([idx1-1, idx2-1])
                if idx2 + 1 < self.size:
                    neighbours.append([idx1-1, idx2+1])
                neighbours.append([idx1-1, idx2])
            if idx1+1 < self.size:
                if idx2 - 1 >= 0:
                    neighbours.append([idx1+1, idx2-1])
                if idx2 + 1 < self.size:
                    neighbours.append([idx1+1, idx2+1])
                neighbours.append([idx1+1, idx2])
            if idx2 - 1 >= 0:
                neighbours.append([idx1, idx2-1])
            if idx2 + 1 < self.size:
                neighbours.append([idx1, idx2+1])
            # checking neighbours
            if self.field[idx1][idx2] == '*':
                for neighbour in neighbours:
                    n_idx1, n_idx2 = neighbour[0], neighbour[1]
                    if self.field[n_idx1][n_idx2] != '*':
                        self.field[n_idx1][n_idx2] += 1
            idx2 += 1
            if idx2 > self.size-1:
                idx2 = 0
                idx1 += 1
        return self.field

    def __repr__(self):
        text = ''
        for string in self.field:
            text += ' '.join([str(elem) for elem in string])
            text += '\n'
        return text

    def __int__(self):
        return self.mines


def main():
    new_map = MineMap()
    new_map.checking()
    print(new_map, '\n', int(new_map), sep='')


if __name__ == '__main__':
    main()
