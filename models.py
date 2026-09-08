import constants



class Model:
    def __init__(self):
        self.freq = [0] * (constants.TOTAL_SYMBOLS + 1)
        self.cum_freq = [0] * (constants.TOTAL_SYMBOLS + 1)



class FixedSource(Model):
    def __init__(self):
        super().__init__()
        self.freq = [
                0,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 124, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1,   1, 1, 1, 1, 1, 1,
                1236, 1,21, 9, 3, 1,25,15, 2, 2,   2, 1,79,19,60, 1,
               15,15, 8, 5, 4, 7, 5, 4, 4, 6,   3, 2, 1, 1, 1, 1,
                1,24,15,22,12,15,10, 9,16,16,   8, 6,12,23,14,11,
               14, 1,14,28,29, 6, 3,11, 1, 3,   1, 1, 1, 1, 1, 3,
               1,491, 85,173,232,744,127,110,293,418,6,39,250,139,429,446,
               111,5,388,375,531,152,57,97,12,101,5,2,1,2,3,1,
               1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
               1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
               1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
               1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
               1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
               1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
               1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
               1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
               1
        ]

        for i in reversed(range (1, constants.TOTAL_SYMBOLS+ 1)):
            self.cum_freq[i-1] =  self.cum_freq[i] + self.freq[i] 

        if self.cum_freq[0] > constants.MAX_FREQUENCY: # making sure max frequency is not exceeded
            return

    def update_model(self,symbol):
        symbol # do nothing

class AdaptiveSource(Model):
    def __init__(self):
        super().__init__()
        for i in range (0, constants.TOTAL_SYMBOLS + 1):
            self.freq[i] = 1
            self.cum_freq[i] = constants.TOTAL_SYMBOLS-i

        self.freq[0] = 0


    def update_model(self,symbol):
        
        if (self.cum_freq[0] == constants.MAX_FREQUENCY):
            cumulative_calc = 0
            for i in reversed(range (1, constants.TOTAL_SYMBOLS + 1)):
                self.freq[i] = (self.freq[i ] + 1) // 2
                self.cum_freq[i] = cumulative_calc
                cumulative_calc += self.cum_freq[i]

        i = symbol
        while(self.freq[i] == self.freq[i-1]):
            i -= 1

        self.freq[i] += 1
        while(i > 0):
            i -= 1
            self.cum_freq[i] += 1

