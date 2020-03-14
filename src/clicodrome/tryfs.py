from fs.Feature import *
from fs.Features import *
from fs.Value import *
from fs.ListFeatures import *

features = Features([Feature("a", Value("b"))])
features.add(Feature("c", Value("d")))


print(features.toString())



# features = Features([Feature("a1", Value("v1")), \
#                      Feature("a2", Value(ListFeatures(\
#                                                       [Features([Feature("a3", Value("v3")), \
#                                                                  Feature("a4", Value("v4")), \
#                                                                  Feature("a5", Value("v5"))]), \
#                                                        Features([Feature("a6", Value("v6"))])])))])
#print(features.toString())

