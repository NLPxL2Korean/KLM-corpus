# -*- coding: utf-8 -*-

"""
Modified on June 21, 2023

This is a Python code for converting the L2-NIKL morpheme annotation xml file into conllu format file and preprocessing the data
Anonymized and streamlined for review
"""

'''
prep: import packages need for preprocessing
'''
from xml.etree import ElementTree as ET
import pandas as pd
from lxml import etree

import os
import unicodedata as ud

import re

def remove_empty_value(lst):
    '''
    This function takes an input and removes empty values (e.g., white space)
    included in the list

    Parameters: lst

    Returns: list values joined by "+" symbol with empty values all removed 
    (Korean morphemes and corresponding POS tags are joined by "+")
    '''
    result = "+".join(word.strip() for word in lst if word.strip())
    return result

def parse_xml(xml_string):
    '''
    This function parses XML string and extracts necessary information 
    (including word, text, lemma, pos, morpheme) to create a dictionary
    with keys (FORM, LEMMA, XPOS)

    Parameters: xml_string 

    Returns: lst of sentences as dictionaries with relevant keys
    '''
    root = ET.fromstring(xml_string)

    sentences = []
    for sentence in root.findall(".//SENTENCE"):
        sentence_text = sentence.find("s").text
        morph_annotations = sentence.find("MorphemeAnnotations")
        words = []
        for word in morph_annotations.findall("word"):
            w = word.find("w").text
            morphs = word.findall("morph")
            tok = [m.text for m in morphs]
            tok = [remove_empty_value(tok)]
            pos = [m.attrib["pos"] for m in morphs]
            pos = [remove_empty_value(pos)]          
            morph= [(m.text, m.attrib["pos"]) for m in morphs]
            words.append({"FORM": w, "LEMMA": tok, "XPOS": pos})
        sentences.append({"sentence": sentence_text, "words": words})
    return sentences

def dic_to_dataframe(input):
    '''
    This function converts list of dics to dataframe

    Parameters: lst of dics with keys (FORM, XPOS, LEMMA)

    Returns: dataframe (with values from each input dics)
    '''
    output_list = []
    for dl in input:
        extracted_dict = {}
        extracted_dict['FORM'] = dl['FORM']
        extracted_dict['XPOS'] = dl['XPOS']
        extracted_dict['LEMMA'] = dl['LEMMA']
        resp_df = pd.DataFrame.from_dict(extracted_dict)
        output_list.append(resp_df)
    df1 = pd.concat(output_list, ignore_index=True)
    
    return(df1)

def convert_dataframe_to_conllu(df, conllu_str=''):
    '''
    This function convers dataframe to CoNLL-U format

    Parameters: dataframe, conllu_str(str)-frame to append lines to

    Returns: str-final lines appended with necessary datas from dataframe 
    in the CoNLL-U format
    '''
    line_num = 1
    for i in df.index:
        row = df.loc[i]
        conllu_str += str(line_num) + '\t'
        conllu_str += str(df.loc[i, 'FORM']) + '\t'
        conllu_str += str(df.loc[i, 'LEMMA']) + '\t'
        conllu_str += df.loc[i, 'XPOS'] + '\t'
        conllu_str += '\n'
        line_num += 1
    conllu_str += '\n'           
    return conllu_str

def extract_id(file):
    '''
    This function extracts ID (metadata) 

    Parameter: (xml)file

    Returns: str (extraced information, combined)
    '''
    tree = ET.parse(file)
    root = tree.getroot()

    header = root.find("Header")
    sample_seq = header.find("SampleSeq").text
    source_type = header.find("SourceType").text
    AssignmentType = header.find("AssignmentType").text
    AssignmentGenre = header.find("AssignmentGenre").text
    AssignmentTheme = header.find("AssignmentTheme").text
    learner_info = header.find("LearnerInfo")
    data_grade = learner_info.find("DataGrade").text
    Nationality = learner_info.find("Nationality").text

    id = str(sample_seq) + "_" + str(source_type) + "_" + str(AssignmentType) + "_" + str(AssignmentGenre) + "_" + str(AssignmentTheme) + "_" + str(data_grade) + "_" + str(Nationality)
    return id

def dataframe_to_save(df, file, conllu_str=''):
    '''
    This function converts dataframe to a CoNNL-U format string

    Parameters: 
    dataframe (containing morpheme annotations)
    file (file path used to extract metadata)
    conllu_str (optional string lines to append)

    Returns:
    str
    '''
    for i in df.index:
        conllu_str += '# text_id = ' + str(extract_id(file)) + '\n'
        conllu_str += '# sent = ' + df.loc[i, 'sentence'] + '\n'
        conllu_str += df.loc[i, 'conllu'] 
    return conllu_str


