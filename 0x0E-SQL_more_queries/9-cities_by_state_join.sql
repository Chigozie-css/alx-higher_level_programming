-- Lists all cities in the database hbtn_0d_usa.
-- Records are sorted in order of ascending cities.id.
SELECT c.`id`, c.`name`, s.`name`
FROM `hbtn_0d_usa`.`cities` AS c
INNER JOIN `hbtn_0d_usa`.`states` AS s
ON c.`state_id` = s.`id`
ORDER BY c.`id`;
