-- hehehehe 
SELECT tv_shows.title,
       (SELECT tv_show_genres.genre_id FROM @database_name.tv_show_genres WHERE tv_show_genres.show_id = tv_shows.id) AS genre_id
FROM @database_name.tv_shows
ORDER BY tv_shows.title ASC, genre_id ASC;