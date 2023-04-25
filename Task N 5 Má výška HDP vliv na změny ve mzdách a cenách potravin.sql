SELECT
	t.payroll_year,
	e.GDP,
	t.food_name,
	t.food_price,
	t.average_salary
FROM 
(SELECT
	country,
	round(GDP,0) AS GDP,
	`year`
FROM economies e 
WHERE country = 'Czech Republic'
	AND GDP IS NOT NULL
	AND `year` >= '2006' AND `year` <= '2018') AS GDP_resume
JOIN 
	ON e.`year` = t.payroll_year
(SELECT
	food_name,
	food_price,
	average_salary,
	payroll_year
FROM t_lenka_oumrtova_project_sql_primary_final t
WHERE food_price IN (
	SELECT avg(value)
	FROM czechia_price)
	AND statistical_variable = '5958') AS food_salary_resume
GROUP BY payroll_year
ORDER BY payroll_year
;
