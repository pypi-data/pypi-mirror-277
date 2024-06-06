from Textmater.utils import utils
from unittest import TestCase
import copy 
class test_utils(TestCase):

    ### --- replace_between tests
    def test_replace_between(self):
        """
        #### Function: 
            -utils.replace_between
        #### Inputs: 
            -@text: an example string  
            -@start_string: a string found in text
            -@end_string: a string found in text after start string
            -@to_replace: a string found several times in between start_string and end_string
            -@replace_with: '+'
        #### Expected Behaviour:
            - The returned string returns with the instances of to_replace replaced with replace_with values
        #### Assertions:
            - The returned string matches expected output
        """
        example_string = """
key1: val1 key2: val2
key3: val3
key4: val4
"""     
        expected_output = """
key1: val1 key2= val2
key3= val3
key4: val4
"""
        resp = utils.replace_between(example_string, 'key1:', 'key4:', ':', '=')
        assert resp == expected_output

    def test_replace_between_not_present(self):
        """
        #### Function: 
            -utils.replace_between
        #### Inputs:
            -@text: an example string 
            -@start_string: a string not found in example_string
            -@end_string: a string found in example_string
            -@to_replace: a string found in example_string
            -@replace_with: a string found in example_string
        #### Expected Behaviour:
            - Because start_string is not found in example_string, return the input text 
        #### Assertions:
            - the returned string matches @text input
        """
        example_string = 'testing 1 text here, , ,and 2 here'
        resp = utils.replace_between(text=example_string, start_string='unavailable', end_string='2', to_replace=',', replace_with='.')
        assert(resp == example_string)

    ### --- spread_primary_key tests
    def test_spread_item(self):
        """
        #### Function: 
            -utils.spread_item
        #### Inputs:
            -@input_dict: 2d dict, values are dicts 
            -@spread_dict: a dict with 3 items in it 
        #### Expected Behaviour: 
            -the values of input_dict are looped through, for each one the items 
            of spread_dict are added
        #### Assertions:
            - the values in input_dict all have the items of spread_dict inside them 
        """
        in_dict = {'key1': {'test1': 't1'}, 'key2': {'test2': 't2'}}
        spr_dict = {'newkey1': 'newval1', 'newkey2': 'newval2', 'newkey3': 'newval3'}
        utils.spread_items(input_dict=in_dict, spread_dict=spr_dict)
        assert(in_dict['key1']=={'test1': 't1', 'newkey1': 'newval1', 'newkey2': 'newval2', 'newkey3': 'newval3'})
        assert(in_dict['key2']=={'test2': 't2', 'newkey1': 'newval1', 'newkey2': 'newval2', 'newkey3': 'newval3'})

       
    ### --- chain_access_delete tests
    def test_chain_access_delete_missing(self):
        """
        #### Function:
            -utils.chain_access_delete
        #### Inputs:
            -@input_dict: a 3d dict, some values are dicts
            -@chain: a list of keys, the second isn't present in the second layer of nesting
        #### Expected Behaviour:
            -The first chain item is present in the input_dict, so it recurses and tries to use the next 
            chain item in the value retrieved. It is not present so the function returns. 
            No deletion has been made and the returned list is the same as the input 
        #### Assertions: 
            -The returned dict has the same items as the input
        """
        input = {'key1': 'value1',
                      'key2': {'inner2': 'value2'},
                      'key3': {'inner3': {'inner4': 'value3'},
                               'inner32': 'value32'}}
        input_check = copy.deepcopy(input)
        input_chain = ['key2', 'nothing']
        utils.chain_access_delete(input_dict=input, chain=input_chain)
        assert(input == input_check )

    def test_chain_access_delete_found(self):
        """
        #### Function: 
            -utils.chain_access_delete
        #### Inputs:
            -@input_dict: a 3d dict, some values are dicts
            -@chain: a list of keys, the first is present in input_dict, the second is present in 
            the value saved in the first
        #### Expected Behaviour: 
            -the first chain item is present in the input_dict, so it recurses and tries to use the chain
            item in the value retrieved. This is present and the list is empty after the item was popped, so
            it deletes the key
        #### Assertions: 
            -the key was deleted from the nested dict
        """
        input = {'key1': 'value1',
                      'key2': {'inner2': 'value2'},
                      'key3': {'inner3': {'inner4': 'value3'},
                               'inner32': 'value32'}}
        input_chain = ['key2', 'inner2']
        expected_result = {'key1': 'value1',
                      'key2': {},
                      'key3': {'inner3': {'inner4': 'value3'},
                               'inner32': 'value32'}}
        utils.chain_access_delete(input_dict=input, chain=input_chain)
        assert(input == expected_result)

    def test_chain_access_delete_not_found(self):
        """
        #### Function:
            -utils.chain_access_delete
        #### Inputs: 
            -@input_dict: a 3d dict, some values are dicts
            -@chain: a list of keys, the first item is present in input_dict, the value is a dict
            but the second chain item is not in the value dict
        #### Expected Behaviour: 
            -the first chain item is found and the value dict is entered, passing it into chain_delete
            and passing the remaining chain (with 1 item) in. The second item isn't found in the dict 
            so it returns without having deleted anything 
        #### Assertions:
            -the dict passed in is returned unchanged
        """
        input = {'key1': 'value1',
                      'key2': {'inner2': 'value2'},
                      'key3': {'inner3': {'inner4': 'value3'},
                               'inner32': 'value32'}}
        input_check = copy.deepcopy(input)
        input_chain = ['key2', 'key_none']
        utils.chain_access_delete(input_dict=input,chain=input_chain)
        assert(input == input_check)

    def test_chain_access_delete_too_long(self):
        """
        #### Function: 
            -utils.chain_access_delete
        #### Inputs:
            -@input_dict: a 3d dict, some values are dicts
            -@chain: a list of 3 keys
        #### Expected Behaviour: 
            - the first and second keys are found in order but the second value is not a dict 
            so can't be passed to chain_delete, it raises an exception
        #### Assertions: 
            - the expected exception is raised 
        """
        input = {'key1': 'value1',
                      'key2': {'inner2': 'value2'},
                      'key3': {'inner3': {'inner4': 'value3'},
                               'inner32': 'value32'}}
        input_chain = ['key2', 'inner2', 'too_long']
        with self.assertRaises(Exception) as context:
            utils.chain_access_delete(input_dict=input, chain=input_chain)
        assert(str(context.exception) == 'chain too long! end of nesting reached at "inner2"')

        
    #--- chain_access_get tests
    def test_chain_access_get_found(self):
        """
        #### Function: 
            - utils.chain_access_get
        #### Inputs:
            -@input_dict: a nested dict
            -@chain: a list with the first element found in the outer dict, second element found in 
            the nested dict
        Excpected Behaviour:
             - the first link is found at the first level, which makes a recursive call, 
             which returns the value found at the second level
        Assertions:
            - returned value is as expected
        """
        example_dict = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': {'inner1': 'innerval1',
                     'inner2': 'innerval2'}
        }
        resp = utils.chain_access_get(example_dict, ['key3', 'inner2'])
        assert resp == 'innerval2'

    def test_chain_access_get_not_found(self):
        """
        #### Function: 
            - utils.chain_access_get
        #### Inputs:
            -@dict: a nested dict
            -@chain: a chain with the first link found in the first level but the second link not found
        #### Expected Behaviour:
            - the first link is found at the first level,
            makes a recursive call but the second link isn't found, so returns None
        Assertions:
            returned value is none
        """
        example_dict = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': {'inner1': 'innerval1',
                     'inner2': 'innerval2'}
        }
        with self.assertRaises(Exception) as context:
            utils.chain_access_get(example_dict, ['key3','missing'])
        assert(str(context.exception) == 'Missing Link! key "missing" not found at expected level' )

    def test_chain_access_get_chain_too_long(self):
        """
        ##### Function:
            - utils.chain_access_get
        #### Inputs:
            -@input_dict: a nested dict 
            -@chain: a chain of length 2 with the first link found but it returns a non-dict so throws an error
        #### Expected Behaviour:
            - the first link is found but the value is not a dict 
            and the chain still has remaining links so it throws an error
        #### Assertions:
            - expected exception is thrown     
        """
        example_dict = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': {'inner1': 'innerval1',
                     'inner2': 'innerval2'}
        }
        with self.assertRaises(Exception) as context:
            utils.chain_access_get(example_dict, ['key2','missing'])
        assert(str(context.exception) == 'chain too long! value at key "key2" is not a dict' )


 # -- chain_access_locate tests
    def test_chain_access_locate_flat_found(self):
        """
        #### Function:
            - utils.chain_access_locate
        #### Inputs:
            -@input_dict: a 2d dict, no values are dicts
            -@key_to_find that is found within the dict
        #### Expected Behaviour:
            - the key_to_find is found in the dict and returns (value2, ['key1'])
        #### Assertions:
            - The returned tuple has the value, and a list with the key in it
        """
        example_dict = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3'
        }
        resp = utils.chain_access_locate(example_dict, 'key2')
        assert(resp == ('value2', ['key2']))


    def test_chain_access_locate_nested_found(self):
        """
        #### Function: 
            - utils.chain_access_locate
        #### Inputs:
            input_dict that is nested
            a key_to_find that is found in a nested section of the dict
        Expected Behaviour:
            The outer_key results in a recursive call and appends 
            to the _accessor_list, in the nested list the value is found and
            also appends to the _accessor_list the key. 
            This returns ('value', [outer_key, inner_key])
        Assertions:
            The returned value is ('value', ['outer_key', 'inner_key'])
        """
        example_dict = {
            'key1': 'value1',
            'key2': 'value2',
            'outer_key': {
                'inner1' : 'here',
                'inner_key': 'value',
                'inner2': 'here2'
            },
            'key3': 'value3'
        }
        resp = utils.chain_access_locate(example_dict, 'inner_key')
        assert resp[0] == 'value'
        assert resp[1] == ['outer_key', 'inner_key']

    def test_chain_access_locate_nested_not_found(self):
        """
        Function: chain_access_locate
        Input/s:
            input_dict that is nested
            a key_to_find that is not found in the dict
        Expected Behaviour:
            recursive calls are made, all return (None, [])
            results in (None, [] being the final return value)
        Assertions:
            The returned value is (None, [])
        """
        example_dict = {
            'key1': 'value1',
            'key2': 'value2',
            'outer_key': {
                'inner1' : 'here',
                'inner_key': 'value',
                'inner2': 'here2'
            },
            'key3': 'value3'
        }
        resp = utils.chain_access_locate(example_dict, 'not_found')
        assert resp[0] == None
        assert resp[1] == []


    ### --- get_in_nested_dict tests 
    def test_get_in_nested_dict_nested_found(self):
        """
        Function: get_in_nested_dict
        Input/s:
            a nested dictionary
            a key_to_find that is present in the nested dictionary
        Expected Behaviour:
            1. key is found after recurisve call then returned
        Assertions: 
            returned value is as expected
        """
        input_dict = {'key1': {'inner1': {'inner_inner': 'important_value'},
                               'inner2': 'value2'},
                    'key2': 'value3',
                    'key2': {'inner3': 'value4'}}
        resp = utils.get_in_nested_dict(input_dict, 'inner_inner')
        assert resp == 'important_value'

    def test_get_in_nested_dict_nested_not_found(self):
        """
        Function: get_in_nested_dict
        Input/s:
            a nested dictionary
            a key_to_find that is NOT present in the nested dictionary
        Expected Behaviour:
            1. key is not found after recurisve calls
        Assertions: 
            returned value is None
        """
        input_dict = {'key1': {'inner1': {'inner_inner': 'important_value'},
                               'inner2': 'value2'},
                    'key2': 'value3',
                    'key2': {'inner3': 'value4'}}
        resp = utils.get_in_nested_dict(input_dict, 'not_key')
        assert resp == None


    ### --- add_to_dict tests
    def test_add_to_dict_no_overwrite(self):
        """
        Function: add_to_dict
        Input/s: 2 nested dicts, some keys are shared between them,
                overwrite_duplicate_keys = False
        Expected Behaviour: 
            1. key1 in input_dict 2 won't fit in the key1 spot of input_dict_1
            2. is placed in key1_2
            3. key2 in input_dict_2 can only fit in key2_3 of input_dict_1
            4. key4 can go directly in 
        """
        input_dict_1= {
            'key1': 'value1',
            'key2': 'value2',
            'key2_2': 'value6',
            'key3': {'inner1': 'innerval1'}
        }
        input_dict_2 = {
            'key1': 'value3',
            'key2': 'value5',
            'key4': {'inner1': 'innerval1'}
        }
        utils.add_to_dict(input_dict_1, input_dict_2, overwrite_duplicate_keys=False)
        expected_dict = {
            'key1': 'value1',
            'key1_2': 'value3',
            'key2': 'value2',
            'key2_2': 'value6',
            'key2_3': 'value5',
            'key3': {'inner1': 'innerval1'},
            'key4': {'inner1': 'innerval1'}
        }
        assert input_dict_1 == expected_dict

    def test_add_to_dict_overwrite(self):
        """
        Function: add_to_dict
        Input/s: 2 nested dicts, some keys are shared between them 
                overwrite_duplicate_keys = True
        Expected Behaviour: 
            1. key1 clashes, overwrites the input_dict_1 value
            2. key2 clashes, overwrites the input_dict_1 value
            3. key3 does not clash, no overwrite
        """
        input_dict_1= {
            'key1': 'value1',
            'key2': 'value2',
            'key3': {'inner1': 'innerval1'}
        }
        input_dict_2 = {
            'key1': 'value3',
            'key2': 'value5',
            'key4': {'inner1': 'innerval1'}
        }
        utils.add_to_dict(input_dict_1, input_dict_2, overwrite_duplicate_keys=True)
        expected_dict = {
            'key1': 'value3',
            'key2': 'value5', 
            'key3': {'inner1': 'innerval1'},
            'key4': {'inner1': 'innerval1'}
        }
        assert input_dict_1 == expected_dict


    ### --- create_csv_header_list tests
    def test_create_csv_header_list(self):
        """
        #### Function: 
            - utils.create_csv_header_list
        #### Input:
            -@input_dict_list: a list with each item having some overlap with other items' keys
        #### Expected Behaviour: 
            - the list is iterated over and the header_set is updated with the dicts' keys.
            this is then returned as a list
        #### Assertions: 
            - the returned list has all the expected values 
        """
        input_dict_list = [
            {'key1': 'value', 'key2': 'value2', 'key3': 'value3'},
            {'key2': 'value4', 'key3': 'value5', 'key4': 'value5', 'key5': 'value6'},
            {'key4': 'value4', 'key7': 'value7'}
        ]
        resp_list = utils.create_csv_header_list(input_dict_list)
        assert(resp_list.sort() == ['key1', 'key2', 'key3', 'key4', 'key5', 'key7'].sort())


    ### --- append_records_to_section_dict tests
    def test_append_records_to_section_dict(self):
        """
        #### Function: 
            - utils.append_records_to_section_dict
        #### Inputs:
            -@section_dict: a dict with 3 keys
            -@records_dict: a dict with 3 keys corresponding to section_dict keys and one non-shared,
            values are dicts
        #### Expected Behaviour: 
            - the dict values in records_dict are added to the corresponding keys in the section_dict 
            - the one key that isn't shared is created as a new key in the section_dict and appended to its value 
        #### Assertions: 
            - section_dict values have the expected dicts added to them 
        """
        in_section_dict = {'key1': [{'in1': 'val1'}], 'key2': [], 'key3': []}
        in_records_dict = {'key1': {'in2': 'val2'}, 'key2': {'in3': 'val3'}, 'key3': {'in4': 'val4'}, 'key4': {'in4': 'val5'}}
        utils.append_records_to_section_dict(section_dict=in_section_dict, records_dict=in_records_dict)
        expected_dict = {'key1': [{'in1': 'val1'}, {'in2': 'val2'}],
                         'key2': [{'in3': 'val3'}],
                         'key3': [{'in4': 'val4'}],
                         'key4': [{'in4': 'val5'}]}
        assert(in_section_dict == expected_dict)
    
    
 

    





   
    





