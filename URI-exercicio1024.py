import math

def shiftFirstHalf(letter):
    charNumber = ord(letter)
    if 65 <= charNumber <= 90 or 97 <= charNumber <= 122:
        return chr(charNumber + 2)
    else:
        return chr(charNumber - 1)

def shiftSecondHalf(letter):
    charNumber = ord(letter)
    if 65 <= charNumber <= 90 or 97 <= charNumber <= 122:
        return chr(charNumber + 3)
    else:
        return letter

####Begin of execution###
test_cases = int(input())

for i in range(test_cases):
    line = list(input())
    line = list(map(shiftFirstHalf, line[:math.ceil(len(line)/2)])) + list(map(shiftSecondHalf, line[math.ceil(len(line)/2):]))
    result = ''.join(line)
    print(result[::-1])

    # for j in range(math.ceil(len(line)/2)):
    #     charNumber = ord(line[j])
    #     if 65 <= charNumber <= 90 or 97 <= charNumber <= 122:
    #         line[j] = chr(charNumber + 2) 
    #     else:
    #         line[j] = chr(charNumber - 1)

    # for k in range(math.ceil(len(line)/2), len(line)):
    #     charNumber = ord(line[k])
    #     if 65 <= charNumber <= 90 or 97 <= charNumber <= 122:
    #         line[k] = chr(charNumber + 3) 
    
    # result = ''.join(line)
    # print(result[::-1])