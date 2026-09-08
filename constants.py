
## DEFINITIONS

NUM_CODE_BITS = 16

NUM_SYMBOLS = 256
TOTAL_SYMBOLS = NUM_SYMBOLS + 1 


# Maximum decimal value (using 16 bits)
TOP_VALUE = (1 << NUM_CODE_BITS) - 1 


# Values splitting the code into quarters
FIRST_QUARTER = TOP_VALUE // 4 + 1
HALF = 2 * FIRST_QUARTER
THIRD_QUARTER = 3 * FIRST_QUARTER

# Maximum Frequency for ensuring no collisions
MAX_FREQUENCY = 16383

EOF_SYMBOL = TOTAL_SYMBOLS


