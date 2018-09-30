# -*- coding: utf-8 -*-

import os
import json
import difflib

################################################################################
##  Sort and generate diff data file.
################################################################################
_TYPE_STR = type(str())
_TYPE_UNICODE = type(unicode())
_TYPE_DICT = type(dict())
_TYPE_LIST = type(list())

def _is_str(inputData):
    """
    note   : Return if input data is a instance of "str".
    param  :
        inputData   : Input data.
    return : The conclusion.
    """
    typeInput = type(inputData)
    return typeInput == _TYPE_STR or typeInput == _TYPE_UNICODE


def _is_list(inputData):
    """
    note   : Return if input data is a instance of "list".
    param  :
        inputData   : Input data.
    return : The conclusion.
    """
    return type(inputData) == _TYPE_LIST


def _is_dict(inputData):
    """
    note   : Return if input data is a instance of "dict".
    param  :
        inputData   : Input data.
    return : The conclusion.
    """
    return type(inputData) == _TYPE_DICT


def _stringlize_list(inputList):
    """
    note   : Stringlize a input list.
    param  :
        inputData   : Input list.
    return : Stringlized list.
    """
    result = ""

    if not inputList:
        return result

    for e in inputList:
        if _is_list(e):
            s = _stringlize_list(e)
        elif _is_dict(e):
            s = _stringlize_dict(e)
        else:
            s = str(e)

        result = result + s

    return result


def _stringlize_dict(inputDict):
    """
    note   : Stringlize input dict.
    param  :
        inputData   : Input dict.
    return : Stringlized dict.
    """
    result = ""

    if not inputDict:
        return result

    for k in sorted(inputDict.keys()):
        v = inputDict[k]
        if _is_list(v):
            s = _stringlize_list(v)
        elif _is_dict(v):
            s = _stringlize_dict(v)
        elif _is_str(v):
            # It seems got a problem that it depend the input data. 
            # Recommend to trans data in ensure_ascii=False
            #s = v.encode('utf-8')
            s = v
        else:
            s = str(v)

        result = result + s

    return result


def _get_sort_key(inputData):
    """
    note   : Stringlize input data.
    param  :
        inputData   : Input data.
    return : Stringlized data.
    """
    if _is_list(inputData):
        result = _stringlize_list(inputData)
    elif _is_dict(inputData):
        result = _stringlize_dict(inputData)
    else:
        result = str(inputData)

    return result


def _sort_list(inputList):
    """
    note   : Sort input list.
    param  :
        inputData   : Input list.
    return : Sorted list(copy).
    """
    length = len(inputList)
    tmpList_A = []
    midMap = {}
    for i in range(length):
        tmpList_A.append(_sort_list_in_data(inputList[i]))
        midMap[i] = _get_sort_key(tmpList_A[i])

    sortedIndex = sorted(\
            midMap.items(), \
            key = lambda x:x[1], \
            reverse = False)
    tmpList_B = []
    for pair in sortedIndex:
        tmpList_B.append(tmpList_A[pair[0]])

    return tmpList_B


def _sort_dict(inputDict):
    """
    note   : Sort input dict.
    param  :
        inputData   : Input dict.
    return : Sorted dict(copy).
    """
    tmpDict = {}
    for key, value in inputDict.items():
        if _is_list(value):
            sortedValue = _sort_list(value)
        elif _is_dict(value):
            sortedValue = _sort_dict(value)
        else:
            sortedValue = value

        tmpDict[key] = sortedValue

    return tmpDict


def _sort_list_in_data(inputData):
    """
    note   : Sort input data.
    param  :
        inputData   : Input data.
    return : Sorted data(copy).
    """
    if _is_list(inputData):
        return _sort_list(inputData)
    elif _is_dict(inputData):
        return _sort_dict(inputData)
    else:
        return inputData


