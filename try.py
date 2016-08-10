names = [
	"Alice",
	"Bob",
	"Chloe",
	"Daniel"
]

	#Alice
		#Bob
			#Chloe
				#Daniel
pairScore = [
	[0,	1,	2,	1], #Alice
	[1, 0,	1,	2], #Bob
	[2,	1,	0,	1], #Chloe
	[1,	2,	1,	0] #Daniel
]

seats = [
	[0, 0],
	[1, 0],
	[1, 1],
	[2, 0]
]

def getSeatNeighbors(seats):
	seatNeighborIndexes = [[] for seat in seats]

	for i1, seat1 in enumerate(seats):
		x1 = seat1[0]
		y1 = seat1[1]

		for i2, seat2 in enumerate(seats):
			x2 = seat2[0]
			y2 = seat2[1]

			delta = (x2-x1)**2 + (y2-y1)**2

			print seat1, seat2, delta



def getPerson(seat):
	pass

def getSeat(person):
	pass

def getNeighboringSeats(seat):
	pass

def getNeighboringPersons(person):
	pass

def assignSeats(persons, seats):
	personKeys = persons.keys()
	for i, seatKey in enumerate(seats.keys()):
		seats[seatKey]["person"] = persons[personKeys[i]]



if __name__ == '__main__':
	getSeatNeighbors(seats)
	# print seats
