
  #Magnus
      #Nils
          #Martin
              #Caroline
                  #Emma
                      #Samuel
                          #Viktor
                              #Jacob
                                  #Jonas
                                      #Sigrid
personPairScore = [
  [0, 3,  3,  1,  1,  1,  2,  2,  2,  3], #Magnus
  [3, 0,  3,  1,  1,  1,  2,  2,  2,  3], #Nils
  [3, 3,  0,  1,  1,  1,  2,  2,  2,  3], #Martin
  [1, 1,  1,  0,  1,  1,  1,  1,  1,  2], #Caroline
  [1, 1,  1,  1,  0,  1,  1,  1,  1,  2], #Emma
  [1, 1,  1,  1,  1,  0,  1,  1,  1,  1], #Samuel
  [1, 1,  1,  1,  1,  0,  0,  3,  3,  2], #Viktor
  [1, 1,  1,  1,  1,  0,  3,  0,  3,  2], #Jacob
  [1, 1,  1,  1,  1,  0,  3,  3,  0,  2], #Jonas
  [3, 3,  3,  2,  2,  1,  2,  2,  2,  0] #Sigrid
]

# One table of six and one table of four
# seats = [
#   [0, 0],
#   [1, 0],
#   [2, 0],
#   [0, 1],
#   [1, 1],
#   [2, 1],
#   [6, 0],
#   [7, 0],
#   [6, 1],
#   [7, 1],
# ]


def objectiveFunction(personOrder):
  p = personOrder
  r = range(len(p))
  return sum([personPairScore[p[j]][p[i]]*seatPairScore[j][i] for i in r for j in r])