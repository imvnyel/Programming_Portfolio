'''The point of this program was to practice creating, accessing, and modifying dicitonaries created 04-2020 by Emmanuel Kaunda'''

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {k:v for k,v in zip(letters, points)}
letter_to_points.update({' ': 0})




def score_word(word):
  point_total = 0
  for i in word:
    if i.upper() in letter_to_points:
      point_total = point_total + letter_to_points[i]
  return point_total


player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 
'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 
'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 
'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

player_to_points = {}

def update_point_totals(player_to_words):
  #player_to_points = {}
  for i in player_to_words:
    player_points = 0
    player = i
    words = player_to_words[i]
    for word in words:
      x = score_word(word)
      player_points = player_points + score_word(word)
      if i in player_to_points:
        player_to_points[i].append(player_points)
      else:
        player_to_points.update({i: [player_points]})
  return player_to_points

players = ['player1' , 'dARKwingdrunk420','mcgILLagorILLa', 'FASTUDIOUS'] 
words = ['GRANDIOUS', 'MISSIONARY', 'FASTUDIOUS']

def play_word(players, word):
  for k,v in zip(players, words):
    if k in player_to_words:
      player_to_words[k].append(v)
    else:
      player_to_words.update({k:[v]})
  return

play_word(players, words)
xx = update_point_totals(player_to_words)

for k in player_to_points:
    print("{k} scored {v} points with the word: {w}".format(k=k, v=player_to_points[k][-1], w=player_to_words[k][-1]))