

class HeapMax:

    def __init__(self):
        self.values = []

    def add(self, v):
        i = len(self.values)

        self.values.append(v)
        self.b_up(i)

    def b_up(self, i):
        if i == 0 or i > len(self.values):
            return
        p = int((i - 1) / 2)
        if self.values[i] >= self.values[p]:
            self.swap(i, p)
            self.b_up(p)

    def b_down(self, i):
        l = i * 2 + 1
        r = i * 2 + 2

        for child in [l, r]:
            if child < len(self.values):
                if self.values[child] > self.values[i]:
                    self.swap(i, child)
                    self.b_down(child)

    def swap(self, i, j):
        v = self.values[i]
        self.values[i] = self.values[j]
        self.values[j] = v

    def max(self, drop=False):
        if drop is False:
            return self.values[0]
        self.swap(0, self.last())
        v = self.values.pop(self.last())
        if len(self.values) > 0:
            self.b_down(0)

        return v

    def last(self):
        return len(self.values) - 1


class HeapMin:

    def __init__(self):
        self.values = []

    def add(self, v):
        i = len(self.values)

        self.values.append(v)
        self.b_up(i)

    def b_up(self, i):
        if i == 0 or i > len(self.values):
            return
        p = int((i - 1) / 2)
        if self.values[i] <= self.values[p]:
            self.swap(i, p)
            self.b_up(p)

    def b_down(self, i):
        l = i * 2 + 1
        r = i * 2 + 2

        for child in [l, r]:
            if child < len(self.values):
                if self.values[child] < self.values[i]:
                    self.swap(i, child)
                    self.b_down(child)

    def swap(self, i, j):
        v = self.values[i]
        self.values[i] = self.values[j]
        self.values[j] = v

    def min(self, drop=False):
        if drop is False:
            return self.values[0]
        self.swap(0, self.last())
        v = self.values.pop(self.last())
        if len(self.values) > 0:
            self.b_down(0)

        return v

    def last(self):
        return len(self.values) - 1

