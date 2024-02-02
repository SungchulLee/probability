import numpy as np
import random


class Monty:
    def __init__(self):
        self.doors = [0, 1, 2]
        self.car_position = np.random.choice(self.doors)
        self.first_choice = None
        self.host_choice = None
        self.final_choice = None
    def first_round(self):
        self.first_choice = int(input(f'Choose one from {self.doors} : '))
        print(f'You choose Door {self.first_choice} as your first choice.')
    def host_round(self):
        host_list = [0, 1, 2]
        host_list.remove(self.car_position)
        try:
            host_list.remove(self.first_choice)
        except ValueError:
            pass
        self.host_choice = np.random.choice(host_list)
        print(f'Host open Door {self.host_choice} and show a goat.')
    def final_round(self):
        player_list = [0, 1, 2]
        player_list.remove(self.host_choice)
        self.final_choice = int(input(f'Choose one from {player_list} : '))
        print(f'You choose Door {self.final_choice} as your final choice.')
    def open_final_round_door(self):
        print(f'Let\'s open Door {self.final_choice}.')
        if self.final_choice == self.car_position:
            print('Congrat! You have a brand new car!')
        else:
            print('Sorry, you have a goat.')
    def run(self):
        self.first_round()
        self.host_round()
        self.final_round()
        self.open_final_round_door()


class MontyStick:
    
    def __init__(self):
        self.doors = [0, 1, 2]
        self.car_position = random.choice(self.doors)
        self.final_choice = random.choice(self.doors)
            
    def run(self):
        if self.final_choice == self.car_position:
            return 1
        else:
            return 0
        

class MontySwitch:
    
    def __init__(self):
        self.doors = [0, 1, 2]
        self.car_position = random.choice(self.doors)
        self.first_choice = None
        self.host_choice = None
        self.final_choice = None
        
    def first_round(self):
        self.first_choice = random.choice(self.doors)
        
    def host_round(self):
        host_list = [0, 1, 2]
        host_list.remove(self.car_position)
        try:
            host_list.remove(self.first_choice)
        except ValueError:
            pass
        self.host_choice = random.choice(host_list)
        
    def final_round(self):
        player_list = [0, 1, 2]
        player_list.remove(self.first_choice)
        player_list.remove(self.host_choice)
        self.final_choice = player_list[0]
        
    def open_final_round_door(self):
        if self.final_choice == self.car_position:
            return 1
        else:
            return 0
            
    def run(self):
        self.first_round() 
        self.host_round()
        self.final_round()
        return self.open_final_round_door()