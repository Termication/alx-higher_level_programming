-- This query retrieves all TV shows and their associated genres from the
-- 'hbtn_0d_tvshows' database.
-- The results are sorted alphabetically by the show title and then by the genre name.

SELECT t.`title`, g.`name`
  FROM `tv_shows` AS t
       LEFT JOIN `tv_show_genres` AS s
       ON t.`id` = s.`show_id`
       LEFT JOIN `tv_genres` AS g
       ON s.`genre_id` = g.`id`
 ORDER BY t.`title`, g.`name`;
