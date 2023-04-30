/*
 * č. 5 Má výška HDP vliv na změny ve mzdách a cenách potravin? 
 * Neboli, pokud HDP vzroste výrazněji v jednom roce, 
 * projeví se to na cenách potravin či mzdách ve stejném nebo násdujícím roce výraznějším růstem?
 */

SELECT
	t.`year`,
	t1.`year` AS previous_year,
	round((t.food_price - t1.food_price) / t1.food_price * 100, 1) AS food_price_growth,
	round((t.average_salary - t1.average_salary) / t1.average_salary * 100, 1) AS salary_growth,
	round((t.GDP - t1.GDP) / t1.GDP  * 100,1) AS gdp_growth
FROM t_lena_oumrtova_project_sql_primary_final t
JOIN t_lena_oumrtova_project_sql_primary_final t1 
	ON t.`year` = t1.`year` + 1
GROUP BY `year`
;
