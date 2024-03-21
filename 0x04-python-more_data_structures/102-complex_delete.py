#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    _keys = list(a_dictionary.keys())

    for v_dic in _keys:
        if value == a_dictionary.get(v_dic):
            del a_dictionary[v_dic]

    return (a_dictionary)
