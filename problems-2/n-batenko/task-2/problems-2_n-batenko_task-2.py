import unittest

def eng_latin_rearrange_sort(filename = "problems-2/n-batenko/task-2/english_latin_dictionary.txt"):
    eng_latin = {}
    with open(filename) as f:

        latins = []
        eng = ""
        for line in f:
            temp = line.split(" - ")
            print(temp)
            eng = temp[0]
            latins = temp[1].split(", ")

            eng_latin[eng] = latins

            #for word in latins:
            #   eng_latin[word.strip()] += eng

    latin_eng = {}
    for k, v in eng_latin.items():
        for sub_value in v:
            latin_eng[sub_value] = []
        

    sorted_dict = {}
    sorted_keys = sorted(eng_latin.keys())
    for k in sorted_keys:
        sorted_dict[k] = eng_latin[k]
    
    return sorted_dict

def dict_printer(eng_latin : dict):
    for k, v in eng_latin.items():
        print(k, " - ", v)


'''class TestDictionary(unittest.TestCase):

    def task_example_test(self):
        text = "baca - fruit\nbacca - fruit\nmalum - apple, punishment
multa - punishment
pomum - apple
popula - apple
popum - fruit"
        self.assertEqual(eng_latin_rearrange_sort(), )'''

dict_printer(eng_latin_rearrange_sort())