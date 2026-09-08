import constants



class Encoder:
    def __init__(self):
        self.low = 0
        self.high = constants.TOP_VALUE
        self.bits_to_follow = 0

    def append_bit_and_follow(self, bits, bit):
        bits.append(bit)
        while (self.bits_to_follow > 0):
            if bit == 0 : 
                bits.append(1)
            else :
                bits.append(0)
            self.bits_to_follow -= 1
            

    def encode_symbol(self, symbol, cum_freq): 

        range_val = (self.high - self.low) + 1
        self.high = self.low + (range_val * cum_freq[symbol-1])//cum_freq[0]-1
        self.low = self.low + (range_val * cum_freq[symbol])//cum_freq[0]


        # Encoding the range using bits
        
        output_bits = []

        while (True) :
            if (self.high < constants.HALF) :
                self.append_bit_and_follow(output_bits, 0)
                
            elif (self.low >= constants.HALF) :
                self.append_bit_and_follow(output_bits,1)
                self.low -= constants.HALF
                self.high -= constants.HALF

            elif (self.low >=constants.FIRST_QUARTER and self.high < constants.THIRD_QUARTER) :   
                self.bits_to_follow += 1
                self.low -= constants.FIRST_QUARTER
                self.high -= constants.FIRST_QUARTER
            else:
                break

            self.low = 2 * self.low
            self.high = 2 * self.high + 1
        
        return output_bits


    def done_encoding(self,output_bits):  
        self.bits_to_follow += 1

        if (self.low < constants.FIRST_QUARTER):
            self.append_bit_and_follow(output_bits,0)
        else :
            self.append_bit_and_follow(output_bits,1)
        
