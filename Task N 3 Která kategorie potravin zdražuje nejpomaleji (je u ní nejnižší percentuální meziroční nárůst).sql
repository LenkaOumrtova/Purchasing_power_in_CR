/*
 * č. 3 Která kategorie potravin zdražuje nejpomaleji (je u ní nejnižší percentuální meziroční nárůst)?
 */

SELECT
	t.food_name,
	t.`year`,
	t1.`year` AS previous_year,
	round((t.food_price - t1.food_price) / t1.food_price * 100, 1) AS food_price_growth
FROM t_lena_oumrtova_project_sql_primary_final t
JOIN t_lena_oumrtova_project_sql_primary_final t1 
	ON t.`year` = t1.`year` + 1
ORDER BY food_price_growth
;
