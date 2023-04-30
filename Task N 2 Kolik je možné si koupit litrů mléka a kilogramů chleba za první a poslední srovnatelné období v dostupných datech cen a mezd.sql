/* č. 2 Kolik je možné si koupit litrů mléka a kilogramů chleba za první a poslední srovnatelné období 
 * v dostupných datech cen a mezd?
 * 
 * první srovnávané období je rok 2006
 * poslední srovnávané období je rok 2018
 */

/*
 * chléb
 */
SELECT 
	average_salary,
	`year`,
	food_name,
	food_price,
	round((average_salary / food_price),0) AS bread_number
FROM t_lena_oumrtova_project_sql_primary_final
WHERE food_name LIKE ('%chléb%')
	AND `year` IN (2006, 2018)
GROUP BY `year`
;


/*
 * mléko
 */

SELECT 
	average_salary,
	`year`,
	food_name,
	food_price,
	round((average_salary / food_price),0) AS milk_number
FROM t_lena_oumrtova_project_sql_primary_final
WHERE food_name LIKE ('%mléko%')
	AND `year` IN (2006, 2018)
GROUP BY `year`
;

