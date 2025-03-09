class UpperLower:
    def __init__(self):
        self.__upper_count = 0
        self.__lower_count = 0
    def amount_upper_lower(self, text):
        for i in (range(0, len(text))):
            tmp_char = text[i]
            if tmp_char.isupper():
                self.__upper_count += 1
            elif tmp_char.islower():
                self.__lower_count += 1
    
    def get_upper_count(self):
        return self.__upper_count
    
    def get_lower_count(self):
        return self.__lower_count