/*
 * tabulka _secondary_final
 */

CREATE OR REPLACE TABLE t_Lena_Oumrtova_project_SQL_secondary_final AS
SELECT
	c.country,
	e.year,
	e.gdp,
	e.gini
FROM countries c 
JOIN economies e 
	ON c.country = e.country 
	AND e.`year` BETWEEN 2006 AND 2018
;

SELECT *
FROM t_lena_oumrtova_project_sql_secondary_final;
