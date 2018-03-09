#!/usr/bin/python
#input file schema:
#'dev/file.txt' 'oldPhrase' 'newPhrase'


class InputFileReader:
    '''
    Read input file, which is given as an argument to constructor.
    Stores data from input file as a list: data_container
    Stores input file name as string: input
    '''
    def __init__(self, file_name):
        '''
        Constructor fo class.
        :param file_name: string, name of input file
        '''
        self.input = file_name
        self.data_container = list()

    def read_file(self):
        '''
        Reading file line by line. Splitting each line to make a list from every element of line.
        Later these lists are added to main list (data_container)
        :return: none
        '''
        input_file_handler = open(self.input)
        for line in input_file_handler:
            tmp_list = list()
            tmp_line = line.split('\' \'')
            for element in tmp_line:
                tmp_list.append(self.parse_element(element))
            self.data_container.append(tmp_list)

    def parse_element(self, element):
        '''
        Cutting apostrophe sign from start or from end of string
        :param element: string
        :return: string
        '''
        if element.startswith('\''):
            element = element[1:]
        if element.endswith('\''):
            element = element[0:-1]
        print(element.strip())
        return element.strip()

    def get_container(self):
        '''
        Returns data_container (list)
        :return: data_container, list of lists
        '''
        return self.data_container

    def print_container(self):
        '''
        Prints data_container (list)
        :return: none
        '''
        for element in self.data_container:
            print(element)


class Replacer:
    '''
    Handling one replace task
    '''
    def __init__(self, file_path, old_phrase, new_phrase):
        '''
        Constructor
        :param file_path: string, path to file to rewrite
        :param old_phrase: string, phrase to replace
        :param new_phrase: string, replacement phrase
        '''
        self.path = file_path
        self.phrase_old = old_phrase
        self.phrase_new = new_phrase

    def replace(self):
        '''
        Replace function. Read lines from file, then checking each line if that contains searched phrase.
        If contains, adds [0:start] to tmp_line, later add replacement phrase, and rest of old line
        :return: none
        '''
        try:
            old_file_handler = open(self.path, 'r')
            old_content = old_file_handler.readlines()
            old_file_handler.close()
            new_content = ""
            for line in old_content:
                if line.find(self.phrase_old) > -1:
                    new_line = ""
                    phrase_start_position = line.find(self.phrase_old)
                    new_line += line[0:phrase_start_position]
                    new_line += self.phrase_new
                    phrase_end_position = phrase_start_position + len(self.phrase_old)
                    new_line += line[phrase_end_position:]
                    new_content += new_line
                    continue
                new_content += line
            new_file_handler = open(self.path, 'w')
            new_file_handler.write(new_content)
            new_file_handler.close()
        except IOError as error:
            print(error)


class ReplaceManager:
    '''
    Manage all replace tasks. Tasks are stored as a lists at container (list)
    '''
    def __init__(self, input_list):
        '''
        Constructor.
        :param input_list: list of lists
        '''
        self.container = input_list

    def replace_paths(self):
        '''
        Replace every replacing task given in input file.
        :return: none
        '''
        for element in self.container:
            tmp_replace = Replacer(element[0], element[1], element[2])
            tmp_replace.replace()


class Controller:
    def __init__(self, input_name):
        '''
        Constructor.
        :param input_name: string, name of input file
        '''
        self.input_controller = InputFileReader(input_name)
        self.input_controller.read_file()
        self.manager = ReplaceManager(self.input_controller.get_container())
        self.manager.replace_paths()
        self.print_done_info()

    @staticmethod
    def print_done_info():
        '''
        Static method. Print information about end of all tasks.
        :return: none
        '''
        print('All jobs done!')



def main(input_name):
    Controller(input_name)


if __name__ == "__main__":
    import sys
    main((sys.argv[1]))
