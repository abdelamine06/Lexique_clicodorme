from main.models import *
import regex

def strToDict(mot):
    dict={}
    patternSimple='[^=,\ \[\]]+=[^,\[\]]+'
    patternComplexe='[^=,\ \[\]]+=\[((?:[^\[\]]*|(?R))*)\]'
    infos=[]
    tmp=regex.search(patternComplexe,mot)
    if tmp!=None:
        infos+=[tmp.group(0)]
    tmp=regex.sub(patternComplexe,'',mot)
    tmp=regex.findall(patternSimple,tmp)
    if tmp!=[]:
        infos+=tmp
    for info in infos:
        index=info.find('=')
        if '[' in info:
            dict[info[0:index]]=strToDict(info[index+2:len(info)-1])
        else:
            dict[info[0:index]]=info[index+1:]
    return dict

def DictToStr(dict):
    res=str(dict)
    res=res[1:len(res)-1]
    res=res.replace('{','[')
    res=res.replace('}',']')
    res=res.replace(': ','=')
    res=res.replace('\'','')
    return res

def unification(dict1,dict2):
    res=dict1
    for cle,val in dict2.items():
        if cle in dict1:
            if dict1[cle]!=val:
                return {}
        else:
            res[cle]=val
    return res

def unifiable(dict1,dict2):
    print(dict1,dict2)
    res=False
    for cle,val in dict2.items():
        if cle in dict1:
            if isinstance(dict1[cle],dict):
                if isinstance(val,dict):
                    tmp=False
                    for c,v in dict1[cle].items():
                        if c in val and val[c]==v:
                            tmp=True
                            break
                    res=tmp
                else:
                    tmp=False
                    for c,v in dict1[cle].items():
                        if v==val:
                            tmp=True
                            break
                    res=tmp
            else:
                if isinstance(dict2[cle],dict):
                    tmp=False
                    for c,v in val:
                        if c==cle and dict1[cle]==v:
                            tmp=True
                            break
                    res=tmp
                else:
                    if val==dict1[cle]:
                        res=True
    return res

def transforme(mot,transformation):
    terminaisonIndex=mot.Mot.rfind(transformation.Terminaison)
    if transformation.Terminaison=='':
        terminaisonIndex+=1
    formeMot=mot.Mot[:terminaisonIndex+1]+transformation.Transformation
    infos=unification(strToDict(mot.Infos),strToDict(transformation.Infos))
    if infos!={}:
        formeMot=FormeMot(Mot=formeMot,Affiche=formeMot,Table=mot.Table,Infos=DictToStr(infos))
        formeMot.save()
    return formeMot

def transformeTous():
    formesMots=FormeMot.objects.all()
    for formeMot in formesMots:
        formeMot.delete()
    mots=Mot.objects.all()
    for mot in mots:
        transformations=TableTransformation.objects.filter(NumTab=mot.Table)
        for transformation in transformations:
            transforme(mot,transformation)
    return
