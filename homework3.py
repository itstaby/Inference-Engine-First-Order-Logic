import random
import sys
import os
import numpy as np
import copy
import time
import copy
###########################classes
class predicate:
    name = None
    constant = None
    variable = None
    arg_list = None
    ind = None

    def __init__(self):
        self.arg_list = []
        self.name = ""
        self.constant = []
        self.variable = []
        self.ind = 0

class sentence:
    sent = None
    def __init__(self):
        sent = []
###################################

###############functions

def pred_filter(inp_str):
    predi = predicate()
    temp = inp_str.split('(')
    temp1 = temp[0]
    if(temp1[0] == '~'):
        predi.ind = 1
        temp1=temp1.replace("~","")
    predi.name = temp1
    temp1 = temp[1].split(',')
    for a in range(temp1.__len__()):
        len = temp1[a].__len__()
        if(temp1[a].find(")")> -1):
            ind = temp1[a].find(")")
            temp1[a] = temp1[a][:ind]
        if(temp1[a][0].isupper()):
            predi.constant.append(temp1[a])
            predi.arg_list.append(temp1[a])
        else:
            predi.variable.append(temp1[a])
            predi.arg_list.append(temp1[a])
    return predi

def copySentence(sentence):
    newSentence = []
    newPredicate = predicate()

    for i in range(0,sentence.__len__()):
        oldPredicate = sentence[i]
        for j in range(0,oldPredicate.arg_list.__len__()):
            newPredicate.arg_list.append(oldPredicate.arg_list[j])
        newPredicate.name = oldPredicate.name
        newPredicate.ind = oldPredicate.ind
        newSentence.append(newPredicate)
        newPredicate = predicate()

    return newSentence

def unification1(sentence1R, sentence2R, predicate1,predicate2, s1Index, s2Index):

    sentence2 = []
    sentence1 = []
    sentence1 = copySentence(sentence1R)#copy.deepcopy(sentence1R)
    sentence2 = copySentence(sentence2R)#copy.deepcopy(sentence2R)



    const_var_list = []
    const_var = []
    pred_unified = predicate1
    pred_unify = predicate2
    setCantUnify=False

    for c in range(pred_unified.arg_list.__len__()):
        isPredicate1ArgumentConstant = pred_unified.arg_list[c][0].isupper()
        isPredicate2ArgumentConstant = pred_unify.arg_list[c][0].isupper()
        if (isPredicate1ArgumentConstant == True and isPredicate2ArgumentConstant == True):
            if(pred_unified.arg_list[c]!=pred_unify.arg_list[c]):
                return None

    for c in range(pred_unified.arg_list.__len__()):
        isPredicate1ArgumentConstant = pred_unified.arg_list[c][0].isupper()
        isPredicate2ArgumentConstant = pred_unify.arg_list[c][0].isupper()
        if(isPredicate1ArgumentConstant == True and isPredicate2ArgumentConstant == False):
            const_var.append(pred_unified.arg_list[c])
            const_var.append(pred_unify.arg_list[c])
            const_var_list.append(const_var)
            const_var = []

    for d in range(sentence2.__len__()):
        for e in range(sentence2[d].arg_list.__len__()):
            for f in range(const_var_list.__len__()):
                if(sentence2[d].arg_list[e] == const_var_list[f][1]):
                    sentence2[d].arg_list[e] = const_var_list[f][0]
    const_var_list = []


    for c in range(pred_unified.arg_list.__len__()):
        isPredicate1ArgumentConstant = pred_unified.arg_list[c][0].isupper()
        isPredicate2ArgumentConstant = pred_unify.arg_list[c][0].isupper()
        if(isPredicate1ArgumentConstant == False and isPredicate2ArgumentConstant == True):
            const_var.append(pred_unify.arg_list[c])
            const_var.append(pred_unified.arg_list[c])
            const_var_list.append(const_var)


    for g in range(sentence1.__len__()):
        for h in range(sentence1[g].arg_list.__len__()):
            for i in range(const_var_list.__len__()):
                if (sentence1[g].arg_list[h] == const_var_list[i][1]):
                    sentence1[g].arg_list[h] = const_var_list[i][0]


    for c in range(pred_unified.arg_list.__len__()):
        isPredicate1ArgumentConstant = pred_unified.arg_list[c][0].isupper()
        isPredicate2ArgumentConstant = pred_unify.arg_list[c][0].isupper()
        if(isPredicate1ArgumentConstant == False and isPredicate2ArgumentConstant == False):
            sentence1Variable = pred_unified.arg_list[c]
            sentence2Variable = pred_unify.arg_list[c]

            if(sentence1Variable != sentence2Variable):
                for i in range(0,sentence2.__len__()):
                    for j in  range(0,sentence2[i].arg_list.__len__()):
                        if(sentence2[i].arg_list[j] == sentence1Variable):
                            sentence2[i].arg_list[j] += '2'

                for i in range(0,sentence2.__len__()):
                    for j in  range(0,sentence2[i].arg_list.__len__()):
                        if(sentence2[i].arg_list[j] == sentence2Variable):
                            sentence2[i].arg_list[j] = sentence1Variable

            const_var.append(pred_unify.arg_list[c])
            const_var.append(pred_unified.arg_list[c])
            const_var_list.append(const_var)

    del sentence1[s1Index]
    del sentence2[s2Index]

    finalSentence = sentence1 + sentence2

    if(checkRepeat(finalSentence)):
        return None
    return finalSentence





def print_predicate(predicate):
    if(predicate.ind == 1):
        print('~', end='')
    print(predicate.name, end='')
    print('(', end='')
    for a in range(predicate.arg_list.__len__()):
        print(predicate.arg_list[a], end='')
        if(a < predicate.arg_list.__len__()-1):
            print(',', end='')
    print(')', end='')


