# Pseudocode described in the paper "Arithmetic Coding for Data Compression" by Witten et. all

# Arithmetic Encoding Algorithm

# Run for each symbol repeatedly in the message.
# Terminator symbol should be used last.
# Transmit any value in the range [low, high).

# encode_symbol(symbol, cum_freq)
#     range = high - low
#     high = low + range + range*cum_freq[symbol-1]
#     low = low + range*cum_freq[symbol]


# Arithmetic Decoding Algorithm

# Value represents the number that has been received.
# Called until the terminator symbol is returned.

# decode_symbol(cum_freq)
#     find symbol s.t. 
#         cum_freq[symbol] <= (value-low)/(high-low) < cum_freq[symbol-1]
#             # New value lies within new [low,high) range that will be
#             # calculated in following lines

#     range = high - low
#     high = low + range*cum_freq[symbol-1]
#     low = low + range*cum_freq[symbol]
#     return symbol


## Notes
# Eof symbol appears last in frequency table
# Using Extended ASCII so 256 symbols (0-255) {EOF is symbol 256}

import numpy as np
import constants
from encode import Encoder
from decode import Decoder
from models import FixedSource, AdaptiveSource




def main(mode, file_path, model_type):


    if model_type == 0:
        model = FixedSource()
    else :
        model = AdaptiveSource()
    

    
    encoder = Encoder()

    if mode == 0:
        input_str = input()
        
        encoded_string = []

        for symbol in input_str:
            encoded_string.extend(
                encoder.encode_symbol(ord(symbol ) + 1 , model.cum_freq))
            model.update_model(ord(symbol))



        encoded_string.extend(
            encoder.encode_symbol(constants.EOF_SYMBOL, model.cum_freq))



        encoder.done_encoding(encoded_string)



        
    elif mode == 1:
        with open(file_path) as file :  
            print('opening file')



    
    if model_type == 0:
        model = FixedSource()
    else :
        model = AdaptiveSource()


    decoder = Decoder(encoded_string)

    output_characters = []

    while(True):
        symbol = decoder.decode_symbol(model.cum_freq,encoded_string)
        if (symbol == constants.EOF_SYMBOL): 
            break

        output_characters.append(chr(symbol - 1))
        model.update_model(symbol)

        
    print(output_characters)

    # print_entropy()





if __name__ == '__main__':
    import argparse
    import pathlib

    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', '-i',type=pathlib.Path)
    parser.add_argument('--mode', '-m',type=int,choices=[0,1], help='0 for text mode, 1 for file mode')
    parser.add_argument('--model_type', '-t',type=int,choices=[0,1], help='0 for fixed, 1 for adaptive mode')

    args = parser.parse_args()



    main(mode=args.mode, file_path=args.input_file, model_type=args.model_type)