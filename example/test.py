#!/usr/bin/python
# -*- coding: utf8 -*-
from colorama import Fore, Back, Style

# Available formatting constants are:
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

# calc

# def log(message, info_type)
# 	if info_type == 'error':
# 		print(Fore.RED + message + Fore.RESET)
# 	elif info_type == 'warning':
# 		print(Fore.YELLOW + message + Fore.RESET)
# 	elif info_type == 'info':
# 		print(Fore.GREEN + message + Fore.RESET)
# 	else:
# 		print(message)

print(Fore.GREEN)
lost_points = input(Fore.GREEN + "Input losing points: " + Fore.RESET)
print(Fore.RESET)

if (lost_points.isnumeric() == False or int(lost_points) > 4200):
	print(Fore.RED + 'Invalid value' + Fore.RESET)
	exit()

oponent_max_battle_points = 4200 - int(lost_points)
target_prize_point	= 134
max_prize_point		= 500
out_factor 			= target_prize_point/max_prize_point	#0.268
enemy_factor 		= 1 - out_factor 						#0.732
our_battle_points	= (oponent_max_battle_points * out_factor) / enemy_factor

print('Oponent max points: '	+ str(oponent_max_battle_points))
print('Our target:         '	+ str(int(our_battle_points)) + '\n')

print("Press <ENTER> to quit")
input()
