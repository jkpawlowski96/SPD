class HeapMax:

    def __init__(self):
        self.values = []

    def add(self, v):
        i = len(self.values)
        self.values.append(v)
        self.b(i)

    def b(self, i):
        if i == 0:
            return
        p = int((i - 1)/2)
        if self.values[i] >= self.values[p]:
            self.swap(i, p)
            self.b(p)

    def b2(self, i):
        l = i * 2 + 1
        p = i * 2 + 2
        if l < len(self.values):
            self.b(l)
            self.b2(l)

        if p < len(self.values):
            self.b(p)
            self.b2(p)

    def swap(self, i, j):
        v = self.values[i]
        self.values[i] = self.values[j]
        self.values[j] = v

    def max(self, drop=False):
        if drop is False:
            return self.values[len(self.values) - 1]
        self.swap(0, len(self.values) - 1)
        v = self.pop(len(self.values) - 1)
        self.b2(0)
        return v

    def pop(self, i):
        return self.values.pop(i)


class HeapMin:

    def __init__(self):
        self.values = []

    def add(self, v):
        i = len(self.values)
        self.values.append(v)
        self.b(i)

    def b(self, i):
        if i == 0:
            return
        p = int((i - 1) / 2)
        if self.values[i] <= self.values[p]:
            self.swap(i, p)
            self.b(p)

    def b2(self, i):
        l = i * 2 + 1
        p = i * 2 + 2
        if l < len(self.values):
            self.b(l)
            self.b2(l)

        if p < len(self.values):
            self.b(p)
            self.b2(p)

    def swap(self, i, j):
        v = self.values[i]
        self.values[i] = self.values[j]
        self.values[j] = v

    def min(self, drop=False):
        if drop is False:
            return self.values[len(self.values) - 1]
        self.swap(0, len(self.values) - 1)
        v = self.pop(len(self.values) - 1)
        self.b2(0)
        return v

    def pop(self, i):
        return self.values.pop(i)

