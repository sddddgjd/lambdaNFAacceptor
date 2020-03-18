def byStep(x):
  return x["step"]

f = open("input.in", "r")
from collections import defaultdict

# read input
stari = int(f.readline())
nrCaractere = int(f.readline())
caractere = f.readline()
stareInit = f.readline().strip()
nrStariFinale = f.readline()
stariFinale = f.readline().strip().split(" ")
nrTranslatii = int(f.readline())


# map table with transitions from state to states
nextState = {}

for i in range(0, nrTranslatii):
  translatie = f.readline().strip().split(" ")
  prevState = translatie[0]
  caracter = translatie[1]
  stareFin = translatie[2]
  try:
    nextState[prevState][caracter].append(stareFin)
  except KeyError:
    newDict = {caracter: [stareFin]}
    if prevState in nextState:
      nextState[prevState].update(newDict)
    else:
      nextState[prevState] = newDict

teste = f.readlines()

for test in teste:
  #initialize variables for every test
  success = 0
  currentStep = 0
  start = 0
  end = 1
  #keep our current states in a queue
  coada = []
  coada.append({'step': 0, 'state': stareInit})
  test = test.strip()

  for char in test:
    #go through our current states and add the next state to our array
    
    while start < end and coada[start]["step"] == currentStep:

      #if it's a normal transition increase the current ste[]
      currentState = coada[start]["state"]

      if char in nextState[currentState]:
        for newState in nextState[currentState][char]:
          coada.append({'step': currentStep + 1, 'state': newState})
          end = end + 1

      #if we have a lambda transition we don't want to increase the current step
      #since a lambda transition doesn't read a character
      if '$' in nextState[currentState]:
        for newState in nextState[currentState]['$']:
          coada.append({'step': currentStep, 'state': newState})
          end = end + 1

      start = start + 1
      #sort again by step so things don't get messed up, could've done this better but lazy
      coada.sort(key=byStep)
    currentStep = currentStep + 1

  for i in range(start, end):
    if coada[i]["state"] in stariFinale:
      success = 1

  if success:
    print("DA")
  else:
    print("NU") 
