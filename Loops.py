import flask

#while loops just like JS
counter = 1
while (counter < 10):
    print (counter)
    counter = counter + 1
    
# For Loops
planets = ["Earth", "Mars", "Neptune", "Venus", "Mercury", "Saturn", "Jupiter", "Uranus"]
	
for i in planets:
    print(i)

# For in loop
planets = {"Earth": 40075, "Saturn": 378675, "Jupiter": 439264}

for planet in planets:
    print(planet, planets[planet])

# basic function syntax
def characterCount(test):
    count = len(test)
    print(count)

characterCount('bananas')

characterCount('test')