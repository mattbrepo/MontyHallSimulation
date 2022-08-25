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

# open a door that is not 'pick1' and get the door in case the participant switches door
def openDoor(doors, pick1):
  pick2 = ''
  if doors[pick1] == '*':
    # --- the participant picked the winning one
    altIdx = random.randint(0, 1)
    altCount = 0
    for i in range(3):
      if str(i) == pick1:
        continue # cannot open the picked door
      if altCount == altIdx:
        pick2 = str(i) # in case the participant switches door
        break
      altCount = altCount + 1

  else:
    # --- the participant didn't pick the winning one
    for i in range(3):
      if str(i) == pick1:
        continue # cannot open the picked door
      if doors[str(i)] == '*':
        pick2 = str(i) # in case the participant switches door
        break

  return pick2

# is pick a winning door?
def isWin(doors, pick):
  if doors[pick] == '*':
    return True
  return False

# simulation of a Monty Hall game
def simulation():
  # get the three doors
  doors = getDoors()
  
  # pick a random door from 'doors'
  pick1 = str(random.randint(0, 2))

  # open the door
  pick2 = openDoor(doors, pick1)
  
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

print('number of winning game when sticking with the first door: ' + str(count1) + ' / ' + str(countTotal) + ' (' + str(round(count1 * 100 / countTotal)) + '%)')
print('number of winning game when switching door: ' + str(count2) + ' / ' + str(countTotal) + ' (' + str(round(count2 * 100 / countTotal)) + '%)')