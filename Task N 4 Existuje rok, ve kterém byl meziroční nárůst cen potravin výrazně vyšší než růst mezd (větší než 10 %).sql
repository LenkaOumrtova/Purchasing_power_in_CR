/*
 * č. 4 Existuje rok, ve kterém byl meziroční nárůst cen potravin výrazně vyšší než růst mezd (větší než 10 %)?
 */


SELECT
	t.`year`,
	t1.`year` AS previous_year,
	round((t.food_price - t1.food_price) / t1.food_price * 100, 1) AS food_price_growth,
	round((t.average_salary - t1.average_salary) / t1.average_salary * 100, 1) AS salary_growth
FROM t_lena_oumrtova_project_sql_primary_final t
JOIN t_lena_oumrtova_project_sql_primary_final t1 
	ON t.`year` = t1.`year` + 1
GROUP BY `year`
;
