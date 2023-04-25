
SELECT 
	t.food_name,
	t.payroll_year,
	t.payroll_year + 1 AS next_year,
	round (min((t2.food_price - t.food_price) / t.food_price * 100, 1)) AS food_price_growth
FROM t_lenka_oumrtova_project_sql_primary_final t
JOIN t_lenka_oumrtova_project_sql_primary_final t2
	ON t.food_code = t2.food_code 
	AND t.payroll_year = t2.payroll_year + 1
	AND t.payroll_year <=2018 
ORDER BY food_name
;
