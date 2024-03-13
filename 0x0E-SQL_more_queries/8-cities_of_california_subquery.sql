-- Lists all cities of CA in the database hbtn_0d_usa.
-- Results are ordered by ascending cities.id.
SELECT `id`, `name`
FROM `hbtn_0d_usa`.`cities`
WHERE `state_id` = (
	SELECT `id`
	FROM `hbtn_0d_usa`.`states`
	WHERE `name` = "California"
)
ORDER BY `id`;
