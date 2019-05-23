# -*- coding: utf-8 -*-
'''
Changes name of the file
'''

import os

if __name__=='__main__':
    change = 'Ban'
    for i in os.listdir('./screenshots'):
        if i.endswith('.jpg') and not i.startswith('_'):
            ### This is where you specify the string to prepend to the name (ex. _12.jpg -> example_12.jpg)
            os.rename(i, change + i)
            print('{} -> {}'.format(i, change + i))
	for i in os.listdir('./annotations'):
        if i.endswith('.xml') and not i.startswith('_'):
            ### This is where you specify the string to prepend to the name (ex. _12.jpg -> example_12.jpg)
            os.rename(i, change + i)
            print('{} -> {}'.format(i, change + i))
    input()