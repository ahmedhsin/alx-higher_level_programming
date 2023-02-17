-- count_shows_by_genre
SELECT name AS 'genre', COUNT(*) AS 'number_of_shows' 
FROM tv_genres INNER JOIN tv_show_genres 
ON id = genre_id GROUP BY genre_id 
ORDER BY COUNT(*) DESC;
