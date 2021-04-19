from pokedex import pokedex
import os
import time
import threading

class Player:
  def __init__(self, name, player_name):
    self.name = name
    self.player_name = player_name
    self.number_of_pokemon = 0
    self.poke_owned = []
    return

  def add_pokemon(self, pokemon):
    if len(self.poke_owned) <= 5:
      self.poke_owned.append(pokemon)
    #print('Added {owned} to Pokedeck'.format(owned=pokemon))
      self.number_of_pokemon += 1
      pokemon.trainer = self.player_name
      for i in range(len(self.poke_owned)):
        print('Just added: \n', self.poke_owned[i])
      return
    else:
      print('Your Pokedeck is already full')
    return

class Trainer(Player):
  def __init__(self):
    autogen_players = {}

class Pokemon(Player):
  healing_potions = {
                1: ['Pheonix Down', 10],
                2: ['Max potion', 10], 
                3: ['Normal potion', 10],
                4: ['||--->', 'Main Menu']
    }
  def __init__(self, name, level, poketype):
    self.name = name
    self.level = level
    self.poketype = poketype
    self.max_health = level * 30
    self.current_health = self.max_health
    self.ko = False
    self.trainer = None
    
  def lose_health(self, damage):
    low_limit = 0
    self.current_health = self.current_health - damage #inflict damage
    if self.current_health <= low_limit: #set low limit to 
      self.current_health = low_limit
      self.ko = True
      print('Your Pokemon has taken {} damage'.format(damage))
      print('Your Pokemon has been KO\'d')
    else:
      print('Your Pokemon has taken {} damage'.format(damage))
      
      
      
  def regen(self, potion):
    #keep count of healing inventory
    self.healing_potions = {
                      1: ['Pheonix Down', 10],
                      2: ['Max potion', 10], 
                      3: ['Normal potion', 10],
                      4: ['Exit', '']
    }
    self.potion = potion #User input to determine which potion to use
    
    #Pokemon revive, can only be used on pokemon that are KOd
    if self.potion == 1:
      if self.ko == True: #checks if Pokemon is KOd
        self.current_health = 10 #pheonix down on revives and adds 10pts to health
        self.ko = False #resets ko status to false
        self.healing_potions[1][1] -= 1 #removes item from list
        item = self.healing_potions[1][0]
        count = self.healing_potions[1][1]
        print('You used {item}'.format(item=item))
        print('You used {item}: {count} remaining'.format(count=count, item=item)) 
      else:
        print('Revive potions can only be used on a Pokemon that is KO\'d')
        hospital(self)
    
    #using potions 2 and 3
    if self.ko != True: #checks if Pokemon is KOd
      if self.potion > 1:
        self.healing_potions[self.potion][1] -= 1
        item = self.healing_potions[self.potion][0]
        count = self.healing_potions[self.potion][1]
        print('You used {item}: {count} remaining'.format(count=count, item=item))   
        
      if self.potion == 2:
        #restores health to 100%
        self.current_health = self.max_health
        
      elif self.potion == 3:
        #increases health by 50% of the difference between max and current health
        print('You used {item}'.format(item=item))
        self.current_health = self.current_health + ((self.max_health - self.current_health) * .5)
        
    else:
      print('Your Pokemon is KO\'d!\nyou must use a Revive potion!')
      

  def healing_items_list(self):
    return self.healing_potions

  def __str__(self): #String representation of pokemon
    if self.trainer == None:
      return '\nThis is a wild Pokemon!\nName:{name}\nLevel:{level}\nHealth: {current}/{max}max\nType:{types}'.format(name=self.name, level=self.level, current=self.current_health, max=self.max_health, types=self.poketype)
    else:
      return '\nName:{name}\nTrainer:{trainer}\nLevel:{level}\nHealth: {current}/{max}max\nType:{types}'.format(trainer=self.trainer, name=self.name, level=self.level, current=self.current_health, max=self.max_health, types=self.poketype)
#init entire program

def create_player():
  name = input('Please enter your initials: ')
  player_name = input('Please create a player name: ')
  player_saved = {name: player_name}
  #new_player = create_player()
  for i in player_saved: 
    p1 = Player(i, player_saved[i].upper())
  return p1

def start_program(): 
  
  #Prints the output in neat columns.
  print('Welcome to PokeChoose...')
  print('I am ANFANG, your Digital Guide...')
  print('You can choose 1 Pokemon to start...\n')
  time.sleep(3)
  os.system('cls')
  os.system('clear')


  col_w = [pokedex[items][0] for items in pokedex]
  colwid = max(len(i) for i in col_w)
  for item in pokedex:
    name = pokedex[item][0]
    level = pokedex[item][1]
    poketype = pokedex[item][2]
    print(name.ljust(colwid), str(level).center(colwid), poketype.ljust(colwid))

  choice = int(input('Pick your Pokemon (1-{pokedex_len}): '.format(pokedex_len=len(pokedex)-1)))
  print('\n')
  poke_pick = pokedex[choice]
  
  return poke_pick

def my_menu():
  menu = {
        1: 'My Pokemon',
        2: 'Health',
        3: 'Battle Arena',
        4: 'Quit'}
  os.system('clear')
  print('\n<------------Main Menu------------>\n')
  for item in menu:
    print('{item}>>{menu_item}'.format(item=item, menu_item=menu[item]).ljust(5))
  menu_choice = int(input('Choice >>> '))
  return menu_choice

def hospital(poke): #Pokemon hospital, where you can heal and revive your pokemon
  print('\nWelcome to the Poke Hosptial!\n')
  items_list = poke.healing_items_list()
  print('Your current available items:')
  print('\nItem', 'Quantity'.center(40))
  print('----', '--------'.center(40))
  col_width = [items_list[items][0] for items in items_list]
  column_width = max(len(i) for i in col_width)
  for item in items_list:
    print(items_list[item][0].ljust(column_width), str(items_list[item][1]).rjust(column_width))
  print(poke.name, '\nHealth: {current}/ {max}'.format(max=poke.max_health, current=poke.current_health))
  potion = int(input('What would you like to do(1-{length})? '.format(length=len(items_list))))
  if potion is not 4:
    poke.regen(potion)
  else:
    my_menu()


#creating player
def run():
  p1 = create_player()
  print('\nThank you for creating your player {name}\n'.format(name=p1.player_name))
  print('Player'.ljust(13), 'Pokemon Owned'.rjust(13))
  print(p1.player_name.ljust(13), p1.number_of_pokemon, '\n')
  return p1





current_player = run() #game start, create character   
keypress = input('continue? ')
clear_screen = os.system('cls')
os.system('clear')

poke_pick = start_program() #Pick you pokemon
add_poke = input('Would you like to add another Pokemon(Y/N)? ')
counter = 0 
while add_poke.lower != 'N':
  count += 1
  current_pokemon = Pokemon(poke_pick[0], poke_pick[1], poke_pick[2])
  current_player.add_pokemon(current_pokemon)

menu_choice = my_menu()

while menu_choice != 4:
  if menu_choice == 1:
    print(str(current_pokemon),'\n')
    keypress = input('continue? ')
    menu_choice = my_menu()
  elif menu_choice == 2:
    hospital(current_pokemon)
    #keypress = input('continue? ')
    clear_screen = os.system('cls')
    os.system('clear')
    menu_choice = my_menu()

