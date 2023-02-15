-- avg rows
SELECT city ,AVG(value) AS 'avg_tmp'
FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC LIMIT 3;
