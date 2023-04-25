Lenka Oumrtová
Datová akademie ENGETO
SQL Projekt


Kupní síla v České republice

Obsah
1. Zadání projektu
2. Výzkumné otázky
3. Výstup
4. Poznámky k řešení

1. Zadání projektu
	Projekt týkající se životní úrovní občanů, jehož cílem je zjištění dostupnosti základních potravin široké veřejnosti. Prostřednictvím vydefinovaných otázek bude analyzována životní úroveň občanů ČR. Zodpovězené otázky a výsledky analýzy bude tiskové oddělení následně prezentovat na tiskové konferenci. Pro realizaci analýzy je třeba připravit robustní datové podklady, ve kterých bude možné vidět porovnání dostupnosti potravin na základě průměrných příjmů za určité časové období.
	Jako dodatečný materiál je třeba připravit i tabulku s HDP, GINI koeficientem a populací dalších evropských států ve stejném období, jako primární přehled pro ČR.

2. Výzkumné otázky
1. Rostou v průběhu let mzdy ve všech odvětvích, nebo v některých klesají?
- z dlouhodobého hlediska rostou mzdy ve všech odvětvích
- z roku na rok v některých odvětvích klesly, viz tabulka a přiložený pomocný excel soubor.

2. Kolik je možné si koupit litrů mléka a kilogramů chleba za první a poslední srovnatelné období v dostupných datech cen a mezd?
- chléb 2006: 740 ks, 2018: 859 ks
- mléko 2006: 893 ks, 2018: 1090 ks

3. Která kategorie potravin zdražuje nejpomaleji (je u ní nejnižší percentuální meziroční nárůst)?
- bohužel nebylo možné zodpovědět otázku, protože localhost v DBeaveru nefungoval dostatečně a dotaz se nedokončil

4. Existuje rok, ve kterém byl meziroční nárůst cen potravin výrazně vyšší než růst mezd (větší než 10 %)?
- bohužel nebylo možné zodpovědět otázku, protože localhost v DBeaveru nefungoval dostatečně a dotaz se nedokončil

5. Má výška HDP vliv na změny ve mzdách a cenách potravin? Neboli, pokud HDP vzroste výrazněji v jednom roce, projeví se to na cenách potravin či mzdách ve stejném nebo následujícím roce výraznějším růstem?
- bohužel nebylo možné zodpovědět otázku, protože localhost v DBeaveru nefungoval dostatečně a dotaz se nedokončil

3. Výstup
	Dvě tabulky v databázi, ze kterých se požadovaná data dají získat. t_Lenka_Oumrtova_project_SQL_primary_final (pro data mezd a cen potravin za Českou republiku sjednocených na totožné porovnatelné období – společné roky) 
t_Lenka_Oumrtova_project_SQL_secondary_final (pro dodatečná data o dalších evropských státech).
	Dále sada SQL, která z připravených tabulek získá datový podklad k zodpovězení na vytyčené výzkumné otázky. Pozor, otázky/hypotézy mohou být výstupy podporovány i vyvraceny! Záleží na tom, co říkají data.

4. Poznámky k řešení
- tvorba tabulky s českými daty
	- k datové sadě czechia_payroll je nutné připojit pro lepší orientaci:
		- sadu s názvy odvětví czechia_payroll_industry_branch
		- sadu s názvy jednotek czechia_payroll_unit
		- sadu s názvy typů hodnot czechia_payroll_value_type
	- připojit také informace o cenách potravin czechia_price a jejich kategoriích pro lepší 	přehlednost czechia_price_category

- práce s daty k zodpovězení výzkumných otázek
Otázka č. 1 byla složitá v proveditelnosti dotazu, aby byl jednoduchý, a přitom poskytoval potřebná data. Takový skript se mi bohužel nepodařilo napsat, proto jsem zvolila cestu mnoha jednoduchých skriptů a jejich výsledky zaznamenávala do excelu, kde jsem data dále analyzovala.
Otázka č. 2 – předpokladem je, že prvním obdobím je rok 2006 a posledním rok 2018. Oba tyto roky jsou hraniční pro údaje mezd a cen.
Otázky č. 3 – 5, zde mi bohužel nešly načíst dotazy, ačkoli jsem se snažila tím, že jsem DBeaver přeinstalovala, přesto po kratší době začaly i jednoduché dotazy trvat velmi dlouho.
Problém s localhostem v DBeaveru přetrvával i po kontaktování lektorů.

