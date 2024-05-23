-- This script lists all Comedy shows in the specified database.
-- Results are sorted in ascending order by the show title.

SELECT t.title
FROM tv_shows AS t
INNER JOIN tv_show_genres AS s
ON t.id = s.show_id
INNER JOIN tv_genres AS g
ON s.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY t.title;
