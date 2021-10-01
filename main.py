








def numeralsToInt(userNumList: str) -> int:

  numeralDictionary = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
  }
  numeralToConvert = userNumList

  total = 0
  previousNumeral = 0
  currentNumeral = 0

  for x in range (len(numeralToConvert)):
    currentNumeral = numeralDictionary[numeralToConvert[x]]
    if currentNumeral > previousNumeral:
      total = total + currentNumeral - 2 * previousNumeral

    else:
      total += currentNumeral
    
    previousNumeral = currentNumeral
    x+=1

  print (numeralToConvert," is equal too ", total)

userInp =input("Please enter a Roman Numeral: ").upper()
userNumList = list(userInp)

numeralsToInt( userNumList = userInp )