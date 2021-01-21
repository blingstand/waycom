class Worker(): 
    """this class aims to validate Waycom test"""
    
    NON_ACCEPTED = '1234567890&é"(-è_çà)=)\'~}{[]|`\\^@]?./§,;:!%ù^$£€*µ)><'

    def __init__(self): 
        """ init the class """
        self.plain_text = self.get_input_text()
        self.pure_text = self.remove_non_accepted(self.plain_text)
        self.split_input = (self.pure_text.split())
    
    def get_input_text(self):
        """this function returns the line from stdin"""
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


    def remove_non_accepted(self, text):
        """ this function removes NON_ACCEPTED char"""
        text = text.replace('\t', "")
        new_text = ""
        for word in text:
            if word not in [char for char in self.NON_ACCEPTED]: 
                new_text += word
        return new_text


    @property
    def display_answer(self):
        """ this function organizes print output"""
        dict_counter = {}
        msg = ""
        for word in self.split_input: 
            dict_counter[word] = 1 if word not in [key for key in dict_counter.keys()] else dict_counter[word] + 1

        # for key in (dict_counter): #simple display
        for key in sorted(dict_counter, key=dict_counter.get, reverse=True): #sorted display
            msg += f'{dict_counter[key]} : {key}\n'
        return msg
