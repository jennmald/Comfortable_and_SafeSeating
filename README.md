# Comfortable_and_SafeSeating

## Final Project for AMS 595

### Jennefer Maldonado

The Covid-19 pandemic took away many of our favorite social events such as sporting events, concerts, graduations, and movies. It is a sacrifice we are all making to ensure public health. Technology can be used to develop algorithms to determine how we can host these events again at a safe social distance. Project Euler’s website describes a problem called Comfortable Distance II (https://projecteuler.net/problem=472). With a row of N seats available the task is to determine how an undetermined number of people can sit at a safe distance from each other. 

There are some rules:
1. No person sits beside another.
2. The first person chooses any seat.
3. Each subsequent person chooses the seat furthest from anyone else already seated if it does not violate rule 1. If there is more than one choice satisfying this condition, then the person chooses the leftmost choice.

With the use of the Safe Seating class any row of seats can be analyzed to find an optimal seating arrangement. I hope that one day an algorithm of this kind can be used in the real world to aid in the effort to curb the spread of Covid-19.
