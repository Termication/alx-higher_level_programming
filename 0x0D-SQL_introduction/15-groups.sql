-- Selects the number of records grouped by score from second_table.
-- Results are ordered by the count of records in descending order.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
