#!/usr/bin/python
#input file schema:
#'dev/file.txt' 'oldPhrase' 'newPhrase'


class InputFileReader:
    ''' Class: InputFileReader
    Read input file, which is given as an argument to constructor.
    Stores data from input file as a list: data_container
    Stores input file name as string: input
    '''
    def __init__(self, file_name):
        '''Constructor. Argument(s): file_name'''
        self.input = file_name
        self.data_container = list()

    def read_file(self):
        '''Reading file line by line. Splitting each line to make a list from every element of line.
        Later these lists are added to main list (data_container)
        Argument(s): none'''
        input_file_handler = open(self.input)
        for line in input_file_handler:
            tmp_list = list()
            tmp_line = line.split()
            for element in tmp_line:
                tmp_list.append(element[1:-1])
            self.data_container.append(tmp_list)

    def get_container(self):
        '''Returns data_container (list)
        Argument(s): none'''
        return self.data_container

    def print_container(self):
        '''Prints data_container (list)
        Argument(s): none'''
        for element in self.data_container:
            print(element)


class Replacer:
    ''' Class: Replacer
    Constructor takes as an argument(s): path to file, phrase to replace and new phrase.
    file_path -- string
    phrase_old -- string
    phrase_new -- string
    Case sensitive.
    '''
    def __init__(self, file_path, old_phrase, new_phrase):
        '''Constructor.
        Argument(s): file_path, old_phrase, new_phrase'''
        self.path = file_path
        self.phrase_old = old_phrase
        self.phrase_new = new_phrase

    def replace(self):
        '''Replace function. Read lines from file, then checking each line if that contains searched phrase.
         If contains, split line, replace element, checking if element is whole phrase or contains prefix or suffix.
         Later connect line, add it to file. If phrase is not in line, just add a line to string.
         After that save new content to the same file (overwrite its content)
         Argument(s): none'''
        try:
            old_file_handler = open(self.path, 'r')
            old_content = old_file_handler.readlines()
            old_file_handler.close()
            new_content = ""
            for line in old_content:
                print(line)
                if line.find(self.phrase_old) > -1:
                    print('Ping #1')
                    new_line = ""
                    tmp_line = line.split()
                    for element in tmp_line:
                        if self.phrase_old in element:
                            phrase_start_position = element.find(self.phrase_old)
                            if phrase_start_position == 0 and len(element) == len(self.phrase_old):
                                new_line += self.phrase_new
                            elif phrase_start_position > 0:
                                new_line += element[0:phrase_start_position] + self.phrase_new
                                if (phrase_start_position + len(self.phrase_old)) < len(element):
                                    new_line += element[phrase_start_position+len(self.phrase_old): len(element)+1]
                        else:
                            new_line += " " + element
                    new_content += new_line + '\n'
                    continue
                new_content += line
            new_file_handler = open(self.path, 'w')
            new_file_handler.write(new_content)
            new_file_handler.close()
        except IOError as error:
            print(error)


class ReplaceManager:
    ''' Class: ReplaceManager
    Constructor takes as an argument(s): list of replace tasks.
    container -- list - contains 3 element lists inside each element
    '''
    def __init__(self, input_list):
        '''Constructor.
        Argument(s): input_list (list)'''
        self.container = input_list

    def replace_paths(self):
        '''Replace every replacing task given in input file.
        Argument(s): none'''
        for element in self.container:
            tmp_replace = Replacer(element[0], element[1], element[2])
            tmp_replace.replace()


class Controller:
    ''' Class: Controller
    Constructor takes as an argument(s): input_name
    input_name -- string - contains name of input file
    Case sensitive.
    Filename extension sensitive.
    '''
    def __init__(self, input_name):
        self.input_controller = InputFileReader(input_name)
        self.input_controller.read_file()
        self.input_controller.print_container()
        self.manager = ReplaceManager(self.input_controller.get_container())
        self.manager.replace_paths()


def main(input_name):
    Controller(input_name)


if __name__ == "__main__":
    import sys
    main((sys.argv[1]))
