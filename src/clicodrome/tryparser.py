from fs.Parser import *

parser = Parser()

print("##############################")
print('tryparser.py(11): unification of two features that will succeed')
features1 = parser.parse("[a:[person:_2|_4|_6|_8|_10]]")
features2 = parser.parse("[a:[person:_1|_3|_6|_5|_10|_7|_9]]")
print ('feature 1 : ', features1.toString())
print ('feature 2 : ', features2.toString())
try:
    unif = features1.unify(features2, True)
except UnificationException as e:
    print (e)
else:
    print ('unification result: ', unif.toString())
 
print("\n##############################")
print('tryparser.py(11): unification of two features that will succeed')
features1 = parser.parse("[pos:verb, lexeme:eat, subject:[person:_1|_2, number:sg], tense:present, mode:indicative]")
features2 = parser.parse("[subject:[lexeme:pro, person:_2, number:sg]]")
print ('feature 1 : ', features1.toString())
print ('feature 2 : ', features2.toString())
try:
    unif = features1.unify(features2, True)
except UnificationException as e:
    print (e)
else:
    print ('unification result: ', unif.toString())
 
print("\n##############################")
print('tryparser.py(21): unification of two features that will succeed')
features1 = parser.parse("[pos:verb, lexeme:eat, subject:[person:_1|_2, number:sg]|[person:_3, number:pl], tense:present, mode:indicative]")
features2 = parser.parse("[subject:[def:true, number:pl]]")
print ('feature 1 : ', features1.toString())
print ('feature 2 : ', features2.toString())
try:
    unif = features1.unify(features2, True)
except UnificationException as e:
    print (e)
else:
    print ('unification result: ', unif.toString())
  
print("\n##############################")
print('tryparser.py(21): unification of two features that will succeed')
features1 = parser.parse("[subject:[def:true, number:pl, person:_3|_6]]")
features2 = parser.parse("[pos:verb, lexeme:eat, subject:[person:_1|_2, number:sg]|[person:_3, number:pl], tense:present, mode:indicative]")
print ('feature 1 : ', features1.toString())
print ('feature 2 : ', features2.toString())
try:
    unif = features1.unify(features2, True)
except UnificationException as e:
    print (e)
else:
    print ('unification result: ', unif.toString())
  
print("\n##############################")
print('tryparser.py(31): unification of two features that will failed')
features1 = parser.parse("[pos:verb, lexeme:eat, subject:[person:_1|_2, number:sg], tense:present, mode:indicative]")
features2 = parser.parse("[subject:[lexeme:pro, person:_1, number:pl]]")
print ('feature 1 : ', features1.toString())
print ('feature 2 : ', features2.toString())
try:
    unif = features1.unify(features2, True)
except UnificationException as e:
    print (e)
else:
    print ('unification result: ', unif.toString())
