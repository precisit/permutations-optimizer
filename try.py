import random
import math
from matplotlib import pyplot as plt

discRadians = {
	"is":	15 * math.pi,
	"i":	 45 * math.pi,
	"id":	75 * math.pi,
	"di":	105 * math.pi,
	"d":	 135 * math.pi,
	"dc":	165 * math.pi,
	"cd":	195 * math.pi,
	"c":	 225 * math.pi,
	"cs":	255 * math.pi,
	"sc":	285 * math.pi,
	"s":	 315 * math.pi,
	"si":	345 * math.pi,
}

people = [
	# {
	# 	"name": "Sigrid",
	# 	"months": 45,
	# "disc": "c"
	# },
	{
		"name": "Samuel",
		"months": 16,
		"disc": "c"
	},
	{
		"name": "Jacob",
		"months": 23,
		"disc": "c"
	},
	# {
	# 	"name": "Kajsabet",
	# 	"months": 25,
	# "disc": "c"
	# },
	{
		"name": "Jonas",
		"months": 25,
		"disc": "c"
	},
	{
		"name": "Siri",
		"months": 17,
		"disc": "c"
	},
	# {
	# 	"name": "Caroline",
	# 	"months": 24,
	# "disc": "c"
	# },
	{
		"name": "Kerstin",
		"months": 18,
		"disc": "c"
	},
	{
		"name": "Magnus",
		"months": 51,
		"disc": "c"
	},
	{
		"name": "Martin",
		"months": 35,
		"disc": "c"
	},
	{
		"name": "Emma",
		"months": 14,
		"disc": "c"
	},
	{
		"name": "Karolin",
		"months": 3,
		"disc": "c"
	},
	{
		"name": "Marika",
		"months": 7,
		"disc": "c"
	},
	{
		"name": "Simon",
		"months": 9,
		"disc": "c"
	},
]

# Coordinates of seats
seats = [
	[0, 0],
	[1, 0],
	[2, 0],
	[3, 0],
	[4, 0],
	[5, 0],
	# [6, 0],
	# [7, 0],
	[0, 1],
	[1, 1],
	[2, 1],
	[3, 1],
	[4, 1],
	[5, 1],
	# [6, 1],
	# [7, 1]
]

names = [person["name"] for person in people]
monthsInCompany = [person["months"] for person in people]
discProfiles = [person["disc"] for person in people]

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

def timeDifferenceObjectiveFunction(personOrder):
	p = personOrder
	r = range(len(p))
	return sum([-abs(monthsInCompany[p[j]] - monthsInCompany[p[i]])*seatPairScore[j][i] for i in r for j in r])

def discDifferenceObjectiveFunction(personOrder):
	p = personOrder
	r = range(len(p))
	d1 = discRadians[discProfiles[p[i]]]
	d2 = discRadians[discProfiles[p[j]]]

	x1 = cos(d1)
	y1 = sin(d1)
	x2 = cos(d2)
	y2 = sin(d2)

	return sum(((x1-x2)^2 + (y1-y2)^2)*seatPairScore[j][i] for i in r for j in r])

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

	temperature = 3000
	alpha = 0.999

	bestCost = float("inf")
	bestPersonOrder = []

	iAll = range(100)
	costs = list(iAll)

	for i in iAll:
		newPersonOrder = getNewPersonOrder(personOrder)

		cost1 = discDifferenceObjectiveFunction(personOrder)
		cost2 = discDifferenceObjectiveFunction(newPersonOrder)

		costs[i] = cost1

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

	plt.subplot(2, 1, 1)
	plt.plot(iAll, [-x for x in costs])

	ax = plt.subplot(2, 1, 2)
	for i, name in enumerate([names[i] for i in personOrder]):
		x = seats[i][0]
		y = seats[i][1]
		ax.text(x, y, name)

		ax.plot(x-1, y, '.w')
		ax.plot(x, y-1, '.w')
		ax.plot(x+1, y, '.w')
		ax.plot(x, y+1, '.w')



	plt.show()
