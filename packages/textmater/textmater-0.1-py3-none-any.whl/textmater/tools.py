from . import utils
class Tools():


    def __init__(self):
        pass

    @staticmethod
    def remove_delimiters_between(delimiter, delimit_free_keys: list[tuple], text):
        """
        -@delimit_free_keys: List of tuples defining sections of the text that should have their delimiters removed
            - [0] = key defining the start of the text 
            - [1] = key defining the end of the text
            - [2] = str: the delimiter
            - [3] = str: the replacement delimiter 
        """
        for delimit_free_key in delimit_free_keys:
            text = utils.replace_between(text, delimit_free_key[0] + [2], delimit_free_key[1], delimiter, [3])

    def delete_page_features(text: str, eop_delimiter: str = '--EOP--'):
        """
        Method for removing repeated lines of text. Will result in any line that occurs more than once 
        will have all instances removed. 
        Useful if the same text appears at the top of a number of pages
        """
        page_count = 1
        
        return_text = ''
        past_dict = {eop_delimiter: 2}
        current_set = set()
        for line in text.splitlines():
                    
            if f'page {page_count}' in line.lower():
                past_dict[line] = 2

            if line == eop_delimiter:
                page_count +=1 
                for each in current_set:
                    past_dict[each] = past_dict.get(each, 0) + 1
                current_set = set()
            else: 
                current_set.add(line)

        for line in text.splitlines():
            if past_dict.get(line, 0) <= 1:
                return_text += f'{line}\n'

        return(return_text)