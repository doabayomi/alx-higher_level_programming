-- Showing the cities in california
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California")
ORDER BY id;
