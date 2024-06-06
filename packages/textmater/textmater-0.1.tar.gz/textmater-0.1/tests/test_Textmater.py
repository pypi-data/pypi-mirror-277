from Textmater import Textmater
from unittest import TestCase
import os 
import tempfile
import json
import csv
class test_Textmater(TestCase):

    ### --- write_results_to_json tests
    def test_write_results_to_json_empty(self):
        """
        #### Function: 
            -Textmater.write_results_to_json
        #### Inputs: 
            -self.section dict is empty
        #### Expected Behaviour:
            - the output folder is made, but with nothing to iterate over in the 
            section_dict, nothing is written to it 
        #### Assertions: 
            - the file list after is the same as before + 'output_json', 
            - the 'output_json' folder is empty
        """
        resource = Textmater()
        with tempfile.TemporaryDirectory() as tempdir:
            os.chdir(tempdir)
            starting_file_list = os.listdir(os.getcwd())
            resource.write_results_to_json()
            resulting_file_list = os.listdir(os.getcwd())
            assert(starting_file_list + ['output_json'] == resulting_file_list)
            inside_output_folder = os.listdir(f'{os.getcwd()}/output_json')
            assert(inside_output_folder == [])

    def test_write_result_to_json(self):
        """
        #### Function: 
            - Textmater.write_results_to_json
        #### Inputs; 
            - self.section_dict has 2 keys with dicts as values
        #### Expected Behaviour:    
            - self.section_dict is looped through, the 2 keys result in 2 files 
            being written 'key1.json' and 'key2.json'. They have the contents of the value 
            dumped into them
        #### Assertions: 
            - The 2 expected files are written to
            - the contents of the files matches the values in the section_dict,
            and have filenames corresponding to section keys
        """
        resource = Textmater()
        resource.section_dict = {
            'key1': [{'inner1': 'value_1',
                  'inner2': 'value_2'},
                  {'inner1': 'value_1',
                   'inner2' : 'value_2'}],
            'key2': [{'inner3': 'value_1',
                      'inner4': 'value_2'},
                     {'inner3': 'value_1',
                      'inner4': 'value_2'}]
        }
        with tempfile.TemporaryDirectory() as tempdir:
            os.chdir(tempdir)
            resource.write_results_to_json()
            os.chdir('output_json')
            output_file_list = os.listdir(os.getcwd())
            assert output_file_list == ['key1.json', 'key2.json']
            with open('key1.json', 'r') as r1:
                r1_dict = json.load(r1)
                assert(r1_dict == resource.section_dict['key1'])
            with open('key2.json', 'r') as r2:
                r2_dict = json.load(r2)
                assert(r2_dict == resource.section_dict['key2'])


    ### --- write_results_to_csv tests
    def test_write_results_to_csv_empty(self):
        """
        #### Function: 
            - Textmater.write_results_to_csv
        #### Inputs:
            - self.dict_list is empty
        #### Expected Behaviour:
            - No csv is output 
        #### Assertions:
            - file list after execution is same as before
        """
        resource = Textmater()
        with tempfile.TemporaryDirectory() as tempdir:
            os.chdir(tempdir)
            starting_file_list = os.listdir(os.getcwd())
            resource.write_results_to_csv()
            resulting_file_list = os.listdir(os.getcwd())
            assert(starting_file_list + ['output_csv'] == resulting_file_list)
            inside_ouput_folder = os.listdir(f'{os.getcwd()}/output_csv')
            assert(inside_ouput_folder == [])

    
    def test_write_results_to_csv(self):
        """
        #### Function: 
            - Textmater.write_results_to_csv
        #### Inputs: 
            - self.section_dict has entries
        #### Expected Behaviour: 
            - CSV is output, with headers corresponding to keys in section_dict,
            and rows corresponding to dicts found in the the dict_list value 
        #### Assertions:
            - output csvs read back into a dict_reader correspond to the dict_lists 
            found in the dict section_dict values, with empty values in keys that were added
            from the create_headers_from_dict_list call
        """
        resource = Textmater()
        resource.section_dict = {'section_1': [{'inner_key_1': 'inner_value_1', 'inner_key_2': 'inner_value_2'},
                                               {'inner_key_1': 'inner_value_3', 'inner_key_3': 'inner_value_3'}],
                                 'section_2': [{'inner_key_3': 'inner_value_4', 'inner_key_4': 'inner_value_5'},
                                               {'inner_key_3': 'inner_value_6', 'inner_key_5': 'inner_value_7'}] }
        with tempfile.TemporaryDirectory() as tempdir:
            os.chdir(tempdir)
            resource.write_results_to_csv()
            os.chdir('output_csv')
            with open('section_1.csv', 'r') as r1:
                reader1 = csv.DictReader(r1)
                result_1 = []
                expected_1 = [{'inner_key_1': 'inner_value_1', 'inner_key_2': 'inner_value_2', 'inner_key_3': ''},
                               {'inner_key_1': 'inner_value_3', 'inner_key_2': '', 'inner_key_3': 'inner_value_3'}]
                for row in reader1:
                    result_1.append(row)
                assert(result_1 == expected_1)
            with open('section_2.csv', 'r') as r2:
                reader2 = csv.DictReader(r2)
                result_2 = []
                expected_2 = [{'inner_key_3': 'inner_value_4', 'inner_key_4': 'inner_value_5', 'inner_key_5': ''},
                              {'inner_key_3': 'inner_value_6', 'inner_key_4': '', 'inner_key_5': 'inner_value_7'}]
                for row in reader2:
                    result_2.append(row)
                assert(result_2 == expected_2)


    #### --- line_reader tests
    def test_line_reader_base_case(self):
        """
        #### Function: 
            - Textmater.line_reader
        #### Inputs:
            -@current_line = 'testing_string',
            i.e string that does not have the delimiter present in it 
        #### Expected Behaviour: 
            1. Delimiter count == 0
            2. Falls to base case of else: and returns the input string
        #### Assertions:
            - The returned value is the same as the input value
        """
        resource = Textmater()
        input_string = 'testing'
        resp = resource.line_reader(input_string)
        assert resp == input_string
    
    def test_line_reader_count_1_non_empty_value(self):
        """
        #### Function: 
            Textmater.line_reader
        #### Inputs:
            - current_line = 'testing_key:testing_value',
            i.e string that has the delimiter present and a value after the delimiter
        #### Expected Behaviour:
            1. Delimiter count == 1
            2. enters first if statement
            3. makes partition
            4. value is found after partition, so returns a dict with a single key-value pair,
            the key == 'testing_key' and the value == 'testing_value'
        #### Assertions:
            - Returned value == {'testing_key' : 'testing_value'}
        """
        resource = Textmater()
        resp = resource.line_reader('testing_key:testing_value')
        assert resp == {'testing_key': 'testing_value'}

    def test_line_reader_count_1_empty_value(self):
        """
        #### Function: 
            - Textmater.line_reader
        #### Input/s: 
            - current_line = 'testing_key: \n',
            i.e string that has the delimiter present and no non-whitespace characters after
        #### Expected Behaviour:
            1. Delimiter count == 1
            2. enters first if statement 
            3. makes partition
            4. no value is found after the partition so a dict is returned with a single key-value pair,
            the key == 'testing_key', value is ''
        #### Assertions: 
            - returned value == {'testing_key: ''}
        """
        resource = Textmater()
        resp = resource.line_reader('testing_key: \n')
        assert resp == {'testing_key': ''}

    def test_line_reader_count_2(self):
        """
        #### Function: 
            - Textmater.line_reader
        #### Inputs:
            -@current_line = 'testing_outer': 'testing_inner' : 'inner_value'
        #### Expected Behaviour: 
            1. Delimiter count == 2 
            2. recursive call to return {'testing_inner': 'inner_value'}
            3. returns {'testing_outer' : {'testing_inner': 'inner_values'}}
        #### Assertions:
            - return value == {'testing_outer' : {'testing_inner': 'inner_value'}}
        """
        resource = Textmater()
        input_value = 'testing_outer: testing_inner :inner_value'
        resp = resource.line_reader(input_value)
        expected_value = {'testing_outer': 'testing_inner :inner_value'}
        assert resp == expected_value

    ### --- check_rear_mirror tests
    def test_check_rear_mirror(self):
        """
        #### Function: 
            - Textmater.check_rear_mirror
        #### Inputs: 
            -@text: example_text with delimiters on each line, one line with 2 
        #### Expected Behaviour: 
            - the lines are split and read through in reverse, the first line being testing3...
            this line and all above it have a delimiter in it so they result in key value pairs in the 
            returned dict. 
            - the second line has 2 delimiters so only the first is used to separate key and value, the second 
            delimiter becomes part of the string 
        #### Assertions: 
            - returned dict is as expected
        """
        example_text = """
Testing1:
Testing2: TestingInner1: TestingValue
Testing3: value2
                        """
        resource = Textmater()
        resp = resource.check_rear_mirror(example_text)
        expected_response = {
            'Testing1': '',
            'Testing2': 'TestingInner1: TestingValue',
            'Testing3': 'value2'}
        assert resp == expected_response

    def test_check_rear_mirror(self):
        """
        #### Function: 
            - Textmater.check_rear_mirror
        #### Inputs: 
            -@text: example_text with 2 lines lacking delimiters 
        #### Expected Behaviour: 
            - the lines are split and read in reverse. The first line has no delimiter so it's carried 
            up to the one above, which does have a delimiter. The line after that again has no delimiter so it's 
            carried up. This results in 2 keys in the returned dict
        #### Assertions: 
            - returned dict is as expected
        """
        resource = Textmater()
        example_text = """
Testing1: value1
Testing 2
Testing 3: value2
Testing 4
"""
        resp = resource.check_rear_mirror(example_text)
        expected_response = {'Testing1': 'value1Testing 2', 'Testing 3': 'value2Testing 4'}
        assert(resp == expected_response)


    ### --- drive tests
    def test_drive_spread_keys_empty(self):
        """
        #### Function:
            - Textmater.drive
        #### Inputs: 
            -@text: text with 2 sections and 3 keys in each
            - section_headers: ['section 1', 'section 2']
            - spread_items: [('section 1', 'not_found')] (a key that isn't found)
        #### Expected Behaviour: 
            - the text is split into its sections of the record_dict
            - the spread item key 'not_found' isn't found in 'section 1' so it throws an exception
        #### Assertions: 
            - the expected exception is thrown
        """
        example_text = 'section 1\nkey1:value1\nkey2:value2\nkey3:\nvalue3section 2\nkey4:value4\nsolokey:value5\nkey6:\nvalue6'
        spread_items = [('section 1', 'not_found')]
        resource = Textmater(spread_keys=spread_items, section_header_list=['section 1', 'section 2'])
        with self.assertRaises(Exception) as context:
            resource.drive(example_text)
        assert(str(context.exception) == 'Attempt to spread empty value for key "not_found"')

    def test_drive_spread_keys_section(self):
        """
        #### Function: 
            - Textmater.drive
        #### Inputs:
            -@text: text with 2 sections and 3 keys in each
            - section_headers: ['section 1', 'section 2']
            - spread_items: [('section 1', 'key1'), ('section 2', 'key4'), ('','solokey')]
        #### Expected Behaviour: 
            - the text is split into its sections of the record_dict
            - the first spread_item collects the value in key1 of section1 and spreads it to the other section
            same with key4 of section2 being spread. The final spread_item has no section specified so the solokey is found 
            in the second section and spread to the first
        #### Assertions: 
            - the returned dict has the expected items spread across the sections
        """
        example_text = 'section 1\nkey1:value1\nkey2:value2\nkey3:\nvalue3section 2\nkey4:value4\nsolokey:value5\nkey6:\nvalue6'
        spread_items = [('section 1', 'key1'), ('section 2', 'key4'), ('','solokey')]
        resource = Textmater(spread_keys=spread_items, section_header_list=['section 1', 'section 2'])
        resource.drive(example_text)
        expected_section_dict = {
            'section 1': [{'primary_key': '0', 'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'solokey': 'value5'}],
            'section 2': [{'primary_key': '0', 'key1': 'value1', 'key4': 'value4', 'solokey': 'value5', 'key6': 'value6'}]
        }
        assert(resource.section_dict == expected_section_dict)

    def test_drive_cleanup_functions(self):
        """
        #### Function:
            - Textmater.drive
        #### Inputs: 
            -@text: text with one section and 3 keys inside
            - cleanup_functions: 2 functions, the first replaces 'a' characters with 'b' in values,
            the second deletes items with 'b' in the value. both of these are only acting on the sections, the nested dict
        #### Expected Behaviour: 
            - after the section_dict is filled, the first function replaces 1 value
            - the second cleanup function deletes the 2 items with b in the value
        #### Assertions: 
            - The second dict has the 1 section with one item in it and the pkey
        """
        input_text = 'test1\nkey1:valuea\nkey2: valueb\nkey3:gluec'
        def cleanup_function_1(input_dict):
            for inner_dict in input_dict.values():
                for key, value in inner_dict.items():
                    inner_dict[key] = value.replace('a', 'b')
            return(input_dict)
        
        def cleanup_function_2(input_dict):
            for inner_dict in input_dict.values():
                delete_keys = []
                for key, value in inner_dict.items():
                    if('b' in value):
                        delete_keys.append(key)
                for each in delete_keys:
                    del(inner_dict[each])
            return(input_dict)

        resource = Textmater(section_header_list=['test1'], cleanup_functions=[cleanup_function_1, cleanup_function_2])
        resource.drive(input_text)
        expected_section_dict = {'test1': [{'key3': 'gluec', 'primary_key': '0'}]}
        assert(resource.section_dict == expected_section_dict)

    def test_drive_cleanup_functions_exception(self):
        """
        #### Function:
            - Textmater.drive
        #### Inputs: 
            -@text: text with one section and 3 keys inside
            - cleanup_functions: 1 function it doesn't return anything
        #### Expected Behaviour: 
            - after the section_dict is filled, the first cleanup function returns None which trips the exception
        #### Assertions: 
            - The expected exception is raised
        """
        input_text = 'test1\nkey1:valuea\nkey2: valueb\nkey3:gluec'
        def cleanup_function_1(input_dict):
            for inner_dict in input_dict.values():
                continue

        resource = Textmater(section_header_list=['test1'], cleanup_functions=[cleanup_function_1])
        with self.assertRaises(Exception) as context:
            resource.drive(input_text)
        assert(str(context.exception) == 'cleanup function returned None, ensure functions return a dict of dicts')


    def test_drive_sections_skipped_notfound(self):
        """
        #### Function:
            - Textmater.drive
        #### Inputs: 
            @text: example string which contains 'test1' but not 'test2'
            - section_headers: ['test1', 'test2']
            - sections_to_skip: ['test1']
        #### Expected Behaviour:    
            - The first section is in the sections to skip, so it's skipped,
            - The second section isn't present at all in the text so it doesn't create an entry in the section_dict
        #### Assertions: 
            - the section_dict has no entries
        """
        example_string = 'test1\nkey1: value1, \nother things'
        resource = Textmater(section_header_list=['test1', 'test2'], sections_to_skip=['test1'])
        resource.drive(example_string)
        assert(resource.section_dict == {})

    def test_drive_section_header_duplicate_exception(self):
        """
        #### Function:
            - Textmater.drive
        #### Inputs: 
            -@text: '' (text isn't read before the exception if no filter or transform function passed in)
            - section_headers, ['test1', 'test2', 'test1'] (1 duplicated)
        #### Expected Behaviour: 
            - duplicate headers will match the condition of the len(section_headers) check and raise the exception.
            All code before this is skipped because the only paramater passed in is the header_list
        #### Assertions: 
            - the expected exception is raised 
        """
        with self.assertRaises(Exception) as context:
            resource = Textmater(section_header_list=['test1', 'test2', 'test1'])
            resource.drive('example text')
        assert(str(context.exception) == 'Duplicate section headers found. If non-eronious fix by transforming text to remove duplicate')

    def test_drive_section_header_regex(self):
        """
        #### Function: 
            - Textmater.drive
        #### Inputs: 
            -@text: text with 2 _word_ instances to be recognised as section_headers. 
        #### Expected Behaviour:
            - the section_header_regex of '_[a-zA-Z]*_' is used to identify 2 headers. 
            - the text within them is then used to retrieve a key and value 
            - these are then added to the section_dict under their section_header 
        #### Assertions: 
            - the section_header dict has the two keys 
        """
        regex_pattern = '_[a-zA-Z]*_'
        example_text = '_headerA_\nkeyA : valueA\n keyB : valueB\n _HeaderB_ \n keyC: valueC\nkeyD: valueD'
        expected_dict = {
            '_headerA_': [{'keyA': 'valueA', 'keyB': 'valueB', 'primary_key': '0'}],
            '_HeaderB_': [{'keyC': 'valueC', 'keyD': 'valueD', 'primary_key': '0'}]
        }
        resource = Textmater(section_header_regex=regex_pattern)
        resource.drive(example_text)
        assert(resource.section_dict == expected_dict)

    def test_drive_transformation_functions(self):
        """
        #### Function: 
            - Textmater.drive
        #### Inputs:
            -@text: with 2 key value lines,
            -transformation_function which turns 'hat' into 'dog'
            -transformation_function which turns 'dog' into 'mouse'
        #### Expected Behaviour: 
            - The first transformation function turns the 'hat' string in example_text into 'dog',
            - the second transformation function turns the (now 2) 'dog' substrings into 'mouse'
            - then the fields are extracted and returned in non-section dict 
        #### Assertions: 
            - the non-section dict value is {'example' : 'mouse', 'test': 'dog', 'primary_key': '0'}
        """
        example_text = '''example : hat 
test: dog'''
        def transformation_function_1(input_text):
            return(input_text.replace('hat', 'dog'))
        def transformation_function_2(input_text):
            return(input_text.replace('dog', 'mouse'))
        
        resource = Textmater(transformation_functions=[transformation_function_1, transformation_function_2])
        resource.drive(example_text)
        print(resource.section_dict)
        expected_dict = {'example': 'mouse', 'test': 'mouse', 'primary_key': '0'}
        assert(resource.section_dict['non-section'] == [expected_dict])

    def test_drive_filter_functions(self):
        """
        #### Function: 
            - Textmater.drive
        #### Inputs:
            -2 calls 
            -@text 1st call has the word 'fail' in it, 
            -@text 2nd call does not have the word fail in it
            - self.filter_functions has 2 functions, one to return true at all times,
                one to return false if the text has the word 'fail' in it 
        #### Expected Behaviour: 
            - drive called on example_text_1 will proceed through the filter functions and add a dict to self.dict_list
            - drive called on example_text_2 will not pass the second filter function and return nothing
        #### Assertions:
            - the first call is not filtered out and as it's non-sectional the only item found is 
            added to the non-section key in the section_dict, and a primary key is added
            - the second call is filtered out and doesn't affect the section_dict at all 
        """
        example_text_1 = "not : here"
        example_text_2 = "fail here"
        def filter_function_1(input_text):
            return True
        
        def filter_function_2(input_text):
            return('fail' not in input_text)
        
        resource = Textmater(filter_functions=[filter_function_1, filter_function_2])
        resource.drive(example_text_1)
        expected_dict = {'not': 'here', 'primary_key': '0'}
        assert(resource.section_dict['non-section'] == [expected_dict])
        resource.drive(example_text_2)
        assert(resource.section_dict['non-section'] == [expected_dict])


    ### __init__ tests
    def test__init__header_exception(self):
        """
        #### Function: 
            - Textmater.__init__
        #### Inputs:
            -@section_header_list: ['test1', 'test2', 'test3']
            -@section_header_regex: '_[a-zA-Z]*_'
        #### Expected Behaviour: 
            - Because the section_header_list and section_header_regex are both set, 
            the exception is thrown 
        #### Assertions: 
            - the expected exception is thrown 
        """
        with self.assertRaises(Exception) as context:
            resource = Textmater(section_header_list=['test1', 'test2', 'test3'], section_header_regex='_[a-zA-Z]*_')
        assert(str(context.exception) == 'section_header_regex and section_headers should not be used together')




   




        
        