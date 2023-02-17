-- my_genres
SELECT tv_genres.name AS 'name'
FROM tv_genres INNER JOIN tv_show_genres INNER JOIN tv_shows
ON tv_show_genres.genre_id = tv_genres.id AND tv_show_genres.show_id = tv_shows.id 
WHERE tv_shows.title = 'Dexter' 
ORDER BY tv_genres.name;
