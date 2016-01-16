# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return [ dct[k] for k in keylist ]

def list2dict(L, keylist): return { b:a for (a,b) in zip(L, keylist) }

def listrange2dict(L): return { i:L[i] for i in range(len(L)) }

