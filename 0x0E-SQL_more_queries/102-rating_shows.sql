-- This query selects all TV shows from the 'hbtn_0d_tvshows_rate' database along with their total rating.
-- The results are sorted in descending order based on the rating.

SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS t
       INNER JOIN `tv_show_ratings` AS r
       ON t.`id` = r.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;
