-- 10-genre_id_by_show.sql
SELECT title, genre_id
FROM tv_shows INNER JOIN tv_show_genres
ON id = show_id
ORDER BY title, genre_id;

