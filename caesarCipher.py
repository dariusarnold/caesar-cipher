#!/usr/bin/env python

import string
try:
    from IPython.display import clear_output  # clears ipython console
except ImportError:
    # not running in IPython notebook, no clear_output function available
    def clear_output(): pass
try:
    input = raw_input
except NameError: pass

class Coder(object):
    """
    Implements a caesar cipher encoder and decoder. Use Coder.use() to run class
    """

    lower_case = list(string.ascii_lowercase)
    upper_case = list(string.ascii_uppercase)
    case = lower_case + upper_case

    def use(self):
        self.mode = self.get_mode()
        clear_output()
        self.input_string = self.get_user_input_string()
        clear_output()
        self.input_cipher = self.get_user_cipher()
        clear_output()
        if self.mode == 'd':
            self.result = self.decode(self.input_string, self.input_cipher)
        elif self.mode == 'e':
            self.result = self.encode(self.input_string, self.input_cipher)
        print("Output: " + self.result)

    def get_mode(self):
        """
        Get user input and set mode to decoding or encoding
        :return: Coding mode string: (d)ecoding or (e)ncoding
        :rtype: str
        """
        mode = input("Enter d to decode, e to encode\n").lower()
        if mode not in ('d', 'e'):
            clear_output()
            print("Invalid input, choose Encoding (e) or decoding (d)")
            return self.get_mode()
        return mode

    def get_user_input_string(self):
        string = input("Please input a string: ")
        return string

    def get_user_cipher(self):
		"""
		Get cipher (number to shift by), limited between 0...26, 
		allowing only numeric input.
		:rtype: int
		"""
        cipher = input("Please input cipher (default: 13): ")
        if cipher == "": return 13
        if cipher.isdigit():
            cipher = int(cipher)
            # limit cipher to numbers < 26, since shifting more has no effect
            if cipher > 26:
                cipher = cipher % 26
            return cipher
        else:
            print("Only numbers allowed!")
            if cipher.isalpha():
                return int(self.get_user_cipher())
            else:
                print("Stripping letters out of input")
                cipher = "".join([symbol for symbol in cipher if symbol.isdigit()])
                return int(cipher)

    def encode(self, string, cipher):
        """
        Encode string by looping through all symbols. Letters will be shifted by cipher, 
        while special characters will just be appended to the result
        """
        result = ""
        for symbol in string:
            if symbol not in self.case:
                # non alpha characters will just be appended without encoding
                result = result + symbol
            else:
                if symbol.isupper():
                    index = self.upper_case.index(symbol)
                    index += cipher
                    if index > 25:
                        index -= 26
                    result = result + self.upper_case[index]
                else:
                    index = self.lower_case.index(symbol)
                    index += cipher
                    if index > 25:
                        index -= 26
                    result = result + self.lower_case[index]
        return result

    def decode(self, string, cipher):
        """
        decoding is implemented as encoding 'in reverse'.
        """
        return self.encode(string, abs(cipher - 26))


if __name__ == "__main__":
    coder = Coder()
    coder.use()
