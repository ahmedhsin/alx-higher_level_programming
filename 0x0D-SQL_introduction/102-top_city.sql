-- avg rows
SELECT city ,AVG(value) AS 'avg_temp'
FROM temperatures
where month in (7, 8)
GROUP BY city
ORDER BY AVG(value) DESC LIMIT 3;
