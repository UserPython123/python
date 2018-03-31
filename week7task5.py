# -*- coding: utf-8 -*-
"""
Created on 

@author: 
"""

sentence1 = input("Enter first sentence: ")
sentence2 = input("Enter second sentence: ")

newSentence = sentence1 + sentence2
print("New sentence: ", newSentence)

words = newSentence.split(" ")
print("The words here are: ",words)
words.sort()
print("The sorted words are: ",words)

print("Number of words in ",newSentence,": ", len(words))
tpl = tuple(words)
dict = {}
for eachWord in tpl:
    dic = dict.fromkeys(tpl,tpl.count(eachWord))   #to count the occurance of each word 
            
print(str(dict))