def print_KB(KB):
    print(KB.__len__())
    for a in range(KB.__len__()):
        for b in range(KB[a].__len__()):
            print_predicate(KB[a][b])
            if(KB[a].__len__() > 1 and b != KB[a].__len__()-1):
                print(' ', end='')
                print('|', end='')
                print(' ', end='')
        print('')
def print_queries(queries):
    #print(queries.__len__())
    for a in range(queries.__len__()):
        print_predicate(queries[a])
        print('')


def doSomething():
    print("Something")

def checkContradiction(predicate1, predicate2):
    if(predicate1.name == predicate2.name and predicate1.ind != predicate2.ind):
        if(predicate1.arg_list.__len__() == predicate2.arg_list.__len__()):
            for i in range(0, predicate1.arg_list.__len__()):
                if(predicate1.arg_list[i] != predicate2.arg_list[i]):
                    return False
            return True
    return False

def customResolution(KB,querySentence, depthLimit = 5000):
    depthLimit-=1
    if(depthLimit ==0):
        return 'limit'
    if(depthLimit==1990):
        x=0
    for i in range(0, KB.__len__()):
        kbSentence = KB[i].copy()
        for j in range(0, kbSentence.__len__()):
            currentPredicateFromKB = kbSentence[j]
            for k in range(0,querySentence.__len__()):
                queryPredicate = querySentence[k]
                if (currentPredicateFromKB.name == queryPredicate.name and currentPredicateFromKB.ind != queryPredicate.ind):
                    if (querySentence.__len__() == 1 and kbSentence.__len__() == 1):
                        if (checkContradiction(querySentence[0], kbSentence[0])):
                            return 'true'

                    unifiedSentence = unification1(querySentence, kbSentence.copy(),queryPredicate,currentPredicateFromKB,k,j)

                    if(unifiedSentence != None):
                        if (unifiedSentence.__len__() == 0):
                            return 'true'

                        if(not checkLoop(unifiedSentence)):
                            loopDetectionList.append(unifiedSentence)
                            returnedValue = customResolution(KB,unifiedSentence,depthLimit)
                            if(returnedValue == 'limit' or returnedValue == 'true'):
                                return returnedValue
                            #check if output was true, if yes, reuturn
                        else:
                            continue


def checkLoop(unifiedSentence):
    if(loopDetectionList.__len__()==0):
        return False

    check = False
    for sentence in loopDetectionList:
        if(sentence.__len__() == unifiedSentence.__len__()):
            check = patternRecognition(sentence,unifiedSentence,0,[])
            if(check):
                return check

    return check


def checkRepeat(unifiedSentence):
    for i in range(0, unifiedSentence.__len__()):
        for j in range(0, unifiedSentence.__len__()):
            if (i == j):
                continue
            if (unifiedSentence[i].name == unifiedSentence[j].name):
                if (unifiedSentence[i].ind == unifiedSentence[j].ind):
                    for k in range(0, unifiedSentence[i].arg_list.__len__()):
                        if (unifiedSentence[i].arg_list[k] != unifiedSentence[j].arg_list[k]):
                            break
                    return True

    return False


def patternRecognition(sentence1, sentence2, indexToCheck, matching):
    if(indexToCheck <sentence1.__len__()):
        predicate1 = sentence1[indexToCheck]
        predicate2 = sentence2[indexToCheck]
        if(predicate1.name != predicate2.name):
            return False
        for i in range(0,sentence1[indexToCheck].arg_list.__len__()):
            var1 = predicate1.arg_list[i]
            var2 = predicate2 .arg_list[i]
            if(var1[0].isupper() and var2[0].isupper and var1!=var2):
                return False
            for j in range(0,matching.__len__()):
                first = (matching[j][0]==var1)
                second = (matching[j][1]==var2)
                if(first != second ):
                    return False
            matching.append((var1,var2))
        return patternRecognition(sentence1, sentence2, indexToCheck+1, matching)
    else:
        return True
######################

####################################main code ##########################


loopDetectionList =[]

input = "input.txt"
input_data = []
queries = []
file = open(input, "r")
# data  identification
for line in file:
    input_data.append(line)
no_queries = int(input_data[0])
no_sentences = int(input_data[no_queries+1])
queries = []
sentence_kb = []
KB = []
for a in range(1,no_queries+1):
    queries.append(pred_filter(input_data[a]))
for st in range(no_queries+2,no_sentences+no_queries+2):
    if(input_data[st].find("|") > -1):
        input_data[st] = input_data[st].replace(" ","")
        or_split = input_data[st].split("|")
        for or_sp in range(or_split.__len__()):
            sentence_kb.append(pred_filter(or_split[or_sp]))
    else:
        sentence_kb.append(pred_filter(input_data[st]))
    KB.append(sentence_kb)
    sentence_kb = []
querySentence = []
querySentence.append(queries[0])

solutionFound = False

p1 = predicate()
p1.name='Father'
p1.arg_list = ['x']


p2 = predicate()
p2.name='Father'
p2.arg_list = ['x']
sentence = [p1,p2]

output = open('output.txt', 'w')

for i in range(0,queries.__len__()):
    querySentence=[]
    querySentence.append(queries[i])
    querySentence[0].ind = abs(querySentence[0].ind -1)
    loopDetectionList = [querySentence]
    solutionFound = customResolution(KB.copy(),querySentence)
    answer = None
    if(solutionFound == "true"):
        answer = "TRUE\n"
    else:
        answer = "FALSE\n"
    output.write(answer)
