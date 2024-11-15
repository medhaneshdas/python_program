create database plant_data;
use plant_data;
create table plant(
Id int auto_increment primary key,
Plant_Name varchar(50),
Location varchar(50),
Climate varchar(50),
Watering_Remainder varchar(50),
Fertilizing_Remainder varchar(50),
Other_Care_Remainder varchar(50),
Tips varchar(500));

insert into Plant(
Plant_Name, Location, Climate, Watering_Remainder, Fertilizing_Remainder, Other_Care_Remainder, Tips)
values ('Pilodendron','Indoor Plant','Moderate',
'Every 7 Days','once a Month','Trim Brom Leaves',
'Keep Your Philodendron In Bright,Indirect light,Water when The Top Inch Of Soil Is Dry,And Maintain Moderate Humidity For Optimal growth');

insert into Plant(
Plant_Name, Location, Climate, Watering_Remainder, Fertilizing_Remainder, Other_Care_Remainder, Tips)
values ('Pothos','Indoor Plant','Humid','Every 5 Days','Every 2 Week','Wipe Leaves',
'Pothos Plants Thrive In Indirect Lights,Require Infrequent Watering, and are easy to care for');

insert into Plant(
Plant_Name, Location, Climate, Watering_Remainder, Fertilizing_Remainder, Other_Care_Remainder, Tips)
values ('ZZ Plant','Indoor Plant','Dry','Every 14 Days','Once In 2 Months','Avoid Overwatering',
'Allow The Soil To Dry Out Completely Between Watering To Prevent Overwatering');

insert into Plant(
Plant_Name, Location, Climate, Watering_Remainder, Fertilizing_Remainder, Other_Care_Remainder, Tips)
values ('Rose','Indoor Plant','Moderate','Every 5 Days','Once a Month','Trim Long Stems',
'Plant Roses In Well-Drained Soil With Plenty Of Sunlight And Regular Pruncing For Healthy Growth And Vibrant Blooms');

select * from Plant;