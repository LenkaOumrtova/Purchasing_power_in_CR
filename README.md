Lenka Oumrtová
Datová akademie ENGETO
SQL Projekt

Kupní síla v České republice

Obsah
Zadání projektu
Výzkumné otázky
Výstup
Poznámky k řešení

1. Zadání projektu
	Projekt týkající se životní úrovní občanů, jehož cílem je zjištění dostupnosti základních potravin široké veřejnosti. Prostřednictvím vydefinovaných otázek bude analyzována životní úroveň občanů ČR. Zodpovězené otázky a výsledky analýzy bude tiskové oddělení následně prezentovat na tiskové konferenci. Pro realizaci analýzy je třeba připravit robustní datové podklady, ve kterých bude možné vidět porovnání dostupnosti potravin na základě průměrných příjmů za určité časové období.
	Jako dodatečný materiál je třeba připravit i tabulku s HDP, GINI koeficientem a populací dalších evropských států ve stejném období, jako primární přehled pro ČR.

2. Výzkumné otázky
	1. Rostou v průběhu let mzdy ve všech odvětvích, nebo v některých klesají?
		- z dlouhodobého hlediska rostou mzdy ve všech odvětvích
		- z roku na rok v některých odvětvích klesly, viz tabulka a přiložený pomocný excel soubor

	2. Kolik je možné si koupit litrů mléka a kilogramů chleba za první a poslední srovnatelné období v dostupných datech cen a mezd?
		- chléb 2006: 723 ks, 2018: 916 ks
		- mléko 2006: 871 ks, 2018: 1117 ks

	3. Která kategorie potravin zdražuje nejpomaleji (je u ní nejnižší percentuální meziroční nárůst)?
		- Jogurt bílý netučný.

	4. Existuje rok, ve kterém byl meziroční nárůst cen potravin výrazně vyšší než růst mezd (větší než 10 %)?
		- ano, bylo to v letech 2014 (z roku 2013) a 2018 (z roku 2017)

	5. Má výška HDP vliv na změny ve mzdách a cenách potravin? Neboli, pokud HDP vzroste výrazněji v jednom roce, projeví se to na cenách potravin či mzdách ve 		stejném nebo následujícím roce výraznějším růstem?
		- jelikož pro výrazný růst nebyl stanoven přesný koeficient v úkolu č. 5, byl stanoven při vypracování na limit 5 % a v takovém případě je odpověď ano:
		- v r. 2007 vzrostl GDP o 5,6 %, to ovlivnilo v témže i následujícím roce růst mezd a pokles cen
		- v r. 2015 vzrostl GDP o 5,4 %, to ovlivnilo v témže roce pokles cen a v následujícím mírnější růst mezd
		- v r. 2017 vzrostl GDP o 5,2 %, to ovlivnilo v témže roce výrazný růst mezd, avšak v následujícím se zvýšily i ceny.

3. Výstup
	Dvě tabulky v databázi, ze kterých se požadovaná data dají získat. t_Lena_Oumrtova_project_SQL_primary_final (pro data mezd a cen potravin za Českou republiku sjednocených na totožné porovnatelné období – společné roky) 
t_Lena_Oumrtova_project_SQL_secondary_final (pro dodatečná data o dalších evropských státech).
	Dále sada SQL, která z připravených tabulek získá datový podklad k zodpovězení na vytyčené výzkumné otázky. 
Project_SQL_Task_N1
Project_SQL_Task_N2
Project_SQL_Task_N3
Project_SQL_Task_N4
Project_SQL_Task_N5

4. Poznámky k řešení
Tvorba tabulky s českými daty _primary_final: 
- byly vytvořeny dvě samostatné tabulky payroll a prices, z nichž každá byla již předdefinována
- k tabulce czechia_payroll byla připojena pro lepší orientaci tabulka s názvy odvětví czechia_payroll_industry_branch
- k tabulce o cenách potravin czechia_price a jejich kategoriích pro lepší přehlednost czechia_price_category
- obě dílčí tabulky byly následně spojeny ještě s tabulkou economies, která poskytuje ekonomické údaje, pro potřeby tabulky primary_final byly údaje z economies osekány pouze pro Českou republiku
- přidání tabulky economies proběhlo až při zpracovávání 5. úkolu, protože se tato cesta ukázala nejschůdnější.

Práce s daty k zodpovězení výzkumných otázek:
- po úpravě základní tabulky _primary_final byla již tvorba samotných dotazovacích sql skriptů snazší
- pro otázky 1, 3 a 5 existuje pomocný excelový soubor, díky kterému byla data následně snáze analyzována.
