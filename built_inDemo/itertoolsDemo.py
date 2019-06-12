# -*- coding: utf-8 -*-

"""iteratools applications"""

__author__ = 'katherinelove'

import itertools

if __name__ == '__main__':
    nuture=itertools.count(1)
    lst=itertools.takewhile(lambda x:x<100,nuture)
    print(list(lst))

    lst1=["A","a","a","A"]
    lst2=[2,3,4,5]
    iter1=itertools.chain(lst1,lst2)
    print(list(iter1))

    for key,group in itertools.groupby("AABBaaAAVVVb"):
        print(key,list(group))
    print("=="*50)
    for key,group in itertools.groupby("AABBaaaVVVb",lambda x:x.upper()):
        print(key,list(group))