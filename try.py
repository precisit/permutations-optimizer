import random
import math

names = [
	"Magnus",
	"Nils",
	"Martin",
	"Caroline",
	"Emma",
	"Samuel"
]

	#Magnus
		#Nils
			#Martin
				#Caroline
					#Emma
						#Samuel
personPairScore = [
	[0,	3,	3,	1,	1,	1], #Magnus
	[3,	0,	3,	1,	1,	1], #Nils
	[3,	3,	0,	1,	1,	1], #Martin
	[1,	1,	1,	0,	1,	1], #Caroline
	[1,	1,	1,	1,	0,	1], #Emma
	[1,	1,	1,	1,	1,	0], #Samuel
]

seats = [
	[0, 0],
	[1, 0],
	[2, 0],
	[0, 1],
	[1, 1],
	[2, 1]
]

def getSeatPairScore(seats):
	seatPairScore = [[] for seat in seats]

	for i1, seat1 in enumerate(seats):
		x1 = seat1[0]
		y1 = seat1[1]

		for i2, seat2 in enumerate(seats):
			x2 = seat2[0]
			y2 = seat2[1]

			delta = (x2-x1)**2 + (y2-y1)**2

			weight = 0
			if (delta == 1):
				weight = 4
			elif (delta == 2):
				weight = 3

			seatPairScore[i1].append(weight)

	return seatPairScore

def objectiveFunction(personOrder, personPairScore, seatPairScore):
	p = personOrder
	r = range(len(p))
	return sum([personPairScore[p[j]][p[i]]*seatPairScore[j][i] for i in r for j in r])

def getNewPersonOrder(personOrder):
	n = len(personOrder)
	newPersonOrder = list(personOrder)

	i = random.randint(0, n - 1)
	j = random.randint(0, n - 1)

	newPersonOrder[i], newPersonOrder[j] = personOrder[j], personOrder[i]

	return newPersonOrder


if __name__ == '__main__':
	random.seed(0)
	seatPairScore = getSeatPairScore(seats)

	n = len(names)
	personOrder = range(n)
	# personOrder = [0,3,1,4,2,5]

	temperature = sum([sum(s) for s in personPairScore])
	alpha = 0.99

	bestCost = float("inf")
	bestPersonOrder = []

	for r in range(500):
		newPersonOrder = getNewPersonOrder(personOrder)

		cost1 = objectiveFunction(personOrder, personPairScore, seatPairScore)
		cost2 = objectiveFunction(newPersonOrder, personPairScore, seatPairScore)

		costDelta = cost2 - cost1

		print cost1, [names[i] for i in personOrder]

		if cost1 < bestCost:
			bestPersonOrder = personOrder
			bestCost = cost1

		if cost2 < bestCost:
			bestPersonOrder = newPersonOrder
			bestCost = cost2

		if costDelta <= 0 or math.exp(-costDelta/temperature) > random.random():
			personOrder = newPersonOrder


		temperature = temperature*alpha

	print "**************"
	print bestCost, [names[i] for i in personOrder]
