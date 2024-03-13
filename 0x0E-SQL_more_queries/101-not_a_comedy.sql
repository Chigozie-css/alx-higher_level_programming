-- Lists all shows without the comedy genre in the database hbtn_0d_tvshows.
-- Records are ordered by ascending show title.
SELECT DISTINCT t.`title`
FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS s ON t.`id` = s.`show_id`
LEFT JOIN `tv_genres` AS g ON s.`genre_id` = g.`id` AND g.`name` = "Comedy"
WHERE g.`id` IS NULL
ORDER BY t.`title`;
