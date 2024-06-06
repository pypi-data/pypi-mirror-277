import copy 

class utils():



    @staticmethod
    def append_records_to_section_dict(section_dict: dict[str: list[dict]], records_dict: dict[str: dict]):
        """
        #### Inputs: 
            -@section_dict: dict => {section header: list of records}
            -@records_dict: dict => {section header: record for that section}
        #### Expected Behaviour: 
            -for each key in the records_dict, append the value to the same key in the section_dict
        #### Returns: 
            -None
        #### Side-Effects: 
            -section_dict values will be appended to 
        #### Exceptions: 
            -None
        """
        
        for key, value in records_dict.items():
            if type(value) == dict:
                section_dict[key] = section_dict.get(key, []) + [value]

    
    @staticmethod
    def create_csv_header_list(input_dict_list: list[dict])->list:
        """ Tested
        #### Input:
            -@input_dict_list: list of dicts 
        #### Expected Behaviour: 
            - loops through each dict in the list, adding its keys to a set
            - then the set is turned to a list and returned
        #### Return: 
            - list[]; of unique values 
        #### Side-Effects: 
            - None
        #### Exceptions:
            - None
        """
        header_set = set()
        for current_dict in input_dict_list:
            header_set.update(current_dict.keys())
        return(list(header_set))

        
    def add_to_dict(main_dict: dict, adding_dict: dict, overwrite_duplicate_keys: bool =True):
        """ Tested
        #### Input: 
            -@main_dict: dict to update 
            -@adding_dict: dict with items to add to main_dict
            -@overwrite_duplicate_keys: if true will overwrite values in shared keys, otherwise will 
            create a new key, 'key_i' where i is an integer not already present
        #### Expected Behaviour: 
            - loop through the adding_dict, attempt to add each item to the main dict,
            if overwriting is allowed just write directly each item,
            - if overwriting is not allowed, any key clashes are incremented in the _i suffix until
            the key is unique 
        #### Returns:
            - None 
        #### Side Effects: 
            - modifies main_dict 
        #### Exceptions: 
            - None 
        """
        for adding_key, adding_value in adding_dict.items():
            if not overwrite_duplicate_keys and adding_key in main_dict:
                i = 2
                while f'{adding_key}_{str(i)}' in main_dict:
                    i+=1 
                main_dict[f'{adding_key}_{str(i)}'] = adding_value
            else:
                main_dict[adding_key] = adding_value

    @staticmethod
    def get_in_nested_dict(input_dict: dict, key_to_find: str, default_return_val=None): 
        """ Tested
        #### Input: 
            -@input_dict: nested dict you want to find a key in 
            -@key_to_find: the key you want to find
            -@default_return_val: the value to return if key is not found
        #### Expected Behaviour: 
            - Essentially .get() in a nested dictionary. If it exists returns the value, else returns default_return_val
        #### Returns: 
            - value found saved in key within dict, or default_return_val 
        #### Side Effects: 
            - None 
        #### Exceptions: 
            - None 
        """
        if key_to_find in input_dict:
            return(input_dict.get(key_to_find))
        else:
            for value in input_dict.values():
                if type(value) == dict:
                    resp = utils.get_in_nested_dict(value, key_to_find)
                    if resp != None: #required as [] is not the same as None, we want type to be accurate in return
                        return(resp)
        return(default_return_val)


    def chain_access_locate(input_dict: dict, key_to_find: any) -> tuple[str, list[any]]: 
        """ Tested
        #### Input: 
            -@input_dict: nested dict to locate in
            -@key_to_find: any type key
        #### Expected Behaviour: 
            -using breadth-first search find key_to_find anywhere in the nested dict, building up
            the accessor_list and returning the value and the accessor_list if found
        #### Returns:
            -[0]: the value if found 
            -[1]: the chain of values used to access it 
        #### Side Effects: 
            - None 
        #### Exceptions: 
            - None 
        """
        def locate(in_dict: dict, in_key: str, accessor_list: list):
            for key, value in in_dict.items():
                if key == in_key:
                    return(value, accessor_list+[key])
                elif type(value) == dict:
                    resp = locate(value, in_key, accessor_list + [key])
                    if resp[1]: #if there are any values in the chain it has been located
                        return(resp)
            return(None, [])
        resp = locate(in_dict=input_dict, in_key=key_to_find, accessor_list=[])
        return(resp)

    @staticmethod
    def chain_access_get(input_dict: dict, chain: list):
        """ Tested
        #### Inputs: 
            -@input_dict: nested dict to get value from
            -@chain: list of keys, each one level deeper than the previous
        #### Expected Behaviour:
            - the list is popped from and the value used as an accessor in input_dict, 
            - recursively call on the result, popping and using the value to move deeper into the 
            nesting until the end of the chain, the last value is returned 
        #### Return:
            - the value found at the end of chain
        #### Side Effects: 
            - None 
        #### Exceptions: 
            - 'Missing Link!...' if key in chain isn't found 
            - 'chain too long!...' if nesting runs out and chain still has length
        """
        current_key = chain.pop(0)
        val = input_dict.get(current_key)
        if not val:
            raise Exception(f'Missing Link! key "{current_key}" not found at expected level')
        if len(chain) == 0:
            return(val)
        elif len(chain) and type(val) != dict:
            raise Exception(f'chain too long! value at key "{current_key}" is not a dict') 
        else:
            return(utils.chain_access_get(val, chain))
    
    @staticmethod
    def chain_access_delete(input_dict: dict, chain: list) -> dict:
        """ Tested
        #### Inputs:
            -@input_dict: a nested dict
            -@chain: a list of values, if > 1 will use the value to access the next level 
            of nesting, if = 1 then delete the key
        #### Expected Behaviour: 
            - pop the first value from the list, if it's not in the dict return
            - if it is in the dict and it's not the last value in the list, use it as an accessor
            to go deeper into the nesting 
            - if it's in the dict and the last value in the list, delete the key 
            - if its in the dict, not the last value, and you can't go deeper in nesting, raise exception
        #### Return: 
            - None
        #### Side Effects: 
            - Modifies input_dict
        #### Exceptions: 
            - 'chain too long!...' if chain has further keys and no dicts to nest into 
        """
        def chain_delete(in_dict: dict, in_chain: list):
            current_key = in_chain.pop(0)
            if current_key not in in_dict:
                return()
            elif len(chain) == 0:
                del(in_dict[current_key])
            elif len(chain) and type(in_dict[current_key]) != dict: 
                raise Exception(f'chain too long! end of nesting reached at "{current_key}"') 
            else:
                chain_delete(in_dict[current_key], in_chain)
        chain_delete(input_dict, chain)
    

    @staticmethod
    def spread_items(input_dict: dict, spread_dict: dict):
        """ Tested
        #### Inputs: 
            -@input_dict: a dict with keys being section names
            -@spread_dict: a dict where keys are to spread with values stored in them
        #### Expected Behaviour: 
            - for each value in the input dict; add the items in the spread_dict 
        #### Returns: 
            - None 
        #### Side Effects: 
            - modifies input_dict 
        #### Exceptions: 
            - None
        """
        for val in input_dict.values():
                for key, value in spread_dict.items(): 
                    val[key] = value
        


    @staticmethod
    def replace_between(text: str, start_string: str, end_string:str, to_replace: str, replace_with:str) -> str: 
        """ Tested
        #### Inputs:
            -@text: The superset of text to work within 
            -@start_string: string that delimits the start of the section you want to replace within
            -@end_string: string that delimits the end of the section you want to replace within
            -@to_replace: string which instances of will be replaced
            -@replace_with: string which will replace the to_replace instances
        #### Expected Behaviour: 
            - the text is partitioned to work between start_string and end_string (text_in), and then 
            replace is called on this. Then the text_in is placed back into the text it was inside, and 
            the enter text is returned 
        #### Return: 
            - str: text variable with replacements 
        #### Side-Effects: 
            - None 
        #### Exceptions: 
            - None
        """
        if start_string not in text or end_string not in text:
            return(text)
        first_partition = text.partition(start_string)
        text_before = first_partition[0] + first_partition[1]
        text_in = first_partition[2]
        second_partition = text_in.partition(end_string)
        text_after = second_partition[1] + second_partition[2]
        text_in = second_partition[0]
        text_in = text_in.replace(to_replace, replace_with)
        return(text_before + text_in + text_after)

 





