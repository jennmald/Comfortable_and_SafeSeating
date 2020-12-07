###############################
## Jennefer Maldonado        ##
## Date Due: December 3 2020 ##
###############################

import numpy as np

class Safe_Seating:
	def __init__(self):
		# holds a seat array
		self.seats = None
		# the number of seats in a row
		self.N = None
		# the current person to sit
		self.person = 1
		# store the number of max possible seats
		self.max_arrangement = 0
		#the number of times the max seating occurs
		self.total_max = 0

	# initializes the number of given seats to zero
	# zero will denote that a seat is not taken
	def set_seats(self, n):
		self.seats = np.zeros((1,n))[0]
		self.N = n

	# places a person in a seat 
	# (mostly for testing)
	def sit(self, p):
		self.seats[p] = self.person
		self.person +=1

	# determines if a seat is taken
	# 0 - False, seat is open
	# anything else - True, seat is taken
	def is_taken(self, seat_number):
		if self.seats[seat_number] == 0:
			return False
		else:
			return True

	# determines if a seat has two neighbors
	# if it does returns true
	# if it doesn't returns false
	def has_neighbors(self, seat_number):
		# special cases 0, or leftmost seat
		if seat_number == 0:
			right_seat = seat_number + 1
			if self.is_taken(right_seat):
				# has a neighbor
				return True
			else:
				return False
		# special cases N or rightmost seat
		elif seat_number == self.N-1:
			left_seat = seat_number - 1
			if self.is_taken(left_seat):
				# has a neighbor
				return True
			else:
				return False
		# all other seats have a left and right seat
		else:
			right_seat = seat_number + 1
			left_seat = seat_number - 1
			if self.is_taken(left_seat) or self.is_taken(right_seat):
				# has a neighbor
				return True
			else:
				return False

	# Used to empty the current seating arrangement
	def clear_seats(self):
		c = len(self.seats)
		self.seats = np.zeros((1,c))[0]
		self.person = 1

	# Used to empty the maximums for summations
	def clear_max(self):
		self.max_arrangement = 0
		self.total_max = 0

	# Computes what the next farthest seat is from the current
	# Parameters: None, checks the list from the class for who
	# is currently sitting
	# Returns: the next availiable seat
	def farthest_seat(self):
		# how many seats are in total for loops
		l = len(self.seats)
		# create an empty list to store distances
		seat_dist = []
		# make the list the same size as the seats array
		# set everything greater than the number of seats
		# for distance comparisons later
		for i in range(0,l):
			seat_dist.append(self.N + 1)
		# loop through each seat
		for s in range(0, l):
			#check if the seat is taken
			if self.is_taken(s):
				# if it's taken set it's value to -1
				# this way it won't be considered the
				# next loop around
				seat_dist[s]=-1
				# check all distances of seats around a taken seat
				for t in range(0,l):
					dist = abs(s-t)
					# if the distance is 1 it's the neighbor
					# neighbors are not checked due to rule 1
					if dist == 1:
						seat_dist[t] = -1
					else:
						# if the seat is open update minimum distance
						if seat_dist[t] != -1:
							if dist <= seat_dist[t]:
								seat_dist[t] = dist
		# variables for storing final results
		left_max_dist = 0
		new_seat = 0
		# verify that the algorithm is done
		# -1 for all seats means none are available
		negative = all(s == -1 for s in seat_dist)
		if negative:
			# sets the new seat to -1
			new_seat = -1
		else:
		# loop through in reverse
		# start at l and end at 1, decrementing by 1
			for d in range(l-1,-1,-1):
				if seat_dist[d] >= left_max_dist:
					left_max_dist= seat_dist[d]
					new_seat = d
		#return the leftmost seat
		return new_seat

	def is_max_arrangement(self, seat_array):
		people = max(seat_array)
		if people > self.max_arrangement:
			self.max_arrangement = people
			self.total_max = 1
		elif people == self.max_arrangement:
			self.total_max += 1
		#else:
			#do nothing

	# function that handles the seating arrangements
	# starts at first seat and sits the first person
	# at a new seat each time, then generalizes
	# the seating arrangement using the farthest
	# seat function
	def arrange(self):
		first_seat = 0
		# ensure the first person sits in every seat
		# at least once
		while first_seat < self.N:
			self.sit(first_seat)
			i = 0
			# iterate through until the farthest
			# seat is -1, this means the arrangement
			# has been found
			while i < self.N:
				next_seat = self.farthest_seat()
				if next_seat == -1:
					#terminates when all seats are taken
					i = self.N+1;
				else:
					self.sit(next_seat)
				i+=1
			# display for testing
			#print(self.seats)
			# check max arrangement values
			self.is_max_arrangement(self.seats)
			# clear seats for new arrangement
			self.clear_seats()
			# move first person over one seat
			first_seat += 1
		return(self.total_max)

	# finds the summation values where N is the 
	# upper bound, the lower bound by default is 1
	# returns the value of the summation
	def sums(self, N):
		total_sum = 0
		# start with one seat and go to N seats
		for n in range(1, N+1):
			self.set_seats(n) # set the seats
			current_sum = self.arrange() # arrange
			# add to the total sum
			total_sum = total_sum + current_sum 
			# clear each time to restart the count
			self.clear_max()
		# return
		return total_sum

# Create object
test_seats = Safe_Seating()
# To print the seating arrangements for N = 15
# uncomment these two lines and line 170
#test_seats.set_seats(15)
#test_seats.arrange()

# To print the sum of maximum seating arrangements from 1 to 20
# uncomment this line
print(test_seats.sums(20))

# To print the sum of maximum seating arrangements from 1 to 500
# uncomment this line
#print(test_seats.sums(500))

