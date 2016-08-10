persons = [
	{
		"name": "A"
	},
	{
		"name": "B"
	}
]

seats = {
	1: {
		"person": 0,
		"neighboringSeats": [2]
	},
	2: {
		"person": 0,
		"neighboringSeats": [1, 3]
	},
	3: {
		"person": 0
		"neighboringSeats": [2]
	}
}

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
	assignSeats(persons, seats)
	print seats
