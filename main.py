import datetime,re
from datetime import datetime
from collections import OrderedDict




class sort:
    def __init__(self):
        pattern_dict = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}
        pattern_dict.update({chr(i): i - ord('A') + 27 for i in range(ord('A'), ord('Z') + 1)})
        symbols = '"!£$%^&*'
        for i, symbol in enumerate(symbols, start=52):
            pattern_dict[symbol] = i
        self.alphabet_dict = {v: k for k, v in pattern_dict.items()}
        self.c_time='12:59:17'
        self.encoded_time = []
    def spiller(self,type=None):
        self.encoded_time = []
        b = re.split(':', self.c_time)
        print(b)
        if type == '2':
            self.encode_2(b)
        else:
            self.encode_1(b)
    def encode_1(self,sut):
        for i in range(len(sut)):
            self.encoded_time.append(self.alphabet_dict[int(sut[i])])
        x=''.join(self.encoded_time)
        print(x)
        return x
    def encode_2(self,sut):
        pattern_dict = {chr(i): 53 - (i - ord('a')) for i in range(ord('a'), ord('z') + 1)}
        pattern_dict.update({chr(i): 26 - (i - ord('A')) for i in range(ord('A'), ord('Z') + 1)})
        symbols = '"!£$%^&*'
        for i, symbol in enumerate(symbols, start=53):
            pattern_dict[symbol] = i
        d_swap = {v: k for k, v in pattern_dict.items()}
        res = d_swap
        for i in range(len(sut)):
            self.encoded_time.append(res[int(sut[i])])
        x=''.join(self.encoded_time)
        print(x)
        return x

S = sort()
S.spiller('2')
S.spiller(1)




