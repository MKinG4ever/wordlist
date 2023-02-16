import random
import time
import os
from functools import wraps


def exe_time(func):
    """
        execution time, decorator
        author: NightFox | exe_time Beta v0.1
        e-mail: mking4everking@gmail.com
        git-hub: @MKing4ever
        GNU Open-Source Certification
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        _start = time.time()
        result = func(*args, *kwargs)
        _end = time.time()
        _total = _end - _start
        print(f'ET: {_total:.3}')
        return result

    return wrapper


class WordList:
    """
        WordList Handler Script
        author: NightFox | wordlist Beta v0.3
        e-mail: mking4everking@gmail.com
        git-hub: @MKing4ever
        GNU Open-Source Certification
    """

    # type of 'words' and 'exceptions' changed to set()
    # added: speed and version Variables.
    # removed: duplicate Function.

    def __init__(self):
        # lists
        self.words = {'password', 'passwd', 'pass'}  # set | my wordlist
        self.exceptions = {' ', ''}  # set | my exceptions wordlist
        # file address
        self.address = './'
        self.filename = 'WordList.txt'
        # about
        self.speed = 0  # delay time for echo
        self.version = 'v0.3'  # script version

    def __repr__(self):
        return f'WordList Module {self.version}\nLength: {self.__len__()}\nBackup: {self.exist}\nAddress: {self.file}'

    def __str__(self):
        return self.list2str(self.data)

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    @property
    def data(self):
        self.words.update(self.exceptions)  # exceptions can not add easily
        return self.words

    @property
    def file(self):
        return self.address + self.filename  # ./WordList.txt

    @property
    def exist(self):
        return os.path.isfile(self.file)  # if "./WordList.txt" file & exist

    @staticmethod
    def delay(secs=None):
        """make an interrupt"""
        if secs is None:
            time.sleep(random.random() ** 5 / 3.141592653589793238)
        else:
            time.sleep(secs)

    @staticmethod
    def str2list(data: str) -> list:
        return data.split()  # split with ' '-(Space) and '\n'-(NewLine)

    @staticmethod
    def list2str(data: list or set) -> str:
        return '\n'.join(data)  # make a True wordlist | merge words with '\n'-NewLine

    @staticmethod
    def question(quest, answer):
        """make sure answer is not ''(empty str) or just ' '(spaces)"""
        a = input(quest).strip()
        if a and a != answer:
            answer = a
        return answer

    def echo(self, value: str):
        """print, write, type, echo... this function have many names"""
        for line in value.split('\n'):  # support multi-line text
            chars = ''
            for char in line:
                chars += char
                print(f'\r{chars}', end='')
                if char != ' ':  # skip Spaces
                    self.delay(self.speed)
            print('')  # NewLine

    @exe_time
    def import_list(self):
        if self.exist:
            with open(self.file, 'r') as file:
                data = self.str2list(file.read())
                self.words.update(data)
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
        self.words.update(data)  # update wordlist
        self.echo(f'Length: {self.__len__()}')

    @exe_time
    def add_words(self, words: list):
        w = [f'{i}' for i in words]
        self.words.update(w)  # update wordlist
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
        if ans in ['', 'y', 'yes']:
            self.address = './'  # back to default address
            self.filename = 'WordList.txt'  # default filename
            self.words = {}  # Clear wordlist
            self.exceptions = {' ', ''}
            self.echo('Done.')
        elif ans in ['n', 'no']:
            self.echo('Process suspended.')
        elif ans in ['c', 'clear']:
            self.words = {}  # Clear wordlist
            self.exceptions = {' ', ''}
            self.echo('wordlist cleared.')
        else:
            self.echo('Invalid input: Process canceled.')

    def info(self):
        fn = ['data', 'file', 'exist', 'delay(secs)', 'str2list(data)', 'list2str(data)',
              'question(quest,answer)', 'echo(self, value)', 'import_list(self)',
              'export_list(self)', 'extend_list(self)', 'new_list(self)', 'delete_list(self)', 'read(self)',
              'add_word(self, word)', 'add_words(self, words)', 'remove_word(self,word)', 'clear(self)',
              'info(self)']
        self.echo(f'- WordList Functions (Total:{len(fn)})\n')
        print(self.list2str(['WordList.' + _name for _name in fn]))
        self.echo('for more information use \'help()\', \'dir()\' or __dir__ Built-in Functions')
