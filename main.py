# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 09:31:28 2020

@author: 劉又聖
"""

from add_dish import Add_Dish
from pick_dish import Pick_Dish

def main():

    while True:
        choice = input('input 1 for Add Dish, 2 for Pick Dish, Q for leave.\n>> ')
        
        if   choice == '1':
            Add_Dish()
        elif choice == '2':
            Pick_Dish()
        elif choice == 'Q':
            break
        else:
            print(f'No {choice} this option')

if __name__ == '__main__':
    main()