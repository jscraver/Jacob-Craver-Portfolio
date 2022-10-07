# takes stdin from the console
input1 = ""
x = 7
y = 8

bit7 = []
bit8 = []

string1 = ""
string2 = ""

# detects if binary input is 7 bit
if len(input1)%7 == 0:
    # divides the input into 7 bit strings
    for i in range(0, len(input1), x):
        bit7.append(input1[i:i+x])
        
    # converts the binary to ascii 
    for index in bit7:
        uni = int(index, 2)
        char = chr(uni)
        string1 = string1+char

    # prints stdout to the console
    print("7 Bit: ", string1)

# detects if binary input is 8 bit
if len(input1)%8 == 0:
    # divides the input into 8 bit strings
    for i in range(0, len(input1), y):
        bit8.append(input1[i:i+y])

    # converts the binary to ascii 
    for index in bit8:
        uni = int(index, 2)
        char = chr(uni)
        string2 = string2+char

    # prints stdout to the console
    print("8 Bit: ", string2)

