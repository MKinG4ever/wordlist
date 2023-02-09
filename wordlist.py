import random
import time
import os
from functools import wraps


def exe_time(func):
    """execution time, decorator"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        _start = time.time()
        result = func(*args, *kwargs)
        _end = time.time()
        print(f'Execution Time: {_end - _start}')
        return result

    return wrapper


class WordList:
    """
        WordList Handler Script
        author: NightFox | wordlist Beta v0.2.1
        e-mail: mking4everking@gmail.com
        git-hub: @MKing4ever
        GNU Open-Source Certification
    """

    # notification of features and changes

    def __init__(self):
        # lists
        self.words = ['pass', 'passwd', 'password']  # list | my wordlist
        self.exceptions = [' ', '']  # list | my exceptions wordlist
        # file address
        self.address = './'
        self.filename = 'WordList.txt'

    def __repr__(self):
        return f'WordList Module v0.2\nLength: {self.__len__()}\nBackup: {self.exist}\nAddress: {self.file}'

    def __str__(self):
        return self.list2str(self.data)

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    @property
    def data(self):
        self.words = self.duplicate(self.words)  # Difference between 'words' and 'data'
        return self.words + self.exceptions

    @property
    def file(self):
        return self.address + self.filename  # ./WordList.txt

    @property
    def exist(self):
        return os.path.isfile(self.file)

    @staticmethod
    def delay(secs=0):
        # make an interrupt
        if secs:
            time.sleep(secs)
        else:
            time.sleep((random.random() / 3.1415926535).__pow__(2))

    @staticmethod
    def str2list(data: str) -> list:
        return data.split()  # split with ' '-(Space) and '\n'-(NewLine)

    @staticmethod
    def list2str(data: list) -> str:
        return '\n'.join(data)  # make a True wordlist | merge words with '\n'-NewLine

    @staticmethod
    def duplicate(data: list):
        return sorted(list(set(data)))  # remove duplicates and return sorted list

    @staticmethod
    def question(quest, answer):
        a = input(quest).strip()
        if a and a != answer:
            answer = a
        return answer

    def echo(self, value: str):
        # print, write, type, echo... this function have many names
        for line in value.split('\n'):  # support multi-line text
            chars = ''
            for char in line:
                chars += char
                print(f'\r{chars}', end='')
                if char != ' ':  # skip Spaces
                    self.delay()
            print('')  # NewLine

    @exe_time
    def import_list(self):
        if self.exist:
            with open(self.file, 'r') as file:
                data = self.str2list(file.read())
                self.words.extend(data)
            self.echo(f'File \'{self.filename}\' imported. ({len(data)})')
        else:
            self.echo(f'No \'{self.filename}\' Found.')

    @exe_time
    def export_list(self):
        self.echo(f'File \'{self.filename}\' {"already exist." if self.exist else "not exist."}')
        with open(self.file, 'w') as file:
            file.write(self.list2str(self.data))
        self.echo(f'File \'{self.filename}\' exported.')

    @exe_time
    def extend_list(self):
        if self.exist:
            with open(self.file, 'a') as file:
                file.write(self.list2str(self.data))
            self.echo(f'File \'{self.filename}\' extended.')
        else:
            self.echo(f'No \'{self.filename}\' Found.')

    def new_list(self):
        self.echo('Please enter address and file name.')
        self.address = self.question('file address:', './')
        self.filename = self.question('file name:', 'WordList.txt')

    def delete_list(self):
        if self.exist:
            os.remove(self.file)
            self.echo(f'File \'{self.filename}\' deleted.')
        else:
            self.echo(f'No \'{self.filename}\' Found.')

    @exe_time
    def read(self):
        x = len(str(self.__len__()))  # length reserved
        data = [f'[{k:{x}}]: {v}' for k, v in enumerate(self.data)]
        print(self.list2str(data))
        self.echo('-   -   ' * 5 + f'\nLength: {self.__len__()}')

    @exe_time
    def add_word(self, word: str):
        data = self.str2list(word)  # list | turn  str (input argument) to list
        self.words.extend(data)  # update wordlist
        self.echo(f'Length: {self.__len__()}')

    @exe_time
    def add_words(self, words: list):
        self.words.extend(words)  # update wordlist
        self.echo(f'Length: {self.__len__()}')

    def remove_word(self, word: str):
        if word in self.words:
            self.words.remove(word)  # update wordlist
            self.echo(f'Length: {self.__len__()}')
        else:
            self.echo(f'You can\'t remove \"{word}\" !')

    def clear(self):
        self.echo('Clear list and back to default?')
        ans = input('Y/n/c | Default: Yes').lower().strip()
        if ans in ['', ' ', 'y', 'yes']:
            self.address = './'  # back to default address
            self.filename = 'WordList.txt'  # default filename
            self.words = self.exceptions = []  # Clear wordlist
            self.echo('Done.')
        elif ans in ['n', 'no']:
            self.echo('Process suspended.')
        elif ans in ['c', 'clear']:
            self.words = self.exceptions = []  # Clear wordlist
            self.echo('wordlist cleared.')
        else:
            self.echo('Invalid input: Process canceled.')

    def info(self):
        fn = ['data', 'file', 'exist', 'delay(secs)', 'str2list(data)', 'list2str(data)', 'duplicate(data)',
              'question(quest,answer)', 'echo(self, value)', 'import_list(self)',
              'export_list(self)', 'extend_list(self)', 'new_list(self)', 'delete_list(self)', 'read(self)',
              'add_word(self, word)', 'add_words(self, words)', 'remove_word(self,word)', 'clear(self)',
              'info(self)']
        self.echo(f'- WordList Functions (Total:{len(fn)})')
        print(self.list2str(['WordList.' + _name for _name in fn]))
