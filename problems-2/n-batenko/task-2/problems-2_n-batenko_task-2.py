import unittest

def eng_latin_rearrange_sort(filename = "problems-2/n-batenko/task-2/english_latin_dictionary.txt"):
    eng_latins_tuples = []
    with open(filename) as f:
        for line in f:
            temp = line.split(" - ")

            eng = temp[0]
            latins = temp[1].split(", ")

            eng_latins_tuples.append((eng, latins))
    
    latin_eng_dict = {}
    for tuple in eng_latins_tuples:
        for latin in tuple[1]:
            latin_eng_dict[latin] = tuple[0]

    
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