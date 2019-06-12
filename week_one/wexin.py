#coding:utf8
#author:katherinelove
#copyright:shuai

import itchat


def main():
    itchat.login()
    friends=itchat.get_friends()
    for friend in friends:
        print(friend)


if __name__ == '__main__':
    main()