def check_conllu_file(file_path):
    '''
    This function checks a given CoNLL-U file whether sentence includes Korean characters, 
    has a '# text (sentence) line', and if there is only one sentence in the file 
    (i.e., title of the file) without any content, the file is skipped

    Parameters: file_path (CoNLL-U file path)

    Returns: bool
    '''
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    sent_counter = 0
    has_text_line = False

    for i, line in enumerate(lines):
        # detect non-Korean characters/alphabets
        line = ''.join(c for c in line if 'HANGUL' in ud.name(c, '')) 
        if line.strip() == "":
            if not has_text_line:
                print(f"Sentence {sent_counter} # text missing")
            sent_counter += 1
            has_text_line = False
        elif line.strip().startswith("# text"):
            has_text_line = True

    # check the last sentence (need to catch/check/remove)
    if not has_text_line:
        print(f"Sentence {sent_counter} doesn't have a '# text' line.")

    # check the file (presumably containing only the title)
    if sent_counter == 1:
        print(f"File {file_path} needs to be checked.")
        return False

    return True


def extract_punctuation_and_pos(line):
    '''
    This function extracts the sentence-final punctuation marks, which is the
    last token in a line of a CoNNL-U file. If the token contains a punctuation
    mark at the end, this function extacts it and its corresponding POS tag
    and modifies the token and POS tag in the next line.

    Parameters: str (a line from CoNNL-U file)

    Returns: tuple (extracted token, tag)
    '''
    columns = line.strip().split('\t')

    # Extract the last token and POS tag
    last_token, pos_tag = columns[2], columns[4]

    token_parts = last_token.split('+')
    pos_tag_parts = pos_tag.split('+')

    # Check whether its a sentence-final punctuation mark
    if re.match(r'[.!?]', token_parts[-1]):
        punctuation, punctuation_pos_tag = token_parts[-1], pos_tag_parts[-1]
        token_parts = token_parts[:-1]
        pos_tag_parts = pos_tag_parts[:-1]
    else:
        pass

    columns[1] = ''.join(token_parts)
    columns[2] = '+'.join(token_parts)  
    columns[4] = '+'.join(pos_tag_parts)

    return columns, (punctuation, punctuation, "_", punctuation_pos_tag)

def process_conllu(input_filename, output_filename):
    '''
    This function modifies CoNLL-U file with tokenizing the sentence-final tokens/tags

    Parameters: 
        input_file_name
        output_file_name
    '''
    with open(input_filename, 'r') as f, open(output_filename, 'w') as outf:
        for line in f:
            if line.startswith("#"):
                outf.write(line)
                continue

            elif line.strip() == "":
                outf.write(line)
                continue

            columns = extract_punctuation_and_pos(line)
            new_line = "\t".join(columns)
            outf

def cleaning_conllu(input_filename, output_filename):
    '''
    This function cleans a CoNLL-U file with following operations:
    - Fills empty columns with "_".
    - Removes blank text paragraphs
    - Removes danggling sent id
    - Extracts blank text lines
    - Removes double lines
    - Exclude sentences without sentence-final punctuation marks
    - Remove one token responses

    Parameters:
        input_file_name
        output_filename
    '''

    with open(input_filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        line = line.rstrip('\n')  # remove unnecessary newline character 

        if line.startswith("#") or line == "":  # skip comment lines and empty lines
            new_lines.append(line + '\n')
            continue

        # Fill empty columns (training file requires strict format)
        columns = line.split('\t')
        while len(columns) < 10: 
            columns.append("_")
        new_lines.append('\t'.join(columns) + '\n')

    # Identify paragraphs to be removed
    remove_paragraph_indices = []
    current_paragraph_index = 0
    for i, line in enumerate(new_lines):
        stripped = line.strip()
        if stripped.startswith("# text =") and len(stripped) == len("# text ="):
            remove_paragraph_indices.append(current_paragraph_index)
        if line == "\n":  
            current_paragraph_index = i + 1

    # Remove blank text paragraphs
    final_lines = [new_lines[i] for i, line in enumerate(new_lines) if not any(i >= paragraph_index and (i+1 >= len(new_lines) or new_lines[i+1] == "\n") for paragraph_index in remove_paragraph_indices)]

    # Remove one token responses, sentences without sentence-final punctuation marks, and mismatched morphemes/POS tags
    i = 0
    while i < len(final_lines):
        if final_lines[i].startswith('# sent_id =') and i + 2 < len(final_lines):
            sentence_line = final_lines[i + 2]
            morphemes = sentence_line.split('\t')[2].split('+')  
            pos_tags = sentence_line.split('\t')[4].split('+')  
            tokens = sentence_line.split('\t')[1] 
            if len(tokens.split()) == 1 or not tokens[-1] in ('.', '!', '?') or len(morphemes) != len(pos_tags): 
                del final_lines[i:i + 3]  
            else:
                i += 3 
        else:
            i += 1  

    # Remove orphan sent IDs and double lines
    i = 0
    while i < len(final_lines):
        line = final_lines[i]
        if line.startswith('# sent_id'):
            if i < len(final_lines)

    # Remove consecutive empty lines
    final_lines = [final_lines[0]]
    for i in range(1, len(final_lines)):
        if final_lines[i].strip() == '' and final_lines[i-1].strip() == '':
            continue
        final_lines.append(final_lines[i])

    # Write the processed lines to the output file
    with open(output_filename, 'w', encoding="utf-8") as f:
        f.writelines(final_lines)

    return

