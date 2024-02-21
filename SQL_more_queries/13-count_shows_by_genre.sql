-- jdnjen
SELECT tv_genres.genre AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_show_genres
JOIN (
    SELECT id, title
    FROM tv_shows
) AS tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
JOIN (
    SELECT id, genre
    FROM genres
) AS tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.genre
ORDER BY number_of_shows DESC;
