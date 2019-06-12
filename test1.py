from operator import itemgetter

class People(object):
    name="kate"
    __age=20

    def __init__(self,english):
        self.name='katherine'
        self.sex="female"
        self.english=english

    @classmethod
    def setting_attr(cls,english=12):
        return cls(english=english)

def loop():
    pass
if __name__ == '__main__':
    # p=People()
    # print(People.name)
    # print(p.name)
    # print(p.english)
    # # print(People.__name)
    lst=list(range(1,10))
    lst1=list(range(10,20))
    # print(lst)
    # print(lst[:])
    # print(lst+lst1)

    # al=[1,8,6,9]
    # al_copy=al[:]
    # # print(al)
    # # al.reverse()
    # # print(al)
    # # # al.sort()
    # #
    # #
    # # my_list=[[132,2,2,144],[22,6,6,444],[354,4,4,678],[236,5,5,678]]
    # # print(sorted(my_list,key=itemgetter(3,0)))
    # # print(str(al))
    # # x,y=1,2
    # # x,y=y,x
    # # print(x,y)
    # dic={'2':6,'1':7,'3':4}
    # dic_c=dic.copy()
    # # print(dic_c)
    # # dic_c['3']=4
    # # print(dic,dic_c)
    #
    # print(dic)
    #
    # print(sorted(dic_c.items()))
    #
    # ordered_dict=sorted(dic_c.items(),key=lambda x:x[0])
    # print('keys',dict(ordered_dict))
    # ordered_dict1=sorted(dic_c.items(),key=lambda x:x[1],reverse=True)
    # print('values', dict(ordered_dict))

    d = {"ok": 1, "no": 2}
    # 对字典按键排序，用元组列表的形式返回
    d1 = sorted(d.items(), key=lambda d: d[0], reverse=False)  # [('no', 2), ('ok', 1)]
    # 对字典按值排序，用元组列表的形式返回
    d2 = sorted(d.items(), key=lambda d: d[1], reverse=True)  # [('ok', 1), ('no', 2)]
    print(d1)
    print(d2)