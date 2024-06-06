"""
Don't need to know where I'm goin' , just need to know where I've been
"""
import re
import os
import copy
import json
import csv
from .utils import *
from typing import Union


class Textmater:
    """
    Package for extracting data from text that has known patterns or sections to it, for example; 
    key: value 
    or 
    key: 
    value
    
    called textmater because actually run through the pages in reverse order. Like driving in reverse
    
    """
    #tested     
    def __init__(self,  filter_functions: list = [],
                        transformation_functions: list = [], 
                        section_header_regex: str = '',  
                        section_header_list: list[str] = [], 
                        sections_to_skip: list[str] = [], 
                        cleanup_functions: list = [],
                        overwrite_duplicate_keys: bool = True,
                        spread_keys = [],
                        delimiter: str = ':'):
                    
        """
        #### Inputs: All optional
            -@filter_functions: List of functions applied for filtering out a text in order to skip the drive function,
                all must take in text and return a bool, True = continue, False = skip this text 
            -@transformation_functions: List of functions that are applied to the text before it is scanned, 
                all must take a string and return one
            -@section_header_regex: Regex pattern to find section headers. 
            -@section_headers: List of section headers. Only use this if header_regex is NOT being used
            -@sections_to_skip: List of section headers that if present will be ignored in the output, meaning any text found within them is skipped over. 
            -@cleanup_functions: List of functions that are applied to all records before adding them to the section_dict: 
                                - they need to take in a dict {<section header> : {dict of items in it}} and return the same, 
                                don't worry it does the deepcopy for you! 
            -@overwrite_duplicate_keys: If set to false will generate a unique version of any key that is already present when trying to 
                add to the return dict. It will add _i where i is an integer, starting at 2 
            -@spread_keys: list of tuples, keys that you want shared between all sections:
                [0]: section name
                [1]: key 
                if no section is provided (''), looks anywhere in dict for it 
        """
        #note the section_header 'non-section' will be used for any data found outside sections or if there are no sections
        self.section_dict = {}
        self.filter_functions = filter_functions
        self.transformation_functions = transformation_functions
        self.section_header_regex = section_header_regex
        self.section_headers = section_header_list
        self.sections_to_skip = sections_to_skip
        self.cleanup_functions = cleanup_functions
        self.overwrite_duplicate_keys = overwrite_duplicate_keys
        self.primary_count = 0 
        self.spread_keys = spread_keys
        self.delimiter = delimiter

        if section_header_regex and section_header_list:
            raise Exception('section_header_regex and section_headers should not be used together')
    


   
        




    def drive(self, text: str):
        """
        #### Input: 
            -@text: str
        #### Expected Behaviour: 
            - apply in order there operations on the text: 
            - run all filter_functions over the text, if any return false skip this text
            - run all transformation_functions over the text, each modifying it 
            - identify section headers either through section_header_regex or sections_headers
            - running in reverse over each section, partition the text using between the current 
            header and the next. run check_rear_mirror on teach section of text 
            and add the returned dict to the current_record_dict 
            - spread the values stored in spread_keys across all sections 
            - spread the primary key across all sections 
            - add the current_record_dict to the section_dict
        #### Return: 
            - None 
        #### Side Effects: 
            - self.section_dict is updated
        #### Exceptions: 
            - Duplicate secti...: raised if section headers contain duplicates
            - cleanup functio...: raised if cleanup function returns none 
            - Attempt to spre...: raised if spread_key isn't found 
        """
        current_record_dict = {}
        for filter_function in self.filter_functions:
            if not filter_function(text):
                return
            
        for transformation_function in self.transformation_functions:
            text = transformation_function(text)
        if self.section_header_regex:
            self.section_headers = re.findall(self.section_header_regex, 
                                                text, flags=re.MULTILINE)
        if(len(self.section_headers) > len(set(self.section_headers))):
           raise Exception('Duplicate section headers found. If non-eronious fix by transforming text to remove duplicate')
        
        flipped_section_headers = self.section_headers[::-1] #flip the section headers to read in reverse order
        remaining_text = text
        for section_header in flipped_section_headers:
            partition_using_header = remaining_text.partition(section_header)
            remaining_text = partition_using_header[0]
            if section_header in self.sections_to_skip: #skip after partitioning so remaining_text is set
                continue
            section_text = partition_using_header[2]
            if not section_text: #means the section header wasn't found 
                continue
            section_data = self.check_rear_mirror(section_text)
            if type(section_data) == dict: 
                if(not current_record_dict.get(section_header), None):
                    current_record_dict[section_header] = {}
                utils.add_to_dict(main_dict=current_record_dict[section_header],
                                  adding_dict=section_data,
                                  overwrite_duplicate_keys=self.overwrite_duplicate_keys)
        if remaining_text:
            section_data = self.check_rear_mirror(remaining_text)
            if type(section_data) == dict:
                current_record_dict['non-section'] = {}
                utils.add_to_dict(main_dict = current_record_dict['non-section'],
                                  adding_dict = section_data,
                                  overwrite_duplicate_keys = self.overwrite_duplicate_keys)
        for cleanup_function in self.cleanup_functions:
            current_record_dict = cleanup_function(copy.deepcopy(current_record_dict))
            if(current_record_dict == None):
                raise Exception('cleanup function returned None, ensure functions return a dict of dicts')

        spread_dict = {'primary_key': str(self.primary_count)}
        print(current_record_dict)
        for spread_key in self.spread_keys:
            if spread_key[0] == '':
                value = utils.get_in_nested_dict(input_dict=current_record_dict, key_to_find=spread_key[1]) 
            else:    
                value = current_record_dict.get(spread_key[0]).get(spread_key[1])##this throws an error if the first key isn't found
            if not value: 
                raise Exception(f'Attempt to spread empty value for key "{spread_key[1]}"')
            spread_dict[spread_key[1]] = value
        utils.spread_items(input_dict=current_record_dict, spread_dict=spread_dict) 
        utils.append_records_to_section_dict(self.section_dict, current_record_dict)
        self.primary_count +=1


    def check_rear_mirror(self, text: str, delimiter: str = ':') -> dict[str, str]:
        """
        #### Input: 
            -@text: str 
            -@delimiter: str, used to seperate keys from values. Defaults to ':'
        #### Expected Behaviour: 
            - split the text into lines, run through the lines in reverse, attempting 
            to split them into keys and values using line_reader. If any line doesn't contain a 
            delimiter it gets carried up to the line before it. 
            - each item found is added the returned dict
        #### Return: 
            - dict: {keys before delimiter: values after delimiters}
        #### Side Effects: 
            - None 
        #### Exceptions: 
            - None
        """
        current_lines = [x for x in text.split('\n') if x.strip() != '']
        return_dict = {}
        carry = ''
        for i in range(len(current_lines)-1,-1, -1):
            current_line = current_lines[i] + carry
            returned_value = self.line_reader(current_line, delimiter)
            if type(returned_value) == dict:
                utils.add_to_dict(main_dict=return_dict,
                                  adding_dict=returned_value,
                                  overwrite_duplicate_keys=self.overwrite_duplicate_keys)
                carry = ''
            else:
                carry = returned_value
        return(return_dict)

    
    def line_reader(self, current_line: str, delimiter: str = ':') -> Union[str, dict[str, str]]:
        """
        #### Input:
            -@current_line: 
            -@delimiter: str, used to separate keys from values. Anything before it is a key, 
            after is a value, str, defaults to ':'
        #### Expected Behaviour: 
            - if the delimiter is found in the current_line, return 
            a dict with one element {text before the delimiter: text after delimiter}
            - if delimiter is not found, return the current_line
        #### Return: 
            - str: the current line spat back at you 
            - OR
            - dict: {current_line before delim: current_line after delim}
        #### Side-Effects
            - None
        #### Exceptions: 
            - None
        """
        delimiter_count = current_line.count(delimiter)
        if delimiter_count >= 1:
            current_partition = current_line.partition(delimiter)
            # print(current_partition)
            return({current_partition[0].strip(): current_partition[2].strip()})
        else:
            return(current_line)
    
            
    def write_results_to_csv(self, output_folder: str = 'output_csv'):
        """ Tested
        #### Input: 
            -@output_folder: str; path to save files in
        #### Expected Behaviour: 
            - 
        Writing the extracted data to csv, one csv per section
        As well as the errors 

        It's no longer using a dict list, it needs to use the section_dict 
        """
        if output_folder not in os.listdir():
            os.mkdir(output_folder)
        for filename, dict_list in self.section_dict.items():
            header_list = utils.create_csv_header_list(dict_list) 
            with open(f'{output_folder}/{filename}.csv', 'w') as w:
                writer = csv.DictWriter(w, header_list)
                writer.writeheader()
                writer.writerows(dict_list)
          

    def write_results_to_json(self, output_folder: str = 'output_json'):
        """ Tested
        #### Input: 
            -@output_folder: str; path to save files in 
        #### Expected Behaviour: 
            - read self.section_dict. For each section 
        #### Return: 
            - None 
        #### Side Effects: 
            - writes json files to the output_json path 
        #### Exceptions: 
            - None
        """
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
        for section_name, dict_list in self.section_dict.items():
            with open(f'{output_folder}/{section_name}.json', 'w') as w:
                w.write(json.dumps(dict_list))
        

                        

    
