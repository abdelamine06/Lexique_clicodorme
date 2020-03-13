from fs.Parser import *

parser = Parser()
#features = parser.parse("[pos:verb, lexeme:manger, tense:present, mode:indicative, subject:<[person:3, number:sg]|[person:3, number:sg]>]")
features = parser.parse("[pos:verb, lexeme:eat, subject:[person:_1|_2, number:sg]|[person:_3, number:pl], tense:present, mode:indicative]")
print (features.toString())
