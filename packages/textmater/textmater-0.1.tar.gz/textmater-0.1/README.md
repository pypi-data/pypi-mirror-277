# Textmater

### Don't need to know where you're going, just need to know where you've been 
Extract structured data (key values, grouped into sections) from text. (Runs backwards through text.. hence the name)
Useful for creating configurations for extracting data from a file, which can then be applied to large numbers of these documents. 

## Overview
The general application of this is to construct a configuration of the Textmater class that pulls details out of a format of text. 
This configuration can then be fed further instances of the text and build up a structure of data, which can then be saved to .json or .csv 

## Example
Say we have an example of text like this 

example_text = 
> -Shops-  
> Pete's: Grocers  
> KFC: Fast Food  
> Newsman: Newsagents  
> -Sports-  
> Football: Round Ball  
> AFL: Egg Ball  
> Cricket:Round Ball  

and we want to get every key and value, with keys being anything before a : and values being anything after :.
We also want them to be grouped according to their headers, and we want the output in json
We could create an instance with 

```resource = Textmater(section_header_regex = '_[a-zA-Z]*_')```

then run 
```resource.drive(example_text)```
the resulting resource.section_dict would look like this 
```
{
    '-Shops-': [{"Pete's": "Grocers", "KFC": "Fast Food", "Newsman": "Newsagents"}]
    '-Sports-': [{"Football": "Round Ball", 'AFL": "Egg Ball", "Cricket" : "Round Ball"}]
}
```
If you ran it again on a similarly formatted section of text, '-Shops-' list would be appended to, as would '-Sports-'

then ```resource.write_results_to_json()``` would save it as a json file. One file per section (key in the section_dict)

## importing
``` from textmater import Textmater, tools```

(tools is optional but has useful functions for working with text)

## configuring and running 
```resource = Textmater()```
will instantiate the class, there are a lot of options here. Ones relating to functions run in order of appearance.All are optional
- __filter_functions__: **[function]** takes a list of functions used to skip (or not) an instance of text passed in, each must take in a string and return true or false. E.g you pass in a function that returns false if 'denied' is present in the text anywhere. Then when you run drive this resource over a corpus of documents you can skip the ones with 'denied' in them. 
- __transformation_functions__: **[function]** takes a list of functions that are applied to transform the incoming text before further processing. Functions must take a string and return a string
- __section_header_regex__: **str(regex_pattern)** 1st of 2 ways of specifying section headers. Provided pattern is run through the text to build the list of headers. Not to be used in conjunction with the next argument
- __section_header_list__: **[str]** 2nd of 2 ways of specifying section headers. Direct values that if found in the text will be used to divide items found in the text. In the example, the same effect could have been achieved by passing in ['-Shops-', '-Sports-'] to this parameter instead 
- __sections_to_skip__: **[str]** list of sections headers that if found will promp Textmater to skip over the values in the section. Useful for improving output when there is a large section of a text you don't require the contents of. 
- __cleanup_functions__: **[function]** list of functions applied to each record before it is added to the section_dict. Must take a [current_record_dict](#current_record_dict) (\<section header\>: {dict of items within it}) and return the same. No need to make deepcopies as this is done automatically before passing the dict in. 
- __overwrite_duplicate_keys__: **bool** If set to false will generate a unique version of any key that is already present when trying to add to the current_record_dict. It will add _i where i is an integer, starting at 2. In the unlikely occassion \<key\>_i is also a collision, it increments i until it's not 
- __spread_keys__: **[(str, str)]** list of tuples representing keys in sections that you want to spread (e,g you find a value in one section and want it present in all of them, perhaps as an identifier). 
[0]: section name 
[1]: key 
example, you have a key 'patient id' in a section 'identifiers', you want this id shared across all the sections to use as a primary key. Your value for spread_keys would be [('identifiers', 'patient id')].   
If you don't know the section that a key is in but you still want to spread it if it's found, leaving the section name empty, which would look like ('', 'patient id'), will result in Textmater searching for the key across all sections then spreading it. 
- delimiter: **str** the character/s you want to use as delimiters between keys and values. 



## Appendix 

#### current_record_dict: 
a dict where keys are section headers and values are dicts of items in that section: 
```
{
    'section 1': {'key1' : 'value1', 'key2': 'value2', 'primary_key': '0'},
    'section 2': {'other key 1': 'value 1', 'other key 2': 'value 2', 'primary_key': '0'} 
}
```
resource.current_record_dict stores the result of the most recent extraction in this format

#### section_dict: 
dict for storing combined current_record_dicts. keys are section headers and values are lists of dicts
```
{
    'section 1' : [{'key1' : 'value1', 'key2': 'value2', 'primary_key': '0'},
                {'key1' : 'value3', 'key2': 'value4', 'primary_key': '1'}],
    'section 2' : [{'other key 1' : 'value 1', 'primary_key': '0'},
                    {'other key 1': 'value z', 'primary_key': '1'}] 
}
```
resource.section_dict stores this 



