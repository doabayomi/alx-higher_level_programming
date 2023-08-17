-- Lists all cities by state
SELECT cities.id, cities.name, states.name FROM cities JOIN states
ORDER BY cities.id
