#! /usr/bin/python3

"""This script can be tested : 
    $ pytest test.py -s 
"""
class Worker():
    """ this a working machine ready to follow your order """
    def __init__(self):
        self.plain_text = self.get_input_text()
        self.converted_to_list = self.convert_to_list()

    def get_input_text(self):
        """this function returns one str line from stdin"""
        lines = []
        count = 0
        while True:
            try: 
                line = input()
            except EOFError:
                break
            lines.append(line)

        line = ' '.join(lines)
        return line

    def convert_to_list(self):
        """create a dict from plain_text"""
        modified_text = self.plain_text.replace(":", " ")
        split_text = modified_text.split(" ")
        list_instant_time = []
        list_pairs = []

        for i in range(2, len(split_text)+2, 2):
            start, end = int(split_text[i-2]), int(split_text[i-1])
            list_instant_time.append(start)
            list_instant_time.append(end)
            list_pairs.append((start, end))
        return sorted(list_instant_time), list_pairs


    @property
    def peak_call(self): 
        """this function detects the peak call"""
        list_instant_time, list_pairs = self.converted_to_list
        wm_list_pairs = list_pairs #write mode
        highest_peak = 0
        for instant in sorted(list(set(list_instant_time))):  #to avoid duplicates
            peak = 0 
            item_to_remove = []
            for pair in wm_list_pairs: 
                peak = peak + 1 if  pair[0] <=  instant <= pair[1] else peak
                if instant > pair[1]: 
                    item_to_remove.append(pair)

            if len(item_to_remove) > 0:
                [wm_list_pairs.remove(pair) for pair in item_to_remove]
            highest_peak = peak if peak > highest_peak else highest_peak
        return highest_peak

    @property
    def display_answer(self):
        """ this function organizes print output"""
        return(f"{self.plain_text}\nle nombre maximal d'appel en même temps est de {self.peak_call}.")
