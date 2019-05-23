# -*- coding: utf-8 -*-
'''
Changes name of the file
'''

import os

if __name__=='__main__':
    for i in os.listdir('.'):
        # You can specify the extensions that you want (ex. change this to .xml to change the names of xml files)
        if i.endswith('.xml'):
            ### This is where you specify the string to prepend to the name (ex. _12.jpg -> example_12.jpg)
            change = 'Ban'
            os.rename(i, change + i)
            print('{} -> {}'.format(i, change + i))
    input()