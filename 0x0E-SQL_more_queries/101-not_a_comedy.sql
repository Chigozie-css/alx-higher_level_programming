-- Lists all shows without the comedy genre in the database hbtn_0d_tvshows.
-- Records are ordered by ascending show title.
SELECT DISTINCT t.`title`
FROM `tv_shows` AS t
WHERE t.`id` NOT IN (
    SELECT s.`show_id`
    FROM `tv_show_genres` AS s
    INNER JOIN `tv_genres` AS g ON s.`genre_id` = g.`id`
    WHERE g.`name` = "Comedy"
)
ORDER BY t.`title`;
