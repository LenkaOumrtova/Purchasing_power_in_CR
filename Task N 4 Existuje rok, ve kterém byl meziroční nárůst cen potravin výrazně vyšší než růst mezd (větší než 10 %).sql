SELECT 
	t.payroll_year,
	CASE 
		WHEN min_food_price_growth - min_salary_growth >= 10 THEN hight
		ELSE low
	END AS  differenc_growth_prices_salary
FROM
(SELECT 
	t.food_name,
	t.payroll_year,
	t.payroll_year + 1 AS t.next_year,
	t.food_price,
	round (min((t2.food_price - t.food_price) / t.food_price * 100, 1)) AS food_price_growth
FROM t_lenka_oumrtova_project_sql_primary_final t
JOIN t_lenka_oumrtova_project_sql_primary_final t2
	ON t.food_code = t2.food_code   
GROUP BY t.food_name) AS prices
JOIN
(SELECT
	ts.average_salary,
	ts.payroll_year,
	ts.payroll_year + 1 AS ts.next_year,
	round (min((ts2.average_salary - ts.average_salary) / ts.average_salary * 100, 1)) AS min_salary_growth
FROM t_lenka_oumrtova_project_sql_primary_final ts
JOIN t_lenka_oumrtova_project_sql_primary_final ts2
	ON ts.statistical_variable = ts2.statistical_variable 
GROUP BY ts.average_salary) AS salary
ON prices.payroll_year = salary.payroll_year
ORDER BY t.next_year
;
