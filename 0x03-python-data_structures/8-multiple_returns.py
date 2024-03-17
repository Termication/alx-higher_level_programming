#!/usr/bin/python3
def multiple_returns(sentence):
    _tuple = ()
    if len(sentence) == 0:
        _tuple = 0, "None"
    else:
        _tuple = len(sentence), sentence[0]
    return _tuple
