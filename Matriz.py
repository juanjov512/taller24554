from importlib.metadata import FileHash
from mimetypes import init

class MyClass:

    def __init__(self, row, col, m1, m2) -> None:
        self.row = row
        self.col = col
        self.dim = row * col
        self.m1 = m1
        self.m2 = m2

    def sum(self):
        if True:
            sum = ([0, 0, 0], [0, 0, 0], [0, 0, 0])
            for row in range(len(self.m1)):
                for col in range(len(self.m1)):
                    sum[row][col] = self.m1[row][col] + self.m2[row][col]
            return sum        
        else:
            return 0

    def substract(self):
        if True:
            sub = ([0, 0, 0], [0, 0, 0], [0, 0, 0])
            for row in range(len(self.m1)):
                for col in range(len(self.m1)):
                    sub[row][col] = self.m1[row][col] - self.m2[row][col]
            return sub        
        else:
            return 0


    def mul(self):
        if True:
            mul = ([0, 0, 0], [0, 0, 0], [0, 0, 0])
            for row in range(len(self.m1)):
                for col in range(len(self.m1)):
                    mul[row][col] = self.m1[row][col] * self.m2[row][col]
            return mul        
        else:
            return 0


    def div(self):
        if True:
            div = ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
            for row in range(len(self.m1)):
                for col in range(len(self.m1)):
                    div[row][col] = self.m1[row][col] / self.m2[row][col]
            return div        
        else:
            return 0        
    