def compare_data(inData_A, inData_B, diffFilePrefix):
    """
    note   : Sort and compre if inData_A equals to inData_B.
    param  :
        inData_A   : Input data.
        inData_B   : Another input data.
        diffFilePrefix  : Output diff file prefix.
    return :
        True    : inData_A equals to inData_B.
        False   : inData_A does NOT equals to inData_B.
    """

    dict_A = _sort_list_in_data(inData_A)
    dict_B = _sort_list_in_data(inData_B)

    str_A = json.dumps(dict_A, indent = 4, sort_keys=True, ensure_ascii=False, encoding='utf-8')
    str_B = json.dumps(dict_B, indent = 4, sort_keys=True, ensure_ascii=False, encoding='utf-8')

    if str_A == str_B:
        return True

    fileName = "%s_1_process.data" % diffFilePrefix
    with open(fileName, "w") as f:
        f.write(str_A)

    fileName = "%s_2_expect.data" % diffFilePrefix
    with open(fileName, "w") as f:
        f.write(str_B)

    return False


################################################################################
##  Test
################################################################################
def test_compare_data():
    """
    Test for function compare_data.
    """
    orgInputDict_XX = {
            "AA_02": 5.5, 
            "AA_04": 10,
            "AA_05": "it is a string", 
            "AA_03": [
                {
                    "BB_02": 30, 
                    "BB_03": "string again", 
                    "BB_01": [
                        {
                            "CC_02": 55,
                            "CC_03": "T_T",
                            "CC_01": "what ever"
                            },
                        {
                            "CC_02": 35,
                            "CC_03": "T_T",
                            "CC_01": "what ever"
                            },
                        {
                            "CC_02": 25,
                            "CC_03": "T_T",
                            "CC_01": "what ever"
                            }
                        ]
                    }, 
                {
                    "BB_02": 20, 
                    "BB_03": "string again", 
                    "BB_01": [
                        {
                            "CC_02": 25,
                            "CC_03": "T_T",
                            "CC_01": "what ever"
                            },
                        {
                            "CC_02": 35,
                            "CC_03": "T_T",
                            "CC_01": "what ever"
                            },
                        {
                            "CC_02": 55,
                            "CC_03": "T_T",
                            "CC_01": "what ever"
                            }
                        ]
                    }, 
                {
                    "BB_02": 10, 
                    "BB_03": "string again", 
                    "BB_01": [
                        {
                            "CC_02": 25,
                            "CC_03": "T_T",
                            "CC_01": "what ever"
                            },
                        {
                            "CC_02": 35,
                            "CC_03": "T_T",
                            "CC_01": "what ever"
                            },
                        {
                            "CC_02": 55,
                            "CC_03": "T_T",
                            "CC_01": "what ever"
                            }
                        ]
                    }
                ], 
            "AA_01": {
                "y": 10, 
                "z": 15,
                "x": 5
                }
            }

    orgInputDict_YY = {
            "AA_01": {
                "x": 5, 
                "y": 10, 
                "z": 15
                }, 
            "AA_02": 5.5, 
            "AA_03": [
                {
                    "BB_02": 10, 
                    "BB_03": "string again", 
                    "BB_01": [
                        {
                            "CC_01": "what ever", 
                            "CC_02": 25,
                            "CC_03": "T_T"
                            },
                        {
                            "CC_01": "what ever", 
                            "CC_02": 35,
                            "CC_03": "T_T"
                            },
                        {
                            "CC_01": "what ever", 
                            "CC_02": 55,
                            "CC_03": "T_T"
                            }
                        ]
                    }, 
                {
                    "BB_02": 20, 
                    "BB_03": "string again", 
                    "BB_01": [
                        {
                            "CC_01": "what ever", 
                            "CC_02": 25,
                            "CC_03": "T_T",
                            },
                        {
                            "CC_01": "what ever", 
                            "CC_02": 35,
                            "CC_03": "T_T",
                            },
                        {
                            "CC_01": "what ever", 
                            "CC_02": 55,
                            "CC_03": "T_T",
                            }
                        ]
                    }, 
                {
                    "BB_02": 30, 
                    "BB_03": "AAAAstring again", 
                    "BB_01": [
                        {
                            "CC_01": "what ever", 
                            "CC_02": 25,
                            "CC_03": "T_T"
                            },
                        {
                            "CC_01": "what ever", 
                            "CC_02": 35,
                            "CC_03": "T_T"
                            },
                        {
                            "CC_01": "what ever", 
                            "CC_02": 55,
                            "CC_03": "T_T"
                            }
                        ]
                    },
                ], 
            "AA_04": 1000,
            "AA_05": "it is a string"
            }

    compare_data(orgInputDict_XX, orgInputDict_YY, "tryTest")

if __name__ == "__main__":
    test_compare_data()

