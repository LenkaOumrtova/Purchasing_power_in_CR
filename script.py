"""
USE engeto_2023_02;
/*
* czechia_payroll - Informace o mzdách v různých odvětvích za několikaleté období.
*/
SELECT *
FROM czechia_payroll cp;
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
* \t\t\t\t\t\t\t  E Vodohospodářství, F Stavebnictví, G Obchod a údržba motorových vozidel,
* \t\t\t\t\t\t\t  H Doprava a skladování, I Ubytování, stravování a pohostinství
* \t\t\t\t\t\t\t  J IT, K Peněžnictví a pojišťovnictví, L Činnosti v oblasti nemovitostí
* \t\t\t\t\t\t\t  M Profesní, vědecké a technické činnosti, N Administrativní a podpůrné činnosti
* \t\t\t\t\t\t\t  O Veřejná správa a obrana, P Vzdělávání, Q Zdravotní a sociální péče
* \t\t\t\t\t\t\t  R Kulturní, zábavní a rekreační činnosti, S Ostatní činnosti
*
*
*/
CREATE TABLE t_Lenka_Oumrtova_project_SQL_primary_final AS
SELECT
pay.id AS id,
pay.value AS average_salary,
pay.value_type_code AS statistical_variable,
pay.unit_code AS statistical_unit,
pay.calculation_code AS employee_code,
pay.industry_branch_code AS branch_code,
pay.payroll_year,
price.category_code AS food_code,
price_cat.name AS food_name,
price_cat.price_unit AS food_unit
FROM czechia_payroll pay
LEFT JOIN czechia_payroll_industry_branch branch
ON pay.industry_branch_code = branch.code
JOIN czechia_payroll_unit unit
ON pay.unit_code = unit.code
JOIN czechia_payroll_value_type value
ON pay.value_type_code = value.code
JOIN czechia_price price
ON pay.payroll_year = year(price.date_from)
JOIN czechia_price_category price_cat
ON price.category_code = price_cat.code
;
"""


