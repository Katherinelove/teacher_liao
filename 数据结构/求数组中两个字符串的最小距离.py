# -*- coding: utf-8 -*-

"""
题目：
给定一个数组 strs，其中的数据都是字符串，给定两个字符串 str1，str2。如果这两个字符串都在 strs数组中，就返回它们之间的最小距离；如果其中任何一个不在里面，则返回 -1；如果两个字符串相等，则返回 0。
例如：给定[‘*’,’3’,’*’,’5’,’10’,’9’,’7’,’1’,’*’]，再给定两个字符串’* ‘和’9’，通过函数求得返回值 3。
---------------------
分析
有两种方法，
方法1：遍历数组 strs，分别记录两个 str1 和 str2 的位置。求得最小的一个距离数字。这样做时间复杂度为 o(n^2)。
方法2：
如果查询的次数非常多，为了提高查询的效率，构造Hash表，把每次查询的时间复杂度下降到 o(1)。
Python 的内置 dict 类型就是哈希表，实现方法也是hash 表，其查询的时间复杂度就是 o(1)。哈希表的构造也分很多种：
比如，构造 Hash 表，key值是strs中的每一个字符串，value值是一个hash表，里面存放着该字符串到其它字符串的最小距离。
写成代码就是：hash_table = {“*”:{“3”:1, “5”:1, “10”:2, “9”:3, “7”:2, “1”:1}}
当然这种方法的空间复杂度是 o(n^2)
---------------------

"""
import math
__author__ = 'katherinelove'


def min_distance_1(strs, str1, str2):
    '''
    数组中两个字符串的最小距离，这是方法1，时间复杂度 o(n^2)
    :param strs: 给定的数组中存放有多个字符串
    :param str1: 第一个字符串
    :param str2: 第二个字符串
    :return: 如果其中给定的一个字符串不在数组 strs 中，那么返回-1，否则返回两个字符串之间的最小间距
    '''
    if str1 not in strs or str2 not in strs:
        return -1
    if str1==str2:
        return 0
    dist,min=1,len(strs)
    pos1,pos2=0,len(strs)

    for i in range(len(strs)):
        if strs[i]==str1:
            pos1=i
        for j in range(len(strs)):
            if strs[j]==str2:
                pos2=j
            dist=(int)(abs(pos1-pos2))
            if dist<min:
                min=dist
    return min


if __name__ == '__main__':
    strs=[1,3,5,7,9]
    print(min_distance_1(strs,1,7))