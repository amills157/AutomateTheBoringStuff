#! python3

#randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import re

test = open('C:\\MyPythonScripts\\Test Folder\\1.txt', 'r')
contents = test.read()

expression = input()

testRegex = re.compile(expression)

mo = testRegex.search(contents)

if mo.group() != None:

    print ('Match found: ' + mo.group())

else:
    print ('No match found')
