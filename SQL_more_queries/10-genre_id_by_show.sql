-- wello there
SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tvshows.tv_shows
WHERE EXISTS (SELECT  1 FROM hbtn_0d_tvshows.tv_show_genres WHERE tv_show_genres.show_id = tv_shows.id)
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;