import unittest

def collatz_conjecture(n):
    num = n
    temp = num
    seq = [num]

    while temp != 1:
        if temp % 2 == 0:
            temp //= 2
        else:
            temp = 3 * temp + 1
        seq.append(temp)
    
    return seq

def collatz_input():
    while True:
        x = input("Enter positive integer number: ")
        if (x > 0 & isinstance(x, int)):
            break
        else: 
            raise Exception("Value Error: Invalid number. Try positive integer.")
    collatz_conjecture(x)

def collatz_string(seq):
    result = ''
    for i in range(len(seq)):
        result += str(seq[i])
        if i != (len(seq) - 1):
            result += ' -> '
    
    return result

class CollatzConjectureTests(unittest.TestCase):
    
    def test_3(self):
        print(collatz_string(collatz_conjecture(3)))
        self.assertEqual(collatz_conjecture(3), [3, 10, 5, 16, 8, 4, 2, 1])
    
    def test_19(self):
        print(collatz_string(collatz_conjecture(19)))
        self.assertEqual(collatz_conjecture(19), [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

    def test_27(self):
        print(collatz_string(collatz_conjecture(27)))
        self.assertEqual(collatz_conjecture(27), [27, 82, 41, 124, 62, 31, 94, 47,
                                                    142, 71, 214, 107, 322, 161, 484,
                                                      242, 121, 364, 182, 91, 274, 137,
                                                        412, 206, 103, 310, 155, 466, 233,
                                                          700, 350, 175, 526, 263, 790, 395,
                                                            1186, 593, 1780, 890, 445, 1336, 668,
                                                              334, 167, 502, 251, 754, 377, 1132, 566,
                                                                283, 850, 425, 1276, 638, 319, 958, 479,
                                                                  1438, 719, 2158, 1079, 3238, 1619, 4858,
                                                                    2429, 7288, 3644, 1822, 911, 2734, 1367,
                                                                      4102, 2051, 6154, 3077, 9232, 4616, 2308,
                                                                        1154, 577, 1732, 866, 433, 1300, 650, 325,
                                                                          976, 488, 244, 122, 61, 184, 92, 46, 23, 70,
                                                                            35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1])

if __name__ == '__main__':
    unittest.main()