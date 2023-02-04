import random
import time
import os


class WordList:
    """
        WordList Handler Script
        author: NightFox | wordlist Beta v0.2
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
            time.sleep(random.random() / 3.1415926535)

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
        a = input(quest)
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

    def import_list(self):
        if self.exist:
            with open(self.file, 'r') as file:
                data = file.read()
                self.words.extend(self.str2list(data))
            self.echo(f'File \'{self.filename}\' imported.')
        else:
            self.echo(f'No \'{self.filename}\' Found.')

    def export_list(self):
        self.echo(f'File \'{self.filename}\' {"already exist." if self.exist else "not exist."}')
        with open(self.file, 'w') as file:
            file.write(self.list2str(self.data))
        self.echo(f'File \'{self.filename}\' exported.')

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

    def read(self):
        data = [f"[{k:{len(str(self.__len__()))}}] | \'{v}\'" for k, v in enumerate(self.data)]
        print(self.list2str(data))
        self.echo('-   -   ' * 5 + f'\nLength: {self.__len__()}')

    def add_word(self, word: str):
        data = self.str2list(word)  # list | turn  str (input argument) to list
        self.words.extend(data)  # update wordlist
        self.echo(f'Length: {self.__len__()}')

    def remove_word(self, data: str):
        if data in self.words:
            self.words.remove(data)  # update wordlist
            self.echo(f'Length: {self.__len__()}')
        else:
            self.echo(f'You can\'t remove \"{data}\" !')

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
