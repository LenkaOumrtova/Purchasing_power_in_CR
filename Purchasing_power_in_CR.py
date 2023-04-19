USE engeto_2023_02;


/*
 * czechia_payroll - Informace o mzdách v různých odvětvích za několikaleté období. 
 */
SELECT *
FROM czechia_payroll cp
WHERE value IS NOT NULL;

/*
 * czechia_payroll_calculation - Číselník kalkulací v tabulce mezd.
 */
SELECT *
FROM czechia_payroll_calculation;

/*
 * czechia_payroll_industry_branch - Číseslník kategorií v tabulce mezd.
 */
SELECT *
FROM czechia_payroll_industry_branch;

/*
 * czechia_payroll_unit - Číselník jednotek hodnot v tabulce mezd.
 */
SELECT *
FROM czechia_payroll_unit cpu;

/*
 * czechia_payroll_value_type - Číselník typů hodnot v tabulce mezd.
 */
SELECT *
FROM czechia_payroll_value_type cpvt;

/*
 * czechia_price - Informace o cenách vybraných potravin za několikaleté období.  
 */
SELECT *
FROM czechia_price;

/*
 * czechia_price_category - Názvy kategorií hodnot v tabulce cen.
 */
SELECT *
FROM czechia_price_category cpc;

/* VYSVĚTLIVKY:
 * statistical_variable = 316 počet zaměstnanců nebo 5958 průměrná mzda
 * statistical_unit = 200 KČ nebo 80403 tisíce osob
 * employee_code = 100 reálný počet zaměstnanců nebo 200 zaměstnanci přepočetni na hlavní prac.poměr
 * branch_code = kód odvětví: A Zemědělství, B Těžba, C Zpracovatelský prům., D Výroba a rozvod energií, 
 * 							  E Vodohospodářství, F Stavebnictví, G Obchod a údržba motorových vozidel,
 * 							  H Doprava a skladování, I Ubytování, stravování a pohostinství
 * 							  J IT, K Peněžnictví a pojišťovnictví, L Činnosti v oblasti nemovitostí
 * 							  M Profesní, vědecké a technické činnosti, N Administrativní a podpůrné činnosti
 * 							  O Veřejná správa a obrana, P Vzdělávání, Q Zdravotní a sociální péče
 * 							  R Kulturní, zábavní a rekreační činnosti, S Ostatní činnosti
 */

CREATE OR REPLACE TABLE t_Lenka_Oumrtova_project_SQL_primary_final AS
SELECT 
		pay.value AS average_salary,
		pay.value_type_code AS statistical_variable,
		pay.industry_branch_code AS branch_code,
		pay.payroll_year,
		price.category_code AS food_code,
		price.value AS food_price,
		price_cat.name AS food_name,
		price_cat.price_unit AS food_unit
	FROM czechia_payroll pay
	LEFT JOIN czechia_payroll_industry_branch branch
		ON pay.industry_branch_code = branch.code 
	JOIN czechia_payroll_unit unit 
		ON pay.unit_code = unit.code 
	JOIN czechia_price price 
		ON pay.payroll_year = year(price.date_from)
	JOIN czechia_price_category price_cat
		ON price.category_code = price_cat.code
	JOIN czechia_payroll_value_type value
		ON pay.value_type_code = value.code 
	WHERE value.code = '5958'
	AND pay.value IS NOT NULL 
	;


CREATE OR REPLACE TABLE t_Lenka_Oumrtova_project_SQL_secondary_final AS
SELECT
	c.country,
	c.abbreviation,
	c.avg_height,
	c.capital_city,
	c.continent,
	c.currency_name,
	c.religion,
	c.currency_code,
	c.domain_tld,
	c.elevation,
	c.north,
	c.south,
	c.west,
	c.east,
	c.government_type,
	c.independence_date,
	c.iso_numeric,
	c.life_expectancy,
	c.national_symbol,
	c.national_dish,
	c.population_density,
	c.region_in_world,
	c.surface_area,
	c.yearly_average_temperature,
	c.median_age_2018,
	c.iso2,
	c.iso3,
	e.year,
	e.gdp,
	e.population,
	e.gini,
	e.taxes,
	e.fertility,
	e.mortaliy_under5	
FROM countries c 
LEFT JOIN economies e 
	ON c.country = e.country 
;


SELECT *
FROM t_Lenka_Oumrtova_project_SQL_secondary_final
;


SELECT *
FROM t_Lenka_Oumrtova_project_SQL_primary_final 
;

/*
 * č. 1 Rostou v průběhu let mzdy ve všech odvětvích, nebo v některých klesají?
 */
SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'A'
GROUP BY payroll_year 
;

SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'B'
GROUP BY payroll_year 
;

SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'C'
GROUP BY payroll_year 
;

SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'D'
GROUP BY payroll_year 
;

SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'E'
GROUP BY payroll_year 
;

SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'F'
GROUP BY payroll_year 
;

SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'G'
GROUP BY payroll_year 
;

SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'H'
GROUP BY payroll_year 
;

SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'I'
GROUP BY payroll_year 
;

SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'J'
GROUP BY payroll_year 
;

SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'K'
GROUP BY payroll_year 
;

SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'L'
GROUP BY payroll_year 
;

SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'M'
GROUP BY payroll_year 
;

SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'N'
GROUP BY payroll_year 
;

SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'O'
GROUP BY payroll_year 
;

SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'P'
GROUP BY payroll_year 
;

SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'Q'
GROUP BY payroll_year 
;

SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'R'
GROUP BY payroll_year 
;

SELECT 
	average_salary,
	branch_code,
	payroll_year
FROM t_Lenka_Oumrtova_project_SQL_primary_final tlopspf
WHERE statistical_variable = '5958'
	AND payroll_year >= '2006' AND payroll_year <= '2018'
	AND branch_code = 'S'
GROUP BY payroll_year 
;


/*
 * č. 2 Kolik je možné si koupit litrů mléka a kilogramů chleba za první a poslední srovnatelné období 
 * v dostupných datech cen a mezd?
 * 
 * období s dostupnými daty je v případě mezd i cen 2006 - 2018
 * první srovnávané období je rok 2006
 * poslední srovnávané období je rok 2018
 */

/*
 * chléb
 */
SELECT 
	average_salary,
	payroll_year,
	food_name,
	food_price,
	round(average_salary / food_price) AS bread_number
FROM t_lenka_oumrtova_project_sql_primary_final tlopspf 
WHERE food_name LIKE ('%chléb%')
GROUP BY payroll_year;

/*
 * mléko
 */
SELECT 
	average_salary,
	payroll_year,
	food_name,
	food_price,
	round(average_salary / food_price) AS milk_number
FROM t_lenka_oumrtova_project_sql_primary_final tlopspf 
WHERE food_name LIKE ('%mléko%')
GROUP BY payroll_year
;


/*
 * č. 3 Která kategorie potravin zdražuje nejpomaleji (je u ní nejnižší percentuální meziroční nárůst)?
 */

SELECT 
	t1.food_name,
	t1.payroll_year,
	t2.payroll_year + 1 AS next_year,
	t1.food_price,
	min(round(t2.food_price / t1.food_price) * 100, 1) AS min_food_price_growth
FROM t_lenka_oumrtova_project_sql_primary_final t1
JOIN t_lenka_oumrtova_project_sql_primary_final t2
	ON t1.food_code = t2.food_code   
GROUP BY payroll_year
;


/*
 * č. 4 Existuje rok, ve kterém byl meziroční nárůst cen potravin výrazně vyšší než růst mezd (větší než 10 %)?
 */

SELECT 
	t1.payroll_year,
	CASE 
		WHEN min_food_price_growth - min_salary_growth >= 10 THEN hight
		ELSE low
	END AS  differenc_growth_prices_salary
FROM
(SELECT 
	t1.food_name,
	t1.payroll_year,
	t2.payroll_year + 1 AS next_year,
	t1.food_price,
	min(round(t2.food_price / t1.food_price) * 100, 1) AS min_food_price_growth
FROM t_lenka_oumrtova_project_sql_primary_final t1
JOIN t_lenka_oumrtova_project_sql_primary_final t2
	ON t1.food_code = t2.food_code   
GROUP BY payroll_year) AS prices
JOIN
(SELECT
	ts1.average_salary,
	ts1.payroll_year,
	ts2.payroll_year + 1 AS next_year,
	min(round(ts2.average_salary / ts1.average_salary) * 100, 1) AS min_salary_growth
FROM t_lenka_oumrtova_project_sql_primary_final ts1
JOIN t_lenka_oumrtova_project_sql_primary_final ts2
	ON ts1.statistical_variable = ts2.statistical_variable 
GROUP BY payroll_year) AS salary
ON prices.payroll_year = salary.payroll_year
ORDER BY t1.payroll_year
;

/*
 * č. 5 Má výška HDP vliv na změny ve mzdách a cenách potravin? 
 * Neboli, pokud HDP vzroste výrazněji v jednom roce, 
 * projeví se to na cenách potravin či mzdách ve stejném nebo násdujícím roce výraznějším růstem?
 */

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
