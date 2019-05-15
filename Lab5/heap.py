

class HeapMax:

    def __init__(self):
        self.data = []

    def add(self, v):
        i = len(self.data)

        self.data.append(v)
        self.b_up(i)

    def b_up(self, i):
        if i == 0 or i > len(self.data):
            return
        p = int((i - 1) / 2)
        if self.data[i].value >= self.data[p].value:
            self.swap(i, p)
            self.b_up(p)

    def b_down(self, i):
        l = i * 2 + 1
        r = i * 2 + 2

        for child in [l, r]:
            if child < len(self.data):
                if self.data[child].value > self.data[i].value:
                    self.swap(i, child)
                    self.b_down(child)

    def swap(self, i, j):
        v = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = v

    def max(self, drop=False):
        if drop is False:
            return self.data[0]
        self.swap(0, self.last())
        v = self.data.pop(self.last())
        if len(self.data) > 0:
            self.b_down(0)

        return v

    def last(self):
        return len(self.data) - 1


class HeapMin:

    def __init__(self):
        self.data = []

    def add(self, v):
        i = len(self.data)

        self.data.append(v)
        self.b_up(i)

    def b_up(self, i):
        if i == 0 or i > len(self.data):
            return
        p = int((i - 1) / 2)
        if self.data[i].value <= self.data[p].value:
            self.swap(i, p)
            self.b_up(p)

    def b_down(self, i):
        l = i * 2 + 1
        r = i * 2 + 2

        for child in [l, r]:
            if child < len(self.data):
                if self.data[child].value < self.data[i].value:
                    self.swap(i, child)
                    self.b_down(child)

    def swap(self, i, j):
        v = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = v

    def min(self, drop=False):
        if drop is False:
            return self.data[0]
        self.swap(0, self.last())
        v = self.data.pop(self.last())
        if len(self.data) > 0:
            self.b_down(0)

        return v

    def last(self):
        return len(self.data) - 1

