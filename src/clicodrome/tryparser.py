from fs.Parser import *

parser = Parser()

print('tryparser.py(11): unification of two features that will succeed')
features1 = parser.parse("[pos:verb, lexeme:eat, subject:[person:_1|_2, number:sg], tense:present, mode:indicative]")
features2 = parser.parse("[subject:[lexeme:pro, person:_2, number:sg]]")
print ('feature 1 : ', features1.toString())
print ('feature 2 : ', features2.toString())
try:
    unif = features1.unify(features2)
except UnificationException as e:
    print (e)
else:
    print ('unification result: ', unif.toString())


print()
print('tryparser.py(21): unification of two features that will succeed')
features1 = parser.parse("[pos:verb, lexeme:eat, subject:[person:_1|_2, number:sg]|[person:_3, number:pl], tense:present, mode:indicative]")
features2 = parser.parse("[subject:[lexeme:pro, person:_3, number:pl]]")
print ('feature 1 : ', features1.toString())
print ('feature 2 : ', features2.toString())
try:
    unif = features1.unify(features2)
except UnificationException as e:
    print (e)
else:
    print ('unification result: ', unif.toString())

print()
print('tryparser.py(31): unification of two features that will failed')
features1 = parser.parse("[pos:verb, lexeme:eat, subject:[person:_1|_2, number:sg], tense:present, mode:indicative]")
features2 = parser.parse("[subject:[lexeme:pro, person:_1, number:pl]]")
print ('feature 1 : ', features1.toString())
print ('feature 2 : ', features2.toString())
try:
    unif = features1.unify(features2)
except UnificationException as e:
    print (e)
else:
    print ('unification result: ', unif.toString())
