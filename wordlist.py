import string
import random
import time
import os
import sys


class WordList:
    """
        WordList Handler Script
        author: NightFox | wordlist Beta v0.1
        e-mail: mking4everking@gmail.com
        git-hub: @MKing4ever
        GNU Open-Source Certification
    """

    def __init__(self):
        self.data = ' '  # string | my wordlist

    def __repr__(self):
        return f'WordList Module\nLength: {self.__len__()}\nBackup: {os.path.isfile("WordList.txt")}'

    def __str__(self):
        return self.data

    def __iter__(self):
        return iter(self._duplicate())

    def __len__(self):
        return len(self.data.split('\n'))  # default split with '\n'

    @staticmethod
    def echo(value):
        pass

    def _import(self, address='./'):
        _address = address
        _filename = 'WordList.txt'
        _file = _address + _filename
        if os.path.isfile(_file):
            with open(_file, 'r') as file:  # (READ)
                _data = file.readlines()  # list
                self.data += '\n' + ''.join(_data)  # string | update my wordlist
        else:
            print(f'No \'{_filename}\' Found.')

    def _export(self, address='./'):
        _data = self.data  # string
        _address = address
        _filename = 'WordList.txt'
        _file = _address + _filename
        with open(_file, 'w') as file:  # (WRITE)
            file.write(_data)  # write a new 'WordList.txt'

    def _extend(self, address='./'):
        _data = '\n' + self.data  # string | extend new data start with new line.
        _address = address
        _filename = 'WordList.txt'
        _file = _address + _filename
        if os.path.isfile(_file):
            with open(_file, 'a') as file:  # (APPEND)
                file.write(_data)  # update the 'WordList.txt'
        else:
            print(f'No \'{_filename}\' Found.')

    def _read(self):
        _data = self.data
        print(_data)
        print('---' * 10 + f'\nlength: {self.__len__()}')

    def _word(self, word: str):
        _w = word.split('\n')  # list | split input data
        _s = self._duplicate()  # set | wordlist with no duplicate
        _s = _s.union(_w)  # union Input and Wordlist
        self.data = '\n'.join(_s)  # str | join with '\n' (new-line). update my wordlist

    def _duplicate(self):
        _data = self.data.split('\n')  # list | split with '\n' (new-line).
        _s = set(_data)  # set | remove possible duplicate
        self.data = '\n'.join(_s)  # str | update my wordlist
        return _s  # return set

    def _remove(self, word):
        _s = self._duplicate()  # set
        _s.remove(word)
        self.data = '\n'.join(_s)  # update my wordlist
