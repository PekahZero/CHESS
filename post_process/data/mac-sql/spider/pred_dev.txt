SELECT COUNT(*) FROM singer;
SELECT COUNT(*) FROM singer;
SELECT Name, Country, Age FROM singer ORDER BY Age DESC
SELECT Name, Country, Age FROM singer ORDER BY Age DESC
SELECT AVG(Age) AS Average_Age, MIN(Age) AS Minimum_Age, MAX(Age) AS Maximum_Age FROM singer WHERE Country = 'France';
SELECT AVG(Age) AS Average_Age, MIN(Age) AS Minimum_Age, MAX(Age) AS Maximum_Age FROM singer WHERE Country = 'France';
SELECT Song_Name, Song_release_year FROM singer WHERE Age = (SELECT MIN(Age) FROM singer)
SELECT Song_Name, Song_release_year FROM singer WHERE Singer_ID = (SELECT Singer_ID FROM singer ORDER BY Age ASC LIMIT 1);
SELECT DISTINCT Country FROM singer WHERE Age > 20
SELECT DISTINCT Country FROM singer WHERE Age > 20
SELECT Country, COUNT(*) AS Number_of_Singers FROM singer GROUP BY Country
SELECT Country, COUNT(*) AS NumberOfSingers FROM singer GROUP BY Country
SELECT Song_Name FROM singer WHERE Age > (SELECT AVG(Age) FROM singer);
SELECT Song_Name FROM singer WHERE Age > (SELECT AVG(Age) FROM singer);
SELECT Location, Name FROM stadium WHERE Capacity BETWEEN 5000 AND 10000;
SELECT Location, Name FROM stadium WHERE Capacity BETWEEN 5000 AND 10000;
SELECT MAX(Capacity) AS Maximum_Capacity, AVG(Capacity) AS Average_Capacity FROM stadium;
SELECT AVG(Capacity) AS Average_Capacity, MAX(Capacity) AS Maximum_Capacity FROM stadium;
SELECT Name, Capacity FROM stadium WHERE Average = (SELECT MAX(Average) FROM stadium);
SELECT Name, Capacity FROM stadium WHERE Average = (SELECT MAX(Average) FROM stadium);
SELECT COUNT(*) FROM concert WHERE Year IN ('2014', '2015')
SELECT COUNT(*) FROM concert WHERE Year IN ('2014', '2015')
SELECT T1.`Name`, COUNT(*) FROM stadium AS T1 JOIN concert AS T2 ON T1.`Stadium_ID` = T2.`Stadium_ID` GROUP BY T1.`Stadium_ID`
SELECT T1.`Name`, COUNT(*) AS Number_of_Concerts FROM stadium AS T1 LEFT JOIN concert AS T2 ON T1.`Stadium_ID` = T2.`Stadium_ID` GROUP BY T1.`Stadium_ID`
SELECT T1.`Name`, T1.`Capacity`, COUNT(*) AS Concert_Count FROM stadium AS T1 JOIN concert AS T2 ON T1.`Stadium_ID` = T2.`Stadium_ID` WHERE T2.`Year` >= '2014' GROUP BY T1.`Stadium_ID` ORDER BY Concert_Count DESC LIMIT 1;
SELECT T1.Name, T1.Capacity FROM stadium AS T1 JOIN concert AS T2 ON T1.Stadium_ID = T2.Stadium_ID WHERE T2.Year > '2013' GROUP BY T1.Stadium_ID ORDER BY COUNT(T2.concert_ID) DESC LIMIT 1;
SELECT Year, COUNT(*) AS concert_count FROM concert GROUP BY Year ORDER BY concert_count DESC LIMIT 1;
SELECT Year, COUNT(*) AS concert_count FROM concert GROUP BY Year ORDER BY concert_count DESC LIMIT 1;
SELECT T1.`Name` FROM stadium AS T1 LEFT JOIN concert AS T2 ON T1.`Stadium_ID` = T2.`Stadium_ID` WHERE T2.`concert_ID` IS NULL;
SELECT T1.`Name` FROM stadium AS T1 LEFT JOIN concert AS T2 ON T1.`Stadium_ID` = T2.`Stadium_ID` WHERE T2.`concert_ID` IS NULL;
SELECT DISTINCT Country FROM singer WHERE Age > 40 UNION SELECT DISTINCT Country FROM singer WHERE Age < 30;
SELECT s.Name FROM stadium AS s LEFT JOIN concert AS c ON s.Stadium_ID = c.Stadium_ID AND c.Year = '2014' WHERE c.concert_ID IS NULL;
SELECT s.Name FROM stadium AS s LEFT JOIN concert AS c ON s.Stadium_ID = c.Stadium_ID AND c.Year = '2014' WHERE c.concert_ID IS NULL;
SELECT concert.concert_Name, concert.Theme, COUNT(singer_in_concert.Singer_ID) AS Number_of_Singers FROM concert LEFT JOIN singer_in_concert ON concert.concert_ID = singer_in_concert.concert_ID GROUP BY concert.concert_ID;
SELECT C.concert_Name, C.Theme, COUNT(SIC.Singer_ID) AS Number_of_Singers FROM concert AS C LEFT JOIN singer_in_concert AS SIC ON C.concert_ID = SIC.concert_ID GROUP BY C.concert_ID;
SELECT S.`Name`, COUNT(SIC.`concert_ID`) AS Number_of_Concerts FROM singer AS S LEFT JOIN singer_in_concert AS SIC ON S.`Singer_ID` = SIC.`Singer_ID` GROUP BY S.`Singer_ID`
SELECT s.`Name`, COUNT(sc.`concert_ID`) AS Number_of_Concerts FROM singer AS s LEFT JOIN singer_in_concert AS sc ON s.`Singer_ID` = sc.`Singer_ID` GROUP BY s.`Singer_ID`
SELECT DISTINCT s.`Name` FROM singer AS s JOIN singer_in_concert AS sic ON s.`Singer_ID` = sic.`Singer_ID` JOIN concert AS c ON sic.`concert_ID` = c.`concert_ID` WHERE c.`Year` = '2014'
SELECT DISTINCT s.Name FROM singer AS s JOIN singer_in_concert AS sic ON s.Singer_ID = sic.Singer_ID JOIN concert AS c ON sic.concert_ID = c.concert_ID WHERE c.Year = '2014';
SELECT `Name`, `Country` FROM singer WHERE `Song_Name` LIKE '%Hey%'
SELECT Name, Country FROM singer WHERE Song_Name LIKE '%Hey%'
SELECT DISTINCT S.Name, S.Location FROM stadium AS S JOIN concert AS C ON S.Stadium_ID = C.Stadium_ID WHERE C.Year IN ('2014', '2015') GROUP BY S.Stadium_ID HAVING COUNT(DISTINCT C.Year) = 2;
SELECT S.Name, S.Location FROM stadium AS S JOIN concert AS C ON S.Stadium_ID = C.Stadium_ID WHERE C.Year IN ('2014', '2015') GROUP BY S.Stadium_ID HAVING COUNT(DISTINCT C.Year) = 2;
SELECT COUNT(*) FROM concert WHERE Stadium_ID = (SELECT Stadium_ID FROM stadium ORDER BY Capacity DESC LIMIT 1);
SELECT COUNT(*) FROM concert WHERE Stadium_ID = ( SELECT Stadium_ID FROM stadium ORDER BY Capacity DESC LIMIT 1 )
SELECT COUNT(*) FROM Pets WHERE weight > 10
SELECT COUNT(*) FROM Pets WHERE weight > 10
SELECT weight FROM Pets WHERE PetType = 'dog' ORDER BY pet_age ASC LIMIT 1;
SELECT weight FROM Pets WHERE PetType = 'dog' AND pet_age = (SELECT MIN(pet_age) FROM Pets WHERE PetType = 'dog');
SELECT PetType, MAX(weight) AS Max_Weight FROM Pets GROUP BY PetType
SELECT PetType, MAX(weight) AS MaxWeight FROM Pets GROUP BY PetType;
SELECT COUNT(*) AS NumberOfPets FROM Has_Pet AS HP JOIN Student AS S ON HP.StuID = S.StuID WHERE S.Age > 20;
SELECT COUNT(*) FROM Has_Pet AS HP JOIN Student AS S ON HP.StuID = S.StuID WHERE S.Age > 20;
SELECT COUNT(*) FROM Student AS S JOIN Has_Pet AS HP ON S.StuID = HP.StuID JOIN Pets AS P ON HP.PetID = P.PetID WHERE S.Sex = 'F' AND P.PetType = 'dog';
SELECT COUNT(*) FROM Student AS S JOIN Has_Pet AS HP ON S.StuID = HP.StuID JOIN Pets AS P ON HP.PetID = P.PetID WHERE S.Sex = 'F' AND P.PetType = 'dog';
SELECT COUNT(DISTINCT PetType) FROM Pets;
SELECT COUNT(DISTINCT PetType) FROM Pets;
SELECT DISTINCT S.Fname FROM Student AS S JOIN Has_Pet AS HP ON S.StuID = HP.StuID JOIN Pets AS P ON HP.PetID = P.PetID WHERE P.PetType IN ('cat', 'dog');
SELECT DISTINCT S.Fname FROM Student AS S JOIN Has_Pet AS HP ON S.StuID = HP.StuID JOIN Pets AS P ON HP.PetID = P.PetID WHERE P.PetType IN ('cat', 'dog');
SELECT S.Fname FROM Student AS S JOIN Has_Pet AS HP ON S.StuID = HP.StuID JOIN Pets AS P ON HP.PetID = P.PetID WHERE P.PetType IN ('cat', 'dog') GROUP BY S.StuID HAVING COUNT(DISTINCT P.PetType) = 2;
SELECT S.Fname FROM Student AS S JOIN Has_Pet AS HP ON S.StuID = HP.StuID JOIN Pets AS P ON HP.PetID = P.PetID WHERE P.PetType IN ('cat', 'dog') GROUP BY S.StuID HAVING COUNT(DISTINCT P.PetType) = 2;
SELECT S.Major, S.Age FROM Student AS S LEFT JOIN Has_Pet AS HP ON S.StuID = HP.StuID LEFT JOIN Pets AS P ON HP.PetID = P.PetID AND P.PetType = 'cat' WHERE P.PetID IS NULL;
SELECT S.Major, S.Age FROM Student AS S LEFT JOIN Has_Pet AS HP ON S.StuID = HP.StuID LEFT JOIN Pets AS P ON HP.PetID = P.PetID WHERE P.PetType IS NULL OR P.PetType != 'cat';
SELECT StuID FROM Student AS S WHERE NOT EXISTS ( SELECT 1 FROM Has_Pet AS HP JOIN Pets AS P ON HP.PetID = P.PetID WHERE HP.StuID = S.StuID AND P.PetType = 'cat' );
SELECT S.StuID FROM Student S WHERE NOT EXISTS ( SELECT 1 FROM Has_Pet HP JOIN Pets P ON HP.PetID = P.PetID WHERE HP.StuID = S.StuID AND P.PetType = 'cat' );
SELECT S.Fname, S.Age FROM Student AS S JOIN Has_Pet AS HP ON S.StuID = HP.StuID JOIN Pets AS P ON HP.PetID = P.PetID WHERE P.PetType = 'dog' AND S.StuID NOT IN ( SELECT HP2.StuID FROM Has_Pet AS HP2 JOIN Pets AS P2 ON HP2.PetID = P2.PetID WHERE P2.PetType = 'cat' );
SELECT DISTINCT S.Fname FROM Student S JOIN Has_Pet HP ON S.StuID = HP.StuID JOIN Pets P ON HP.PetID = P.PetID WHERE P.PetType = 'dog' AND S.StuID NOT IN ( SELECT HP2.StuID FROM Has_Pet HP2 JOIN Pets P2 ON HP2.PetID = P2.PetID WHERE P2.PetType = 'cat' );
SELECT PetType, weight FROM Pets WHERE pet_age = (SELECT MIN(pet_age) FROM Pets);
SELECT PetType, weight FROM Pets WHERE pet_age = (SELECT MIN(pet_age) FROM Pets);
SELECT Pets.PetID, Pets.weight FROM Pets WHERE Pets.pet_age > 1
SELECT PetID, weight FROM Pets WHERE pet_age > 1
SELECT P.PetType, AVG(P.pet_age) AS Average_Age, MAX(P.pet_age) AS Maximum_Age FROM Pets AS P JOIN Has_Pet AS HP ON P.PetID = HP.PetID GROUP BY P.PetType;
SELECT PetType, AVG(pet_age) AS Average_Age, MAX(pet_age) AS Maximum_Age FROM Pets GROUP BY PetType;
SELECT PetType, AVG(weight) AS Average_Weight FROM Pets GROUP BY PetType
SELECT PetType, AVG(weight) AS Average_Weight FROM Pets GROUP BY PetType;
SELECT S.Fname, S.Age FROM Student AS S JOIN Has_Pet AS HP ON S.StuID = HP.StuID
SELECT DISTINCT S.Fname, S.Age FROM Student AS S JOIN Has_Pet AS HP ON S.StuID = HP.StuID;
SELECT H.PetID FROM Has_Pet AS H JOIN Student AS S ON H.StuID = S.StuID WHERE S.LName = 'Smith'
SELECT H.PetID FROM Has_Pet AS H JOIN Student AS S ON H.StuID = S.StuID WHERE S.LName = 'Smith'
SELECT H.StuID, COUNT(H.PetID) AS NumberOfPets FROM Has_Pet AS H GROUP BY H.StuID
SELECT StuID, COUNT(PetID) AS PetCount FROM Has_Pet GROUP BY StuID;
SELECT S.Fname, S.Sex FROM Student AS S JOIN Has_Pet AS HP ON S.StuID = HP.StuID GROUP BY S.StuID HAVING COUNT(HP.PetID) > 1;
SELECT S.Fname, S.Sex FROM Student AS S JOIN Has_Pet AS HP ON S.StuID = HP.StuID GROUP BY S.StuID HAVING COUNT(HP.PetID) > 1;
SELECT S.LName FROM Student AS S JOIN Has_Pet AS HP ON S.StuID = HP.StuID JOIN Pets AS P ON HP.PetID = P.PetID WHERE P.PetType = 'cat' AND P.pet_age = 3;
SELECT S.LName FROM Student AS S JOIN Has_Pet AS HP ON S.StuID = HP.StuID JOIN Pets AS P ON HP.PetID = P.PetID WHERE P.PetType = 'cat' AND P.pet_age = 3;
SELECT AVG(S.Age) AS Average_Age FROM Student AS S LEFT JOIN Has_Pet AS HP ON S.StuID = HP.StuID WHERE HP.PetID IS NULL;
SELECT AVG(S.Age) AS Average_Age FROM Student AS S LEFT JOIN Has_Pet AS HP ON S.StuID = HP.StuID WHERE HP.PetID IS NULL;
SELECT COUNT(*) FROM continents;
SELECT COUNT(*) FROM continents;
SELECT c.ContId, c.Continent, COUNT(co.CountryId) AS CountryCount FROM continents AS c LEFT JOIN countries AS co ON c.ContId = co.Continent GROUP BY c.ContId, c.Continent
SELECT c.ContId, c.Continent, COUNT(co.CountryId) AS CountryCount FROM continents AS c LEFT JOIN countries AS co ON c.ContId = co.Continent GROUP BY c.ContId, c.Continent;
SELECT COUNT(*) FROM countries;
SELECT COUNT(*) FROM countries;
SELECT cm.FullName, cm.Id, COUNT(ml.ModelId) AS ModelCount FROM car_makers AS cm LEFT JOIN model_list AS ml ON cm.Id = ml.Maker GROUP BY cm.Id, cm.FullName
SELECT cm.Id, cm.FullName, COUNT(ml.ModelId) AS ModelCount FROM car_makers AS cm LEFT JOIN model_list AS ml ON cm.Id = ml.Maker GROUP BY cm.Id, cm.FullName
-- SQL script type: SELECT SELECT cn.Model FROM cars_data cd JOIN car_names cn ON cd.Id = cn.MakeId WHERE cd.Horsepower = (SELECT MIN(Horsepower) FROM cars_data WHERE Horsepower IS NOT NULL)
SELECT cn.Model FROM cars_data AS cd JOIN car_names AS cn ON cd.Id = cn.MakeId WHERE cd.Horsepower = (SELECT MIN(Horsepower) FROM cars_data)
SELECT cn.Model FROM car_names AS cn JOIN cars_data AS cd ON cn.MakeId = cd.Id WHERE cd.Weight < (SELECT AVG(Weight) FROM cars_data);
SELECT Model FROM car_names WHERE MakeId IN ( SELECT Id FROM cars_data WHERE Weight < (SELECT AVG(Weight) FROM cars_data) )
SELECT DISTINCT cm.Maker FROM car_makers AS cm JOIN model_list AS ml ON cm.Id = ml.Maker JOIN car_names AS cn ON ml.Model = cn.Model JOIN cars_data AS cd ON cn.MakeId = cd.Id WHERE cd.Year = 1970;
SELECT DISTINCT cm.Maker FROM car_makers AS cm JOIN model_list AS ml ON cm.Id = ml.Maker JOIN car_names AS cn ON ml.Model = cn.Model JOIN cars_data AS cd ON cn.MakeId = cd.Id WHERE cd.Year = 1970;
SELECT CN.Make, CD.Year FROM car_names AS CN JOIN cars_data AS CD ON CN.MakeId = CD.Id WHERE CD.Year = (SELECT MIN(Year) FROM cars_data);
SELECT cm.Maker, cd.Year FROM cars_data AS cd JOIN car_names AS cn ON cd.Id = cn.MakeId JOIN model_list AS ml ON cn.Model = ml.Model JOIN car_makers AS cm ON ml.Maker = cm.Id WHERE cd.Year = (SELECT MIN(Year) FROM cars_data);
SELECT DISTINCT Model FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE cars_data.Year > 1980;
SELECT DISTINCT cn.Model FROM cars_data AS cd JOIN car_names AS cn ON cd.Id = cn.MakeId WHERE cd.Year > 1980;
SELECT c.Continent, COUNT(cm.Id) AS MakerCount FROM continents AS c JOIN countries AS co ON c.ContId = co.Continent JOIN car_makers AS cm ON co.CountryId = cm.Country GROUP BY c.Continent;
SELECT c.Continent, COUNT(cm.Id) AS NumberOfCarMakers FROM continents AS c LEFT JOIN countries AS co ON c.ContId = co.Continent LEFT JOIN car_makers AS cm ON co.CountryId = cm.Country GROUP BY c.Continent
SELECT CountryName FROM countries WHERE CountryId IN ( SELECT Country FROM car_makers GROUP BY Country ORDER BY COUNT(*) DESC LIMIT 1 );
SELECT CountryName FROM countries WHERE CountryId IN ( SELECT Country FROM car_makers GROUP BY Country ORDER BY COUNT(*) DESC LIMIT 1 );
SELECT T1.`FullName`, COUNT(T2.`Model`) AS ModelCount FROM car_makers AS T1 JOIN model_list AS T2 ON T1.`Id` = T2.`Maker` GROUP BY T1.`FullName`
SELECT cm.Id, cm.FullName, COUNT(ml.ModelId) AS NumberOfModels FROM car_makers AS cm LEFT JOIN model_list AS ml ON cm.Id = ml.Maker GROUP BY cm.Id, cm.FullName;
SELECT cd.Accelerate FROM cars_data AS cd JOIN car_names AS cn ON cd.Id = cn.MakeId WHERE cn.Model = 'amc hornet sportabout';
SELECT cars_data.Accelerate FROM car_names JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_names.Model = 'hornet sportabout' AND car_names.Make = 'amc';
SELECT COUNT(*) FROM car_makers WHERE Country = (SELECT CountryId FROM countries WHERE CountryName = 'france')
SELECT COUNT(*) FROM car_makers WHERE Country = (SELECT CountryId FROM countries WHERE CountryName = 'france');
SELECT COUNT(DISTINCT ml.Model) AS NumberOfCarModels FROM car_makers AS cm JOIN countries AS c ON cm.Country = c.CountryId JOIN model_list AS ml ON cm.Id = ml.Maker WHERE c.CountryName = 'usa';
SELECT COUNT(*) FROM model_list AS M JOIN car_makers AS C ON M.Maker = C.Id JOIN countries AS CO ON C.Country = CO.CountryId WHERE CO.CountryName = 'usa';
SELECT AVG(MPG) AS Average_MPG FROM cars_data WHERE Cylinders = 4;
SELECT AVG(MPG) FROM cars_data WHERE Cylinders = 4
SELECT MIN(Weight) FROM cars_data WHERE Cylinders = 8 AND Year = '1974';
SELECT MIN(Weight) FROM cars_data WHERE Cylinders = 8 AND Year = '1974';
SELECT car_makers.Maker, model_list.Model FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker;
SELECT car_makers.Maker, model_list.Model FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker;
SELECT c.CountryId, c.CountryName FROM countries AS c JOIN car_makers AS cm ON c.CountryId = cm.Country GROUP BY c.CountryId, c.CountryName;
SELECT DISTINCT c.CountryId, c.CountryName FROM countries AS c JOIN car_makers AS cm ON c.CountryId = cm.Country
SELECT COUNT(*) FROM cars_data WHERE Horsepower > '150'
SELECT COUNT(*) FROM cars_data WHERE Horsepower > '150'
SELECT Year, AVG(Weight) AS Average_Weight FROM cars_data GROUP BY Year;
SELECT Year, AVG(Weight) AS Average_Weight FROM cars_data GROUP BY Year;
SELECT c.CountryName FROM countries AS c JOIN car_makers AS cm ON c.CountryId = cm.Country WHERE c.Continent = (SELECT ContId FROM continents WHERE Continent = 'europe') GROUP BY c.CountryName HAVING COUNT(cm.Id) >= 3;
SELECT c.CountryName FROM countries AS c JOIN car_makers AS m ON c.CountryId = m.Country WHERE c.Continent = (SELECT ContId FROM continents WHERE Continent = 'europe') GROUP BY c.CountryId HAVING COUNT(m.Id) >= 3;
SELECT MAX(cars_data.Horsepower) AS MaxHorsepower, car_names.Make FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId JOIN model_list ON car_names.Model = model_list.Model JOIN car_makers ON model_list.Maker = car_makers.Id JOIN countries ON car_makers.Country = countries.CountryId JOIN continents ON countries.Continent = continents.ContId WHERE cars_data.Cylinders = 3 GROUP BY car_names.Make
SELECT MAX(cars_data.Horsepower) AS MaxHorsepower, car_names.Make FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.Cylinders = 3 GROUP BY car_names.Make ORDER BY MaxHorsepower DESC LIMIT 1;
SELECT car_names.Model FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.MPG = (SELECT MAX(MPG) FROM cars_data);
-- SQL Script Type: SELECT SELECT ml.Model FROM cars_data cd JOIN car_names cn ON cd.Id = cn.MakeId JOIN model_list ml ON cn.Model = ml.Model WHERE cd.MPG IS NOT NULL AND cd.MPG = (SELECT MAX(MPG) FROM cars_data WHERE MPG IS NOT NULL);
SELECT AVG(Horsepower) AS Average_Horsepower FROM cars_data WHERE Year < 1980;
SELECT AVG(Horsepower) AS Average_Horsepower FROM cars_data WHERE Year < 1980;
SELECT AVG(cars_data.Edispl) AS AverageEdispl FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker JOIN car_names ON model_list.Model = car_names.Model JOIN cars_data ON car_names.MakeId = cars_data.Id WHERE car_makers.Maker = 'volvo';
SELECT AVG(cars_data.Edispl) AS Average_Edispl FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId JOIN model_list ON car_names.Model = model_list.Model JOIN car_makers ON model_list.Maker = car_makers.Id WHERE car_makers.Maker = 'volvo';
SELECT Cylinders, MAX(Accelerate) AS Max_Accelerate FROM cars_data GROUP BY Cylinders;
SELECT Cylinders, MAX(Accelerate) AS Max_Accelerate FROM cars_data GROUP BY Cylinders;
SELECT Model, COUNT(DISTINCT Make) AS VersionCount FROM car_names GROUP BY Model ORDER BY VersionCount DESC LIMIT 1;
SELECT Model, COUNT(*) AS VersionCount FROM car_names GROUP BY Model ORDER BY VersionCount DESC LIMIT 1;
SELECT COUNT(*) FROM cars_data WHERE Cylinders > 4;
SELECT COUNT(*) FROM cars_data WHERE Cylinders > 4;
SELECT COUNT(*) FROM cars_data WHERE Year = '1980';
SELECT COUNT(*) FROM cars_data WHERE Year = '1980';
SELECT COUNT(*) FROM model_list AS ml JOIN car_makers AS cm ON ml.Maker = cm.Id WHERE cm.FullName = 'American Motor Company';
SELECT COUNT(*) FROM model_list WHERE Maker = (SELECT Id FROM car_makers WHERE Maker = 'amc')
SELECT cm.FullName, cm.Id FROM car_makers AS cm JOIN model_list AS ml ON cm.Id = ml.Maker GROUP BY cm.Id HAVING COUNT(ml.ModelId) > 3;
SELECT cm.Id, cm.Maker FROM car_makers AS cm JOIN model_list AS ml ON cm.Id = ml.Maker GROUP BY cm.Id HAVING COUNT(ml.ModelId) > 3;
SELECT DISTINCT ml.Model FROM model_list AS ml JOIN car_makers AS cm ON ml.Maker = cm.Id JOIN car_names AS cn ON ml.Model = cn.Model JOIN cars_data AS cd ON cn.MakeId = cd.Id WHERE cm.FullName = 'General Motors' OR cd.Weight > 3500;
SELECT DISTINCT ml.Model FROM model_list AS ml JOIN car_makers AS cm ON ml.Maker = cm.Id JOIN car_names AS cn ON ml.Model = cn.Model JOIN cars_data AS cd ON cn.MakeId = cd.Id WHERE cm.FullName = 'General Motors' OR cd.Weight > 3500;
SELECT DISTINCT Year FROM cars_data WHERE Weight >= 3000 AND Weight <= 4000;
SELECT DISTINCT Year FROM cars_data WHERE Weight < 4000 OR Weight > 3000 GROUP BY Year HAVING COUNT(CASE WHEN Weight < 4000 THEN 1 END) > 0 AND COUNT(CASE WHEN Weight > 3000 THEN 1 END) > 0;
SELECT Horsepower FROM cars_data WHERE Accelerate = (SELECT MAX(Accelerate) FROM cars_data);
SELECT Horsepower FROM cars_data WHERE Accelerate = (SELECT MAX(Accelerate) FROM cars_data);
SELECT MIN(cars_data.Cylinders) FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId JOIN model_list ON car_names.Model = model_list.Model JOIN car_makers ON model_list.Maker = car_makers.Id WHERE car_makers.Maker = 'volvo' ORDER BY cars_data.Accelerate ASC LIMIT 1;
SELECT MIN(cars_data.Cylinders) FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId JOIN model_list ON car_names.Model = model_list.Model JOIN car_makers ON model_list.Maker = car_makers.Id WHERE car_makers.Maker = 'volvo' ORDER BY cars_data.Accelerate ASC LIMIT 1;
SELECT COUNT(*) FROM cars_data WHERE Accelerate > (SELECT MAX(Horsepower) FROM cars_data);
SELECT COUNT(*) FROM cars_data WHERE Accelerate > (SELECT MAX(Horsepower) FROM cars_data);
SELECT COUNT(*) FROM ( SELECT countries.CountryName, COUNT(car_makers.Id) AS MakerCount FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country GROUP BY countries.CountryId HAVING COUNT(car_makers.Id) > 2 ) AS CountryWithMoreThanTwoMakers;
SELECT COUNT(*) FROM ( SELECT countries.CountryName FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country GROUP BY countries.CountryId HAVING COUNT(car_makers.Id) > 2 ) AS subquery;
SELECT COUNT(*) FROM cars_data WHERE Cylinders > 6;
SELECT COUNT(*) FROM cars_data WHERE Cylinders > 6;
SELECT Model FROM model_list AS M JOIN cars_data AS C ON M.ModelId = C.Id WHERE C.Cylinders = 4 ORDER BY C.Horsepower DESC LIMIT 1;
SELECT car_names.Model FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.Cylinders = 4 ORDER BY cars_data.Horsepower DESC LIMIT 1;
SELECT car_names.MakeId, car_names.Make FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.Horsepower > (SELECT MIN(Horsepower) FROM cars_data) AND cars_data.Cylinders <= 3;
SELECT car_names.MakeId, car_names.Make FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.Horsepower < (SELECT MIN(Horsepower) FROM cars_data) AND cars_data.Cylinders < 4;
SELECT MAX(MPG) FROM cars_data WHERE Cylinders = 8 OR Year < 1980;
SELECT MAX(MPG) FROM cars_data WHERE Cylinders = 8 OR Year < 1980;
SELECT CN.Model FROM cars_data AS CD JOIN car_names AS CN ON CD.Id = CN.MakeId JOIN model_list AS ML ON CN.Model = ML.Model JOIN car_makers AS CM ON ML.Maker = CM.Id WHERE CD.Weight < 3500 AND CM.FullName != 'Ford Motor Company';
SELECT DISTINCT cn.Model FROM cars_data AS cd JOIN car_names AS cn ON cd.Id = cn.MakeId JOIN model_list AS ml ON cn.Model = ml.Model JOIN car_makers AS cm ON ml.Maker = cm.Id WHERE cd.Weight < 3500 AND cm.Maker != 'Ford'
SELECT c.CountryName FROM countries AS c LEFT JOIN car_makers AS cm ON c.CountryId = cm.Country WHERE cm.Id IS NULL;
SELECT c.CountryName FROM countries AS c LEFT JOIN car_makers AS cm ON c.CountryId = cm.Country WHERE cm.Country IS NULL;
SELECT cm.Id, cm.Maker FROM car_makers AS cm JOIN model_list AS ml ON cm.Id = ml.Maker GROUP BY cm.Id, cm.Maker HAVING COUNT(ml.ModelId) >= 2 AND (SELECT COUNT(DISTINCT Id) FROM car_makers) > 3;
SELECT cm.Id, cm.Maker FROM car_makers AS cm JOIN model_list AS ml ON cm.Id = ml.Maker JOIN car_names AS cn ON ml.Model = cn.Model JOIN cars_data AS cd ON cn.MakeId = cd.Id GROUP BY cm.Id, cm.Maker HAVING COUNT(DISTINCT ml.Model) >= 2 AND COUNT(cd.Id) > 3;
SELECT c.CountryId, c.CountryName FROM countries AS c LEFT JOIN car_makers AS cm ON c.CountryId = cm.Country GROUP BY c.CountryId HAVING COUNT(cm.Id) > 3 OR c.CountryId IN ( SELECT DISTINCT cn.MakeId FROM car_names AS cn JOIN model_list AS ml ON cn.Model = ml.Model WHERE ml.Maker IN ( SELECT cm.Id FROM car_makers AS cm WHERE cm.Maker = 'fiat' ) );
SELECT DISTINCT c.CountryId, c.CountryName FROM countries AS c LEFT JOIN car_makers AS cm ON c.CountryId = cm.Country LEFT JOIN model_list AS ml ON cm.Id = ml.Maker LEFT JOIN car_names AS cn ON ml.Model = cn.Model WHERE c.CountryId IN ( SELECT Country FROM car_makers GROUP BY Country HAVING COUNT(*) > 3 ) OR c.CountryId IN ( SELECT DISTINCT c.CountryId FROM countries AS c JOIN car_makers AS cm ON c.CountryId = cm.Country JOIN model_list AS ml ON cm.Id = ml.Maker JOIN car_names AS cn ON ml.Model = cn.Model WHERE cn.Model LIKE '%Fiat%' );
SELECT Country FROM airlines WHERE Airline = 'JetBlue Airways'
SELECT Country FROM airlines WHERE Airline = 'JetBlue Airways'
SELECT Abbreviation FROM airlines WHERE Airline = 'JetBlue Airways'
SELECT Abbreviation FROM airlines WHERE Airline = 'JetBlue Airways'
SELECT Airline, Abbreviation FROM airlines WHERE Country = 'USA'
SELECT Airline, Abbreviation FROM airlines WHERE Country = 'USA'
SELECT AirportCode, AirportName FROM airports WHERE City = 'Anthony';
SELECT AirportCode, AirportName FROM airports WHERE City = 'Anthony';
SELECT COUNT(*) FROM airlines;
SELECT COUNT(*) FROM airlines;
SELECT COUNT(*) FROM airports;
SELECT COUNT(*) FROM airports;
SELECT COUNT(*) AS Total_Flights FROM flights;
SELECT COUNT(*) FROM flights
SELECT Airline FROM airlines WHERE Abbreviation = 'UAL'
SELECT Airline FROM airlines WHERE Abbreviation = 'UAL'
SELECT COUNT(*) FROM airlines WHERE Country = 'USA'
SELECT COUNT(*) FROM airlines WHERE Country = 'USA'
SELECT City, Country FROM airports WHERE AirportName = 'Alton';
SELECT City, Country FROM airports WHERE AirportName = 'Alton'
SELECT AirportName FROM airports WHERE AirportCode = 'AKO'
SELECT AirportName FROM airports WHERE AirportCode = 'AKO'
SELECT AirportName FROM airports WHERE City = 'Aberdeen';
SELECT AirportName FROM airports WHERE City = 'Aberdeen';
SELECT COUNT(*) FROM flights WHERE SourceAirport = 'APG';
SELECT COUNT(*) FROM flights WHERE SourceAirport = 'APG'
SELECT COUNT(*) FROM flights WHERE DestAirport = 'ATO';
SELECT COUNT(*) FROM flights WHERE DestAirport = 'ATO';
SELECT COUNT(*) FROM flights WHERE SourceAirport = (SELECT AirportCode FROM airports WHERE City = 'Aberdeen');
SELECT COUNT(*) FROM flights WHERE SourceAirport = (SELECT AirportCode FROM airports WHERE City = 'Aberdeen')
SELECT COUNT(*) FROM flights AS F JOIN airports AS A ON F.DestAirport = A.AirportCode WHERE A.City = 'Aberdeen';
SELECT COUNT(*) FROM flights WHERE DestAirport = (SELECT AirportCode FROM airports WHERE City = 'Aberdeen')
SELECT COUNT(*) FROM flights AS F JOIN airports AS A1 ON F.SourceAirport = A1.AirportCode JOIN airports AS A2 ON F.DestAirport = A2.AirportCode WHERE A1.City = 'Aberdeen' AND A2.City = 'Ashley';
SELECT COUNT(*) FROM flights WHERE SourceAirport = (SELECT AirportCode FROM airports WHERE City = 'Aberdeen') AND DestAirport = (SELECT AirportCode FROM airports WHERE City = 'Ashley');
SELECT COUNT(*) FROM flights WHERE Airline = 'JetBlue Airways';
SELECT COUNT(*) FROM flights WHERE Airline = 'JetBlue Airways';
SELECT COUNT(*) FROM flights WHERE Airline = 'United Airlines' AND DestAirport = 'ASY';
SELECT COUNT(*) FROM flights WHERE Airline = 'United Airlines' AND DestAirport = 'ASY';
SELECT COUNT(*) FROM flights WHERE Airline = 'United Airlines' AND SourceAirport = 'AHD';
SELECT COUNT(*) FROM flights WHERE Airline = 'United Airlines' AND SourceAirport = 'AHD';
SELECT COUNT(*) FROM flights AS F JOIN airports AS A ON F.DestAirport = A.AirportCode JOIN airlines AS AL ON F.Airline = AL.Abbreviation WHERE AL.Airline = 'United Airlines' AND A.City = 'Aberdeen';
SELECT COUNT(*) FROM flights WHERE Airline = 'United Airlines' AND DestAirport = (SELECT AirportCode FROM airports WHERE City = 'Aberdeen');
SELECT a.City, COUNT(f.FlightNo) AS NumberOfArrivals FROM flights AS f JOIN airports AS a ON f.DestAirport = a.AirportCode GROUP BY a.City ORDER BY NumberOfArrivals DESC LIMIT 1;
SELECT a.City, COUNT(f.DestAirport) AS Frequency FROM flights AS f JOIN airports AS a ON f.DestAirport = a.AirportCode GROUP BY a.City ORDER BY Frequency DESC LIMIT 1;
SELECT a.City, COUNT(f.FlightNo) AS NumberOfDepartingFlights FROM flights AS f JOIN airports AS a ON f.SourceAirport = a.AirportCode GROUP BY a.City ORDER BY NumberOfDepartingFlights DESC LIMIT 1;
SELECT a.City, COUNT(*) AS FlightCount FROM flights AS f JOIN airports AS a ON f.SourceAirport = a.AirportCode GROUP BY a.City ORDER BY FlightCount DESC LIMIT 1;
SELECT SourceAirport AS AirportCode FROM flights GROUP BY SourceAirport ORDER BY COUNT(*) DESC LIMIT 1
SELECT SourceAirport AS AirportCode FROM flights GROUP BY SourceAirport ORDER BY COUNT(*) DESC LIMIT 1
SELECT AirportCode FROM ( SELECT SourceAirport AS AirportCode FROM flights UNION ALL SELECT DestAirport AS AirportCode FROM flights ) AS AllAirports GROUP BY AirportCode ORDER BY COUNT(*) ASC LIMIT 1
SELECT AirportCode FROM airports WHERE AirportCode IN ( SELECT SourceAirport FROM flights UNION ALL SELECT DestAirport FROM flights ) GROUP BY AirportCode ORDER BY COUNT(*) ASC LIMIT 1
SELECT Airline, COUNT(*) AS FlightCount FROM flights GROUP BY Airline ORDER BY FlightCount DESC LIMIT 1;
SELECT Airline, COUNT(*) AS FlightCount FROM flights GROUP BY Airline ORDER BY FlightCount DESC LIMIT 1
SELECT A.Abbreviation, A.Country FROM airlines AS A JOIN flights AS F ON A.Airline = F.Airline GROUP BY A.uid ORDER BY COUNT(F.FlightNo) ASC LIMIT 1;
SELECT A.Abbreviation, A.Country FROM airlines AS A JOIN ( SELECT Airline, COUNT(*) AS FlightCount FROM flights GROUP BY Airline ) AS F ON A.Airline = F.Airline WHERE F.FlightCount = ( SELECT MIN(FlightCount) FROM ( SELECT Airline, COUNT(*) AS FlightCount FROM flights GROUP BY Airline ) AS SubQuery )
SELECT DISTINCT f.Airline FROM flights AS f WHERE f.SourceAirport = 'AHD';
SELECT DISTINCT Airline FROM flights WHERE SourceAirport = 'AHD';
SELECT DISTINCT Airline FROM flights WHERE DestAirport = 'AHD';
SELECT DISTINCT Airline FROM flights WHERE DestAirport = 'AHD';
SELECT Airline FROM flights WHERE SourceAirport IN ('APG', 'CVO') GROUP BY Airline HAVING COUNT(DISTINCT SourceAirport) = 2;
SELECT Airline FROM flights WHERE SourceAirport IN ('APG', 'CVO') GROUP BY Airline HAVING COUNT(DISTINCT SourceAirport) = 2;
SELECT DISTINCT f.Airline FROM flights AS f WHERE f.SourceAirport = 'CVO' AND f.Airline NOT IN ( SELECT DISTINCT f2.Airline FROM flights AS f2 WHERE f2.SourceAirport = 'APG' );
SELECT DISTINCT f.Airline FROM flights AS f WHERE f.SourceAirport = 'CVO' AND f.Airline NOT IN ( SELECT DISTINCT f2.Airline FROM flights AS f2 WHERE f2.SourceAirport = 'APG' );
SELECT Airline FROM flights GROUP BY Airline HAVING COUNT(*) >= 10;
SELECT Airline, COUNT(*) AS FlightCount FROM flights GROUP BY Airline HAVING COUNT(*) >= 10;
SELECT a.Airline FROM airlines AS a LEFT JOIN flights AS f ON a.Airline = f.Airline GROUP BY a.Airline HAVING COUNT(f.FlightNo) < 200;
SELECT Airline FROM flights GROUP BY Airline HAVING COUNT(*) < 200;
SELECT FlightNo FROM flights WHERE Airline = 'United Airlines'
SELECT FlightNo FROM flights WHERE Airline = 'United Airlines'
SELECT FlightNo FROM flights WHERE SourceAirport = 'APG';
SELECT FlightNo FROM flights WHERE SourceAirport = 'APG'
SELECT FlightNo FROM flights WHERE DestAirport = 'APG';
SELECT FlightNo FROM flights WHERE DestAirport = 'APG'
SELECT FlightNo FROM flights WHERE SourceAirport = (SELECT AirportCode FROM airports WHERE City = 'Aberdeen');
SELECT FlightNo FROM flights WHERE SourceAirport = (SELECT AirportCode FROM airports WHERE City = 'Aberdeen')
SELECT FlightNo FROM flights WHERE DestAirport IN (SELECT AirportCode FROM airports WHERE City = 'Aberdeen');
SELECT FlightNo FROM flights WHERE DestAirport = (SELECT AirportCode FROM airports WHERE City = 'Aberdeen');
SELECT COUNT(*) FROM flights AS F JOIN airports AS A ON F.DestAirport = A.AirportCode WHERE A.City IN ('Aberdeen', 'Abilene');
SELECT COUNT(*) FROM flights WHERE DestAirport IN ( SELECT AirportCode FROM airports WHERE City IN ('Aberdeen', 'Abilene') );
SELECT AirportName FROM airports WHERE AirportCode NOT IN (SELECT SourceAirport FROM flights) AND AirportCode NOT IN (SELECT DestAirport FROM flights);
SELECT AirportName FROM airports WHERE AirportCode NOT IN (SELECT SourceAirport FROM flights) AND AirportCode NOT IN (SELECT DestAirport FROM flights);
SELECT COUNT(*) FROM employee;
SELECT COUNT(*) FROM employee;
SELECT Name FROM employee ORDER BY Age ASC
SELECT Name FROM employee ORDER BY Age ASC
SELECT City, COUNT(*) AS Number_of_Employees FROM employee GROUP BY City
SELECT City, COUNT(*) AS Employee_Count FROM employee GROUP BY City
SELECT City FROM employee WHERE Age < 30 GROUP BY City HAVING COUNT(*) > 1;
SELECT City FROM employee WHERE Age < 30 GROUP BY City HAVING COUNT(*) > 1;
SELECT Location, COUNT(*) AS Number_of_Shops FROM shop GROUP BY Location
SELECT Location, COUNT(*) AS Number_of_Shops FROM shop GROUP BY Location
SELECT `Manager_name`, `District` FROM shop WHERE `Number_products` = (SELECT MAX(`Number_products`) FROM shop)
SELECT `Manager_name`, `District` FROM shop WHERE `Number_products` = (SELECT MAX(`Number_products`) FROM shop)
SELECT MIN(Number_products) AS Min_Products, MAX(Number_products) AS Max_Products FROM shop;
SELECT MIN(Number_products) AS Min_Products, MAX(Number_products) AS Max_Products FROM shop;
SELECT `Name`, `Location`, `District` FROM shop ORDER BY `Number_products` DESC
SELECT Name, Location, District FROM shop ORDER BY Number_products DESC
SELECT Name FROM shop WHERE Number_products > (SELECT AVG(Number_products) FROM shop);
SELECT Name FROM shop WHERE Number_products > (SELECT AVG(Number_products) FROM shop);
SELECT e.Name FROM employee AS e JOIN evaluation AS ev ON e.Employee_ID = ev.Employee_ID GROUP BY e.Employee_ID ORDER BY COUNT(ev.Year_awarded) DESC LIMIT 1;
SELECT e.Name FROM employee AS e JOIN evaluation AS ev ON e.Employee_ID = ev.Employee_ID GROUP BY e.Employee_ID ORDER BY COUNT(ev.Year_awarded) DESC LIMIT 1
SELECT e.Name FROM employee AS e JOIN evaluation AS ev ON e.Employee_ID = ev.Employee_ID WHERE ev.Bonus = (SELECT MAX(Bonus) FROM evaluation);
SELECT e.Name FROM employee AS e JOIN evaluation AS ev ON e.Employee_ID = ev.Employee_ID WHERE ev.Bonus = (SELECT MAX(Bonus) FROM evaluation)
SELECT e.Name FROM employee AS e LEFT JOIN evaluation AS ev ON e.Employee_ID = ev.Employee_ID WHERE ev.Employee_ID IS NULL;
SELECT e.Name FROM employee AS e LEFT JOIN evaluation AS ev ON e.Employee_ID = ev.Employee_ID WHERE ev.Employee_ID IS NULL;
SELECT S.Name FROM shop AS S JOIN hiring AS H ON S.Shop_ID = H.Shop_ID GROUP BY S.Shop_ID ORDER BY COUNT(H.Employee_ID) DESC LIMIT 1;
SELECT S.Name FROM shop AS S JOIN hiring AS H ON S.Shop_ID = H.Shop_ID GROUP BY S.Shop_ID ORDER BY COUNT(H.Employee_ID) DESC LIMIT 1;
SELECT s.Name FROM shop AS s LEFT JOIN hiring AS h ON s.Shop_ID = h.Shop_ID WHERE h.Employee_ID IS NULL;
SELECT s.Name FROM shop AS s LEFT JOIN hiring AS h ON s.Shop_ID = h.Shop_ID WHERE h.Employee_ID IS NULL;
SELECT S.Name, COUNT(H.Employee_ID) AS Number_of_Employees FROM shop AS S LEFT JOIN hiring AS H ON S.Shop_ID = H.Shop_ID GROUP BY S.Shop_ID;
SELECT S.`Name`, COUNT(H.`Employee_ID`) AS Number_of_Employees FROM shop AS S LEFT JOIN hiring AS H ON S.`Shop_ID` = H.`Shop_ID` GROUP BY S.`Shop_ID`
SELECT SUM(Bonus) AS Total_Bonus FROM evaluation;
SELECT SUM(Bonus) AS Total_Bonus FROM evaluation;
SELECT H.*, S.*, E.* FROM hiring AS H JOIN shop AS S ON H.Shop_ID = S.Shop_ID JOIN employee AS E ON H.Employee_ID = E.Employee_ID;
SELECT H.*, E.*, S.* FROM hiring AS H JOIN employee AS E ON H.Employee_ID = E.Employee_ID JOIN shop AS S ON H.Shop_ID = S.Shop_ID;
SELECT District FROM shop GROUP BY District HAVING SUM(CASE WHEN Number_products < 3000 THEN 1 ELSE 0 END) > 0 AND SUM(CASE WHEN Number_products > 10000 THEN 1 ELSE 0 END) > 0;
SELECT DISTINCT s1.District FROM shop AS s1 JOIN shop AS s2 ON s1.District = s2.District WHERE s1.Number_products < 3000 AND s2.Number_products > 10000;
SELECT COUNT(DISTINCT Location) FROM shop;
SELECT COUNT(DISTINCT Location) FROM shop;
SELECT COUNT(*) FROM Documents;
SELECT COUNT(*) FROM Documents;
SELECT Document_ID, Document_Name, Document_Description FROM Documents
SELECT Document_ID, Document_Name, Document_Description FROM Documents
SELECT D.`Document_Name`, D.`Template_ID` FROM Documents AS D WHERE D.`Document_Description` LIKE '%w%'
SELECT Document_Name, Template_ID FROM Documents WHERE Document_Description LIKE '%w%'
SELECT D.Document_ID, D.Template_ID, D.Document_Description FROM Documents AS D WHERE D.Document_Name = 'Robbin CV'
SELECT D.Document_ID, D.Template_ID, D.Document_Description FROM Documents AS D WHERE D.Document_Name = 'Robbin CV'
SELECT COUNT(DISTINCT Template_ID) AS Different_Template_Count FROM Documents;
SELECT COUNT(DISTINCT Template_ID) FROM Documents;
SELECT COUNT(*) FROM Documents AS D JOIN Templates AS T ON D.Template_ID = T.Template_ID JOIN Ref_Template_Types AS R ON T.Template_Type_Code = R.Template_Type_Code WHERE R.Template_Type_Code = 'PPT';
SELECT COUNT(*) FROM Documents AS D JOIN Templates AS T ON D.Template_ID = T.Template_ID JOIN Ref_Template_Types AS R ON T.Template_Type_Code = R.Template_Type_Code WHERE R.Template_Type_Description = 'Presentation';
SELECT T.Template_ID, COUNT(D.Document_ID) AS Document_Count FROM Templates AS T LEFT JOIN Documents AS D ON T.Template_ID = D.Template_ID GROUP BY T.Template_ID
SELECT D.Template_ID, COUNT(*) AS Usage_Count FROM Documents AS D GROUP BY D.Template_ID;
SELECT T.Template_ID, T.Template_Type_Code FROM Templates AS T JOIN Documents AS D ON T.Template_ID = D.Template_ID GROUP BY T.Template_ID, T.Template_Type_Code ORDER BY COUNT(D.Document_ID) DESC LIMIT 1;
SELECT T.Template_ID, T.Template_Type_Code FROM Templates AS T JOIN Documents AS D ON T.Template_ID = D.Template_ID GROUP BY T.Template_ID, T.Template_Type_Code ORDER BY COUNT(D.Document_ID) DESC LIMIT 1;
SELECT T.Template_ID FROM Templates AS T JOIN Documents AS D ON T.Template_ID = D.Template_ID GROUP BY T.Template_ID HAVING COUNT(D.Document_ID) > 1;
SELECT T.Template_ID FROM Templates AS T JOIN Documents AS D ON T.Template_ID = D.Template_ID GROUP BY T.Template_ID HAVING COUNT(D.Document_ID) > 1;
SELECT T.Template_ID FROM Templates AS T LEFT JOIN Documents AS D ON T.Template_ID = D.Template_ID WHERE D.Document_ID IS NULL;
SELECT T.Template_ID FROM Templates AS T LEFT JOIN Documents AS D ON T.Template_ID = D.Template_ID WHERE D.Document_ID IS NULL;
SELECT COUNT(*) FROM Templates;
SELECT COUNT(*) FROM Templates;
SELECT Template_ID, Version_Number, Template_Type_Code FROM Templates
SELECT Template_ID, Version_Number, Template_Type_Code FROM Templates
SELECT DISTINCT Template_Type_Code FROM Templates
SELECT DISTINCT Template_Type_Code FROM Ref_Template_Types
SELECT T1.Template_ID FROM Templates AS T1 JOIN Ref_Template_Types AS T2 ON T1.Template_Type_Code = T2.Template_Type_Code WHERE T2.Template_Type_Code IN ('PP', 'PPT');
SELECT Template_ID FROM Templates WHERE Template_Type_Code IN ('PP', 'PPT');
SELECT COUNT(*) FROM Templates WHERE Template_Type_Code = 'CV'
SELECT COUNT(*) FROM Templates WHERE Template_Type_Code = (SELECT Template_Type_Code FROM Ref_Template_Types WHERE Template_Type_Description = 'CV')
SELECT Version_Number, Template_Type_Code FROM Templates WHERE Version_Number > 5
SELECT Version_Number, Template_Type_Code FROM Templates WHERE Version_Number > 5
SELECT T1.Template_Type_Code, COUNT(T2.Template_ID) FROM Ref_Template_Types AS T1 LEFT JOIN Templates AS T2 ON T1.Template_Type_Code = T2.Template_Type_Code GROUP BY T1.Template_Type_Code
SELECT T1.Template_Type_Code, COUNT(T2.Template_ID) FROM Ref_Template_Types AS T1 LEFT JOIN Templates AS T2 ON T1.Template_Type_Code = T2.Template_Type_Code GROUP BY T1.Template_Type_Code
SELECT Template_Type_Code, COUNT(*) AS Template_Count FROM Templates GROUP BY Template_Type_Code ORDER BY Template_Count DESC LIMIT 1;
SELECT T1.Template_Type_Code FROM Templates AS T2 JOIN Ref_Template_Types AS T1 ON T2.Template_Type_Code = T1.Template_Type_Code GROUP BY T1.Template_Type_Code ORDER BY COUNT(T2.Template_ID) DESC LIMIT 1;
SELECT T1.Template_Type_Code FROM Ref_Template_Types AS T1 LEFT JOIN Templates AS T2 ON T1.Template_Type_Code = T2.Template_Type_Code GROUP BY T1.Template_Type_Code HAVING COUNT(T2.Template_ID) < 3;
SELECT T1.Template_Type_Code FROM Ref_Template_Types AS T1 LEFT JOIN Templates AS T2 ON T1.Template_Type_Code = T2.Template_Type_Code GROUP BY T1.Template_Type_Code HAVING COUNT(T2.Template_ID) < 3;
SELECT T1.Version_Number, T1.Template_Type_Code FROM Templates AS T1 WHERE T1.Version_Number = (SELECT MIN(Version_Number) FROM Templates);
SELECT T2.Template_Type_Code, MIN(T1.Version_Number) AS Lowest_Version_Number FROM Templates AS T1 JOIN Ref_Template_Types AS T2 ON T1.Template_Type_Code = T2.Template_Type_Code GROUP BY T2.Template_Type_Code ORDER BY Lowest_Version_Number ASC LIMIT 1;
SELECT R.Template_Type_Code FROM Documents AS D JOIN Templates AS T ON D.Template_ID = T.Template_ID JOIN Ref_Template_Types AS R ON T.Template_Type_Code = R.Template_Type_Code WHERE D.Document_Name = 'Data base';
SELECT T.Template_Type_Code FROM Templates AS T JOIN Documents AS D ON T.Template_ID = D.Template_ID WHERE D.Document_Name = 'Data base';
SELECT D.Document_Name FROM Documents AS D JOIN Templates AS T ON D.Template_ID = T.Template_ID JOIN Ref_Template_Types AS R ON T.Template_Type_Code = R.Template_Type_Code WHERE R.Template_Type_Code = 'BK';
SELECT D.Document_Name FROM Documents AS D JOIN Templates AS T ON D.Template_ID = T.Template_ID JOIN Ref_Template_Types AS R ON T.Template_Type_Code = R.Template_Type_Code WHERE R.Template_Type_Code = 'BK';
SELECT T1.Template_Type_Code, COUNT(D.Document_ID) AS Document_Count FROM Ref_Template_Types AS T1 LEFT JOIN Templates AS T2 ON T1.Template_Type_Code = T2.Template_Type_Code LEFT JOIN Documents AS D ON T2.Template_ID = D.Template_ID GROUP BY T1.Template_Type_Code
SELECT R.`Template_Type_Code`, COUNT(D.`Document_ID`) AS Document_Count FROM Ref_Template_Types AS R LEFT JOIN Templates AS T ON R.`Template_Type_Code` = T.`Template_Type_Code` LEFT JOIN Documents AS D ON T.`Template_ID` = D.`Template_ID` GROUP BY R.`Template_Type_Code`
SELECT T.Template_Type_Code, COUNT(D.Document_ID) AS Document_Count FROM Documents AS D JOIN Templates AS T ON D.Template_ID = T.Template_ID GROUP BY T.Template_Type_Code ORDER BY Document_Count DESC LIMIT 1;
SELECT T1.Template_Type_Code FROM Ref_Template_Types AS T1 JOIN Templates AS T2 ON T1.Template_Type_Code = T2.Template_Type_Code JOIN Documents AS T3 ON T2.Template_ID = T3.Template_ID GROUP BY T1.Template_Type_Code ORDER BY COUNT(T3.Document_ID) DESC LIMIT 1;
SELECT T1.Template_Type_Code FROM Ref_Template_Types AS T1 LEFT JOIN Templates AS T2 ON T1.Template_Type_Code = T2.Template_Type_Code LEFT JOIN Documents AS T3 ON T2.Template_ID = T3.Template_ID WHERE T3.Document_ID IS NULL;
SELECT T1.Template_Type_Code FROM Ref_Template_Types AS T1 WHERE T1.Template_Type_Code NOT IN ( SELECT T2.Template_Type_Code FROM Templates AS T2 JOIN Documents AS T3 ON T2.Template_ID = T3.Template_ID );
SELECT Template_Type_Code, Template_Type_Description FROM Ref_Template_Types
SELECT Template_Type_Code, Template_Type_Description FROM Ref_Template_Types
SELECT Template_Type_Description FROM Ref_Template_Types WHERE Template_Type_Code = 'AD'
SELECT Template_Type_Description FROM Ref_Template_Types WHERE Template_Type_Code = 'AD'
SELECT Template_Type_Code FROM Ref_Template_Types WHERE Template_Type_Description = 'Book'
SELECT Template_Type_Code FROM Ref_Template_Types WHERE Template_Type_Description = 'Book'
SELECT DISTINCT RT.Template_Type_Description FROM Ref_Template_Types AS RT JOIN Templates AS T ON RT.Template_Type_Code = T.Template_Type_Code JOIN Documents AS D ON T.Template_ID = D.Template_ID;
SELECT DISTINCT RT.Template_Type_Description FROM Documents AS D JOIN Templates AS T ON D.Template_ID = T.Template_ID JOIN Ref_Template_Types AS RT ON T.Template_Type_Code = RT.Template_Type_Code;
SELECT T1.Template_ID FROM Templates AS T1 JOIN Ref_Template_Types AS T2 ON T1.Template_Type_Code = T2.Template_Type_Code WHERE T2.Template_Type_Description = 'Presentation'
SELECT Template_ID FROM Templates WHERE Template_Type_Code = (SELECT Template_Type_Code FROM Ref_Template_Types WHERE Template_Type_Description = 'Presentation')
SELECT COUNT(*) FROM Paragraphs;
SELECT COUNT(*) FROM Paragraphs;
SELECT COUNT(*) FROM Paragraphs AS P JOIN Documents AS D ON P.Document_ID = D.Document_ID WHERE D.Document_Name = 'Summer Show';
SELECT COUNT(*) FROM Paragraphs AS P JOIN Documents AS D ON P.Document_ID = D.Document_ID WHERE D.Document_Name = 'Summer Show';
SELECT * FROM Paragraphs WHERE Paragraph_Text = 'Korea'
SELECT * FROM Paragraphs WHERE Paragraph_Text LIKE '%Korea%'
SELECT Paragraph_ID, Paragraph_Text FROM Paragraphs WHERE Document_ID = (SELECT Document_ID FROM Documents WHERE Document_Name = 'Welcome to NY')
SELECT P.Paragraph_ID, P.Paragraph_Text FROM Paragraphs AS P JOIN Documents AS D ON P.Document_ID = D.Document_ID WHERE D.Document_Name = 'Welcome to NY'
SELECT P.Paragraph_Text FROM Paragraphs AS P JOIN Documents AS D ON P.Document_ID = D.Document_ID WHERE D.Document_Name = 'Customer reviews';
SELECT P.Paragraph_Text FROM Paragraphs AS P JOIN Documents AS D ON P.Document_ID = D.Document_ID WHERE D.Document_Name = 'Customer reviews';
SELECT D.Document_ID, COUNT(P.Paragraph_ID) AS Number_of_Paragraphs FROM Documents AS D LEFT JOIN Paragraphs AS P ON D.Document_ID = P.Document_ID GROUP BY D.Document_ID ORDER BY D.Document_ID;
SELECT D.Document_ID, COUNT(P.Paragraph_ID) AS Number_of_Paragraphs FROM Documents AS D LEFT JOIN Paragraphs AS P ON D.Document_ID = P.Document_ID GROUP BY D.Document_ID ORDER BY D.Document_ID;
SELECT D.Document_ID, D.Document_Name, COUNT(P.Paragraph_ID) AS Number_of_Paragraphs FROM Documents AS D LEFT JOIN Paragraphs AS P ON D.Document_ID = P.Document_ID GROUP BY D.Document_ID, D.Document_Name
SELECT D.Document_ID, D.Document_Name, COUNT(P.Paragraph_ID) AS Number_of_Paragraphs FROM Documents AS D LEFT JOIN Paragraphs AS P ON D.Document_ID = P.Document_ID GROUP BY D.Document_ID, D.Document_Name
SELECT P.Document_ID FROM Paragraphs AS P GROUP BY P.Document_ID HAVING COUNT(P.Paragraph_ID) >= 2;
SELECT P.Document_ID FROM Paragraphs AS P GROUP BY P.Document_ID HAVING COUNT(*) >= 2;
SELECT D.Document_ID, D.Document_Name FROM Documents AS D JOIN Paragraphs AS P ON D.Document_ID = P.Document_ID GROUP BY D.Document_ID, D.Document_Name ORDER BY COUNT(P.Paragraph_ID) DESC LIMIT 1;
SELECT D.Document_ID, D.Document_Name FROM Documents AS D JOIN Paragraphs AS P ON D.Document_ID = P.Document_ID GROUP BY D.Document_ID ORDER BY COUNT(P.Paragraph_ID) DESC LIMIT 1;
SELECT Document_ID FROM Paragraphs GROUP BY Document_ID ORDER BY COUNT(*) ASC LIMIT 1;
SELECT Document_ID FROM Documents WHERE Document_ID = ( SELECT Document_ID FROM Paragraphs GROUP BY Document_ID ORDER BY COUNT(*) ASC LIMIT 1 )
SELECT Document_ID FROM Paragraphs GROUP BY Document_ID HAVING COUNT(*) BETWEEN 1 AND 2;
SELECT D.Document_ID FROM Documents AS D JOIN Paragraphs AS P ON D.Document_ID = P.Document_ID GROUP BY D.Document_ID HAVING COUNT(P.Paragraph_ID) BETWEEN 1 AND 2;
SELECT Document_ID FROM Paragraphs WHERE Paragraph_Text IN ('Brazil', 'Ireland') GROUP BY Document_ID HAVING COUNT(DISTINCT Paragraph_Text) = 2;
SELECT DISTINCT D.Document_ID FROM Documents AS D JOIN Paragraphs AS P ON D.Document_ID = P.Document_ID WHERE P.Paragraph_Text IN ('Brazil', 'Ireland') GROUP BY D.Document_ID HAVING COUNT(DISTINCT P.Paragraph_Text) = 2;
SELECT COUNT(*) FROM teacher;
SELECT COUNT(*) FROM teacher;
SELECT Name FROM teacher ORDER BY Age ASC
SELECT Name FROM teacher ORDER BY Age ASC
SELECT Age, Hometown FROM teacher
SELECT Age, Hometown FROM teacher
SELECT Name FROM teacher WHERE Hometown != 'Little Lever Urban District'
SELECT Name FROM teacher WHERE Hometown != 'Little Lever Urban District'
SELECT Name FROM teacher WHERE Age IN ('32', '33')
SELECT Name FROM teacher WHERE Age IN ('32', '33')
SELECT Hometown FROM teacher WHERE Age = (SELECT MIN(Age) FROM teacher)
SELECT Hometown FROM teacher WHERE Age = (SELECT MIN(Age) FROM teacher)
SELECT Hometown, COUNT(*) AS Number_of_Teachers FROM teacher GROUP BY Hometown;
SELECT Hometown, COUNT(*) AS Teacher_Count FROM teacher GROUP BY Hometown
SELECT Hometown, COUNT(*) AS Count FROM teacher GROUP BY Hometown ORDER BY Count DESC LIMIT 1;
SELECT Hometown, COUNT(*) AS Count FROM teacher GROUP BY Hometown ORDER BY Count DESC LIMIT 1;
SELECT Hometown FROM teacher GROUP BY Hometown HAVING COUNT(*) >= 2
SELECT Hometown FROM teacher GROUP BY Hometown HAVING COUNT(*) >= 2;
SELECT T1.`Name`, T2.`Course` FROM teacher AS T1 JOIN course_arrange AS T3 ON T1.`Teacher_ID` = T3.`Teacher_ID` JOIN course AS T2 ON T3.`Course_ID` = T2.`Course_ID`
SELECT T1.`Name`, T2.`Course` FROM teacher AS T1 JOIN course_arrange AS T3 ON T1.`Teacher_ID` = T3.`Teacher_ID` JOIN course AS T2 ON T3.`Course_ID` = T2.`Course_ID`
SELECT T1.`Name`, T2.`Course` FROM teacher AS T1 JOIN course_arrange AS T3 ON T1.`Teacher_ID` = T3.`Teacher_ID` JOIN course AS T2 ON T3.`Course_ID` = T2.`Course_ID` ORDER BY T1.`Name` ASC
SELECT T1.Name AS Teacher_Name, T2.Course FROM teacher AS T1 JOIN course_arrange AS T3 ON T1.Teacher_ID = T3.Teacher_ID JOIN course AS T2 ON T3.Course_ID = T2.Course_ID ORDER BY T1.Name ASC;
SELECT T2.`Name` FROM course AS T1 JOIN course_arrange AS T3 ON T1.`Course_ID` = T3.`Course_ID` JOIN teacher AS T2 ON T3.`Teacher_ID` = T2.`Teacher_ID` WHERE T1.`Course` = 'Math'
SELECT DISTINCT teacher.Name FROM teacher JOIN course_arrange ON teacher.Teacher_ID = course_arrange.Teacher_ID JOIN course ON course_arrange.Course_ID = course.Course_ID WHERE course.Course = 'Math'
SELECT T1.`Name`, COUNT(T2.`Course_ID`) FROM teacher AS T1 LEFT JOIN course_arrange AS T2 ON T1.`Teacher_ID` = T2.`Teacher_ID` GROUP BY T1.`Teacher_ID`
SELECT T1.`Name`, COUNT(T2.`Course_ID`) AS Course_Count FROM teacher AS T1 LEFT JOIN course_arrange AS T2 ON T1.`Teacher_ID` = T2.`Teacher_ID` GROUP BY T1.`Teacher_ID`
SELECT T1.Name FROM teacher AS T1 JOIN course_arrange AS T2 ON T1.Teacher_ID = T2.Teacher_ID GROUP BY T1.Teacher_ID HAVING COUNT(DISTINCT T2.Course_ID) >= 2
SELECT T.Name FROM teacher AS T JOIN course_arrange AS CA ON T.Teacher_ID = CA.Teacher_ID GROUP BY T.Teacher_ID HAVING COUNT(CA.Course_ID) >= 2;
SELECT t.Name FROM teacher AS t LEFT JOIN course_arrange AS ca ON t.Teacher_ID = ca.Teacher_ID WHERE ca.Teacher_ID IS NULL;
SELECT t.Name FROM teacher AS t LEFT JOIN course_arrange AS ca ON t.Teacher_ID = ca.Teacher_ID WHERE ca.Course_ID IS NULL;
SELECT COUNT(*) FROM visitor WHERE Age < 30
SELECT Name FROM visitor WHERE Level_of_membership > 4 ORDER BY Level_of_membership DESC
SELECT AVG(Age) FROM visitor WHERE Level_of_membership <= 4
SELECT Name, Level_of_membership FROM visitor WHERE Level_of_membership > 4 ORDER BY Age DESC
SELECT Museum_ID, Name FROM museum WHERE Num_of_Staff = (SELECT MAX(Num_of_Staff) FROM museum);
SELECT AVG(Num_of_Staff) FROM museum WHERE Open_Year < '2009'
SELECT Open_Year, Num_of_Staff FROM museum WHERE Name = 'Plaza Museum'
SELECT Name FROM museum WHERE Num_of_Staff > (SELECT MIN(Num_of_Staff) FROM museum WHERE Open_Year > '2010');
SELECT v.ID, v.Name, v.Age FROM visitor AS v JOIN visit AS vi ON v.ID = vi.visitor_ID GROUP BY v.ID HAVING COUNT(vi.Museum_ID) > 1;
SELECT v.ID, v.Name, v.Level_of_membership FROM visitor AS v JOIN visit AS vi ON v.ID = vi.visitor_ID GROUP BY v.ID, v.Name, v.Level_of_membership ORDER BY SUM(vi.Total_spent) DESC LIMIT 1;
SELECT M.Museum_ID, M.Name FROM museum AS M JOIN visit AS V ON M.Museum_ID = V.Museum_ID GROUP BY M.Museum_ID, M.Name ORDER BY COUNT(V.visitor_ID) DESC LIMIT 1;
SELECT m.Name FROM museum AS m LEFT JOIN visit AS v ON m.Museum_ID = v.Museum_ID WHERE v.visitor_ID IS NULL;
SELECT v.Name, v.Age FROM visitor AS v JOIN visit AS vi ON v.ID = vi.visitor_ID WHERE vi.Num_of_Ticket = (SELECT MAX(Num_of_Ticket) FROM visit)
SELECT AVG(Num_of_Ticket) AS Average_Tickets, MAX(Num_of_Ticket) AS Max_Tickets FROM visit;
SELECT SUM(Total_spent) FROM visit AS T1 JOIN visitor AS T2 ON T1.visitor_ID = T2.ID WHERE T2.Level_of_membership = 1;
SELECT v.Name FROM visitor AS v JOIN visit AS vi1 ON v.ID = vi1.visitor_ID JOIN museum AS m1 ON vi1.Museum_ID = m1.Museum_ID JOIN visit AS vi2 ON v.ID = vi2.visitor_ID JOIN museum AS m2 ON vi2.Museum_ID = m2.Museum_ID WHERE m1.Open_Year < '2009' AND m2.Open_Year > '2011' GROUP BY v.ID
SELECT COUNT(DISTINCT v.ID) AS Num_of_Visitors FROM visitor AS v WHERE v.ID NOT IN ( SELECT DISTINCT vi.visitor_ID FROM visit AS vi JOIN museum AS m ON vi.Museum_ID = m.Museum_ID WHERE m.Open_Year > '2010' );
SELECT COUNT(*) FROM museum WHERE Open_Year > '2013' OR Open_Year < '2008'
SELECT COUNT(*) AS total_players FROM players;
SELECT COUNT(*) FROM players;
SELECT COUNT(*) AS total_matches FROM matches;
SELECT COUNT(*) FROM matches;
SELECT first_name, birth_date FROM players WHERE country_code = 'USA'
SELECT first_name, birth_date FROM players WHERE country_code = 'USA'
SELECT AVG(loser_age) AS average_loser_age, AVG(winner_age) AS average_winner_age FROM matches;
SELECT AVG(loser_age) AS average_loser_age, AVG(winner_age) AS average_winner_age FROM matches;
SELECT AVG(ranking) AS average_rank FROM matches AS m JOIN rankings AS r ON m.winner_id = r.player_id
SELECT AVG(ranking) AS average_rank FROM matches JOIN players ON matches.winner_id = players.player_id JOIN rankings ON players.player_id = rankings.player_id
SELECT MIN(ranking) AS highest_rank FROM players AS p JOIN matches AS m ON p.player_id = m.loser_id JOIN rankings AS r ON p.player_id = r.player_id;
SELECT MIN(ranking) AS best_rank FROM matches AS m JOIN players AS p ON m.loser_id = p.player_id JOIN rankings AS r ON p.player_id = r.player_id
SELECT COUNT(DISTINCT country_code) FROM players;
SELECT COUNT(DISTINCT country_code) FROM players;
SELECT COUNT(DISTINCT loser_name) AS distinct_loser_count FROM matches;
SELECT COUNT(DISTINCT loser_name) FROM matches;
SELECT tourney_name FROM matches GROUP BY tourney_name HAVING COUNT(*) > 10;
SELECT tourney_name FROM matches GROUP BY tourney_name HAVING COUNT(*) > 10;
SELECT DISTINCT winner_name FROM matches WHERE year IN (2013, 2016) GROUP BY winner_name HAVING COUNT(DISTINCT year) = 2;
SELECT winner_name FROM matches WHERE year IN (2013, 2016) GROUP BY winner_id, winner_name HAVING COUNT(DISTINCT year) = 2;
SELECT COUNT(*) FROM matches WHERE strftime('%Y', tourney_date) IN ('2013', '2016');
SELECT COUNT(*) FROM matches WHERE strftime('%Y', tourney_date) IN ('2013', '2016');
SELECT p.country_code, p.first_name FROM players AS p JOIN matches AS m ON p.player_id = m.winner_id WHERE m.tourney_name IN ('WTA Championships', 'Australian Open') GROUP BY p.player_id HAVING COUNT(DISTINCT m.tourney_name) = 2;
-- SQL to find players who won both the WTA Championships and the Australian Open SELECT p.first_name, p.country_code FROM players AS p JOIN matches AS m ON p.player_id = m.winner_id GROUP BY p.player_id HAVING COUNT(DISTINCT m.tournament_id) = 2; -- Assuming tournament_id exists
SELECT first_name, country_code FROM players WHERE birth_date = (SELECT MIN(birth_date) FROM players)
SELECT first_name, country_code FROM players WHERE birth_date = (SELECT MIN(birth_date) FROM players);
SELECT first_name, last_name FROM players ORDER BY birth_date
SELECT first_name || ' ' || last_name AS full_name FROM players ORDER BY birth_date;
SELECT first_name, last_name FROM players WHERE hand = 'L' ORDER BY birth_date;
SELECT first_name || ' ' || last_name AS full_name FROM players WHERE hand = 'L' ORDER BY birth_date;
SELECT p.first_name, p.country_code FROM players AS p JOIN rankings AS r ON p.player_id = r.player_id WHERE r.tours = (SELECT MAX(tours) FROM rankings);
SELECT p.first_name, p.country_code FROM players AS p JOIN rankings AS r ON p.player_id = r.player_id WHERE r.tours = (SELECT MAX(tours) FROM rankings)
SELECT year, COUNT(*) AS match_count FROM matches GROUP BY year ORDER BY match_count DESC LIMIT 1;
SELECT year, COUNT(*) AS match_count FROM matches GROUP BY year ORDER BY match_count DESC LIMIT 1;
SELECT P.first_name || ' ' || P.last_name AS winner_name, R.ranking_points FROM matches AS M JOIN players AS P ON M.winner_id = P.player_id JOIN rankings AS R ON P.player_id = R.player_id GROUP BY M.winner_id ORDER BY COUNT(M.winner_id) DESC LIMIT 1;
SELECT p.first_name || ' ' || p.last_name AS winner_name, r.ranking_points FROM players AS p JOIN matches AS m ON p.player_id = m.winner_id JOIN rankings AS r ON p.player_id = r.player_id GROUP BY p.player_id ORDER BY COUNT(m.winner_id) DESC LIMIT 1;
SELECT p.first_name, p.last_name FROM matches AS m JOIN players AS p ON m.winner_id = p.player_id JOIN rankings AS r ON p.player_id = r.player_id WHERE m.tourney_name = 'Australian Open' ORDER BY r.ranking_points DESC LIMIT 1;
SELECT p.first_name || ' ' || p.last_name AS winner_name FROM matches AS m JOIN players AS p ON m.winner_id = p.player_id JOIN rankings AS r ON p.player_id = r.player_id WHERE m.tourney_name = 'Australian Open' ORDER BY r.ranking_points DESC LIMIT 1;
SELECT winner_name, loser_name FROM matches WHERE minutes = (SELECT MAX(minutes) FROM matches);
SELECT winner_name, loser_name FROM matches WHERE minutes = (SELECT MAX(minutes) FROM matches);
SELECT p.first_name, AVG(r.ranking) AS average_ranking FROM players AS p JOIN rankings AS r ON p.player_id = r.player_id GROUP BY p.player_id;
SELECT p.first_name, AVG(r.ranking) AS average_ranking FROM players AS p JOIN rankings AS r ON p.player_id = r.player_id GROUP BY p.first_name;
SELECT p.first_name, SUM(r.ranking_points) AS total_ranking_points FROM players AS p JOIN rankings AS r ON p.player_id = r.player_id GROUP BY p.player_id;
SELECT p.first_name, SUM(r.ranking_points) AS total_ranking_points FROM players AS p JOIN rankings AS r ON p.player_id = r.player_id GROUP BY p.first_name;
SELECT country_code, COUNT(*) AS player_count FROM players GROUP BY country_code;
SELECT country_code, COUNT(*) AS player_count FROM players GROUP BY country_code;
SELECT country_code FROM players GROUP BY country_code ORDER BY COUNT(*) DESC LIMIT 1;
SELECT country_code FROM players GROUP BY country_code ORDER BY COUNT(*) DESC LIMIT 1;
SELECT country_code FROM players GROUP BY country_code HAVING COUNT(*) > 50;
SELECT country_code FROM players GROUP BY country_code HAVING COUNT(*) > 50;
SELECT ranking_date, SUM(tours) AS total_tours FROM rankings GROUP BY ranking_date;
SELECT ranking_date, SUM(tours) AS total_tours FROM rankings GROUP BY ranking_date;
SELECT year, COUNT(*) AS match_count FROM matches GROUP BY year;
SELECT year, COUNT(*) AS match_count FROM matches GROUP BY year
SELECT p.first_name, p.last_name, r.ranking FROM players AS p JOIN matches AS m ON p.player_id = m.winner_id JOIN rankings AS r ON p.player_id = r.player_id ORDER BY p.birth_date DESC LIMIT 3;
SELECT P.first_name, P.last_name, R.ranking FROM players AS P JOIN matches AS M ON P.player_id = M.winner_id JOIN rankings AS R ON P.player_id = R.player_id ORDER BY P.birth_date DESC LIMIT 3;
SELECT COUNT(DISTINCT winner_id) FROM matches JOIN players ON matches.winner_id = players.player_id WHERE matches.tourney_name = 'WTA Championships' AND players.hand = 'L';
SELECT COUNT(*) FROM matches WHERE winner_hand = 'L';
SELECT p.first_name, p.country_code, p.birth_date FROM players AS p JOIN matches AS m ON p.player_id = m.winner_id JOIN rankings AS r ON p.player_id = r.player_id WHERE r.ranking_points = (SELECT MAX(ranking_points) FROM rankings)
SELECT p.first_name, p.country_code, p.birth_date FROM players AS p JOIN rankings AS r ON p.player_id = r.player_id WHERE r.ranking_points = (SELECT MAX(ranking_points) FROM rankings)
SELECT hand, COUNT(*) AS player_count FROM players GROUP BY hand;
SELECT hand, COUNT(*) AS player_count FROM players GROUP BY hand;
SELECT COUNT(*) FROM ship WHERE disposition_of_ship = 'Captured'
SELECT `name`, `tonnage` FROM ship ORDER BY `name` DESC;
SELECT name, date, result FROM battle
SELECT id, MAX(killed) AS max_death_toll, MIN(killed) AS min_death_toll FROM death GROUP BY id;
SELECT AVG(injured) AS average_injuries FROM death;
SELECT d.killed, d.injured FROM ship AS s JOIN battle AS b ON s.lost_in_battle = b.id JOIN death AS d ON s.id = d.caused_by_ship_id WHERE s.tonnage = 't';
SELECT name, result FROM battle WHERE bulgarian_commander != 'Boril'
SELECT DISTINCT B.id, B.name FROM battle AS B JOIN ship AS S ON B.id = S.lost_in_battle WHERE S.ship_type = 'Brig';
SELECT B.id, B.name FROM battle AS B JOIN ship AS S ON S.lost_in_battle = B.id JOIN death AS D ON D.caused_by_ship_id = S.id GROUP BY B.id, B.name HAVING SUM(D.killed) > 10;
SELECT S.id, S.name FROM ship AS S JOIN death AS D ON S.id = D.caused_by_ship_id GROUP BY S.id, S.name ORDER BY SUM(D.injured) DESC LIMIT 1;
SELECT DISTINCT name FROM battle WHERE bulgarian_commander = 'Kaloyan' AND latin_commander = 'Baldwin I';
SELECT COUNT(DISTINCT result) AS different_results FROM battle;
SELECT COUNT(*) FROM battle AS b WHERE NOT EXISTS ( SELECT 1 FROM ship AS s WHERE s.lost_in_battle = b.id AND s.tonnage = '225' );
SELECT b.name, b.date FROM battle AS b JOIN ship AS s ON b.id = s.lost_in_battle WHERE s.name IN ('Lettice', 'HMS Atalanta');
SELECT b.name, b.result, b.bulgarian_commander FROM battle AS b LEFT JOIN ship AS s ON b.id = s.lost_in_battle WHERE s.location != 'English Channel' OR s.lost_in_battle IS NULL GROUP BY b.id HAVING COUNT(s.id) = 0;
SELECT note FROM death WHERE note LIKE '%East%'
SELECT line_1, line_2 FROM Addresses;
SELECT line_1, line_2 FROM Addresses;
SELECT COUNT(*) FROM Courses;
SELECT COUNT(*) FROM Courses;
SELECT course_description FROM Courses WHERE course_name = 'math';
SELECT course_description FROM Courses WHERE course_id IN (SELECT course_id FROM Sections WHERE course_id IN (SELECT course_id FROM Courses WHERE course_name = 'math'));
SELECT zip_postcode FROM Addresses WHERE city = 'Port Chelsea'
SELECT zip_postcode FROM Addresses WHERE city = 'Port Chelsea';
SELECT department_name, department_id FROM Departments WHERE department_id IN ( SELECT department_id FROM Degree_Programs GROUP BY department_id ORDER BY COUNT(degree_program_id) DESC LIMIT 1 );
SELECT D.department_id, D.department_name FROM Departments AS D JOIN Degree_Programs AS DP ON D.department_id = DP.department_id GROUP BY D.department_id, D.department_name ORDER BY COUNT(DP.degree_program_id) DESC LIMIT 1;
SELECT COUNT(DISTINCT department_id) AS number_of_departments FROM Degree_Programs;
SELECT COUNT(DISTINCT department_id) FROM Degree_Programs;
SELECT COUNT(DISTINCT degree_summary_name) FROM Degree_Programs;
SELECT COUNT(DISTINCT degree_summary_name) FROM Degree_Programs;
SELECT COUNT(*) FROM Degree_Programs WHERE department_id = (SELECT department_id FROM Departments WHERE department_name = 'engineering');
SELECT COUNT(*) FROM Degree_Programs WHERE department_id = (SELECT department_id FROM Departments WHERE department_name = 'engineering');
SELECT section_name, section_description FROM Sections;
SELECT section_name, section_description FROM Sections;
SELECT C.course_id, C.course_name FROM Courses AS C LEFT JOIN Sections AS S ON C.course_id = S.course_id GROUP BY C.course_id, C.course_name HAVING COUNT(S.section_id) <= 2;
SELECT C.course_id, C.course_name FROM Courses AS C LEFT JOIN Sections AS S ON C.course_id = S.course_id GROUP BY C.course_id HAVING COUNT(S.section_id) < 2;
SELECT section_name FROM Sections ORDER BY section_name DESC
SELECT section_name FROM Sections ORDER BY section_name DESC
SELECT S.semester_id, S.semester_name FROM Semesters AS S JOIN Student_Enrolment AS SE ON S.semester_id = SE.semester_id GROUP BY S.semester_id, S.semester_name ORDER BY COUNT(SE.student_id) DESC LIMIT 1;
SELECT S.semester_id, S.semester_name FROM Semesters AS S JOIN ( SELECT semester_id, COUNT(student_id) AS student_count FROM Student_Enrolment GROUP BY semester_id ) AS SE ON S.semester_id = SE.semester_id WHERE SE.student_count = ( SELECT MAX(student_count) FROM ( SELECT semester_id, COUNT(student_id) AS student_count FROM Student_Enrolment GROUP BY semester_id ) AS inner_SE )
SELECT department_description FROM Departments WHERE department_name LIKE '%computer%'
SELECT department_description FROM Departments WHERE department_name LIKE '%computer%'
SELECT S.first_name, S.middle_name, S.last_name, S.student_id FROM Students AS S JOIN Student_Enrolment AS SE ON S.student_id = SE.student_id GROUP BY S.student_id, SE.semester_id HAVING COUNT(DISTINCT SE.degree_program_id) = 2;
SELECT S.student_id, S.first_name, S.middle_name, S.last_name FROM Students AS S JOIN Student_Enrolment AS SE ON S.student_id = SE.student_id GROUP BY S.student_id, SE.semester_id HAVING COUNT(DISTINCT SE.degree_program_id) = 2;
SELECT S.first_name, S.middle_name, S.last_name FROM Students AS S JOIN Student_Enrolment AS SE ON S.student_id = SE.student_id JOIN Degree_Programs AS DP ON SE.degree_program_id = DP.degree_program_id WHERE DP.degree_summary_name = 'Bachelor'
SELECT first_name, middle_name, last_name FROM Students AS S JOIN Student_Enrolment AS SE ON S.student_id = SE.student_id JOIN Degree_Programs AS DP ON SE.degree_program_id = DP.degree_program_id WHERE DP.degree_summary_name = 'Bachelor';
SELECT DP.degree_summary_name, COUNT(SE.student_id) AS student_count FROM Degree_Programs AS DP JOIN Student_Enrolment AS SE ON DP.degree_program_id = SE.degree_program_id JOIN Students AS S ON SE.student_id = S.student_id GROUP BY DP.degree_summary_name ORDER BY student_count DESC LIMIT 1;
SELECT DP.degree_summary_name, COUNT(SE.student_id) AS student_count FROM Degree_Programs AS DP JOIN Student_Enrolment AS SE ON DP.degree_program_id = SE.degree_program_id GROUP BY DP.degree_summary_name ORDER BY student_count DESC LIMIT 1;
SELECT DP.degree_program_id, DP.degree_summary_name FROM Degree_Programs AS DP JOIN Student_Enrolment AS SE ON DP.degree_program_id = SE.degree_program_id GROUP BY DP.degree_program_id, DP.degree_summary_name ORDER BY COUNT(SE.student_id) DESC LIMIT 1;
SELECT DP.degree_program_id, DP.degree_summary_name FROM Degree_Programs AS DP JOIN Student_Enrolment AS SE ON DP.degree_program_id = SE.degree_program_id GROUP BY DP.degree_program_id ORDER BY COUNT(SE.student_id) DESC LIMIT 1;
SELECT S.student_id, S.first_name, S.middle_name, S.last_name, COUNT(SE.student_enrolment_id) AS number_of_enrollments FROM Students AS S JOIN Student_Enrolment AS SE ON S.student_id = SE.student_id GROUP BY S.student_id ORDER BY number_of_enrollments DESC LIMIT 1;
SELECT S.first_name, S.middle_name, S.last_name, S.student_id, COUNT(SE.student_enrolment_id) AS number_of_enrollments FROM Students AS S JOIN Student_Enrolment AS SE ON S.student_id = SE.student_id GROUP BY S.student_id ORDER BY number_of_enrollments DESC LIMIT 1;
SELECT S.semester_name FROM Semesters AS S LEFT JOIN Student_Enrolment AS SE ON S.semester_id = SE.semester_id WHERE SE.student_enrolment_id IS NULL;
SELECT S.semester_name FROM Semesters AS S LEFT JOIN Student_Enrolment AS SE ON S.semester_id = SE.semester_id WHERE SE.student_enrolment_id IS NULL;
SELECT DISTINCT C.course_name FROM Courses AS C JOIN Student_Enrolment_Courses AS SEC ON C.course_id = SEC.course_id;
SELECT DISTINCT C.course_name FROM Courses AS C JOIN Student_Enrolment_Courses AS SEC ON C.course_id = SEC.course_id;
SELECT C.course_name FROM Courses AS C JOIN Student_Enrolment_Courses AS SEC ON C.course_id = SEC.course_id GROUP BY C.course_id ORDER BY COUNT(SEC.student_enrolment_id) DESC LIMIT 1;
SELECT C.course_name FROM Courses AS C JOIN Student_Enrolment_Courses AS SEC ON C.course_id = SEC.course_id JOIN Student_Enrolment AS SE ON SEC.student_enrolment_id = SE.student_enrolment_id GROUP BY C.course_id ORDER BY COUNT(SE.student_id) DESC LIMIT 1;
SELECT S.last_name FROM Students AS S JOIN Addresses AS A ON S.current_address_id = A.address_id WHERE A.city = 'North Carolina' AND S.student_id NOT IN (SELECT student_id FROM Student_Enrolment);
SELECT S.last_name FROM Students AS S JOIN Addresses AS A ON S.current_address_id = A.address_id WHERE A.city LIKE '%North Carolina%' AND S.student_id NOT IN ( SELECT SE.student_id FROM Student_Enrolment AS SE );
SELECT T1.transcript_date, T1.transcript_id FROM Transcripts AS T1 JOIN Transcript_Contents AS T2 ON T1.transcript_id = T2.transcript_id GROUP BY T1.transcript_id HAVING COUNT(T2.student_course_id) >= 2
SELECT T.transcript_id, T.transcript_date FROM Transcripts AS T JOIN Transcript_Contents AS TC ON T.transcript_id = TC.transcript_id GROUP BY T.transcript_id HAVING COUNT(TC.student_course_id) >= 2;
SELECT cell_mobile_number FROM Students WHERE first_name = 'Timmothy' AND last_name = 'Ward';
SELECT cell_mobile_number FROM Students WHERE first_name = 'Timmothy' AND last_name = 'Ward';
SELECT first_name, middle_name, last_name FROM Students ORDER BY date_first_registered LIMIT 1
SELECT first_name, middle_name, last_name FROM Students ORDER BY date_first_registered LIMIT 1
SELECT first_name, middle_name, last_name FROM Students WHERE date_left = (SELECT MIN(date_left) FROM Students);
SELECT first_name, middle_name, last_name FROM Students ORDER BY date_first_registered LIMIT 1;
SELECT first_name FROM Students WHERE current_address_id <> permanent_address_id;
SELECT first_name FROM Students WHERE permanent_address_id <> current_address_id;
SELECT A.address_id, A.line_1, A.line_2, A.line_3, A.city, A.zip_postcode, A.state_province_county, A.country FROM Addresses AS A JOIN Students AS S ON A.address_id = S.current_address_id GROUP BY A.address_id ORDER BY COUNT(S.student_id) DESC LIMIT 1;
SELECT A.address_id, A.line_1, A.line_2 FROM Addresses AS A JOIN Students AS S ON S.current_address_id = A.address_id OR S.permanent_address_id = A.address_id GROUP BY A.address_id ORDER BY COUNT(S.student_id) DESC LIMIT 1;
SELECT DATE(AVG(JULIANDAY(transcript_date))) AS average_transcript_date FROM Transcripts;
SELECT DATE(AVG(JULIANDAY(transcript_date))) AS average_transcript_date FROM Transcripts;
SELECT MIN(transcript_date) AS first_transcript_date, other_details FROM Transcripts;
SELECT T.transcript_date, T.other_details FROM Transcripts AS T WHERE T.transcript_date = (SELECT MIN(transcript_date) FROM Transcripts)
SELECT COUNT(*) FROM Transcripts;
SELECT COUNT(*) FROM Transcripts;
SELECT MAX(transcript_date) AS last_transcript_release_date FROM Transcripts;
SELECT MAX(transcript_date) AS last_transcript_date FROM Transcripts
SELECT student_course_id, COUNT(transcript_id) AS transcript_count FROM Transcript_Contents GROUP BY student_course_id ORDER BY transcript_count DESC LIMIT 1;
SELECT T1.course_id, COUNT(T2.transcript_id) AS transcript_count FROM Student_Enrolment_Courses AS T1 JOIN Transcript_Contents AS T2 ON T1.student_course_id = T2.student_course_id GROUP BY T1.course_id ORDER BY transcript_count DESC LIMIT 1;
SELECT T1.transcript_id, T1.transcript_date FROM Transcripts AS T1 JOIN Transcript_Contents AS T2 ON T1.transcript_id = T2.transcript_id GROUP BY T1.transcript_id ORDER BY COUNT(T2.student_course_id) ASC LIMIT 1;
SELECT T1.transcript_id, T1.transcript_date FROM Transcripts AS T1 JOIN Transcript_Contents AS T2 ON T1.transcript_id = T2.transcript_id GROUP BY T1.transcript_id ORDER BY COUNT(T2.student_course_id) ASC LIMIT 1;
SELECT S.semester_id FROM Student_Enrolment AS SE JOIN Degree_Programs AS DP ON SE.degree_program_id = DP.degree_program_id JOIN Semesters AS S ON SE.semester_id = S.semester_id WHERE DP.degree_summary_name IN ('Master', 'Bachelor') GROUP BY S.semester_id HAVING COUNT(DISTINCT DP.degree_summary_name) = 2;
SELECT DISTINCT se.semester_id FROM Student_Enrolment AS se JOIN Degree_Programs AS dp ON se.degree_program_id = dp.degree_program_id WHERE dp.degree_summary_name IN ('Bachelor', 'Master') GROUP BY se.semester_id HAVING COUNT(DISTINCT dp.degree_summary_name) = 2;
SELECT COUNT(DISTINCT current_address_id) FROM Students;
SELECT DISTINCT A.* FROM Addresses AS A JOIN Students AS S ON A.address_id = S.current_address_id OR A.address_id = S.permanent_address_id;
SELECT * FROM Students ORDER BY last_name DESC, first_name DESC, middle_name DESC
SELECT * FROM Students ORDER BY last_name DESC;
SELECT * FROM Sections WHERE section_name = 'h';
SELECT section_description FROM Sections WHERE section_name = 'h';
SELECT S.first_name FROM Students AS S JOIN Addresses AS A ON S.permanent_address_id = A.address_id WHERE A.country = 'Haiti' OR S.cell_mobile_number = '09700166582';
SELECT S.first_name FROM Students AS S JOIN Addresses AS A ON S.permanent_address_id = A.address_id WHERE A.city = 'Haiti' OR S.cell_mobile_number = '09700166582';
SELECT Title FROM Cartoon ORDER BY Title ASC
SELECT Title FROM Cartoon ORDER BY Title ASC
SELECT Title FROM Cartoon WHERE Directed_by = 'Ben Jones'
SELECT Title FROM Cartoon WHERE Directed_by = 'Ben Jones'
SELECT COUNT(*) FROM Cartoon WHERE Written_by = 'Joseph Kuhr';
SELECT COUNT(*) FROM Cartoon WHERE Written_by = 'Joseph Kuhr';
SELECT Title, Directed_by FROM Cartoon ORDER BY Original_air_date;
SELECT Title, Directed_by FROM Cartoon ORDER BY Original_air_date;
SELECT Title FROM Cartoon WHERE Directed_by IN ('Ben Jones', 'Brandon Vietti')
SELECT Title FROM Cartoon WHERE Directed_by IN ('Ben Jones', 'Brandon Vietti')
SELECT Country, COUNT(*) AS Number_of_TV_Channels FROM TV_Channel GROUP BY Country ORDER BY Number_of_TV_Channels DESC
SELECT Country, COUNT(*) AS Channel_Count FROM TV_Channel GROUP BY Country ORDER BY Channel_Count DESC LIMIT 1;
SELECT COUNT(DISTINCT series_name) AS different_series_names, COUNT(DISTINCT Content) AS different_contents FROM TV_Channel;
SELECT COUNT(DISTINCT series_name) AS different_series, COUNT(DISTINCT Content) AS different_contents FROM TV_Channel;
SELECT Content FROM TV_Channel WHERE series_name = 'Sky Radio'
SELECT Content FROM TV_Channel WHERE series_name = 'Sky Radio';
SELECT Package_Option FROM TV_Channel WHERE series_name = 'Sky Radio'
SELECT Package_Option FROM TV_Channel WHERE series_name = 'Sky Radio'
SELECT COUNT(*) FROM TV_Channel WHERE Language = 'English'
SELECT COUNT(*) FROM TV_Channel WHERE Language = 'English'
SELECT Language, COUNT(*) AS Channel_Count FROM TV_Channel GROUP BY Language HAVING COUNT(*) = (SELECT MIN(Channel_Count) FROM (SELECT COUNT(*) AS Channel_Count FROM TV_Channel GROUP BY Language));
SELECT Language, COUNT(*) AS Channel_Count FROM TV_Channel GROUP BY Language HAVING Channel_Count = ( SELECT MIN(Channel_Count) FROM ( SELECT COUNT(*) AS Channel_Count FROM TV_Channel GROUP BY Language ) AS Language_Counts );
SELECT Language, COUNT(*) AS Number_of_TV_Channels FROM TV_Channel GROUP BY Language
SELECT Language, COUNT(*) AS Number_of_TV_Channels FROM TV_Channel GROUP BY Language
SELECT TV_Channel.series_name FROM Cartoon JOIN TV_Channel ON Cartoon.Channel = TV_Channel.id WHERE Cartoon.Title = 'The Rise of the Blue Beetle!';
SELECT TV_Channel.series_name FROM Cartoon JOIN TV_Channel ON Cartoon.Channel = TV_Channel.id WHERE Cartoon.Title = 'The Rise of the Blue Beetle!';
SELECT Cartoon.Title FROM Cartoon JOIN TV_Channel ON Cartoon.Channel = TV_Channel.id WHERE TV_Channel.series_name = 'Sky Radio';
SELECT Cartoon.Title FROM Cartoon JOIN TV_Channel ON Cartoon.Channel = TV_Channel.id WHERE TV_Channel.series_name = 'Sky Radio';
SELECT Episode FROM TV_series ORDER BY Rating DESC
SELECT Episode FROM TV_series ORDER BY Rating DESC
SELECT Episode, Rating FROM TV_series ORDER BY Rating DESC LIMIT 3
SELECT Episode, Rating FROM TV_series ORDER BY Rating DESC LIMIT 3
SELECT MIN(Share) AS Minimum_Share, MAX(Share) AS Maximum_Share FROM TV_series;
SELECT MAX(Share) AS Max_Share, MIN(Share) AS Min_Share FROM TV_series;
SELECT Air_Date FROM TV_series WHERE Episode = 'A Love of a Lifetime'
SELECT Air_Date FROM TV_series WHERE Episode = 'A Love of a Lifetime';
SELECT TS.Weekly_Rank, TC.series_name FROM TV_series AS TS JOIN TV_Channel AS TC ON TS.Channel = TC.id WHERE TS.Episode = 'A Love of a Lifetime'
SELECT Weekly_Rank FROM TV_series WHERE Episode = 'A Love of a Lifetime';
SELECT TC.series_name FROM TV_Channel AS TC JOIN TV_series AS TS ON TC.id = TS.Channel WHERE TS.Episode = 'A Love of a Lifetime';
SELECT TC.series_name FROM TV_series AS TS JOIN TV_Channel AS TC ON TS.Channel = TC.id WHERE TS.Episode = 'A Love of a Lifetime';
SELECT TV_series.Episode FROM TV_series JOIN TV_Channel ON TV_series.Channel = TV_Channel.id WHERE TV_Channel.series_name = 'Sky Radio';
SELECT TV_series.Episode FROM TV_series JOIN TV_Channel ON TV_series.Channel = TV_Channel.id WHERE TV_Channel.series_name = 'Sky Radio';
SELECT Directed_by, COUNT(*) AS Number_of_Cartoons FROM Cartoon GROUP BY Directed_by;
SELECT Directed_by, COUNT(*) AS Number_of_Cartoons FROM Cartoon GROUP BY Directed_by;
SELECT C.id, C.Channel FROM Cartoon AS C WHERE C.Original_air_date = (SELECT MAX(Original_air_date) FROM Cartoon)
SELECT Production_code, Channel FROM Cartoon ORDER BY Original_air_date DESC LIMIT 1;
SELECT TV_Channel.Package_Option, TV_Channel.series_name FROM TV_Channel WHERE TV_Channel.Hight_definition_TV = 'yes'
SELECT TV_Channel.Package_Option, TV_Channel.series_name FROM TV_Channel WHERE TV_Channel.Hight_definition_TV = 'yes'
SELECT DISTINCT TC.Country FROM Cartoon AS C JOIN TV_Channel AS TC ON C.Channel = TC.id WHERE C.Written_by = 'Todd Casey';
SELECT DISTINCT TC.Country FROM Cartoon AS C JOIN TV_Channel AS TC ON C.Channel = TC.id WHERE C.Written_by = 'Todd Casey';
SELECT DISTINCT Country FROM TV_Channel WHERE id NOT IN ( SELECT DISTINCT Channel FROM Cartoon WHERE Written_by = 'Todd Casey' );
SELECT DISTINCT Country FROM TV_Channel WHERE id NOT IN ( SELECT Channel FROM Cartoon WHERE Written_by = 'Todd Casey' );
SELECT DISTINCT TC.series_name, TC.Country FROM TV_Channel AS TC JOIN Cartoon AS C ON TC.id = C.Channel WHERE C.Directed_by IN ('Ben Jones', 'Michael Chang');
SELECT DISTINCT TC.series_name, TC.Country FROM TV_Channel AS TC JOIN Cartoon AS C ON TC.id = C.Channel WHERE C.Directed_by IN ('Ben Jones', 'Michael Chang') GROUP BY TC.series_name, TC.Country HAVING COUNT(DISTINCT C.Directed_by) = 2;
SELECT Pixel_aspect_ratio_PAR, Country FROM TV_Channel WHERE Language != 'English';
SELECT Pixel_aspect_ratio_PAR, Country FROM TV_Channel WHERE Language != 'English'
SELECT id FROM TV_Channel WHERE Country IN ( SELECT Country FROM TV_Channel GROUP BY Country HAVING COUNT(*) > 2 )
SELECT TV_Channel.id FROM TV_Channel JOIN TV_series ON TV_Channel.id = TV_series.id GROUP BY TV_Channel.id HAVING COUNT(TV_series.id) > 2;
SELECT TC.id FROM TV_Channel AS TC LEFT JOIN Cartoon AS C ON TC.id = C.Channel AND C.Directed_by = 'Ben Jones' WHERE C.id IS NULL;
SELECT TC.id FROM TV_Channel AS TC LEFT JOIN Cartoon AS C ON TC.id = C.Channel AND C.Directed_by = 'Ben Jones' WHERE C.id IS NULL;
SELECT DISTINCT TV_Channel.Package_Option FROM TV_Channel WHERE TV_Channel.id NOT IN ( SELECT Cartoon.Channel FROM Cartoon WHERE Cartoon.Directed_by = 'Ben Jones' );
SELECT DISTINCT TV_Channel.Package_Option FROM TV_Channel LEFT JOIN Cartoon ON TV_Channel.id = Cartoon.Channel WHERE Cartoon.Directed_by != 'Ben Jones' OR Cartoon.Directed_by IS NULL;
SELECT COUNT(*) FROM poker_player;
SELECT COUNT(*) FROM poker_player;
SELECT Earnings FROM poker_player ORDER BY Earnings DESC
SELECT Earnings FROM poker_player ORDER BY Earnings DESC
SELECT Final_Table_Made, Best_Finish FROM poker_player
SELECT pp.Final_Table_Made, pp.Best_Finish FROM poker_player AS pp JOIN people AS p ON pp.People_ID = p.People_ID;
SELECT AVG(Earnings) FROM poker_player
SELECT AVG(Earnings) FROM poker_player
SELECT Money_Rank FROM poker_player WHERE Earnings = (SELECT MAX(Earnings) FROM poker_player)
SELECT Money_Rank FROM poker_player WHERE Earnings = (SELECT MAX(Earnings) FROM poker_player)
SELECT MAX(Final_Table_Made) FROM poker_player WHERE Earnings < 200000;
SELECT MAX(Final_Table_Made) FROM poker_player WHERE Earnings < 200000
SELECT p.Name FROM people AS p JOIN poker_player AS pp ON p.People_ID = pp.People_ID;
SELECT p.Name FROM people AS p JOIN poker_player AS pp ON p.People_ID = pp.People_ID;
SELECT p.Name FROM people AS p JOIN poker_player AS pp ON p.People_ID = pp.People_ID WHERE pp.Earnings > 300000;
SELECT p.Name FROM people AS p JOIN poker_player AS pp ON p.People_ID = pp.People_ID WHERE pp.Earnings > 300000;
SELECT p.Name FROM people AS p JOIN poker_player AS pp ON p.People_ID = pp.People_ID ORDER BY pp.Final_Table_Made ASC
SELECT p.Name FROM people AS p JOIN poker_player AS pp ON p.People_ID = pp.People_ID ORDER BY pp.Final_Table_Made ASC;
SELECT p.Birth_Date FROM poker_player AS pp JOIN people AS p ON pp.People_ID = p.People_ID WHERE pp.Earnings = (SELECT MIN(Earnings) FROM poker_player);
SELECT p.Birth_Date FROM people AS p JOIN poker_player AS pp ON p.People_ID = pp.People_ID WHERE pp.Earnings = (SELECT MIN(Earnings) FROM poker_player);
SELECT pp.Money_Rank FROM poker_player AS pp JOIN people AS p ON pp.People_ID = p.People_ID WHERE p.Height = (SELECT MAX(Height) FROM people)
SELECT Money_Rank FROM poker_player AS pp JOIN people AS p ON pp.People_ID = p.People_ID WHERE p.Height = (SELECT MAX(Height) FROM people);
SELECT AVG(Earnings) FROM poker_player AS P JOIN people AS Pe ON P.People_ID = Pe.People_ID WHERE Pe.Height > 200
SELECT AVG(Earnings) FROM poker_player AS P JOIN people AS Pe ON P.People_ID = Pe.People_ID WHERE Pe.Height > 200
SELECT p.Name FROM people AS p JOIN poker_player AS pp ON p.People_ID = pp.People_ID ORDER BY pp.Earnings DESC
SELECT p.Name FROM people AS p JOIN poker_player AS pp ON p.People_ID = pp.People_ID ORDER BY pp.Earnings DESC;
SELECT Nationality, COUNT(*) AS Number_of_People FROM people GROUP BY Nationality
SELECT Nationality, COUNT(*) AS Number_of_People FROM people GROUP BY Nationality
SELECT Nationality, COUNT(*) AS Count FROM people GROUP BY Nationality ORDER BY Count DESC LIMIT 1
SELECT Nationality, COUNT(*) AS Count FROM people GROUP BY Nationality ORDER BY Count DESC LIMIT 1;
SELECT Nationality FROM people GROUP BY Nationality HAVING COUNT(*) >= 2;
SELECT Nationality FROM people GROUP BY Nationality HAVING COUNT(*) >= 2
SELECT Name, Birth_Date FROM people ORDER BY Name ASC
SELECT Name, Birth_Date FROM people ORDER BY Name ASC
SELECT Name FROM people WHERE Nationality != 'Russia'
SELECT Name FROM people WHERE Nationality != 'Russia'
SELECT p.Name FROM people AS p LEFT JOIN poker_player AS pp ON p.People_ID = pp.People_ID WHERE pp.People_ID IS NULL;
SELECT p.Name FROM people AS p LEFT JOIN poker_player AS pp ON p.People_ID = pp.People_ID WHERE pp.Poker_Player_ID IS NULL;
SELECT COUNT(DISTINCT Nationality) FROM people;
SELECT COUNT(DISTINCT Nationality) FROM people;
SELECT COUNT(DISTINCT state) FROM AREA_CODE_STATE;
SELECT contestant_number, contestant_name FROM CONTESTANTS ORDER BY contestant_name DESC
SELECT vote_id, phone_number, state FROM VOTES
SELECT MAX(area_code) AS max_area_code, MIN(area_code) AS min_area_code FROM AREA_CODE_STATE;
SELECT MAX(created) FROM VOTES WHERE state = 'CA'
SELECT contestant_name FROM CONTESTANTS WHERE contestant_name != 'Jessie Alloway'
SELECT DISTINCT state, created FROM VOTES
SELECT C.contestant_number, C.contestant_name FROM CONTESTANTS AS C JOIN VOTES AS V ON C.contestant_number = V.contestant_number GROUP BY C.contestant_number HAVING COUNT(V.vote_id) >= 2;
SELECT C.contestant_number, C.contestant_name FROM CONTESTANTS AS C JOIN VOTES AS V ON C.contestant_number = V.contestant_number GROUP BY C.contestant_number ORDER BY COUNT(V.vote_id) ASC LIMIT 1;
SELECT COUNT(*) FROM VOTES WHERE state IN ('NY', 'CA');
SELECT COUNT(*) AS unvoted_contestants FROM CONTESTANTS AS C LEFT JOIN VOTES AS V ON C.contestant_number = V.contestant_number WHERE V.vote_id IS NULL;
SELECT A.area_code FROM VOTES AS V JOIN AREA_CODE_STATE AS A ON V.state = A.state GROUP BY A.area_code ORDER BY COUNT(V.vote_id) DESC LIMIT 1;
SELECT V.created, V.state, V.phone_number FROM VOTES AS V JOIN CONTESTANTS AS C ON V.contestant_number = C.contestant_number WHERE C.contestant_name = 'Tabatha Gehling';
SELECT DISTINCT A1.area_code FROM VOTES AS V1 JOIN AREA_CODE_STATE AS A1 ON V1.state = A1.state WHERE V1.contestant_number = (SELECT contestant_number FROM CONTESTANTS WHERE contestant_name = 'Tabatha Gehling') AND V1.phone_number IN ( SELECT V2.phone_number FROM VOTES AS V2 WHERE V2.contestant_number = (SELECT contestant_number FROM CONTESTANTS WHERE contestant_name = 'Kelly Clauss') )
SELECT contestant_name FROM CONTESTANTS WHERE contestant_name LIKE '%Al%'
SELECT Name FROM country WHERE IndepYear > 1950
SELECT Name FROM country WHERE IndepYear > 1950
SELECT COUNT(*) FROM country WHERE GovernmentForm = 'Republic'
SELECT COUNT(*) FROM country WHERE GovernmentForm = 'Republic'
SELECT SUM(SurfaceArea) FROM country WHERE Region = 'Caribbean'
SELECT SUM(SurfaceArea) AS TotalSurfaceArea FROM country WHERE Region = 'Caribbean';
SELECT continent FROM country WHERE Name = 'United Kingdom';
SELECT continent FROM country WHERE Code = 'AIA';
SELECT co.Region FROM city AS c JOIN country AS co ON c.CountryCode = co.Code WHERE c.Name = 'Kabul';
SELECT co.Region FROM city AS c JOIN country AS co ON c.CountryCode = co.Code WHERE c.Name = 'Kabul';
SELECT Language FROM countrylanguage WHERE CountryCode = (SELECT Code FROM country WHERE Name = 'Aruba') ORDER BY Percentage DESC LIMIT 1;
SELECT Language FROM countrylanguage WHERE CountryCode = (SELECT Code FROM country WHERE Name = 'Aruba') AND IsOfficial = 'T' ORDER BY Percentage DESC LIMIT 1;
SELECT Population, LifeExpectancy FROM country WHERE Name = 'Brazil';
SELECT Population, LifeExpectancy FROM country WHERE Name = 'Brazil';
SELECT Region, Population FROM country WHERE Name = 'Angola';
SELECT Region, Population FROM country WHERE Name = 'Angola'
SELECT AVG(LifeExpectancy) AS AverageLifeExpectancy FROM country WHERE Region = 'Central Africa';
SELECT AVG(LifeExpectancy) AS Average_Life_Expectancy FROM country WHERE Region = 'Central Africa';
SELECT Name FROM country WHERE Continent = 'Asia' ORDER BY LifeExpectancy ASC LIMIT 1;
SELECT Name FROM country WHERE Continent = 'Asia' ORDER BY LifeExpectancy ASC LIMIT 1
SELECT SUM(Population) AS Total_Population, MAX(GNP) AS Max_GNP FROM country WHERE Continent = 'Asia';
SELECT SUM(city.Population) AS TotalPopulation, MAX(country.GNP) AS LargestGNP FROM city JOIN country ON city.CountryCode = country.Code WHERE country.Continent = 'Asia';
SELECT AVG(LifeExpectancy) FROM country WHERE Continent = 'Africa' AND GovernmentForm = 'Republic';
SELECT AVG(LifeExpectancy) FROM country WHERE Continent = 'Africa' AND GovernmentForm = 'Republic'
SELECT SUM(SurfaceArea) AS TotalSurfaceArea FROM country WHERE Continent IN ('Asia', 'Europe');
SELECT SUM(SurfaceArea) AS TotalSurfaceArea FROM country WHERE Continent IN ('Asia', 'Europe');
SELECT SUM(Population) FROM city WHERE District = 'Gelderland';
SELECT SUM(Population) AS Total_Population FROM city WHERE District = 'Gelderland';
SELECT AVG(GNP) AS Average_GNP, SUM(Population) AS Total_Population FROM country WHERE GovernmentForm = 'Dependent Territory of the UK';
SELECT AVG(GNP) AS Mean_GNP, SUM(Population) AS Total_Population FROM country WHERE GovernmentForm LIKE '%Territory%'
SELECT COUNT(DISTINCT Language) FROM countrylanguage;
SELECT COUNT(DISTINCT Language) FROM countrylanguage;
SELECT COUNT(DISTINCT GovernmentForm) FROM country WHERE Continent = 'Africa';
SELECT COUNT(DISTINCT GovernmentForm) FROM country WHERE Continent = 'Africa';
SELECT COUNT(*) FROM countrylanguage WHERE CountryCode = (SELECT Code FROM country WHERE Name = 'Aruba');
SELECT COUNT(DISTINCT Language) FROM countrylanguage WHERE CountryCode = (SELECT Code FROM country WHERE Name = 'Aruba');
SELECT COUNT(*) FROM countrylanguage WHERE CountryCode = (SELECT Code FROM country WHERE Name = 'Afghanistan') AND IsOfficial = 'T';
SELECT COUNT(*) FROM countrylanguage WHERE CountryCode = (SELECT Code FROM country WHERE Name = 'Afghanistan') AND IsOfficial = 'T';
SELECT c.Name FROM country c JOIN countrylanguage cl ON c.Code = cl.CountryCode GROUP BY c.Code ORDER BY COUNT(cl.Language) DESC LIMIT 1;
SELECT c.Name FROM country AS c JOIN countrylanguage AS cl ON c.Code = cl.CountryCode GROUP BY c.Code ORDER BY COUNT(cl.Language) DESC LIMIT 1;
SELECT c.Continent, COUNT(DISTINCT cl.Language) AS LanguageCount FROM country AS c JOIN countrylanguage AS cl ON c.Code = cl.CountryCode GROUP BY c.Continent ORDER BY LanguageCount DESC LIMIT 1;
SELECT c.Continent, COUNT(DISTINCT cl.Language) AS LanguageCount FROM country AS c JOIN countrylanguage AS cl ON c.Code = cl.CountryCode GROUP BY c.Continent ORDER BY LanguageCount DESC LIMIT 1;
SELECT COUNT(DISTINCT cl1.CountryCode) AS CountryCount FROM countrylanguage AS cl1 JOIN countrylanguage AS cl2 ON cl1.CountryCode = cl2.CountryCode WHERE cl1.Language = 'English' AND cl2.Language = 'Dutch';
SELECT COUNT(DISTINCT cl1.CountryCode) AS NumberOfNations FROM countrylanguage AS cl1 JOIN countrylanguage AS cl2 ON cl1.CountryCode = cl2.CountryCode WHERE cl1.Language = 'English' AND cl2.Language = 'Dutch';
SELECT DISTINCT c.Name FROM country AS c JOIN countrylanguage AS cl1 ON c.Code = cl1.CountryCode AND cl1.Language = 'English' JOIN countrylanguage AS cl2 ON c.Code = cl2.CountryCode AND cl2.Language = 'French';
SELECT DISTINCT c.Name FROM country AS c JOIN countrylanguage AS cl1 ON c.Code = cl1.CountryCode AND cl1.Language = 'English' JOIN countrylanguage AS cl2 ON c.Code = cl2.CountryCode AND cl2.Language = 'French';
SELECT DISTINCT c1.Name FROM country AS c1 JOIN countrylanguage AS cl1 ON c1.Code = cl1.CountryCode AND cl1.Language = 'English' AND cl1.IsOfficial = 'T' JOIN countrylanguage AS cl2 ON c1.Code = cl2.CountryCode AND cl2.Language = 'French' AND cl2.IsOfficial = 'T';
SELECT c.Name FROM country AS c JOIN countrylanguage AS cl1 ON c.Code = cl1.CountryCode AND cl1.Language = 'English' AND cl1.IsOfficial = 'T' JOIN countrylanguage AS cl2 ON c.Code = cl2.CountryCode AND cl2.Language = 'French' AND cl2.IsOfficial = 'T';
SELECT COUNT(DISTINCT c.Continent) FROM countrylanguage cl JOIN country c ON cl.CountryCode = c.Code WHERE cl.Language = 'Chinese';
SELECT COUNT(DISTINCT continent) FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language = 'Chinese' AND countrylanguage.IsOfficial = 'T';
SELECT DISTINCT Region FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language IN ('English', 'Dutch');
SELECT DISTINCT Region FROM country WHERE Code IN ( SELECT CountryCode FROM countrylanguage WHERE Language IN ('Dutch', 'English') );
SELECT DISTINCT c.Name FROM country AS c JOIN countrylanguage AS cl ON c.Code = cl.CountryCode WHERE cl.IsOfficial = 'T' AND (cl.Language = 'English' OR cl.Language = 'Dutch');
SELECT DISTINCT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.IsOfficial = 'T' AND (countrylanguage.Language = 'English' OR countrylanguage.Language = 'Dutch');
SELECT cl.Language, SUM(cl.Percentage) AS TotalPercentage FROM country AS c JOIN countrylanguage AS cl ON c.Code = cl.CountryCode WHERE c.Continent = 'Asia' GROUP BY cl.Language ORDER BY TotalPercentage DESC LIMIT 1;
SELECT Language FROM countrylanguage WHERE CountryCode IN ( SELECT Code FROM country WHERE Continent = 'Asia' ) GROUP BY Language ORDER BY COUNT(DISTINCT CountryCode) DESC LIMIT 1;
SELECT cl.Language FROM countrylanguage AS cl JOIN country AS c ON cl.CountryCode = c.Code WHERE c.GovernmentForm = 'Republic' GROUP BY cl.Language HAVING COUNT(DISTINCT c.Code) = 1;
SELECT cl.Language FROM countrylanguage AS cl JOIN country AS c ON cl.CountryCode = c.Code WHERE c.GovernmentForm = 'Republic' GROUP BY cl.Language HAVING COUNT(DISTINCT c.Code) = 1;
SELECT c.Name, c.Population FROM city AS c JOIN countrylanguage AS cl ON c.CountryCode = cl.CountryCode WHERE cl.Language = 'English' AND cl.IsOfficial = 'T' ORDER BY c.Population DESC LIMIT 1;
SELECT c.Name, c.Population FROM city AS c JOIN countrylanguage AS cl ON c.CountryCode = cl.CountryCode WHERE cl.Language = 'English' ORDER BY c.Population DESC LIMIT 1;
SELECT Name, Population, LifeExpectancy FROM country WHERE Continent = 'Asia' ORDER BY SurfaceArea DESC LIMIT 1;
SELECT Name, Population, LifeExpectancy FROM country WHERE Continent = 'Asia' ORDER BY SurfaceArea DESC LIMIT 1;
SELECT AVG(LifeExpectancy) FROM country WHERE Code NOT IN ( SELECT CountryCode FROM countrylanguage WHERE Language = 'English' AND IsOfficial = 'T' );
SELECT AVG(LifeExpectancy) AS Mean_Life_Expectancy FROM country WHERE Code NOT IN ( SELECT CountryCode FROM countrylanguage WHERE Language = 'English' AND IsOfficial = 'T' )
SELECT SUM(Population) FROM country WHERE Code NOT IN ( SELECT CountryCode FROM countrylanguage WHERE Language = 'English' );
SELECT SUM(Population) FROM country WHERE Code NOT IN ( SELECT CountryCode FROM countrylanguage WHERE Language = 'English' AND IsOfficial = 'T' );
SELECT cl.Language FROM country AS c JOIN countrylanguage AS cl ON c.Code = cl.CountryCode WHERE c.HeadOfState = 'Beatrix' AND cl.IsOfficial = 'T';
SELECT cl.Language FROM country AS c JOIN countrylanguage AS cl ON c.Code = cl.CountryCode WHERE c.HeadOfState = 'Beatrix' AND cl.IsOfficial = 'T';
SELECT COUNT(DISTINCT Language) FROM countrylanguage WHERE CountryCode IN ( SELECT Code FROM country WHERE IndepYear < 1930 ) AND IsOfficial = 'T';
SELECT COUNT(DISTINCT Language) FROM countrylanguage WHERE CountryCode IN ( SELECT Code FROM country WHERE IndepYear < 1930 ) AND IsOfficial = 'T';
SELECT Name FROM country WHERE SurfaceArea > (SELECT MAX(SurfaceArea) FROM country WHERE Region = 'Western Europe' OR Region = 'Southern Europe' OR Region = 'Northern Europe' OR Region = 'Eastern Europe')
SELECT Name FROM country WHERE SurfaceArea > (SELECT MAX(SurfaceArea) FROM country WHERE Region = 'Southern Europe' OR Region = 'Western Europe' OR Region = 'Eastern Europe' OR Region = 'Northern Europe');
SELECT Name FROM country WHERE Continent = 'Africa' AND Population < (SELECT MIN(Population) FROM country WHERE Continent = 'Asia');
SELECT Name FROM country WHERE Continent = 'Africa' AND Population < (SELECT MIN(Population) FROM country WHERE Continent = 'Asia');
SELECT Name FROM country WHERE Continent = 'Asia' AND Population > (SELECT MAX(Population) FROM country WHERE Continent = 'Africa');
SELECT Name FROM country WHERE Continent = 'Asia' AND Population > (SELECT MAX(Population) FROM country WHERE Continent = 'Africa');
SELECT DISTINCT c.Code FROM country AS c WHERE c.Code NOT IN ( SELECT cl.CountryCode FROM countrylanguage AS cl WHERE cl.Language = 'English' );
SELECT DISTINCT country.Code FROM country WHERE country.Code NOT IN ( SELECT countrylanguage.CountryCode FROM countrylanguage WHERE countrylanguage.Language = 'English' );
SELECT DISTINCT country.Code FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language != 'English';
SELECT DISTINCT country.Code FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language != 'English';
SELECT DISTINCT c.Code FROM country AS c LEFT JOIN countrylanguage AS cl ON c.Code = cl.CountryCode WHERE cl.Language != 'English' OR cl.Language IS NULL AND c.GovernmentForm != 'Republic';
SELECT DISTINCT c.Code FROM country AS c LEFT JOIN countrylanguage AS cl ON c.Code = cl.CountryCode WHERE cl.Language != 'English' OR cl.Language IS NULL AND c.GovernmentForm != 'Republic';
SELECT c.Name FROM city AS c JOIN country AS co ON c.CountryCode = co.Code JOIN countrylanguage AS cl ON co.Code = cl.CountryCode WHERE co.Continent = 'Europe' AND cl.Language = 'English' AND cl.IsOfficial = 'F';
SELECT city.Name FROM city JOIN country ON city.CountryCode = country.Code JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Continent = 'Europe' AND countrylanguage.Language = 'English' AND countrylanguage.IsOfficial = 'F';
SELECT DISTINCT city.Name FROM city JOIN country ON city.CountryCode = country.Code JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Continent = 'Asia' AND countrylanguage.Language = 'Chinese' AND countrylanguage.IsOfficial = 'T';
SELECT DISTINCT city.Name FROM city JOIN country ON city.CountryCode = country.Code JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Continent = 'Asia' AND countrylanguage.Language = 'Chinese' AND countrylanguage.IsOfficial = 'T';
SELECT Name, IndepYear, SurfaceArea FROM country WHERE Population = (SELECT MIN(Population) FROM country);
SELECT Name, IndepYear, SurfaceArea FROM country WHERE Population = (SELECT MIN(Population) FROM country);
SELECT Population, Name, HeadOfState FROM country WHERE SurfaceArea = (SELECT MAX(SurfaceArea) FROM country);
SELECT c.Name, c.Population, c.HeadOfState FROM country AS c ORDER BY c.SurfaceArea DESC LIMIT 1;
SELECT c.Name AS Country_Name, COUNT(cl.Language) AS Number_of_Languages FROM country AS c JOIN countrylanguage AS cl ON c.Code = cl.CountryCode GROUP BY c.Code HAVING COUNT(cl.Language) >= 3
SELECT c.Name, COUNT(cl.Language) AS LanguageCount FROM country AS c JOIN countrylanguage AS cl ON c.Code = cl.CountryCode GROUP BY c.Code HAVING COUNT(cl.Language) > 2;
SELECT District, COUNT(*) AS NumberOfCities FROM city WHERE Population > (SELECT AVG(Population) FROM city) GROUP BY District;
SELECT District, COUNT(*) AS CityCount FROM city WHERE Population > (SELECT AVG(Population) FROM city) GROUP BY District;
SELECT GovernmentForm, SUM(Population) AS TotalPopulation FROM country WHERE LifeExpectancy > 72 GROUP BY GovernmentForm;
SELECT GovernmentForm, SUM(Population) AS TotalPopulation FROM country WHERE LifeExpectancy > 72 GROUP BY GovernmentForm;
SELECT continent, AVG(LifeExpectancy) AS Average_Life_Expectancy, SUM(Population) AS Total_Population FROM country GROUP BY continent HAVING AVG(LifeExpectancy) < 72;
SELECT continent AS Continent, SUM(Population) AS Total_Population, AVG(LifeExpectancy) AS Average_Life_Expectancy FROM country GROUP BY continent HAVING AVG(LifeExpectancy) < 72;
SELECT Name, SurfaceArea FROM country ORDER BY SurfaceArea DESC LIMIT 5;
SELECT Name, SurfaceArea FROM country ORDER BY SurfaceArea DESC LIMIT 5
SELECT Name FROM country ORDER BY Population DESC LIMIT 3
SELECT Name FROM country ORDER BY Population DESC LIMIT 3
SELECT Name FROM country ORDER BY Population ASC LIMIT 3
SELECT Name FROM country ORDER BY Population ASC LIMIT 3
SELECT COUNT(*) FROM country WHERE Continent = 'Asia'
SELECT COUNT(*) FROM country WHERE Continent = 'Asia'
SELECT Name FROM country WHERE Continent = 'Europe' AND Population = 80000;
SELECT Name FROM country WHERE Continent = 'Europe' AND Population = 80000;
SELECT SUM(Population) AS Total_Population, AVG(SurfaceArea) AS Average_Area FROM country WHERE Continent = 'North America' AND SurfaceArea > 3000;
SELECT SUM(Population) AS Total_Population, AVG(SurfaceArea) AS Average_Surface_Area FROM country WHERE Continent = 'North America' AND SurfaceArea > 3000;
SELECT Name FROM city WHERE Population BETWEEN 160000 AND 900000;
SELECT Name FROM city WHERE Population BETWEEN 160000 AND 900000;
SELECT Language, COUNT(DISTINCT CountryCode) AS CountryCount FROM countrylanguage GROUP BY Language ORDER BY CountryCount DESC LIMIT 1;
SELECT Language FROM countrylanguage GROUP BY Language ORDER BY COUNT(DISTINCT CountryCode) DESC LIMIT 1;
SELECT cl.CountryCode, cl.Language FROM countrylanguage AS cl WHERE cl.Percentage = ( SELECT MAX(Percentage) FROM countrylanguage AS cl2 WHERE cl2.CountryCode = cl.CountryCode )
SELECT cl.CountryCode, cl.Language FROM countrylanguage AS cl JOIN ( SELECT CountryCode, MAX(Percentage) AS MaxPercentage FROM countrylanguage GROUP BY CountryCode ) AS max_lang ON cl.CountryCode = max_lang.CountryCode AND cl.Percentage = max_lang.MaxPercentage
SELECT COUNT(DISTINCT c.Code) FROM country AS c JOIN countrylanguage AS cl ON c.Code = cl.CountryCode WHERE cl.Language = 'Spanish' AND cl.IsOfficial = 'T' AND cl.Percentage = ( SELECT MAX(Percentage) FROM countrylanguage WHERE CountryCode = c.Code );
SELECT COUNT(DISTINCT cl.CountryCode) FROM countrylanguage AS cl WHERE cl.Language = 'Spanish' AND cl.IsOfficial = 'T' AND cl.Percentage = (SELECT MAX(Percentage) FROM countrylanguage WHERE CountryCode = cl.CountryCode);
SELECT CountryCode FROM countrylanguage WHERE Language = 'Spanish' ORDER BY Percentage DESC LIMIT 1;
SELECT CountryCode FROM countrylanguage WHERE Language = 'Spanish' AND Percentage = ( SELECT MAX(Percentage) FROM countrylanguage AS cl WHERE cl.CountryCode = countrylanguage.CountryCode )
SELECT COUNT(*) FROM conductor;
SELECT COUNT(*) FROM conductor;
SELECT Name FROM conductor ORDER BY Age ASC
SELECT Name FROM conductor ORDER BY Age
SELECT Name FROM conductor WHERE Nationality != 'USA'
SELECT Name FROM conductor WHERE Nationality != 'USA'
SELECT Record_Company FROM orchestra ORDER BY Year_of_Founded DESC;
SELECT Record_Company FROM orchestra ORDER BY Year_of_Founded DESC
SELECT AVG(Attendance) AS Average_Attendance FROM show;
SELECT AVG(Attendance) AS Average_Attendance FROM show;
SELECT MAX(Share) AS Max_Share, MIN(Share) AS Min_Share FROM performance WHERE Type != 'Live final';
SELECT MAX(Share) AS Max_Share, MIN(Share) AS Min_Share FROM performance WHERE Type != 'Live final'
SELECT COUNT(DISTINCT Nationality) AS Different_Nationalities FROM conductor;
SELECT COUNT(DISTINCT Nationality) FROM conductor;
SELECT Name FROM conductor ORDER BY Year_of_Work DESC
SELECT Name FROM conductor ORDER BY Year_of_Work DESC
SELECT `Name` FROM conductor WHERE `Year_of_Work` = (SELECT MAX(`Year_of_Work`) FROM conductor)
SELECT `Name` FROM conductor WHERE `Year_of_Work` = (SELECT MAX(`Year_of_Work`) FROM conductor)
SELECT c.Name AS Conductor_Name, o.Orchestra AS Orchestra_Name FROM conductor AS c JOIN orchestra AS o ON c.Conductor_ID = o.Conductor_ID;
SELECT c.Name AS Conductor_Name, o.Orchestra AS Orchestra_Name FROM conductor AS c JOIN orchestra AS o ON c.Conductor_ID = o.Conductor_ID;
SELECT C.Name FROM conductor AS C JOIN orchestra AS O ON C.Conductor_ID = O.Conductor_ID GROUP BY C.Conductor_ID HAVING COUNT(DISTINCT O.Orchestra_ID) > 1;
SELECT c.Name FROM conductor AS c JOIN orchestra AS o ON c.Conductor_ID = o.Conductor_ID GROUP BY c.Conductor_ID HAVING COUNT(DISTINCT o.Orchestra_ID) > 1;
SELECT c.Name FROM conductor AS c JOIN orchestra AS o ON c.Conductor_ID = o.Conductor_ID GROUP BY c.Conductor_ID ORDER BY COUNT(o.Orchestra_ID) DESC LIMIT 1;
SELECT c.Name FROM conductor AS c JOIN orchestra AS o ON c.Conductor_ID = o.Conductor_ID GROUP BY c.Conductor_ID ORDER BY COUNT(o.Orchestra_ID) DESC LIMIT 1;
SELECT DISTINCT c.Name FROM conductor AS c JOIN orchestra AS o ON c.Conductor_ID = o.Conductor_ID WHERE o.Year_of_Founded > 2008;
SELECT DISTINCT c.Name FROM conductor AS c JOIN orchestra AS o ON c.Conductor_ID = o.Conductor_ID WHERE o.Year_of_Founded > 2008;
SELECT Record_Company, COUNT(*) AS Number_of_Orchestras FROM orchestra GROUP BY Record_Company;
SELECT Record_Company, COUNT(*) AS Orchestra_Count FROM orchestra GROUP BY Record_Company;
SELECT Major_Record_Format, COUNT(*) AS Format_Count FROM orchestra GROUP BY Major_Record_Format ORDER BY Format_Count ASC;
SELECT Major_Record_Format, COUNT(*) AS Frequency FROM orchestra GROUP BY Major_Record_Format ORDER BY Frequency DESC;
SELECT Record_Company, COUNT(*) AS Orchestra_Count FROM orchestra GROUP BY Record_Company ORDER BY Orchestra_Count DESC LIMIT 1;
SELECT Record_Company FROM orchestra GROUP BY Record_Company ORDER BY COUNT(DISTINCT Orchestra_ID) DESC LIMIT 1;
SELECT o.Orchestra FROM orchestra AS o LEFT JOIN performance AS p ON o.Orchestra_ID = p.Orchestra_ID WHERE p.Performance_ID IS NULL;
SELECT o.Orchestra FROM orchestra AS o LEFT JOIN performance AS p ON o.Orchestra_ID = p.Orchestra_ID WHERE p.Performance_ID IS NULL;
SELECT Record_Company FROM orchestra WHERE Year_of_Founded < 2003 OR Year_of_Founded > 2003 GROUP BY Record_Company HAVING COUNT(CASE WHEN Year_of_Founded < 2003 THEN 1 END) > 0 AND COUNT(CASE WHEN Year_of_Founded > 2003 THEN 1 END) > 0;
SELECT Record_Company FROM orchestra WHERE Year_of_Founded < 2003 OR Year_of_Founded >= 2003 GROUP BY Record_Company HAVING COUNT(DISTINCT CASE WHEN Year_of_Founded < 2003 THEN 1 END) > 0 AND COUNT(DISTINCT CASE WHEN Year_of_Founded >= 2003 THEN 1 END) > 0;
SELECT COUNT(*) FROM orchestra WHERE Major_Record_Format IN ('CD', 'DVD');
SELECT COUNT(*) FROM orchestra WHERE Major_Record_Format IN ('CD', 'DVD');
SELECT DISTINCT o.Year_of_Founded FROM orchestra AS o JOIN performance AS p ON o.Orchestra_ID = p.Orchestra_ID GROUP BY o.Orchestra_ID HAVING COUNT(p.Performance_ID) > 1;
SELECT o.Year_of_Founded FROM orchestra AS o JOIN performance AS p ON o.Orchestra_ID = p.Orchestra_ID GROUP BY o.Orchestra_ID HAVING COUNT(p.Performance_ID) > 1;
SELECT COUNT(*) FROM Highschooler;
SELECT COUNT(*) FROM Highschooler;
SELECT name, grade FROM Highschooler
SELECT name, grade FROM Highschooler
SELECT DISTINCT grade FROM Highschooler
SELECT name, grade FROM Highschooler
SELECT grade FROM Highschooler WHERE name = 'Kyle'
SELECT grade FROM Highschooler WHERE name = 'Kyle'
SELECT name FROM Highschooler WHERE grade = 10
SELECT name FROM Highschooler WHERE grade = 10
SELECT ID FROM Highschooler WHERE name = 'Kyle'
SELECT ID FROM Highschooler WHERE name = 'Kyle'
SELECT COUNT(*) FROM Highschooler WHERE grade IN (9, 10)
SELECT COUNT(*) FROM Highschooler WHERE grade IN (9, 10)
SELECT grade, COUNT(*) AS number_of_highschoolers FROM Highschooler GROUP BY grade
SELECT grade, COUNT(*) AS number_of_highschoolers FROM Highschooler GROUP BY grade
SELECT grade, COUNT(*) AS number_of_highschoolers FROM Highschooler GROUP BY grade ORDER BY number_of_highschoolers DESC LIMIT 1;
SELECT grade, COUNT(*) AS num_students FROM Highschooler GROUP BY grade ORDER BY num_students DESC LIMIT 1;
SELECT grade FROM Highschooler GROUP BY grade HAVING COUNT(*) >= 4;
SELECT grade, COUNT(*) AS number_of_students FROM Highschooler GROUP BY grade HAVING COUNT(*) >= 4;
SELECT H.ID, COUNT(F.friend_id) AS number_of_friends FROM Highschooler AS H LEFT JOIN Friend AS F ON H.ID = F.student_id GROUP BY H.ID
SELECT H.name, COUNT(F.friend_id) AS friend_count FROM Highschooler AS H LEFT JOIN Friend AS F ON H.ID = F.student_id GROUP BY H.ID
SELECT H.name, COUNT(F.friend_id) AS number_of_friends FROM Highschooler AS H LEFT JOIN Friend AS F ON H.ID = F.student_id GROUP BY H.ID
SELECT H.name, COUNT(F.friend_id) AS friend_count FROM Highschooler AS H LEFT JOIN Friend AS F ON H.ID = F.student_id GROUP BY H.ID
SELECT H.name FROM Highschooler AS H JOIN Friend AS F ON H.ID = F.student_id GROUP BY H.ID ORDER BY COUNT(F.friend_id) DESC LIMIT 1
SELECT H.name FROM Highschooler AS H JOIN Friend AS F ON H.ID = F.student_id GROUP BY H.ID ORDER BY COUNT(F.friend_id) DESC LIMIT 1;
SELECT H.name FROM Highschooler AS H JOIN Friend AS F ON H.ID = F.student_id GROUP BY H.ID HAVING COUNT(F.friend_id) >= 3
SELECT H.name FROM Highschooler AS H JOIN Friend AS F ON H.ID = F.student_id GROUP BY H.ID HAVING COUNT(F.friend_id) >= 3
SELECT H2.name FROM Highschooler AS H1 JOIN Friend AS F ON H1.ID = F.student_id JOIN Highschooler AS H2 ON F.friend_id = H2.ID WHERE H1.name = 'Kyle'
SELECT H2.name FROM Friend AS F JOIN Highschooler AS H1 ON F.student_id = H1.ID JOIN Highschooler AS H2 ON F.friend_id = H2.ID WHERE H1.name = 'Kyle';
SELECT COUNT(*) FROM Friend WHERE student_id = (SELECT ID FROM Highschooler WHERE name = 'Kyle')
SELECT COUNT(*) FROM Friend WHERE student_id = (SELECT ID FROM Highschooler WHERE name = 'Kyle')
SELECT ID FROM Highschooler WHERE ID NOT IN (SELECT student_id FROM Friend)
SELECT H.ID FROM Highschooler AS H LEFT JOIN Friend AS F ON H.ID = F.student_id WHERE F.friend_id IS NULL;
SELECT name FROM Highschooler WHERE ID NOT IN (SELECT student_id FROM Friend)
SELECT H.name FROM Highschooler AS H LEFT JOIN Friend AS F ON H.ID = F.student_id WHERE F.student_id IS NULL;
SELECT DISTINCT H.ID FROM Highschooler AS H JOIN Friend AS F ON H.ID = F.student_id JOIN Likes AS L ON H.ID = L.liked_id;
SELECT DISTINCT F.student_id FROM Friend AS F JOIN Likes AS L ON F.student_id = L.student_id;
SELECT H.name FROM Highschooler AS H WHERE H.ID IN (SELECT F.student_id FROM Friend AS F) AND H.ID IN (SELECT L.student_id FROM Likes AS L);
SELECT H.name FROM Highschooler AS H WHERE H.ID IN (SELECT F.student_id FROM Friend AS F) AND H.ID IN (SELECT L.student_id FROM Likes AS L);
SELECT student_id, COUNT(liked_id) AS like_count FROM Likes GROUP BY student_id
SELECT student_id, COUNT(liked_id) AS like_count FROM Likes GROUP BY student_id
SELECT H.name, COUNT(L.liked_id) AS number_of_likes FROM Highschooler AS H JOIN Likes AS L ON H.ID = L.student_id GROUP BY H.ID
SELECT H.name, COUNT(L.liked_id) AS like_count FROM Highschooler AS H JOIN Likes AS L ON H.ID = L.student_id GROUP BY H.ID
SELECT H.name FROM Highschooler AS H JOIN Likes AS L ON H.ID = L.student_id GROUP BY H.ID ORDER BY COUNT(L.liked_id) DESC LIMIT 1
SELECT H.name FROM Highschooler AS H JOIN Likes AS L ON H.ID = L.liked_id GROUP BY H.ID ORDER BY COUNT(L.student_id) DESC LIMIT 1;
SELECT H.name FROM Highschooler AS H JOIN Likes AS L ON H.ID = L.student_id GROUP BY H.ID HAVING COUNT(L.liked_id) >= 2
SELECT H.name FROM Highschooler AS H JOIN Likes AS L ON H.ID = L.student_id GROUP BY H.ID HAVING COUNT(L.liked_id) >= 2;
SELECT H.name FROM Highschooler AS H JOIN Friend AS F ON H.ID = F.student_id WHERE H.grade > 5 GROUP BY H.ID HAVING COUNT(F.friend_id) >= 2;
SELECT H.name FROM Highschooler AS H JOIN Friend AS F ON H.ID = F.student_id GROUP BY H.ID HAVING COUNT(F.friend_id) >= 2
SELECT COUNT(*) FROM Likes WHERE liked_id = (SELECT ID FROM Highschooler WHERE name = 'Kyle')
SELECT COUNT(*) FROM Likes WHERE student_id = (SELECT ID FROM Highschooler WHERE name = 'Kyle')
SELECT AVG(H.grade) AS average_grade FROM Highschooler AS H JOIN Friend AS F ON H.ID = F.student_id;
SELECT AVG(H.grade) AS average_grade FROM Highschooler AS H JOIN Friend AS F ON H.ID = F.student_id;
SELECT MIN(H.grade) FROM Highschooler AS H LEFT JOIN Friend AS F ON H.ID = F.student_id WHERE F.student_id IS NULL;
SELECT MIN(H.grade) FROM Highschooler AS H LEFT JOIN Friend AS F ON H.ID = F.student_id WHERE F.student_id IS NULL;
SELECT DISTINCT O.state FROM Owners O JOIN Professionals P ON O.state = P.state;
SELECT DISTINCT O.state FROM Owners AS O JOIN Professionals AS P ON O.state = P.state;
SELECT AVG(CAST(age AS INTEGER)) AS average_age FROM Dogs WHERE dog_id IN (SELECT dog_id FROM Treatments);
SELECT AVG(D.age) AS average_age FROM Dogs AS D JOIN Treatments AS T ON D.dog_id = T.dog_id;
SELECT P.professional_id, P.last_name, P.cell_number FROM Professionals AS P LEFT JOIN Treatments AS T ON P.professional_id = T.professional_id WHERE P.state = 'Indiana' OR P.professional_id IN ( SELECT professional_id FROM Treatments GROUP BY professional_id HAVING COUNT(*) > 2 )
SELECT professional_id, last_name, cell_number FROM Professionals WHERE state = 'Indiana' OR professional_id IN ( SELECT professional_id FROM Treatments GROUP BY professional_id HAVING COUNT(*) > 2 );
SELECT D.name FROM Dogs AS D LEFT JOIN Treatments AS T ON D.dog_id = T.dog_id GROUP BY D.dog_id HAVING COALESCE(SUM(T.cost_of_treatment), 0) <= 1000;
SELECT D.name FROM Dogs AS D LEFT JOIN Treatments AS T ON D.dog_id = T.dog_id GROUP BY D.dog_id HAVING COALESCE(SUM(T.cost_of_treatment), 0) <= 1000;
SELECT DISTINCT first_name FROM ( SELECT first_name FROM Owners UNION SELECT first_name FROM Professionals ) AS CombinedNames WHERE first_name NOT IN (SELECT name FROM Dogs);
SELECT DISTINCT first_name FROM ( SELECT first_name FROM Owners UNION SELECT first_name FROM Professionals ) AS combined_names WHERE first_name NOT IN (SELECT name FROM Dogs);
SELECT P.professional_id, P.role_code, P.email_address FROM Professionals AS P LEFT JOIN Treatments AS T ON P.professional_id = T.professional_id WHERE T.treatment_id IS NULL;
SELECT P.professional_id, P.role_code, P.email_address FROM Professionals AS P LEFT JOIN Treatments AS T ON P.professional_id = T.professional_id WHERE T.treatment_id IS NULL;
SELECT owner_id, first_name, last_name FROM Owners WHERE owner_id = ( SELECT owner_id FROM Dogs GROUP BY owner_id ORDER BY COUNT(*) DESC LIMIT 1 )
SELECT owner_id, first_name, last_name FROM Owners WHERE owner_id = ( SELECT owner_id FROM Dogs GROUP BY owner_id ORDER BY COUNT(*) DESC LIMIT 1 );
SELECT Professionals.professional_id, Professionals.role_code, Professionals.first_name FROM Treatments JOIN Professionals ON Treatments.professional_id = Professionals.professional_id GROUP BY Professionals.professional_id HAVING COUNT(Treatments.treatment_id) >= 2
SELECT P.professional_id, P.role_code, P.first_name FROM Professionals AS P JOIN Treatments AS T ON P.professional_id = T.professional_id GROUP BY P.professional_id HAVING COUNT(T.treatment_id) >= 2;
SELECT B.breed_name FROM Breeds AS B JOIN Dogs AS D ON B.breed_code = D.breed_code GROUP BY B.breed_name ORDER BY COUNT(D.dog_id) DESC LIMIT 1;
SELECT B.breed_name FROM Dogs AS D JOIN Breeds AS B ON D.breed_code = B.breed_code GROUP BY B.breed_name ORDER BY COUNT(D.dog_id) DESC LIMIT 1;
SELECT O.owner_id, O.last_name FROM Owners AS O JOIN Dogs AS D ON O.owner_id = D.owner_id JOIN Treatments AS T ON D.dog_id = T.dog_id GROUP BY O.owner_id, O.last_name ORDER BY COUNT(T.treatment_id) DESC LIMIT 1;
SELECT O.owner_id, O.last_name FROM Owners AS O JOIN Dogs AS D ON O.owner_id = D.owner_id JOIN Treatments AS T ON D.dog_id = T.dog_id GROUP BY O.owner_id, O.last_name ORDER BY SUM(T.cost_of_treatment) DESC LIMIT 1;
SELECT T1.treatment_type_description FROM Treatment_Types AS T1 JOIN Treatments AS T2 ON T1.treatment_type_code = T2.treatment_type_code GROUP BY T1.treatment_type_code ORDER BY SUM(T2.cost_of_treatment) ASC LIMIT 1;
SELECT T1.treatment_type_description FROM Treatment_Types AS T1 JOIN Treatments AS T2 ON T1.treatment_type_code = T2.treatment_type_code GROUP BY T1.treatment_type_code ORDER BY SUM(T2.cost_of_treatment) ASC LIMIT 1;
SELECT O.owner_id, O.zip_code FROM Owners AS O JOIN Dogs AS D ON O.owner_id = D.owner_id JOIN Treatments AS T ON D.dog_id = T.dog_id GROUP BY O.owner_id, O.zip_code ORDER BY SUM(T.cost_of_treatment) DESC LIMIT 1;
SELECT O.owner_id, O.zip_code FROM Owners AS O JOIN Dogs AS D ON O.owner_id = D.owner_id JOIN Treatments AS T ON D.dog_id = T.dog_id GROUP BY O.owner_id, O.zip_code ORDER BY SUM(T.cost_of_treatment) DESC LIMIT 1;
SELECT T.professional_id, P.cell_number FROM Treatments AS T JOIN Professionals AS P ON T.professional_id = P.professional_id GROUP BY T.professional_id HAVING COUNT(DISTINCT T.treatment_type_code) >= 2;
SELECT P.professional_id, P.cell_number FROM Treatments AS T JOIN Professionals AS P ON T.professional_id = P.professional_id GROUP BY P.professional_id HAVING COUNT(DISTINCT T.treatment_type_code) >= 2;
SELECT P.first_name, P.last_name FROM Professionals AS P JOIN Treatments AS T ON P.professional_id = T.professional_id WHERE T.cost_of_treatment < (SELECT AVG(cost_of_treatment) FROM Treatments);
SELECT P.first_name, P.last_name FROM Professionals AS P JOIN Treatments AS T ON P.professional_id = T.professional_id WHERE T.cost_of_treatment < (SELECT AVG(cost_of_treatment) FROM Treatments);
SELECT Treatments.date_of_treatment, Professionals.first_name FROM Treatments JOIN Professionals ON Treatments.professional_id = Professionals.professional_id;
SELECT Treatments.date_of_treatment, Professionals.first_name FROM Treatments JOIN Professionals ON Treatments.professional_id = Professionals.professional_id;
SELECT T1.cost_of_treatment, T2.treatment_type_description FROM Treatments AS T1 JOIN Treatment_Types AS T2 ON T1.treatment_type_code = T2.treatment_type_code;
SELECT T1.cost_of_treatment, T2.treatment_type_description FROM Treatments AS T1 JOIN Treatment_Types AS T2 ON T1.treatment_type_code = T2.treatment_type_code;
SELECT O.first_name, O.last_name, S.size_description FROM Owners AS O JOIN Dogs AS D ON O.owner_id = D.owner_id JOIN Sizes AS S ON D.size_code = S.size_code;
SELECT O.first_name, O.last_name, S.size_description FROM Owners AS O JOIN Dogs AS D ON O.owner_id = D.owner_id JOIN Sizes AS S ON D.size_code = S.size_code;
SELECT Owners.first_name, Dogs.name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id;
SELECT Owners.first_name, Dogs.name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id;
SELECT D.name AS Dog_Name, T.date_of_treatment AS Treatment_Date FROM Dogs AS D JOIN Breeds AS B ON D.breed_code = B.breed_code JOIN Treatments AS T ON D.dog_id = T.dog_id WHERE B.breed_code = ( SELECT breed_code FROM Dogs GROUP BY breed_code ORDER BY COUNT(*) ASC LIMIT 1 )
SELECT D.name, T.date_of_treatment FROM Dogs AS D JOIN Breeds AS B ON D.breed_code = B.breed_code JOIN Treatments AS T ON D.dog_id = T.dog_id WHERE B.breed_code = ( SELECT breed_code FROM Dogs GROUP BY breed_code ORDER BY COUNT(*) ASC LIMIT 1 )
SELECT Owners.first_name, Dogs.name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id WHERE Owners.state = 'Virginia';
SELECT Owners.first_name, Dogs.name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id WHERE Owners.state = 'Virginia'
SELECT D.date_arrived, D.date_departed FROM Dogs AS D JOIN Treatments AS T ON D.dog_id = T.dog_id;
SELECT D.date_arrived, D.date_departed FROM Dogs AS D JOIN Treatments AS T ON D.dog_id = T.dog_id;
SELECT O.last_name FROM Owners AS O JOIN Dogs AS D ON O.owner_id = D.owner_id WHERE D.age = (SELECT MIN(age) FROM Dogs);
SELECT O.last_name FROM Owners AS O JOIN Dogs AS D ON O.owner_id = D.owner_id WHERE D.age = (SELECT MIN(age) FROM Dogs);
SELECT email_address FROM Professionals WHERE state IN ('Hawaii', 'Wisconsin')
SELECT email_address FROM Professionals WHERE state IN ('Hawaii', 'Wisconsin')
SELECT date_arrived, date_departed FROM Dogs;
SELECT date_arrived, date_departed FROM Dogs;
SELECT COUNT(DISTINCT dog_id) AS number_of_dogs_treated FROM Treatments;
SELECT COUNT(DISTINCT dog_id) FROM Treatments;
SELECT COUNT(DISTINCT professional_id) AS number_of_professionals FROM Treatments;
SELECT COUNT(DISTINCT professional_id) FROM Treatments;
SELECT role_code, street, city, state FROM Professionals WHERE city LIKE '%West%'
SELECT role_code, street, city, state FROM Professionals WHERE city LIKE '%West%'
SELECT first_name, last_name, email_address FROM Owners WHERE state LIKE '%North%'
SELECT first_name, last_name, email_address FROM Owners WHERE state LIKE '%North%'
SELECT COUNT(*) FROM Dogs WHERE age < (SELECT AVG(age) FROM Dogs);
SELECT COUNT(*) FROM Dogs WHERE age < (SELECT AVG(age) FROM Dogs);
SELECT cost_of_treatment FROM Treatments ORDER BY date_of_treatment DESC LIMIT 1
SELECT cost_of_treatment FROM Treatments ORDER BY date_of_treatment DESC LIMIT 1
SELECT COUNT(*) AS DogsWithoutTreatment FROM Dogs AS D LEFT JOIN Treatments AS T ON D.dog_id = T.dog_id WHERE T.treatment_id IS NULL;
SELECT COUNT(*) AS NumberOfDogsWithoutTreatment FROM Dogs AS D LEFT JOIN Treatments AS T ON D.dog_id = T.dog_id WHERE T.treatment_id IS NULL;
SELECT COUNT(*) FROM Owners AS O WHERE NOT EXISTS ( SELECT 1 FROM Dogs AS D WHERE D.owner_id = O.owner_id );
SELECT COUNT(*) FROM Owners AS O LEFT JOIN Dogs AS D ON O.owner_id = D.owner_id WHERE D.dog_id IS NULL;
SELECT COUNT(*) FROM Professionals AS P LEFT JOIN Treatments AS T ON P.professional_id = T.professional_id WHERE T.treatment_id IS NULL;
SELECT COUNT(*) FROM Professionals AS P LEFT JOIN Treatments AS T ON P.professional_id = T.professional_id WHERE T.treatment_id IS NULL;
SELECT name, age, weight FROM Dogs WHERE abandoned_yn = '1'
SELECT name, age, weight FROM Dogs WHERE abandoned_yn = '1'
SELECT AVG(CAST(age AS INTEGER)) AS average_age FROM Dogs;
SELECT AVG(CAST(age AS INTEGER)) AS average_age FROM Dogs;
SELECT MAX(age) AS oldest_dog_age FROM Dogs;
SELECT MAX(age) AS oldest_dog_age FROM Dogs
SELECT charge_type, charge_amount FROM Charges
SELECT charge_type, charge_amount FROM Charges
SELECT MAX(charge_amount) FROM Charges
SELECT MAX(charge_amount) FROM Charges
SELECT email_address, cell_number, home_phone FROM Professionals;
SELECT email_address, cell_number, home_phone FROM Professionals;
SELECT B.breed_name, S.size_description FROM Breeds AS B CROSS JOIN Sizes AS S;
SELECT DISTINCT B.breed_name, S.size_description FROM Dogs AS D JOIN Breeds AS B ON D.breed_code = B.breed_code JOIN Sizes AS S ON D.size_code = S.size_code;
SELECT P.first_name, T.treatment_type_description FROM Professionals AS P JOIN Treatments AS R ON P.professional_id = R.professional_id JOIN Treatment_Types AS T ON R.treatment_type_code = T.treatment_type_code;
SELECT P.first_name, T.treatment_type_description FROM Professionals AS P JOIN Treatments AS R ON P.professional_id = R.professional_id JOIN Treatment_Types AS T ON R.treatment_type_code = T.treatment_type_code;
SELECT COUNT(*) FROM singer;
SELECT COUNT(*) FROM singer
SELECT Name FROM singer ORDER BY Net_Worth_Millions ASC
SELECT Name FROM singer ORDER BY Net_Worth_Millions ASC
SELECT Birth_Year, Citizenship FROM singer
SELECT Birth_Year, Citizenship FROM singer
SELECT Name FROM singer WHERE Citizenship != 'France'
SELECT Name FROM singer WHERE Citizenship != 'France'
SELECT Name FROM singer WHERE Birth_Year IN (1948, 1949)
SELECT Name FROM singer WHERE Birth_Year IN (1948, 1949)
SELECT Name FROM singer WHERE Net_Worth_Millions = (SELECT MAX(Net_Worth_Millions) FROM singer)
SELECT Name FROM singer WHERE Net_Worth_Millions = (SELECT MAX(Net_Worth_Millions) FROM singer)
SELECT Citizenship, COUNT(*) AS Number_of_Singers FROM singer GROUP BY Citizenship
SELECT Citizenship, COUNT(*) AS NumberOfSingers FROM singer GROUP BY Citizenship
SELECT Citizenship, COUNT(*) AS Count FROM singer GROUP BY Citizenship ORDER BY Count DESC LIMIT 1;
SELECT Citizenship, COUNT(*) AS Count FROM singer GROUP BY Citizenship ORDER BY Count DESC LIMIT 1;
SELECT Citizenship, MAX(Net_Worth_Millions) FROM singer GROUP BY Citizenship
SELECT Citizenship, MAX(Net_Worth_Millions) AS Max_Net_Worth FROM singer GROUP BY Citizenship;
SELECT song.Title, singer.Name FROM song JOIN singer ON song.Singer_ID = singer.Singer_ID
SELECT song.Title, singer.Name FROM song JOIN singer ON song.Singer_ID = singer.Singer_ID
SELECT DISTINCT s.Name FROM singer AS s JOIN song AS so ON s.Singer_ID = so.Singer_ID WHERE so.Sales > 300000
SELECT DISTINCT s.Name FROM singer AS s JOIN song AS so ON s.Singer_ID = so.Singer_ID WHERE so.Sales > 300000
SELECT s.Name FROM singer AS s JOIN song AS so ON s.Singer_ID = so.Singer_ID GROUP BY s.Singer_ID HAVING COUNT(so.Song_ID) > 1
SELECT s.Name FROM singer AS s JOIN song AS so ON s.Singer_ID = so.Singer_ID GROUP BY s.Singer_ID HAVING COUNT(so.Song_ID) > 1;
-- SQL Type: SELECT SELECT s.Name, SUM(so.Sales) AS Total_Sales FROM singer AS s JOIN song AS so ON s.Singer_ID = so.Singer_ID GROUP BY s.Singer_ID;
-- SQL Script Type: SELECT SELECT s.Name, SUM(so.Sales) AS Total_Sales FROM singer AS s JOIN song AS so ON s.Singer_ID = so.Singer_ID GROUP BY s.Name
SELECT s.Name FROM singer s LEFT JOIN song so ON s.Singer_ID = so.Singer_ID WHERE so.Song_ID IS NULL;
SELECT s.Name FROM singer AS s LEFT JOIN song AS so ON s.Singer_ID = so.Singer_ID WHERE so.Song_ID IS NULL;
SELECT DISTINCT s1.Citizenship FROM singer AS s1 WHERE s1.Birth_Year < 1945 INTERSECT SELECT DISTINCT s2.Citizenship FROM singer AS s2 WHERE s2.Birth_Year > 1955;
SELECT DISTINCT Citizenship FROM singer WHERE Birth_Year < 1945 INTERSECT SELECT DISTINCT Citizenship FROM singer WHERE Birth_Year > 1955;
SELECT COUNT(*) FROM Other_Available_Features
SELECT RFT.feature_type_name FROM Other_Available_Features OAF JOIN Ref_Feature_Types RFT ON OAF.feature_type_code = RFT.feature_type_code WHERE OAF.feature_name = 'AirCon';
SELECT RPT.property_type_description FROM Properties AS P JOIN Ref_Property_Types AS RPT ON P.property_type_code = RPT.property_type_code WHERE P.property_type_code = 'your_property_type_code_here';
SELECT P.property_name FROM Properties AS P JOIN Ref_Property_Types AS R ON P.property_type_code = R.property_type_code WHERE (R.property_type_description LIKE '%House%' OR R.property_type_description LIKE '%Apartment%') AND P.room_count > 1;
