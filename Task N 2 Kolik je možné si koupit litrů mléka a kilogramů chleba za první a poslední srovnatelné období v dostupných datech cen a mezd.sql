SELECT 
	average_salary,
	payroll_year,
	food_name,
	food_price,
	round(average_salary / food_price) AS bread_number
FROM t_lenka_oumrtova_project_sql_primary_final tlopspf 
WHERE food_name LIKE ('%chléb%')
	AND payroll_year IN (2006, 2018)
GROUP BY payroll_year
;


SELECT 
	average_salary,
	payroll_year,
	food_name,
	food_price,
	round(average_salary / food_price) AS milk_number
FROM t_lenka_oumrtova_project_sql_primary_final tlopspf 
WHERE food_name LIKE ('%mléko%')
	AND payroll_year IN (2006, 2018)
GROUP BY payroll_year
;
