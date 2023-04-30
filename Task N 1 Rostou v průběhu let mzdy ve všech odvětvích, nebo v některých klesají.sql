/*
 * č. 1 Rostou v průběhu let mzdy ve všech odvětvích, nebo v některých klesají?
 */

SELECT 
	branch_code,
	average_salary,
	year
FROM t_lena_oumrtova_project_sql_primary_final
WHERE branch_code IS NOT NULL 
GROUP BY branch_code, year 
;
