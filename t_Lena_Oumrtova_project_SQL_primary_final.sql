/*
 * tabulka payroll
 */
SELECT 
	pay.payroll_year,
	pay.value AS average_salary,
	branch.name AS branch_name,
	pay.industry_branch_code AS branch_code
FROM czechia_payroll pay
JOIN czechia_payroll_industry_branch branch
	ON pay.industry_branch_code = branch.code  
	AND pay.value_type_code = '5958'
	AND pay.payroll_year BETWEEN 2006 AND 2018
GROUP BY pay.payroll_year, pay.industry_branch_code
;

CREATE OR REPLACE TABLE t_Lena_Oumrtova_project_SQL_payroll 
(
	payroll_year int,
	value int,
	branch_name varchar(128),
	branch_code char(1)
);


INSERT INTO t_Lena_Oumrtova_project_SQL_payroll 
(SELECT
    pay.payroll_year,
	pay.value AS average_salary,
	branch.name AS branch_name,
	pay.industry_branch_code AS branch_code
FROM czechia_payroll pay
JOIN czechia_payroll_industry_branch branch
	ON pay.industry_branch_code = branch.code  
	AND pay.value_type_code = '5958'
	AND pay.payroll_year BETWEEN 2006 AND 2018
GROUP BY pay.payroll_year, pay.industry_branch_code
);

/*
 * tabulka prices
 */
SELECT 
	price.value AS food_price,
	year(price.date_from) AS `year`,
	price_cat.name AS food_name
FROM czechia_price price
JOIN czechia_price_category price_cat
	ON price.category_code = price_cat.code 
	AND region_code IS NULL
	AND year(price.date_from) BETWEEN 2006 AND 2018
GROUP BY year(price.date_from), price_cat.name 
;

CREATE OR REPLACE TABLE t_Lena_Oumrtova_project_SQL_prices 
(
	food_price float,
	year int,
	food_name varchar(128)
);

INSERT INTO t_Lena_Oumrtova_project_SQL_prices 
(SELECT 
	price.value AS food_price,
	year(price.date_from) AS `year`,
	price_cat.name AS food_name
FROM czechia_price price
JOIN czechia_price_category price_cat
	ON price.category_code = price_cat.code 
	AND region_code IS NULL
	AND year(price.date_from) BETWEEN 2006 AND 2018
GROUP BY year(price.date_from), price_cat.name 
);

/*
 * tabulka _primary_final
 */

 CREATE OR REPLACE TABLE t_Lena_Oumrtova_project_SQL_primary_final
 (
    year int,
    average_salary int,
	branch_name varchar(128),
	branch_code char(1),
    food_price float,
    food_name varchar(128),
    GDP float
);

INSERT INTO t_Lena_Oumrtova_project_SQL_primary_final
(SELECT
    payroll. *,
	prices.food_price,
	prices.food_name,
	e.GDP
FROM t_Lena_Oumrtova_project_SQL_payroll AS payroll
JOIN t_Lena_Oumrtova_project_SQL_prices AS prices
    ON payroll.payroll_year = prices.YEAR
JOIN economies e 
	ON payroll.payroll_year = e.`year`
	AND e.country = 'Czech Republic'
);

SELECT *
FROM t_lena_oumrtova_project_sql_primary_final ;




