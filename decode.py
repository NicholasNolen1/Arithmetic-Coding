import constants
from bit_input import InputStream

class Decoder :

   


    def __init__(self,bits):
        self.value = 0

        self.input = InputStream()

        for i in range(0, constants.NUM_CODE_BITS): 
            input_bit = self.input.get_input(bits)

            self.value = 2 * self.value + input_bit


        self.low = 0
        self.high = constants.TOP_VALUE

    def decode_symbol(self,cum_freq,bits): 
        range_val = (self.high-self.low) + 1

        cumulative_calc = (((self.value-self.low)+1)*cum_freq[0]-1)//range_val

        symbol = 1
        while (cum_freq[symbol] > cumulative_calc):
            symbol = symbol + 1

        self.high = self.low + (range_val*cum_freq[symbol - 1])//cum_freq[0]-1

        self.low = self.low + (range_val*cum_freq[symbol ])//cum_freq[0]

        while(True):
            if(self.high < constants.HALF):
                pass #do nothing

            elif (self.low >= constants.HALF):
                self.value -= constants.HALF
                self.low -= constants.HALF
                self.high -= constants.HALF

            elif (self.low >= constants.FIRST_QUARTER and
                   self.high < constants.THIRD_QUARTER):
                self.value -= constants.FIRST_QUARTER
                self.low -= constants.FIRST_QUARTER
                self.high -= constants.FIRST_QUARTER

            else:
                break

            self.low = 2*self.low
            self.high = 2*self.high+1

            input = self.input.get_input(bits)
            

            self.value = 2*self.value+input

        return symbol


        
