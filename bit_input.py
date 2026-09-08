import constants

class InputStream:

    def __init__(self):
        self.bits_to_go=0
        self.garbage_bits=0
        self.buffer=[]

    def get_byte(self,bits):
        byte = []

        if (len(bits) >=8):

            for i in range(0,8):
                byte.append(bits.pop(0))
            return byte
        
        elif (len(bits) > 0):
            length_bits = len(bits)
            for i in range(0, length_bits):
                byte.append(bits.pop(0))
            for i in range(0, 8-length_bits):
                byte.append(0)
            return byte
        
        else:
            return -1

    
    def get_input(self,bits):
        if(self.bits_to_go==0):
            self.buffer = self.get_byte(bits)
            if (self.buffer == -1 ) :
                self.garbage_bits += 1
                
                if (self.garbage_bits > constants.NUM_CODE_BITS-2):
                    print("Bad input file\n")
                    exit(-1)
                return 0

            self.bits_to_go = 8
        t = self.buffer.pop(0)
        self.bits_to_go -= 1
        return t