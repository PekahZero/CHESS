SELECT total_cost FROM projects WHERE title = 'Theseus';
SELECT total_cost FROM projects WHERE title = 'Theseus'
SELECT acronym FROM projects WHERE start_year = 2018
SELECT acronym FROM projects WHERE start_year = 2018
SELECT title FROM projects WHERE start_date < '2016-01-01'
SELECT title FROM projects WHERE start_date < '2016-01-01'
SELECT institutions.institutions_name FROM institutions JOIN eu_territorial_units ON institutions.geocode_regions_3 = eu_territorial_units.geocode_regions WHERE eu_territorial_units.description = 'Nordjylland';
SELECT institutions.institutions_name FROM institutions JOIN eu_territorial_units ON institutions.geocode_regions_3 = eu_territorial_units.geocode_regions WHERE eu_territorial_units.description = 'Nordjylland';
SELECT p.full_name FROM people AS p JOIN projects AS pr ON p.unics_id = pr.principal_investigator WHERE pr.start_year = 2014;
SELECT p.full_name FROM people AS p JOIN projects AS pr ON p.unics_id = pr.principal_investigator WHERE pr.start_year = 2014;
SELECT p.unics_id, p.acronym, p.title FROM projects AS p JOIN project_subject_areas AS psa ON p.unics_id = psa.project JOIN subject_areas AS sa ON psa.subject_area = sa.code WHERE sa.title = 'Mathematics and Statistics' AND psa.subject_area IS NOT NULL AND p.unics_id IS NOT NULL;
SELECT p.acronym, sa.description FROM projects AS p JOIN project_subject_areas AS psa ON p.unics_id = psa.project JOIN subject_areas AS sa ON psa.subject_area = sa.code WHERE sa.title = 'Mathematics and Statistics';
SELECT DISTINCT T2.topic FROM projects AS T1 JOIN project_topics AS T2 ON T1.unics_id = T2.project WHERE T1.end_year = 2014;
SELECT DISTINCT t.title FROM topics AS t JOIN project_topics AS pt ON t.code = pt.topic JOIN projects AS p ON pt.project = p.unics_id WHERE p.end_year = 2014;
SELECT DISTINCT p.acronym FROM projects AS p JOIN project_members AS pm ON p.unics_id = pm.project WHERE pm.country = 'GR';
SELECT institutions_name FROM institutions JOIN countries ON institutions.country_id = countries.unics_id WHERE countries.country_name IN ('France', 'Germany');
SELECT institutions_name FROM institutions WHERE country_id != (SELECT unics_id FROM countries WHERE country_name = 'France');
SELECT COUNT(*) FROM projects WHERE start_year = 2016
SELECT title FROM projects ORDER BY total_cost DESC LIMIT 1
SELECT pm.member_name FROM project_members AS pm JOIN projects AS p ON pm.project = p.unics_id WHERE p.total_cost < (SELECT AVG(total_cost) FROM projects);
SELECT project, COUNT(*) AS member_count FROM project_members GROUP BY project HAVING member_count >= 100;
SELECT fs.code, fs.title FROM funding_schemes AS fs JOIN projects AS p ON fs.code = p.ec_fund_scheme GROUP BY fs.code, fs.title ORDER BY COUNT(p.unics_id) DESC LIMIT 1;
SELECT SUM(total_cost) AS total_costs FROM projects;
SELECT title FROM projects WHERE start_year > 2006 AND end_year IS NOT NULL;
SELECT SELECT unics_id, title, start_year, end_year FROM projects WHERE start_year IS NOT NULL AND end_year IS NOT NULL ORDER BY (end_year - start_year) DESC LIMIT 1;
SELECT title FROM topics WHERE title LIKE 'Raw materials%'
SELECT title FROM topics WHERE title LIKE '%climate%'
SELECT COUNT(*) FROM projects WHERE principal_investigator = (SELECT unics_id FROM people WHERE full_name = 'Thomas Bell');
SELECT DISTINCT full_name FROM people;
SELECT acronym FROM projects WHERE total_cost BETWEEN 100000 AND 200000
SELECT title FROM projects WHERE total_cost > 1000000
SELECT title FROM projects WHERE total_cost > 1000000
SELECT projects.title, project_members.member_name FROM projects JOIN project_members ON projects.unics_id = project_members.project WHERE project_members.member_role = 'Partner' AND project_members.member_name IS NOT NULL;
SELECT DISTINCT description FROM erc_research_domains;
SELECT country_name FROM countries JOIN institutions ON countries.unics_id = institutions.country_id;
SELECT DISTINCT countries.country_name FROM institutions JOIN countries ON institutions.country_id = countries.unics_id;
SELECT country_code2, country_code3 FROM countries WHERE country_name = 'Andorra'
SELECT code FROM funding_schemes WHERE title = 'Framework Partnership Agreement'
SELECT title FROM programmes WHERE short_name = 'Transport';
SELECT pm.member_name, pm.member_role FROM project_members AS pm JOIN projects AS p ON pm.project = p.unics_id WHERE p.acronym = 'GTBB';
SELECT pm.member_name, pm.member_role FROM project_members AS pm JOIN projects AS p ON pm.project = p.unics_id WHERE p.acronym = 'GTBB';
SELECT title FROM programmes WHERE parent = 'FP7'
SELECT title FROM programmes WHERE parent = 'FP7';
SELECT ep.description FROM erc_panels AS ep JOIN erc_research_domains AS erd ON ep.part_of = erd.code WHERE erd.description = 'Life Sciences';
SELECT ep.description FROM erc_panels AS ep JOIN erc_research_domains AS erd ON ep.part_of = erd.code WHERE erd.description = 'Life Sciences';
SELECT SELECT pm.unics_id, pm.member_name, pm.activity_type, pm.institution_id FROM project_members AS pm JOIN project_member_roles AS pmr ON pm.member_role = pmr.code WHERE pmr.description = 'Participant' AND pm.unics_id IS NOT NULL AND pm.member_name IS NOT NULL AND pm.activity_type IS NOT NULL AND pm.institution_id IS NOT NULL;
SELECT pm.member_name FROM project_members AS pm JOIN activity_types AS at ON pm.activity_type = at.code WHERE at.description = 'Research Organisations';
SELECT objective FROM projects WHERE title = 'DEEPCARBON';
SELECT objective FROM projects WHERE acronym = 'DEEPCARBON';
SELECT title FROM projects WHERE objective LIKE '%carbon capturing%'
SELECT COUNT(*) FROM projects WHERE objective LIKE '%carbon capturing%'
SELECT institutions_name FROM institutions WHERE country_id = (SELECT unics_id FROM countries WHERE country_name = 'France') AND geocode_regions_3 <> (SELECT geocode_regions FROM eu_territorial_units WHERE description = 'Paris');
SELECT DISTINCT i.institutions_name FROM institutions i JOIN countries c ON i.country_id = c.unics_id JOIN project_members pm ON i.unics_id = pm.institution_id WHERE c.country_name = 'France' AND pm.city <> 'PARIS';
SELECT i.institutions_name FROM institutions AS i LEFT JOIN project_members AS pm ON i.unics_id = pm.institution_id AND pm.member_role = 'Coordinator' WHERE pm.institution_id IS NULL;
SELECT i.institutions_name FROM institutions AS i LEFT JOIN project_members AS pm ON i.unics_id = pm.institution_id AND pm.member_role = (SELECT code FROM project_member_roles WHERE description = 'Coordinator') WHERE pm.project IS NULL;
SELECT SELECT p.full_name FROM project_members pm JOIN people p ON pm.unics_id = p.unics_id WHERE pm.project IS NOT NULL GROUP BY p.unics_id HAVING COUNT(DISTINCT pm.project) > 1;
SELECT SELECT pm.unics_id, p.full_name FROM project_members pm JOIN people p ON pm.unics_id = p.unics_id WHERE pm.project IS NOT NULL GROUP BY pm.unics_id, p.full_name HAVING COUNT(DISTINCT pm.project) > 1;
SELECT sa.title FROM subject_areas AS sa JOIN project_subject_areas AS psa ON sa.code = psa.subject_area JOIN projects AS p ON psa.project = p.unics_id GROUP BY sa.code ORDER BY SUM(p.ec_max_contribution) DESC LIMIT 1;
SELECT sa.title, SUM(p.ec_max_contribution) AS total_funding FROM project_subject_areas AS psa JOIN subject_areas AS sa ON psa.subject_area = sa.code JOIN projects AS p ON psa.project = p.unics_id GROUP BY sa.title ORDER BY total_funding DESC LIMIT 1;
SELECT sa.title, SUM(p.ec_max_contribution) AS total_funding FROM project_subject_areas AS psa JOIN subject_areas AS sa ON psa.subject_area = sa.code JOIN projects AS p ON psa.project = p.unics_id GROUP BY sa.title ORDER BY total_funding ASC LIMIT 1;
SELECT sa.title FROM subject_areas AS sa JOIN project_subject_areas AS psa ON sa.code = psa.subject_area JOIN projects AS p ON psa.project = p.unics_id GROUP BY sa.code ORDER BY SUM(p.ec_max_contribution) ASC LIMIT 1;
SELECT institutions.institutions_name, COUNT(project_members.project) AS project_count FROM institutions JOIN project_members ON institutions.unics_id = project_members.institution_id GROUP BY institutions.unics_id ORDER BY project_count DESC LIMIT 1;
SELECT institutions.institutions_name, COUNT(projects.unics_id) AS project_count FROM institutions JOIN project_members ON institutions.unics_id = project_members.institution_id JOIN projects ON project_members.project = projects.unics_id GROUP BY institutions.unics_id ORDER BY project_count DESC LIMIT 1;
SELECT institutions.institutions_name, COUNT(project_members.project) AS project_count FROM institutions LEFT JOIN project_members ON institutions.unics_id = project_members.institution_id GROUP BY institutions.unics_id ORDER BY project_count ASC LIMIT 1;
SELECT institutions.institutions_name, COUNT(project_members.project) AS project_count FROM institutions LEFT JOIN project_members ON institutions.unics_id = project_members.institution_id GROUP BY institutions.unics_id ORDER BY project_count ASC LIMIT 1;
SELECT ec_fund_scheme, SUM(ec_max_contribution) AS total_funding FROM projects GROUP BY ec_fund_scheme ORDER BY total_funding DESC LIMIT 1;
SELECT fs.title, MIN(p.ec_max_contribution) AS least_funding FROM projects AS p JOIN funding_schemes AS fs ON p.ec_fund_scheme = fs.code GROUP BY fs.title ORDER BY least_funding ASC LIMIT 1;
SELECT SELECT i.institutions_name AS industrial_partner, SUM(pm.ec_contribution) AS total_funding FROM project_members AS pm JOIN institutions AS i ON pm.institution_id = i.unics_id WHERE pm.member_role = 'Partner' -- Assuming 'Partner' indicates industrial partners AND pm.ec_contribution IS NOT NULL -- Exclude NULL contributions GROUP BY i.institutions_name HAVING SUM(pm.ec_contribution) > 0 -- Ensure we only include partners with funding ORDER BY total_funding DESC;
SELECT p.total_cost AS funding_amount, GROUP_CONCAT(i.institutions_name) AS industrial_partners FROM projects AS p JOIN project_members AS pm ON p.unics_id = pm.project JOIN institutions AS i ON pm.institution_id = i.unics_id GROUP BY p.total_cost ORDER BY p.total_cost DESC;
SELECT title, start_year FROM projects ORDER BY start_year DESC LIMIT 1
SELECT SELECT unics_id, title, start_date FROM projects WHERE start_date IS NOT NULL AND start_date = (SELECT MAX(start_date) FROM projects WHERE start_date IS NOT NULL);
SELECT title, start_year FROM projects WHERE start_year = (SELECT MAX(start_year) FROM projects);
SELECT SELECT unics_id, title, start_date FROM projects WHERE start_date IS NOT NULL ORDER BY start_date ASC LIMIT 5;
SELECT MIN(start_date) AS first_start_date FROM projects WHERE start_date IS NOT NULL;
SELECT MIN(start_date) FROM projects WHERE start_date IS NOT NULL;
SELECT p.title FROM projects AS p JOIN project_subject_areas AS psa ON p.unics_id = psa.project JOIN subject_areas AS sa ON psa.subject_area = sa.code WHERE sa.title = 'Climate change and Carbon cycle research';
SELECT p.title FROM projects AS p JOIN project_subject_areas AS psa ON p.unics_id = psa.project WHERE psa.subject_area = 'CCC';
SELECT DISTINCT description FROM project_member_roles;
SELECT DISTINCT description FROM project_member_roles;
SELECT COUNT(*) FROM erc_panels AS EP JOIN erc_research_domains AS ERD ON EP.part_of = ERD.code WHERE ERD.description = 'Life Sciences';
SELECT COUNT(*) FROM erc_panels AS EP JOIN erc_research_domains AS ERD ON EP.part_of = ERD.code WHERE ERD.description = 'Life Sciences';
SELECT erc_panels.code, erc_panels.description FROM erc_panels JOIN erc_research_domains ON erc_panels.part_of = erc_research_domains.code WHERE erc_research_domains.description = 'Social Sciences And Humanities';
SELECT COUNT(*) FROM erc_panels AS T1 JOIN erc_research_domains AS T2 ON T1.part_of = T2.code WHERE T2.description = 'Social Sciences And Humanities';
SELECT SELECT pm.unics_id, pm.project, pm.member_name, pm.member_role FROM project_members pm JOIN institutions i ON pm.institution_id = i.unics_id WHERE pm.member_role = 'Partner' AND pm.institution_id IS NOT NULL AND i.institutions_name IS NOT NULL; -- Assuming we want to ensure the institution name is not null
SELECT pm.member_name FROM project_members pm JOIN project_member_roles pmr ON pm.member_role = pmr.code WHERE pmr.description = 'Partner';
SELECT COUNT(*) FROM project_members WHERE member_role = (SELECT code FROM project_member_roles WHERE description = 'Partner');
SELECT COUNT(*) FROM project_members WHERE member_role IN ( SELECT code FROM project_member_roles WHERE description IN ('Higher Education Establishment', 'Secondary Education Establishment') );
SELECT COUNT(*) FROM project_members WHERE member_role = 'Host institution' OR member_role = 'Partner';
SELECT COUNT(*) FROM projects AS P JOIN project_topics AS PT ON P.unics_id = PT.project JOIN topics AS T ON PT.topic = T.code WHERE T.title LIKE '%Robotics%'
SELECT COUNT(DISTINCT ps.project) AS number_of_projects FROM project_subject_areas AS ps JOIN subject_areas AS sa ON ps.subject_area = sa.code WHERE sa.title = 'Robotics';
SELECT institutions.institutions_name, SUM(projects.ec_max_contribution) AS total_funding FROM project_members JOIN institutions ON project_members.institution_id = institutions.unics_id JOIN projects ON project_members.project = projects.unics_id WHERE institutions.country_id NOT IN (/* List of EU country IDs */) GROUP BY institutions.institutions_name ORDER BY total_funding DESC LIMIT 1;
SELECT institutions.institutions_name, SUM(projects.ec_max_contribution) AS total_funding FROM institutions JOIN project_members ON institutions.unics_id = project_members.institution_id JOIN projects ON project_members.project = projects.unics_id WHERE institutions.country_id NOT IN (SELECT unics_id FROM countries WHERE country_code2 IN ('AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL', 'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE', 'GB')) GROUP BY institutions.institutions_name ORDER BY total_funding DESC LIMIT 1;
SELECT SELECT institution_id, SUM(ec_contribution) AS total_funding FROM project_members WHERE country NOT IN ( SELECT country_code2 FROM countries WHERE country_name IN ( SELECT country_name FROM countries WHERE country_code2 IN ( 'AD', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL', 'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE', 'GB' ) ) ) AND country IS NOT NULL GROUP BY institution_id ORDER BY total_funding ASC LIMIT 1;
SELECT institutions.institutions_name, MIN(projects.ec_max_contribution) AS least_funding FROM project_members JOIN institutions ON project_members.institution_id = institutions.unics_id JOIN projects ON project_members.project = projects.unics_id WHERE institutions.country_id NOT IN (SELECT unics_id FROM countries WHERE country_code2 IN ('AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL', 'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE')) GROUP BY institutions.institutions_name ORDER BY least_funding ASC LIMIT 1;
SELECT COUNT(DISTINCT institution_id) FROM project_members WHERE country NOT IN ('AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL', 'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE', 'GB');
SELECT DISTINCT institutions.institutions_name FROM project_members JOIN institutions ON project_members.institution_id = institutions.unics_id JOIN countries ON institutions.country_id = countries.unics_id WHERE countries.country_code2 NOT IN ( 'AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL', 'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE', 'GB' );
SELECT * FROM programmes WHERE title LIKE '%climate%'
SELECT * FROM programmes WHERE title LIKE '%climate%'
SELECT p.title AS programme_title, SUM(pr.total_cost) AS total_funds_allocated FROM programmes AS p JOIN project_programmes AS pp ON p.code = pp.programme JOIN projects AS pr ON pp.project = pr.unics_id GROUP BY p.code, p.title;
SELECT SELECT p.title AS Programme_Title, SUM(pr.ec_max_contribution) AS Total_Funding FROM programmes AS p JOIN project_programmes AS pp ON p.code = pp.programme JOIN projects AS pr ON pp.project = pr.unics_id WHERE pr.ec_max_contribution IS NOT NULL GROUP BY p.title;
SELECT * FROM disease_mutation WHERE ref_aa = 'E'
SELECT COUNT(*) FROM biomarker_fda_test WHERE test_manufacturer = '23andMe';
SELECT speciescommonname FROM species WHERE genus = 'Mus';
SELECT DISTINCT speciescommonname FROM species;
SELECT * FROM disease_mutation
SELECT biomarker_description FROM biomarker;
SELECT COUNT(DISTINCT test_trial_id) FROM biomarker_fda_test_trial WHERE test_trade_name IN ( SELECT test_trade_name FROM biomarker_fda_test WHERE test_manufacturer = 'ABBOTT MOLECULAR INC' );
SELECT biomarker.gene_symbol, biomarker.biomarker_description FROM biomarker WHERE biomarker.test_is_a_panel = 'false'
SELECT * FROM disease WHERE name LIKE '%cancer%'
SELECT biomarker_title, qa_state FROM biomarker_edrn WHERE phase = 'Two';
SELECT biomarker_title, qa_state FROM biomarker_edrn WHERE phase = 'Two';
SELECT gene_symbol FROM biomarker
SELECT SELECT id, biomarker_title, biomarker_type FROM biomarker_edrn WHERE biomarker_type IS NOT NULL AND biomarker_type != 'Protein';
SELECT biomarker_title FROM biomarker_edrn WHERE biomarker_type != 'Protein';
SELECT DISTINCT gene_symbol FROM differential_expression WHERE doid = (SELECT id FROM disease WHERE name = 'lung cancer');
SELECT biomarker.gene_symbol, biomarker.biomarker_description FROM biomarker JOIN biomarker_fda ON biomarker.id = biomarker_fda.id JOIN biomarker_fda_test ON biomarker_fda.test_trade_name = biomarker_fda_test.test_trade_name JOIN disease ON biomarker_fda_test.doid = disease.id WHERE disease.name = 'breast cancer';
SELECT SELECT DISTINCT phase FROM biomarker_edrn WHERE phase IS NOT NULL;
SELECT test_method.platform_method, test_method.test_study_design FROM biomarker_fda_test AS test_method WHERE test_method.test_manufacturer = 'Dako Denmark A/S' AND test_method.platform_method IS NOT NULL AND test_method.test_study_design IS NOT NULL;
SELECT de.pvalue FROM differential_expression AS de JOIN disease AS d ON de.doid = d.id WHERE d.name = 'lung cancer';
SELECT chromosome_pos FROM disease_mutation WHERE doid = (SELECT id FROM disease WHERE name = 'skin cancer');
SELECT dm.chromosome_pos FROM disease_mutation AS dm JOIN disease AS d ON dm.doid = d.id WHERE d.name = 'skin cancer';
SELECT * FROM disease_mutation WHERE ref_aa = 'E';
SELECT COUNT(*) FROM biomarker_fda_test WHERE test_manufacturer = '23andMe';
SELECT d.name FROM disease AS d JOIN differential_expression AS de ON d.id = de.doid WHERE de.gene_symbol = 'A1BG' AND de.statistical_significance = 'Yes' AND de.log2fc > 0;
SELECT * FROM species;
SELECT de.gene_symbol, de.pvalue FROM differential_expression AS de JOIN disease AS d ON de.doid = d.id WHERE de.gene_symbol = 'EGFR' AND d.name = 'lung cancer';
SELECT gene_symbol, pvalue FROM differential_expression WHERE doid = (SELECT id FROM disease WHERE name = 'lung cancer') AND gene_symbol = 'EGFR';
SELECT * FROM disease_mutation
SELECT COUNT(*) FROM healthy_expression AS HE JOIN stage AS S ON HE.uberon_developmental_id = S.id WHERE S.name = 'late adult stage';
SELECT d.name FROM differential_expression AS de JOIN disease AS d ON de.doid = d.id WHERE de.gene_symbol = 'A1BG' AND de.statistical_significance = 'Yes';
SELECT d.name FROM differential_expression AS de JOIN disease AS d ON de.doid = d.id WHERE de.gene_symbol = 'A1BG' AND de.statistical_significance = 'Yes';
SELECT biomarker_description FROM biomarker;
SELECT biomarker.gene_symbol, biomarker.biomarker_description FROM biomarker WHERE biomarker.test_is_a_panel = 'false';
SELECT test_trade_name FROM biomarker_fda_test_use WHERE actual_use = 'predisposition';
SELECT gene_symbol FROM biomarker;
SELECT * FROM biomarker_edrn WHERE biomarker_type = 'Protein' AND phase = 'Two'
SELECT biomarker_edrn.biomarker_title FROM biomarker_edrn WHERE biomarker_edrn.biomarker_type = 'Protein' AND biomarker_edrn.phase = 'Two';
SELECT b.gene_symbol, b.biomarker_description FROM biomarker AS b JOIN biomarker_fda_test AS bf ON b.id = bf.doid JOIN disease AS d ON bf.doid = d.id WHERE d.name = 'breast cancer';
SELECT SELECT DISTINCT phase FROM biomarker_edrn WHERE phase IS NOT NULL;
SELECT pvalue FROM differential_expression WHERE doid = (SELECT id FROM disease WHERE name = 'lung cancer');
SELECT COUNT(DISTINCT xref_gene_ensembl.gene_symbol) FROM xref_gene_ensembl JOIN species ON xref_gene_ensembl.speciesid = species.speciesid WHERE species.genus = 'Homo';
SELECT COUNT(DISTINCT xref_gene_ensembl.ensembl_gene_id) AS gene_ensemble_count FROM xref_gene_ensembl JOIN species ON xref_gene_ensembl.speciesid = species.speciesid WHERE species.genus = 'Homo';
SELECT DISTINCT test_trade_name FROM biomarker_fda_test WHERE test_manufacturer LIKE 'Roche%'
SELECT test_trade_name, test_submission FROM biomarker_fda_test WHERE test_manufacturer LIKE 'Roche%'
SELECT DISTINCT cds_pos FROM disease_mutation WHERE cds_pos IS NOT NULL;
SELECT COUNT(*) FROM disease_mutation WHERE cds_pos = 102997;
SELECT gene_symbol FROM differential_expression WHERE pvalue BETWEEN 0.39 AND 0.41;
SELECT gene_symbol FROM differential_expression WHERE pvalue BETWEEN 0.39 AND 0.41;
SELECT DISTINCT dm.chromosome_id FROM disease_mutation AS dm JOIN disease AS d ON dm.doid = d.id WHERE d.name = 'breast cancer';
SELECT DISTINCT dm.chromosome_id FROM disease AS d JOIN disease_mutation AS dm ON d.id = dm.doid WHERE d.name = 'breast cancer';
SELECT ae.name FROM anatomical_entity AS ae JOIN healthy_expression AS he ON ae.id = he.uberon_anatomical_id WHERE he.expression_level_gene_relative = 'LOW' AND he.expression_level_anatomical_relative = 'HIGH';
SELECT name FROM anatomical_entity WHERE id IN ( SELECT uberon_anatomical_id FROM healthy_expression WHERE expression_level_gene_relative = 'LOW' AND expression_level_anatomical_relative = 'HIGH' );
SELECT name FROM anatomical_entity WHERE name LIKE 'bone%'
SELECT speciescommonname FROM species WHERE genus = 'Mus';
SELECT d.name FROM differential_expression AS de JOIN disease AS d ON de.doid = d.id WHERE de.gene_symbol = 'A1BG' AND de.expression_change_direction = 'up';
SELECT COUNT(*) FROM healthy_expression AS HE JOIN stage AS S ON HE.uberon_developmental_id = S.id WHERE S.name LIKE 'late adult%'
SELECT COUNT(*) FROM biomarker_fda_test_trial AS T1 JOIN biomarker_fda_test AS T2 ON T1.test_trade_name = T2.test_trade_name AND T1.test_submission = T2.test_submission WHERE T2.test_manufacturer = 'ABBOTT MOLECULAR INC';
SELECT test_trade_name FROM biomarker_fda_test_use WHERE actual_use = 'predisposition';
SELECT DISTINCT de.gene_symbol FROM differential_expression AS de JOIN disease AS d ON de.doid = d.id WHERE d.name = 'lung cancer';
SELECT platform_method, test_study_design FROM biomarker_fda_test WHERE test_manufacturer = 'Dako Denmark A/S' AND platform_method IS NOT NULL AND test_study_design IS NOT NULL
SELECT biomarker.biomarker_description FROM biomarker JOIN biomarker_fda_test ON biomarker.id = biomarker_fda_test.doid WHERE biomarker_fda_test.test_approval_status = 'class II';
SELECT b.biomarker_description FROM biomarker AS b JOIN biomarker_fda AS bf ON b.biomarker_id = bf.id JOIN biomarker_fda_test AS bft ON bf.test_trade_name = bft.test_trade_name AND bf.test_submission = bft.test_submission WHERE bft.test_approval_status = 'class II';
SELECT * FROM healthy_expression WHERE expression_score > (SELECT AVG(expression_score) FROM healthy_expression);
SELECT * FROM healthy_expression WHERE expression_score > (SELECT AVG(expression_score) FROM healthy_expression);
SELECT b.gene_symbol FROM biomarker AS b JOIN biomarker_edrn AS e ON b.id = e.id JOIN anatomical_entity AS a ON e.uberon_anatomical_id = a.id WHERE e.biomarker_type = 'Genomic' AND a.name = 'breast';
SELECT b.gene_symbol FROM biomarker_edrn AS edrn JOIN biomarker AS b ON edrn.id = b.id JOIN anatomical_entity AS ae ON edrn.uberon_anatomical_id = ae.id WHERE edrn.biomarker_type = 'Genomic' AND ae.name = 'breast';
SELECT d.name FROM disease AS d JOIN disease_mutation AS dm ON d.id = dm.doid JOIN disease_mutation_tissue AS dmt ON dm.id = dmt.disease_mutation_id WHERE dmt.uberon_anatomical_id = (SELECT id FROM anatomical_entity WHERE name = 'liver');
SELECT DISTINCT d.name FROM disease AS d JOIN disease_mutation AS dm ON d.id = dm.doid JOIN disease_mutation_tissue AS dmt ON dm.id = dmt.disease_mutation_id JOIN anatomical_entity AS ae ON dmt.uberon_anatomical_id = ae.id WHERE ae.name = 'liver';
SELECT DISTINCT bft.test_manufacturer FROM biomarker AS bm JOIN biomarker_fda AS bf ON bm.id = bf.id JOIN biomarker_fda_test AS bft ON bf.id = bft.biomarker_fda_id WHERE bm.gene_symbol = 'BRAF' AND bft.test_manufacturer IS NOT NULL;
SELECT DISTINCT bft.test_manufacturer FROM biomarker AS b JOIN biomarker_fda AS bf ON b.id = bf.id JOIN biomarker_fda_test AS bft ON bf.id = bft.test_submission WHERE b.gene_symbol = 'BRAF';
SELECT anatomical_entity.name AS anatomical_entity_name, species.speciescommonname AS species_name FROM anatomical_entity CROSS JOIN species;
SELECT DISTINCT he.uberon_anatomical_id FROM healthy_expression AS he JOIN xref_gene_ensembl AS xg ON he.ensembl_gene_id = xg.ensembl_gene_id WHERE xg.gene_symbol = 'A1BG';
SELECT b.gene_symbol, b.biomarker_description FROM biomarker AS b JOIN biomarker_edrn AS e ON b.id = e.id WHERE e.phase = 'One' AND (b.biomarker_description LIKE '%breast%' OR e.biomarker_title LIKE '%breast%');
SELECT ae.name, he.expression_score FROM healthy_expression AS he JOIN anatomical_entity AS ae ON he.uberon_anatomical_id = ae.id WHERE he.ensembl_gene_id IN ('ENSMUSG00000000037', 'ENSMUSG00000000078');
SELECT bft.ncit_biomarker FROM biomarker AS b JOIN biomarker_fda AS bf ON b.id = bf.id JOIN biomarker_fda_ncit_term AS bft ON bf.id = bft.biomarker_fda_id WHERE b.gene_symbol = 'ALDH4A1';
SELECT dm.* FROM disease_mutation AS dm JOIN disease_mutation_tissue AS dmt ON dm.id = dmt.disease_mutation_id JOIN anatomical_entity AS ae ON dmt.uberon_anatomical_id = ae.id WHERE ae.name = 'liver';
SELECT dm.* FROM disease_mutation AS dm JOIN disease_mutation_tissue AS dmt ON dm.id = dmt.disease_mutation_id JOIN anatomical_entity AS ae ON dmt.uberon_anatomical_id = ae.id WHERE ae.name = 'liver';
SELECT DISTINCT b.gene_symbol FROM biomarker b JOIN biomarker_fda bf ON b.id = bf.id JOIN biomarker_fda_test bft ON bf.test_trade_name = bft.test_trade_name AND bf.test_submission = bft.test_submission WHERE bft.test_approval_status = 'PMP';
SELECT b.biomarker_description FROM biomarker AS b JOIN biomarker_fda AS fda ON b.id = fda.id JOIN biomarker_fda_test AS fda_test ON fda.id = fda_test.doid JOIN biomarker_fda_test_use AS fda_test_use ON fda_test.test_trade_name = fda_test_use.test_trade_name JOIN biomarker_fda_ncit_term AS fda_ncit ON fda.id = fda_ncit.biomarker_fda_id JOIN disease AS d ON fda_ncit.ncit_biomarker = d.id WHERE d.name = 'breast cancer';
SELECT ae.name AS Anatomical_Entity, COUNT(b.id) AS Biomarker_Count FROM anatomical_entity AS ae LEFT JOIN biomarker_edrn AS be ON ae.id = be.uberon_anatomical_id LEFT JOIN biomarker AS b ON be.id = b.id GROUP BY ae.id, ae.name;
SELECT * FROM disease_mutation WHERE ref_aa = 'F'
SELECT * FROM disease WHERE name LIKE '%cancer%'
SELECT DISTINCT bft.test_manufacturer FROM biomarker AS bm JOIN biomarker_fda AS bfa ON bm.id = bfa.id JOIN biomarker_fda_test AS bft ON bfa.id = bft.test_trade_name WHERE bm.gene_symbol = 'BRAF' AND bft.test_manufacturer IS NOT NULL;
SELECT b.gene_symbol, b.biomarker_description, b.biomarker_id FROM biomarker AS b JOIN biomarker_fda AS fda ON b.id = fda.id WHERE b.test_is_a_panel = 'true' AND b.biomarker_id IS NOT NULL AND b.biomarker_description IS NOT NULL
SELECT b.biomarker_description FROM biomarker AS b JOIN biomarker_fda AS fda ON b.id = fda.id JOIN biomarker_fda_test AS fda_test ON fda.test_trade_name = fda_test.test_trade_name WHERE fda_test.test_manufacturer = '23andMe' AND b.biomarker_description IS NOT NULL;
SELECT DISTINCT bft.test_manufacturer FROM biomarker_fda_test AS bft JOIN biomarker_fda AS bf ON bft.test_trade_name = bf.test_trade_name AND bft.test_submission = bf.test_submission JOIN biomarker AS b ON bf.id = b.biomarker_id JOIN disease AS d ON bft.doid = d.id WHERE d.name LIKE '%breast cancer%'
SELECT b.biomarker_description, b.biomarker_id, f.test_trade_name, f.test_submission FROM biomarker AS b JOIN biomarker_edrn AS edrn ON b.id = edrn.id JOIN biomarker_fda AS fda ON b.id = fda.id JOIN biomarker_fda_test AS f ON fda.test_trade_name = f.test_trade_name AND fda.test_submission = f.test_submission WHERE edrn.qa_state = 'Accepted' AND f.test_approval_status = 'Class II 510(k)' AND b.biomarker_description LIKE '%breast cancer%' AND b.biomarker_description IS NOT NULL;
SELECT ae.name, COUNT(be.id) AS biomarker_count FROM anatomical_entity AS ae JOIN biomarker_edrn AS be ON ae.id = be.uberon_anatomical_id GROUP BY ae.id ORDER BY biomarker_count DESC LIMIT 1;
SELECT 1;
SELECT d.name AS cancer_type, COUNT(de.gene_symbol) AS entry_count FROM differential_expression AS de JOIN disease AS d ON de.doid = d.id GROUP BY d.name ORDER BY entry_count DESC LIMIT 3;
SELECT SELECT edrn.id, edrn.biomarker_title, edrn.qa_state, edrn.biomarker_type FROM biomarker_edrn AS edrn LEFT JOIN biomarker_fda AS fda ON edrn.id = fda.id WHERE fda.id IS NULL AND edrn.id IS NOT NULL;
SELECT edrn.biomarker_title, fda_test.test_trade_name, fda_test.test_submission FROM biomarker_edrn AS edrn JOIN biomarker AS bm ON edrn.id = bm.id JOIN biomarker_fda AS fda ON bm.id = fda.id JOIN biomarker_fda_test AS fda_test ON fda.test_trade_name = fda_test.test_trade_name AND fda.test_submission = fda_test.test_submission WHERE fda_test.test_approval_status IN ('Class II 510(k)', 'PMA', '513(f)(2)', 'PMP', 'class II') AND fda_test.test_approval_status IS NOT NULL;
SELECT SELECT chromosome_id, data_source, COUNT(*) AS mutation_count FROM disease_mutation WHERE data_source = 'cosmic' GROUP BY chromosome_id, data_source HAVING COUNT(*) = ( SELECT MAX(mutation_count) FROM ( SELECT COUNT(*) AS mutation_count FROM disease_mutation WHERE data_source = 'cosmic' GROUP BY chromosome_id ) )
SELECT DISTINCT xref_gene_ensembl.gene_symbol FROM disease JOIN disease_mutation ON disease.id = disease_mutation.doid JOIN biomarker ON disease_mutation.id = biomarker.id JOIN xref_gene_ensembl ON biomarker.gene_symbol = xref_gene_ensembl.gene_symbol WHERE disease.name = 'prostate cancer' AND xref_gene_ensembl.gene_symbol IS NOT NULL;
SELECT bftu.approved_indication, COUNT(DISTINCT bft.test_trade_name) AS test_count FROM biomarker_fda_test_use AS bftu JOIN biomarker_fda_test AS bft ON bftu.test_trade_name = bft.test_trade_name AND bftu.test_submission = bft.test_submission JOIN biomarker AS b ON bftu.id = b.id WHERE bftu.approved_indication IS NOT NULL GROUP BY bftu.approved_indication HAVING COUNT(DISTINCT bft.test_trade_name) > 0
SELECT bft.test_trade_name FROM biomarker_fda_test bft JOIN biomarker_fda_test_use bftu ON bft.test_trade_name = bftu.test_trade_name AND bft.test_submission = bftu.test_submission WHERE (bft.test_approval_status = 'PMA' OR bft.test_approval_status = 'Class II 510(k)') AND bftu.approved_indication = 'diagnosis';
SELECT DISTINCT bft.test_manufacturer FROM biomarker_fda_test AS bft JOIN biomarker_fda AS bf ON bft.test_trade_name = bf.test_trade_name AND bft.test_submission = bf.test_submission JOIN disease AS d ON bft.doid = d.id WHERE d.name = 'lung cancer' AND bft.test_approval_status IN ('Class II 510(k)', 'PMA', '513(f)(2)', 'PMP', 'class II') AND bft.test_trade_name IS NOT NULL; -- Ensuring we only get tests that have a name
SELECT DISTINCT d.name FROM disease AS d JOIN biomarker_fda_test AS bft ON d.id = bft.doid JOIN biomarker_fda_test_use AS bftu ON bft.test_trade_name = bftu.test_trade_name AND bft.test_submission = bftu.test_submission WHERE bft.specimen_type = 'blood';
SELECT SELECT DISTINCT biomarker.id AS biomarker_id, biomarker.gene_symbol, biomarker.biomarker_description, species.genus, species.species, species.speciescommonname FROM biomarker JOIN healthy_expression ON biomarker.id = healthy_expression.ensembl_gene_id JOIN xref_gene_ensembl ON biomarker.gene_symbol = xref_gene_ensembl.gene_symbol JOIN species ON xref_gene_ensembl.speciesid = species.speciesid WHERE healthy_expression.expression_level_gene_relative != 'ABSENT' AND healthy_expression.ensembl_gene_id IS NOT NULL;
SELECT p.objid, p.run, p.field, pt.name AS photo_type_name FROM photoobj AS p JOIN photo_type AS pt ON p.type = pt.value WHERE pt.name = 'STAR';
SELECT * FROM photoobj AS p JOIN photo_type AS pt ON p.type = pt.value WHERE pt.name = 'STAR';
SELECT p.objid, p.ra, p.dec FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE p.type = (SELECT value FROM photo_type WHERE name = 'STAR');
SELECT p.objid, p.ra, p.dec FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE p.type = 'STAR' AND s.specobjid IS NOT NULL;
SELECT DISTINCT p.objid FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE s.class = 'GALAXY';
SELECT DISTINCT specobj.specobjid FROM specobj JOIN photoobj ON specobj.bestobjid = photoobj.objid WHERE specobj.class = 'GALAXY';
SELECT p.objid, p.ra, p.dec FROM specobj AS s JOIN photoobj AS p ON s.bestobjid = p.objid WHERE s.class = 'GALAXY' AND s.specobjid IN (SELECT specobjid FROM galspecline)
SELECT p.objid, p.ra, p.dec FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE s.class = 'GALAXY' AND p.clean = 1;
SELECT p.objid, p.ra, p.dec FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE s.class = 'GALAXY' AND p.ra > 185 AND p.ra < 186 AND p.dec > 15 AND p.dec < 16;
SELECT p.objid, p.ra, p.dec FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE s.class = 'GALAXY' AND p.ra BETWEEN 185 AND 186 AND p.dec BETWEEN 15 AND 16;
SELECT SELECT p.objid, p.ra, p.dec FROM photoobj p JOIN photo_type pt ON p.type = pt.value WHERE pt.name = 'STAR' AND p.ra > 185 AND p.ra < 186 AND p.dec > 15 AND p.dec < 16 AND p.clean = 1;
SELECT SELECT DISTINCT p.objid, p.ra, p.dec FROM photoobj p JOIN neighbors n ON p.objid = n.objid WHERE n.mode = 1 -- Assuming '1' corresponds to photometric observation AND p.ra BETWEEN 185 AND 186 AND p.dec BETWEEN 15 AND 16 AND p.ra IS NOT NULL AND p.dec IS NOT NULL;
SELECT so.specobjid AS object_id, so.ra AS right_ascension, so.dec AS declination, po.type AS photometric_object_type FROM specobj AS so JOIN photoobj AS po ON so.bestobjid = po.objid WHERE so.class = 'STAR' AND so.ra > 185 AND so.ra < 186 AND so.dec > 15 AND so.dec < 16;
SELECT SELECT photoobj.objid, specobj.ra, specobj.dec, specobj.z FROM specobj JOIN photoobj ON specobj.bestobjid = photoobj.objid WHERE specobj.class = 'STAR' AND specobj.ra BETWEEN 185 AND 186 AND specobj.dec BETWEEN 15 AND 16;
SELECT * FROM specobj WHERE class = 'GALAXY' AND ra > 185 AND ra < 186 AND dec > 15 AND dec < 16;
SELECT so.specobjid AS object_id, so.ra AS right_ascension, so.dec AS declination, so.z AS redshift FROM specobj AS so WHERE so.class = 'GALAXY' AND so.ra > 185 AND so.ra < 186 AND so.dec > 15 AND so.dec < 16;
SELECT * FROM photoobj WHERE ABS(u - g) < 0.4 AND ABS(g - r) < 0.7 AND ABS(r - i) > 0.4 AND ABS(i - z) > 0.4 AND objid IN (SELECT objid FROM neighbors WHERE type = 3) -- Assuming type 3 corresponds to stars
SELECT p.* FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE s.class = 'STAR' AND (p.u - p.g) < 0.4 AND (p.g - p.r) < 0.7 AND (p.r - p.i) > 0.4 AND (p.i - p.z) > 0.4;
SELECT p.objid FROM photoobj AS p JOIN neighbors AS n ON p.objid = n.objid JOIN specobj AS s ON p.objid = s.bestobjid WHERE n.distance < 0.05 AND ABS(p.u - p.g) < 0.4 AND ABS(p.g - p.r) < 0.7 AND ABS(p.r - p.i) > 0.4 AND ABS(p.i - p.z) > 0.4 AND s.class = 'STAR';
SELECT 1;
SELECT COUNT(*) FROM specobj AS S JOIN photoobj AS P ON S.bestobjid = P.objid WHERE S.class = 'GALAXY' AND P.cmodelmag_r < 17 AND P.clean = 1; -- Assuming clean flag indicates valid photometry
SELECT COUNT(*) FROM specobj AS S JOIN photoobj AS P ON S.bestobjid = P.objid WHERE S.class = 'GALAXY' AND P.cmodelmag_r < 17 AND P.clean = 1; -- Assuming clean = 1 indicates photometrically observable
SELECT p.objid, p.g FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE s.class = 'GALAXY' AND p.g < 22 AND (p.u - p.g) BETWEEN -0.27 AND 0.71 AND (p.g - p.r) BETWEEN -0.24 AND 0.35 AND (p.r - p.i) BETWEEN -0.27 AND 0.57 AND (p.i - p.z) BETWEEN -0.35 AND 0.7 ORDER BY p.g DESC;
SELECT SELECT p.objid, p.g FROM photoobj AS p WHERE p.g < 22 AND (p.u - p.g) >= -0.27 AND (p.u - p.g) < 0.71 AND (p.g - p.r) >= -0.24 AND (p.g - p.r) < 0.35 AND (p.r - p.i) >= -0.27 AND (p.r - p.i) < 0.57 AND (p.i - p.z) >= -0.35 AND (p.i - p.z) < 0.7 ORDER BY p.g DESC;
SELECT objid, ra, dec FROM photoobj WHERE i < 19 AND i > 0 AND (g - r) > 2.26 AND (i - z) < 0.25 AND ((u - g) > 2.0 OR u > 22.3);
SELECT SELECT p.objid FROM photoobj AS p JOIN neighbors AS n ON p.objid = n.objid JOIN photo_type AS pt ON p.type = pt.value WHERE pt.name = 'STAR' AND p.i < 19 AND p.i > 0 AND ABS(p.g - p.r) > 2.26 AND ABS(p.i - p.z) < 0.25 AND (ABS(p.u - p.g) > 2.0 OR p.u > 22.3);
SELECT p.objid, p.ra, p.dec FROM photoobj AS p JOIN photo_type AS pt ON p.type = pt.value WHERE pt.name = 'GALAXY' AND p.ra BETWEEN 140.9 AND 141.1 AND p.g < 18.0 AND (p.u - p.g) > 2.2;
SELECT p.objid, p.ra, p.dec FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE s.class = 'GALAXY' AND p.ra BETWEEN 140.9 AND 141.1 AND p.g < 18.0 AND (p.u - p.g) > 2.2
SELECT p.objid, p.ra, p.dec FROM specobj AS s JOIN photoobj AS p ON s.bestobjid = p.objid WHERE s.class = 'GALAXY' AND p.g BETWEEN 17 AND 18 AND s.z < 0.05;
SELECT so.specobjid AS objid, so.ra, so.dec FROM specobj AS so JOIN photoobj AS po ON so.bestobjid = po.objid WHERE so.class = 'GALAXY' AND po.g < 18.0 AND po.g > 17 AND so.z < 0.05;
SELECT SELECT DISTINCT p.objid, p.ra, p.dec FROM photoobj AS p JOIN neighbors AS n ON p.objid = n.objid WHERE p.type = 'STAR' AND p.clean = 1 AND ABS(n.distance) < 0.5; -- Assuming distance represents the magnitude difference
SELECT p.objid, p.ra, p.dec FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE s.class = 'STAR' AND (p.u - p.g) < 0.5 AND p.clean = 1;
SELECT u, g, r, i, z FROM photoobj WHERE type = (SELECT value FROM photo_type WHERE name = 'STAR') AND ABS(u - g) < 0.5;
SELECT p.u, p.g, p.r, p.i, p.z FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE s.class = 'STAR' AND (p.u - p.g) < 0.5;
SELECT p.objid, p.ra, p.dec FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE p.g > 17 AND p.g < 18 AND s.z < 0.05 AND s.class = 'GALAXY';
SELECT so.specobjid, po.ra, po.dec FROM specobj AS so JOIN photoobj AS po ON so.bestobjid = po.objid WHERE so.class = 'GALAXY' AND po.g BETWEEN 17 AND 18 AND so.z < 0.05;
SELECT p.u, p.g, p.r, p.i, p.z FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE s.class = 'GALAXY' AND p.g BETWEEN 17 AND 18 AND s.z < 0.05;
SELECT p.u, p.g, p.r, p.i, p.z FROM specobj AS s JOIN photoobj AS p ON s.bestobjid = p.objid WHERE s.class = 'GALAXY' AND p.g > 17 AND p.g < 18 AND s.z < 0.05;
SELECT p.objid AS Object_ID, n.neighborobjid AS Nearest_Neighbor_ID, n.distance AS Distance_to_Neighbor, p.type AS Center_Type FROM photoobj AS p JOIN neighbors AS n ON p.objid = n.objid;
SELECT n.objid AS Object_ID, n.neighborobjid AS Nearest_Neighbor_ID, n.distance AS Distance_To_Neighbor, n.type AS Center_Type FROM neighbors AS n
SELECT DISTINCT type FROM photoobj WHERE ra > 100 AND dec < 100
SELECT DISTINCT po.type FROM photoobj AS po JOIN specobj AS so ON po.objid = so.bestobjid WHERE so.ra > 100 AND so.dec < 100;
SELECT COUNT(*) FROM photoobj AS p JOIN photo_type AS pt ON p.type = pt.value WHERE pt.name = 'STAR';
SELECT COUNT(*) FROM photoobj JOIN photo_type ON photoobj.type = photo_type.value WHERE photo_type.name = 'STAR';
SELECT DISTINCT type FROM photoobj UNION SELECT DISTINCT neighbortype FROM neighbors;
SELECT DISTINCT mode FROM photoobj;
SELECT * FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE s.class = 'GALAXY';
SELECT * FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE s.class = 'GALAXY';
SELECT p.objid, p.ra, p.dec, pt.name AS observed_type FROM photoobj AS p JOIN photo_type AS pt ON p.type = pt.value WHERE pt.name = 'STAR';
SELECT p.ra, p.dec, pt.name AS observed_type FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid JOIN photo_type AS pt ON p.type = pt.value WHERE s.class = 'STAR';
SELECT p.objid, s.specobjid FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE s.class = 'GALAXY' AND (p.u - p.r) > 2.22 AND (p.g - p.i) > 1;
SELECT p.objid AS photometric_obj_id, s.specobjid AS spectroscopic_obj_id FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE s.class = 'GALAXY' AND (u - r > 2.22) AND (g - i > 1);
SELECT p.objid, p.mjd FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE s.class = 'STAR' AND s.subclass LIKE 'K%'
SELECT p.objid, p.mjd FROM specobj AS s JOIN photoobj AS p ON s.bestobjid = p.objid WHERE s.class = 'STAR' AND s.subclass IS NOT NULL;
SELECT specobj.z AS redshift, photoobj.ra AS right_ascension, photoobj.dec AS declination FROM photoobj JOIN specobj ON photoobj.objid = specobj.bestobjid WHERE specobj.subclass = 'STARFORMING';
SELECT s.z AS redshift, p.ra AS right_ascension, p.dec AS declination FROM specobj AS s JOIN photoobj AS p ON s.bestobjid = p.objid WHERE s.class = 'GALAXY' AND s.subclass = 'STARFORMING';
SELECT p.run, MIN(p.extinction_r) AS min_extinction_r FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE s.class = 'GALAXY' GROUP BY p.run
SELECT p.run, MIN(n.distance) AS min_extinction_r FROM photoobj AS p JOIN neighbors AS n ON p.objid = n.objid GROUP BY p.run;
SELECT p.ra, p.dec FROM specobj AS s JOIN photoobj AS p ON s.bestobjid = p.objid WHERE s.class = 'QSO';
SELECT ra, dec FROM specobj WHERE class = 'QSO';
SELECT COUNT(*) FROM neighbors AS n JOIN photoobj AS p ON n.objid = p.objid JOIN specobj AS s ON n.objid = s.bestobjid WHERE n.distance < 0.05 AND ABS(p.u - p.g) < 0.4 AND ABS(p.g - p.r) < 0.7 AND ABS(p.r - p.i) > 0.4 AND ABS(p.i - p.z) > 0.4 AND s.class = 'STAR' AND s.subclass = 'BINARY';
SELECT SELECT COUNT(*) FROM neighbors AS n JOIN photoobj AS p ON n.objid = p.objid WHERE n.distance < 0.05 AND n.type = 3 -- Assuming type 3 corresponds to Binary Star systems AND p.mode = 1; -- Assuming mode 1 corresponds to photometric observations
SELECT 1;
SELECT COUNT(*) FROM photoobj AS p JOIN neighbors AS n ON p.objid = n.objid WHERE n.distance < 0.05 AND p.type = 'Binary Star' -- Assuming 'Binary Star' is the type for Binary Star systems AND (p.u - p.g) < 0.4 -- Assuming p.u and p.g are the magnitudes for u and g bands AND (p.g - p.r) < 0.7 -- Assuming p.g and p.r are the magnitudes for g and r bands AND (p.r - p.i) > 0.4 -- Assuming p.r and p.i are the magnitudes for r and i bands AND (p.i - p.z) > 0.4; -- Assuming p.i and p.z are the magnitudes for i and z bands
SELECT DISTINCT p.objid FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE s.subclass = 'Carbon' AND p.type = (SELECT value FROM photo_type WHERE name = 'STAR');
SELECT SELECT DISTINCT p.objid FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid JOIN galspecline AS g ON s.specobjid = g.specobjid JOIN spplines AS sp ON s.specobjid = sp.specobjid WHERE p.type = 'STAR' AND p.clean = 1 AND s.subclass = 'Carbon';
SELECT COUNT(*) FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid WHERE s.class = 'GALAXY';
SELECT COUNT(*) FROM specobj AS s JOIN photoobj AS p ON s.bestobjid = p.objid WHERE s.class = 'GALAXY' AND p.clean = 1;
SELECT p.objid, s.class, s.subclass FROM specobj AS s JOIN photoobj AS p ON s.bestobjid = p.objid WHERE s.class = 'GALAXY' AND s.subclass LIKE '%AGN%'
SELECT specobj.specobjid, specobj.class, specobj.subclass FROM specobj JOIN photoobj ON specobj.bestobjid = photoobj.objid WHERE specobj.class = 'GALAXY' AND specobj.subclass = 'AGN';
SELECT SELECT MIN(n.distance) AS least_distance FROM neighbors AS n JOIN photoobj AS p ON n.objid = p.objid WHERE p.type = 'STAR' AND n.distance IS NOT NULL
SELECT MIN(n.distance) AS minimal_distance FROM neighbors AS n JOIN photoobj AS p ON n.objid = p.objid WHERE p.type = (SELECT value FROM photo_type WHERE name = 'STAR');
SELECT MAX(distance) AS longest_distance FROM neighbors WHERE type = 3;
SELECT MAX(n.distance) FROM neighbors AS n JOIN photoobj AS p ON n.objid = p.objid WHERE p.type = (SELECT value FROM photo_type WHERE name = 'STAR');
SELECT p.ra, p.dec, n.distance FROM neighbors AS n JOIN photoobj AS p ON n.objid = p.objid WHERE n.distance = (SELECT MIN(distance) FROM neighbors)
SELECT p.b AS Galactic_Latitude, p.l AS Galactic_Longitude, MIN(n.distance) AS Least_Distance FROM neighbors AS n JOIN photoobj AS p ON n.objid = p.objid GROUP BY p.objid ORDER BY Least_Distance ASC LIMIT 1;
SELECT P.ra, P.dec, N.distance FROM neighbors AS N JOIN photoobj AS P ON N.objid = P.objid WHERE N.distance = (SELECT MIN(distance) FROM neighbors)
SELECT p.ra, p.dec, n.distance FROM neighbors AS n JOIN photoobj AS p ON n.objid = p.objid WHERE n.distance = (SELECT MIN(distance) FROM neighbors)
SELECT 1;
SELECT s.z FROM specobj AS s JOIN photoobj AS p ON s.bestobjid = p.objid WHERE p.objid = ( SELECT n.objid FROM neighbors AS n ORDER BY n.distance LIMIT 1 );
SELECT 1;
SELECT s.z FROM specobj AS s JOIN photoobj AS p ON s.bestobjid = p.objid WHERE p.objid = ( SELECT n.objid FROM neighbors AS n ORDER BY n.distance LIMIT 1 );
SELECT DISTINCT run FROM photoobj;
SELECT DISTINCT run FROM photoobj;
SELECT COUNT(DISTINCT run) AS different_run_numbers FROM photoobj;
SELECT COUNT(DISTINCT run) AS unique_run_count FROM photoobj;
SELECT pt.name, COUNT(po.objid) AS object_count FROM photoobj AS po JOIN photo_type AS pt ON po.type = pt.value GROUP BY pt.name;
SELECT type, COUNT(*) AS object_count FROM photoobj GROUP BY type;
SELECT p.ra, p.dec, pt.name AS photometric_type FROM specobj AS s JOIN photoobj AS p ON s.bestobjid = p.objid JOIN photo_type AS pt ON p.type = pt.value WHERE s.class = 'GALAXY' OR s.class = 'STAR';
SELECT ra, dec FROM specobj WHERE class IN ('GALAXY', 'STAR');
SELECT objid, type FROM photoobj WHERE ra > 100 AND dec < 100
SELECT photoobj.objid, photo_type.name FROM photoobj JOIN photo_type ON photoobj.type = photo_type.value WHERE photoobj.ra > 100 AND photoobj.dec < 100;
SELECT p.objid, p.ra, p.dec FROM photoobj AS p JOIN specobj AS s ON p.objid = s.bestobjid JOIN galspecline AS g ON s.specobjid = g.specobjid WHERE s.class = 'GALAXY';
SELECT p.objid, p.ra, p.dec FROM specobj AS s JOIN photoobj AS p ON s.bestobjid = p.objid WHERE s.class = 'GALAXY';
SELECT DISTINCT so.specobjid FROM specobj AS so WHERE so.class IN ('GALAXY', 'STAR');
SELECT specobj.specobjid, specobj.class, specobj.subclass FROM specobj WHERE specobj.class = 'STAR';
SELECT COUNT(*) FROM specobj WHERE class IN ('GALAXY', 'STAR');
SELECT COUNT(*) FROM specobj WHERE class IN ('GALAXY', 'STAR');
SELECT * FROM specobj AS so JOIN galspecline AS g ON so.specobjid = g.specobjid WHERE so.class = 'GALAXY';
SELECT * FROM specobj AS so JOIN galspecline AS gsc ON so.specobjid = gsc.specobjid WHERE so.class = 'GALAXY';
