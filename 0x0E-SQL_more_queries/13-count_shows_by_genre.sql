-- This query retrieves all genres from the database 'hbtn_0d_tvshows' and counts the number of TV shows associated with each genre.
-- It filters out genres that have no associated TV shows.
-- The results are sorted in descending order based on the number of associated TV shows.

SELECT g.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS t
       ON g.`id` = t.`genre_id`
 GROUP BY g.`name`
 ORDER BY `number_of_shows` DESC;
