import numpy as np
class Job:
    # Constructor of jobe
    def __init__(self, time_on_machine):
        self.time_on_machine = time_on_machine
        self.size = np.shape(time_on_machine)[0]

    # Time on machine
    def time(self, machine):
        if machine < self.size:
            return self.time_on_machine[machine]
        else:
            print('Job time() size error')
            return None


