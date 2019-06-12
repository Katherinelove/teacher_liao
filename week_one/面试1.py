# -*- coding: utf-8 -*-

"""面试"""

__author__ = 'katherinelove'

if __name__ == '__main__':
    d=dict(zip(["a","b","c","d","e"],[1,2,3,4,5]))
    print(d)
    for x in d:
        print(x)
    lst1=[d[key] for key in d]
    print(lst1)
    lst2={i:i*i for i in lst1}
    print(lst2)