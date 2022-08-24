import random

# get the original three doors (winning door is marked with a '*')
def getDoors():
  doors = {}
  winDoor = random.randint(0, 2)
  for i in range(3):
    content = '-' # regular door
    if i == winDoor:
      content = '*' # winning door
    doors[str(i)] = content
  return doors

# get a new set of doors by removing the first non-winning door that is not 'pick1'
def getDoors2(doors, pick1):
  doors2 = doors.copy()
  for i in range(3):
    if str(i) == pick1:
      continue # cannot remove the picked door
    if doors2[str(i)] == '-':
      doors2.pop(str(i)) # remove the first non-winning door
      break
  return doors2

# pick a random door from 'doors'
def pick(doors):
  pickIdx = random.randint(0, len(doors) - 1)
  pick = list(doors)[pickIdx]
  return pick # pick is a string

# is pick a winning door?
def isWin(doors, pick):
  if doors[pick] == '*':
    return True
  return False

# simulation of a Monty Hall game
def simulation():
  doors = getDoors()
  pick1 = pick(doors)
  doors2 = getDoors2(doors, pick1)
  pick2 = pick(doors2)
  
  res1 = isWin(doors, pick1)
  res2 = isWin(doors, pick2)
  return (res1, res2)

#
# MAIN
#

countTotal = 100000
#random.seed(1)

count1 = 0
count2 = 0
for i in range(countTotal):
  res = simulation()
  if res[0]:
    count1 = count1 + 1
  if res[1]:
    count2 = count2 + 1    
    
print('# of winning when sticking with the first pick: ' + str(count1) + ' / ' + str(countTotal) + ' (' + str(round(count1 * 100 / countTotal)) + '%)')
print('# of winning when switching pick: ' + str(count2) + ' / ' + str(countTotal) + ' (' + str(round(count2 * 100 / countTotal)) + '%)')