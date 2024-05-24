SELECT city, AVG(temperature) AS avg_temp
FROM temperature_data
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
