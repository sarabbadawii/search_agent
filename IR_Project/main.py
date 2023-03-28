# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from nltk import word_tokenize
from nltk.corpus import stopwords
from Tokenization import Tokenization






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    docslist = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt', '7.txt', '8.txt', '9.txt', '10.txt']
    b=Tokenization
    index_list={}
    index_list=b.get_p_index(docslist)
    print(index_list)
    query=input("please enter the query: ")
    result=b.process_query(query ,index_list)
    print(result)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
