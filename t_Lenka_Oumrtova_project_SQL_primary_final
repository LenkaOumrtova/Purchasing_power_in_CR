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

