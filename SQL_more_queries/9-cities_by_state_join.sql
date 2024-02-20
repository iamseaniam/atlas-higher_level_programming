-- helo
SELECT cities.id, cities.name, (SELECT states.name FROM hbtn_0d_usa.states WHERE states.id = cities.state_id) AS state_name
FROM hbtn_0d_usa.cities
ORDER BY cities.id ASC;