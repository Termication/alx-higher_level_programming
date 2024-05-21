-- Selects all records from second_table where the name is not empty.
-- Results are ordered by score in descending order.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
