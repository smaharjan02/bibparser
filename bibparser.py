import argparse
import re
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bwriter import BibTexWriter
  
#filters bibtex with keywords key only
def bibtex_with_key(bibtex_dictlist):
    newDict_list = []
    i = 0
    key = 'keywords'
    while i < len(bibtex_dictlist):
        if(key in bibtex_dictlist[i]):
            newDict_list.append(bibtex_dictlist[i])
        i +=1
    return newDict_list

#filter desired keywords in the bibtex 
def bibtex_filter(bibtex_dictlist,keywords):
    bibtex_keywordlist= []
    final_bibtex = []
    key = 'keywords'
    l=0
    #print(len(bibtex_dictlist))
    while l < len(bibtex_dictlist):
        if key in bibtex_dictlist[l]:
            bibtex_keywordlist.append(bibtex_dictlist[l])
            final_bibtex.append(bibtex_dictlist[l])
        l +=1
    #print("bibtex with key list: ", len(bibtex_keywordlist))
    #print("Final bibtex: ", len(final_bibtex))
    n=0
    while n < len(bibtex_keywordlist):
        for line in bibtex_keywordlist[n][key]:
            final_bibtex[n][key] = bibtex_keywordlist[n][key].replace(line,line.replace(';',','))
        result = keywords.findall(final_bibtex[n][key])

        if(result):   
            for line in result:
                all_str = ','.join(result)
                final_bibtex[n][key] = final_bibtex[n][key].replace(final_bibtex[n][key],all_str)
        else:
            final_bibtex[n][key] = final_bibtex[n][key].replace(final_bibtex[n][key],' ')
        #print("New Dict keywords: ",final_bibtex[n][key])
        n += 1
    return final_bibtex

def empty_keywords_remove(filtered_bibtex):
    i = 0
    key = 'keywords'
    while i <len(filtered_bibtex):
        #print(filtered_bibtex[i][key])
        if(filtered_bibtex[i][key] == ' '):
            #print("It is empty")
            filtered_bibtex[i].pop(key)
        i+=1
    return filtered_bibtex


def read_write_bibtex(input_bibtex_file,output_bibtex,keywords):

    with open(input_bibtex_file, encoding="utf-8" ) as bibtex_file: #bibtex file Parsed
        bib_database = bibtexparser.load(bibtex_file)
    dict_list = bib_database.get_entry_list()
    
    bibtex_list = bibtex_with_key(dict_list)

    filtered_bibtex = bibtex_filter(bibtex_list,keywords)

    filter_emptykey = empty_keywords_remove(filtered_bibtex)

    db = BibDatabase()
    for line in filter_emptykey:
        db.entries.append(line)
    writer = BibTexWriter()

    with open(output_bibtex, 'w', encoding="utf-8") as bib_file:
        bib_file.write(writer.write(db))

def argparse_bibtex():
    keywords_strings = []
#Initialize the parser
    parser=argparse.ArgumentParser()
    parser.add_argument("-ib", "--input_bibtex_file", help ="input bibtex file", required=True)
    parser.add_argument("-ob", "--output_bibtex_file", help ="output bibtex file", required=True)
    parser.add_argument("-k", "--keywords_file", help ="keywords file", required=True)

#parse the arguments
    args=parser.parse_args()
    input_bibtex_file = args.input_bibtex_file
    output_bibtex = args.output_bibtex_file
    keywords_file = args.keywords_file
    
    with open(keywords_file) as file:
        for line in file:
            keywords_strings.append(line.strip())
#keywords to look for in the bibtex_library
    keyword_string ='|'.join(keywords_strings)
    keywords = re.compile(keyword_string)

    read_write_bibtex(input_bibtex_file,output_bibtex,keywords)

if __name__ == '__main__':
   argparse_bibtex()
