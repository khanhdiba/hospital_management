DROP SCHEMA IF EXISTS HMS;
CREATE SCHEMA HMS;
USE HMS;

CREATE TABLE HMS.Department (
    departmentID CHAR(2),
    departmentName VARCHAR(50),
    PRIMARY KEY (departmentID)
);

INSERT INTO HMS.Department VALUES ('01', 'Cardiology');
INSERT INTO HMS.Department VALUES ('02', 'Neurology');
INSERT INTO HMS.Department VALUES ('03', 'Orthopedics');
INSERT INTO HMS.Department VALUES ('04', 'Pediatrics');
INSERT INTO HMS.Department VALUES ('05', 'Oncology');
INSERT INTO HMS.Department VALUES ('06', 'Dermatology');
INSERT INTO HMS.Department VALUES ('07', 'Radiology');
INSERT INTO HMS.Department VALUES ('08', 'Surgery');
INSERT INTO HMS.Department VALUES ('09', 'Psychiatry');
INSERT INTO HMS.Department VALUES ('10', 'Gastroenterology');



CREATE TABLE HMS.Medical_Staff (
    staffID	CHAR(7),
    staffSSN CHAR(10) NOT NULL UNIQUE,
    firstName VARCHAR(20) NOT NULL,
    midName	 VARCHAR(50),
    lastName VARCHAR(20),
    staffDoB DATE,
    gender	ENUM ('F', 'M'),
    phoneNumber	CHAR(10),
    salary	INT UNSIGNED,
    departmentID CHAR(2),
    
    PRIMARY KEY (staffID),
    FOREIGN KEY (departmentID) REFERENCES Department (departmentID)
);
INSERT INTO HMS.Medical_Staff VALUES ('D100001', '1111111111', 'Alice', 'Marie', 'Johnson', '1980-05-15', 'F', '9998887776', 70000, '01');
INSERT INTO HMS.Medical_Staff VALUES ('D100002', '2222222222', 'Bob', 'Andrew', 'Smith', '1975-09-23', 'M', '8887776665', 80000, '02');
INSERT INTO HMS.Medical_Staff VALUES ('D100003', '3333333333', 'Clara', 'Louise', 'Brown', '1990-11-10', 'F', '7776665554', 75000, '03');
INSERT INTO HMS.Medical_Staff VALUES ('D100004', '4444444444', 'David', 'Michael', 'Taylor', '1982-01-22', 'M', '6665554443', 72000, '04');
INSERT INTO HMS.Medical_Staff VALUES ('D100005', '5555555555', 'Ella', 'Grace', 'Davis', '1995-04-30', 'F', '5554443332', 71000, '05');
INSERT INTO HMS.Medical_Staff VALUES ('D100006', '6666666666', 'Frank', 'John', 'Miller', '1978-06-18', 'M', '4443332221', 76000, '06');
INSERT INTO HMS.Medical_Staff VALUES ('D100007', '7777777777', 'Grace', 'Emily', 'Wilson', '1987-08-05', 'F', '3332221110', 74000, '07');
INSERT INTO HMS.Medical_Staff VALUES ('D100008', '8888888888', 'Henry', 'Arthur', 'Moore', '1985-03-12', 'M', '2221110009', 73000, '08');
INSERT INTO HMS.Medical_Staff VALUES ('D100009', '9999999999', 'Isabella', 'Sophia', 'Harris', '1992-12-20', 'F', '1110009998', 78000, '09');
INSERT INTO HMS.Medical_Staff VALUES ('D100010', '1010101010', 'Jack', 'Thomas', 'Martinez', '1989-07-01', 'M', '0009998887', 77000, '10');
INSERT INTO HMS.Medical_Staff VALUES ('D100011', '1212121211', 'Emily', 'Charlotte', 'Adams', '1983-02-17', 'F', '9876543210', 72000, '01');
INSERT INTO HMS.Medical_Staff VALUES ('D100012', '1313131311', 'Nathan', 'James', 'Carter', '1977-10-14', 'M', '8765432109', 80000, '01');
INSERT INTO HMS.Medical_Staff VALUES ('D100013', '1414141411', 'Olivia', 'Amelia', 'Walker', '1991-09-30', 'F', '7654321098', 75000, '03');
INSERT INTO HMS.Medical_Staff VALUES ('D100014', '1515151511', 'Ethan', 'Lucas', 'White', '1980-03-25', 'M', '6543210987', 71000, '04');
INSERT INTO HMS.Medical_Staff VALUES ('D100015', '1616161611', 'Sophia', 'Isabel', 'Allen', '1994-06-05', 'F', '5432109876', 73000, '04');
INSERT INTO HMS.Medical_Staff VALUES ('D100016', '1717171711', 'Liam', 'Benjamin', 'Scott', '1979-12-19', 'M', '4321098765', 76000, '01');
INSERT INTO HMS.Medical_Staff VALUES ('D100017', '1818181811', 'Chloe', 'Victoria', 'Hill', '1990-08-09', 'F', '3210987654', 74000, '10');
INSERT INTO HMS.Medical_Staff VALUES ('D100018', '1919191911', 'Michael', 'Alexander', 'Green', '1986-11-29', 'M', '2109876543', 78000, '06');
INSERT INTO HMS.Medical_Staff VALUES ('D100019', '2020202023', 'Mia', 'Ava', 'King', '1993-04-15', 'F', '1098765432', 77000, '09');
INSERT INTO HMS.Medical_Staff VALUES ('D100020', '2121212128', 'Daniel', 'Samuel', 'Baker', '1981-01-11', 'M', '0987654321', 79000, '09');



INSERT INTO HMS.Medical_Staff VALUES ('N100001', '1212121212', 'Karen', 'Anne', 'Anderson', '1985-04-10', 'F', '1112223334', 50000, '01');
INSERT INTO HMS.Medical_Staff VALUES ('N100002', '1313131313', 'Louis', 'Edward', 'Brooks', '1990-06-15', 'M', '2223334445', 48000, '02');
INSERT INTO HMS.Medical_Staff VALUES ('N100003', '1414141414', 'Mia', 'Sophia', 'Clark', '1992-09-20', 'F', '3334445556', 51000, '03');
INSERT INTO HMS.Medical_Staff VALUES ('N100004', '1515151515', 'Noah', 'James', 'Evans', '1988-03-08', 'M', '4445556667', 52000, '04');
INSERT INTO HMS.Medical_Staff VALUES ('N100005', '1616161616', 'Olivia', 'Grace', 'Green', '1995-12-01', 'F', '5556667778', 50000, '05');
INSERT INTO HMS.Medical_Staff VALUES ('N100006', '1717171717', 'Peter', 'George', 'Hill', '1991-07-18', 'M', '6667778889', 48000, '06');
INSERT INTO HMS.Medical_Staff VALUES ('N100007', '1818181818', 'Quinn', 'Diana', 'Jones', '1983-11-25', 'F', '7778889990', 52000, '07');
INSERT INTO HMS.Medical_Staff VALUES ('N100008', '1919191919', 'Ryan', 'William', 'King', '1987-08-30', 'M', '8889990001', 51000, '08');
INSERT INTO HMS.Medical_Staff VALUES ('N100009', '2020202020', 'Sophia', 'Charlotte', 'Lee', '1990-05-12', 'F', '9990001112', 50000, '09');
INSERT INTO HMS.Medical_Staff VALUES ('N100010', '2121212121', 'Thomas', 'Henry', 'Moore', '1985-10-03', 'M', '0001112223', 48000, '10');
INSERT INTO HMS.Medical_Staff VALUES ('N100011', '2222222223', 'Ava', 'Emily', 'Nelson', '1994-03-14', 'F', '1112223335', 50000, '01');
INSERT INTO HMS.Medical_Staff VALUES ('N100012', '2323232323', 'Blake', 'Andrew', 'Parker', '1989-11-20', 'M', '2223334446', 48000, '02');
INSERT INTO HMS.Medical_Staff VALUES ('N100013', '2424242424', 'Charlotte', 'Rose', 'Adams', '1993-08-25', 'F', '3334445557', 51000, '03');
INSERT INTO HMS.Medical_Staff VALUES ('N100014', '2525252525', 'Daniel', 'Michael', 'Scott', '1990-07-15', 'M', '4445556668', 52000, '04');
INSERT INTO HMS.Medical_Staff VALUES ('N100015', '2626262626', 'Ella', 'Victoria', 'Morgan', '1996-06-10', 'F', '5556667779', 50000, '05');
INSERT INTO HMS.Medical_Staff VALUES ('N100016', '2727272727', 'Ethan', 'Henry', 'Taylor', '1987-04-05', 'M', '6667778890', 48000, '06');
INSERT INTO HMS.Medical_Staff VALUES ('N100017', '2828282828', 'Grace', 'Isabelle', 'Bell', '1985-09-12', 'F', '7778889991', 52000, '07');
INSERT INTO HMS.Medical_Staff VALUES ('N100018', '2929292929', 'Hannah', 'Sophia', 'Carter', '1992-05-30', 'F', '8889990002', 51000, '08');
INSERT INTO HMS.Medical_Staff VALUES ('N100019', '3030303030', 'Jack', 'Arthur', 'White', '1991-02-18', 'M', '9990001113', 50000, '09');
INSERT INTO HMS.Medical_Staff VALUES ('N100020', '3131313131', 'Liam', 'George', 'Harris', '1988-10-25', 'M', '0001112224', 48000, '01');


CREATE TABLE HMS.Doctor (
    doctorID CHAR(7),
    license	CHAR(12),
    
    PRIMARY KEY (doctorID),
    FOREIGN KEY (doctorID) REFERENCES Medical_Staff (staffID)
);
INSERT INTO HMS.Doctor VALUES ('D100001', 'LIC00000001');
INSERT INTO HMS.Doctor VALUES ('D100002', 'LIC00000002');
INSERT INTO HMS.Doctor VALUES ('D100003', 'LIC00000003');
INSERT INTO HMS.Doctor VALUES ('D100004', 'LIC00000004');
INSERT INTO HMS.Doctor VALUES ('D100005', 'LIC00000005');
INSERT INTO HMS.Doctor VALUES ('D100006', 'LIC00000006');
INSERT INTO HMS.Doctor VALUES ('D100007', 'LIC00000007');
INSERT INTO HMS.Doctor VALUES ('D100008', 'LIC00000008');
INSERT INTO HMS.Doctor VALUES ('D100009', 'LIC00000009');
INSERT INTO HMS.Doctor VALUES ('D100010', 'LIC00000010');
INSERT INTO HMS.Doctor VALUES ('D100011', 'LIC00000011');
INSERT INTO HMS.Doctor VALUES ('D100012', 'LIC00000012');
INSERT INTO HMS.Doctor VALUES ('D100013', 'LIC00000013');
INSERT INTO HMS.Doctor VALUES ('D100014', 'LIC00000014');
INSERT INTO HMS.Doctor VALUES ('D100015', 'LIC00000015');
INSERT INTO HMS.Doctor VALUES ('D100016', 'LIC00000016');
INSERT INTO HMS.Doctor VALUES ('D100017', 'LIC00000017');
INSERT INTO HMS.Doctor VALUES ('D100018', 'LIC00000018');
INSERT INTO HMS.Doctor VALUES ('D100019', 'LIC00000019');
INSERT INTO HMS.Doctor VALUES ('D100020', 'LIC00000020');


CREATE TABLE HMS.Manages (
    departmentID CHAR(2),
    doctorID CHAR(7) NOT NULL UNIQUE,
    startDate DATE NOT NULL,
    
    PRIMARY KEY (departmentID),
    FOREIGN KEY (departmentID) REFERENCES Department (departmentID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (doctorID) REFERENCES Doctor (doctorID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO HMS.Manages VALUES ('01', 'D100001', '2015-06-01');
INSERT INTO HMS.Manages VALUES ('02', 'D100002', '2017-09-15');
INSERT INTO HMS.Manages VALUES ('03', 'D100003', '2016-01-20');
INSERT INTO HMS.Manages VALUES ('04', 'D100004', '2018-04-10');
INSERT INTO HMS.Manages VALUES ('05', 'D100005', '2019-11-05');
INSERT INTO HMS.Manages VALUES ('06', 'D100006', '2014-07-23');
INSERT INTO HMS.Manages VALUES ('07', 'D100007', '2020-03-18');
INSERT INTO HMS.Manages VALUES ('08', 'D100008', '2021-12-01');
INSERT INTO HMS.Manages VALUES ('09', 'D100009', '2022-05-15');
INSERT INTO HMS.Manages VALUES ('10', 'D100010', '2023-02-10');


CREATE TABLE HMS.Specialization (
    doctorID CHAR(7),
    aSpecialization	VARCHAR(20),
    
    PRIMARY KEY (doctorID, aSpecialization),
    FOREIGN KEY (doctorID) REFERENCES Doctor (doctorID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO HMS.Specialization VALUES ('D100001', 'Cardiology');
INSERT INTO HMS.Specialization VALUES ('D100001', 'Internal Medicine');
INSERT INTO HMS.Specialization VALUES ('D100002', 'Neurology');
INSERT INTO HMS.Specialization VALUES ('D100002', 'Pediatrics');
INSERT INTO HMS.Specialization VALUES ('D100003', 'Orthopedics');
INSERT INTO HMS.Specialization VALUES ('D100003', 'Sports Medicine');
INSERT INTO HMS.Specialization VALUES ('D100004', 'General Surgery');
INSERT INTO HMS.Specialization VALUES ('D100004', 'Trauma Surgery');
INSERT INTO HMS.Specialization VALUES ('D100005', 'Dermatology');
INSERT INTO HMS.Specialization VALUES ('D100005', 'Cosmetic Medicine');
INSERT INTO HMS.Specialization VALUES ('D100006', 'Radiology');
INSERT INTO HMS.Specialization VALUES ('D100006', 'Nuclear Medicine');
INSERT INTO HMS.Specialization VALUES ('D100007', 'Ophthalmology');
INSERT INTO HMS.Specialization VALUES ('D100007', 'Laser Surgery');
INSERT INTO HMS.Specialization VALUES ('D100008', 'Endocrinology');
INSERT INTO HMS.Specialization VALUES ('D100008', 'Diabetes Management');
INSERT INTO HMS.Specialization VALUES ('D100009', 'Gastroenterology');
INSERT INTO HMS.Specialization VALUES ('D100009', 'Hepatology');
INSERT INTO HMS.Specialization VALUES ('D100010', 'Psychiatry');
INSERT INTO HMS.Specialization VALUES ('D100010', 'Behavioral Medicine');
INSERT INTO HMS.Specialization VALUES ('D100011', 'Neurology');
INSERT INTO HMS.Specialization VALUES ('D100012', 'Cardiology');
INSERT INTO HMS.Specialization VALUES ('D100012', 'Internal Medicine');
INSERT INTO HMS.Specialization VALUES ('D100012', 'Pediatrics');
INSERT INTO HMS.Specialization VALUES ('D100013', 'Orthopedics');
INSERT INTO HMS.Specialization VALUES ('D100014', 'Sports Medicine');
INSERT INTO HMS.Specialization VALUES ('D100014', 'General Surgery');
INSERT INTO HMS.Specialization VALUES ('D100014', 'Trauma Surgery');
INSERT INTO HMS.Specialization VALUES ('D100015', 'Dermatology');
INSERT INTO HMS.Specialization VALUES ('D100015', 'Cosmetic Medicine');
INSERT INTO HMS.Specialization VALUES ('D100016', 'Radiology');
INSERT INTO HMS.Specialization VALUES ('D100016', 'Nuclear Medicine');
INSERT INTO HMS.Specialization VALUES ('D100017', 'Ophthalmology');
INSERT INTO HMS.Specialization VALUES ('D100017', 'Laser Surgery');
INSERT INTO HMS.Specialization VALUES ('D100017', 'Endocrinology');
INSERT INTO HMS.Specialization VALUES ('D100018', 'Diabetes Management');
INSERT INTO HMS.Specialization VALUES ('D100018', 'Gastroenterology');
INSERT INTO HMS.Specialization VALUES ('D100019', 'Behavioral Medicine');
INSERT INTO HMS.Specialization VALUES ('D100020', 'Hepatology');
INSERT INTO HMS.Specialization VALUES ('D100020', 'Psychiatry');


CREATE TABLE HMS.Nurse (
    nurseID	CHAR(7),
    yearExperience INT,
    
    PRIMARY KEY (nurseID),
    FOREIGN KEY (nurseID) REFERENCES Medical_Staff (staffID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO HMS.Nurse VALUES ('N100001', 5);
INSERT INTO HMS.Nurse VALUES ('N100002', 3);
INSERT INTO HMS.Nurse VALUES ('N100003', 8);
INSERT INTO HMS.Nurse VALUES ('N100004', 2);
INSERT INTO HMS.Nurse VALUES ('N100005', 6);
INSERT INTO HMS.Nurse VALUES ('N100006', 4);
INSERT INTO HMS.Nurse VALUES ('N100007', 7);
INSERT INTO HMS.Nurse VALUES ('N100008', 10);
INSERT INTO HMS.Nurse VALUES ('N100009', 1);
INSERT INTO HMS.Nurse VALUES ('N100010', 9);
INSERT INTO HMS.Nurse VALUES ('N100019', 5);
INSERT INTO HMS.Nurse VALUES ('N100020', 3);
INSERT INTO HMS.Nurse VALUES ('N100018', 8);
INSERT INTO HMS.Nurse VALUES ('N100016', 2);
INSERT INTO HMS.Nurse VALUES ('N100017', 6);
INSERT INTO HMS.Nurse VALUES ('N100014', 4);
INSERT INTO HMS.Nurse VALUES ('N100015', 7);
INSERT INTO HMS.Nurse VALUES ('N100013', 10);
INSERT INTO HMS.Nurse VALUES ('N100012', 1);
INSERT INTO HMS.Nurse VALUES ('N100011', 9);


CREATE TABLE HMS.Room (
    roomID CHAR(3),
    capacity INT,
    roomType VARCHAR(20),
    
    PRIMARY KEY (roomID)
);
INSERT INTO HMS.Room VALUES ('101', 2, 'General Ward');
INSERT INTO HMS.Room VALUES ('102', 1, 'ICU');
INSERT INTO HMS.Room VALUES ('103', 3, 'General Ward');
INSERT INTO HMS.Room VALUES ('104', 1, 'ICU');
INSERT INTO HMS.Room VALUES ('105', 2, 'Private Room');
INSERT INTO HMS.Room VALUES ('106', 4, 'General Ward');
INSERT INTO HMS.Room VALUES ('107', 1, 'ICU');
INSERT INTO HMS.Room VALUES ('108', 3, 'Semi-Private Room');
INSERT INTO HMS.Room VALUES ('109', 2, 'Private Room');
INSERT INTO HMS.Room VALUES ('110', 4, 'General Ward');


CREATE TABLE HMS.Patient (
    patientID CHAR(7),
    patientSSN CHAR(10)	NOT NULL UNIQUE,
    firstName VARCHAR(20) NOT NULL,
    midName	VARCHAR(50),
    lastName VARCHAR(20),
    patientDoB DATE,
    gender ENUM ('F', 'M'),
    phoneNumber CHAR(10),
    street VARCHAR(50),
    district VARCHAR(50),
    city VARCHAR(50),    
    
    PRIMARY KEY (patientID)
);
INSERT INTO HMS.Patient VALUES ('P000001', '1234567890', 'John', 'Michael', 'Doe', '1990-01-15', 'M', '1234567890', '123 Oak St', 'Downtown', 'CityA');
INSERT INTO HMS.Patient VALUES ('P000002', '9876543210', 'Alice', 'Marie', 'Smith', '1985-07-23', 'F', '2345678901', '456 Maple Ave', 'Uptown', 'CityB');
INSERT INTO HMS.Patient VALUES ('P000003', '5647382910', 'Robert', 'Lee', 'Johnson', '1978-12-02', 'M', '3456789012', '789 Pine Rd', 'Suburb', 'CityC');
INSERT INTO HMS.Patient VALUES ('P000004', '1928374650', 'Linda', 'Ann', 'Brown', '1992-09-17', 'F', '4567890123', '321 Birch Ln', 'Westside', 'CityA');
INSERT INTO HMS.Patient VALUES ('P000005', '5738291046', 'Michael', 'James', 'Williams', '1980-05-10', 'M', '5678901234', '654 Cedar Dr', 'Eastside', 'CityB');
INSERT INTO HMS.Patient VALUES ('P000006', '2847361820', 'Sophia', 'Grace', 'Taylor', '2000-04-20', 'F', '6789012345', '123 Elm St', 'Northside', 'CityC');
INSERT INTO HMS.Patient VALUES ('P000007', '3746281930', 'David', 'Charles', 'Miller', '1995-11-05', 'M', '7890123456', '987 Oak St', 'Southside', 'CityA');
INSERT INTO HMS.Patient VALUES ('P000008', '8745629301', 'Emma', 'Rose', 'Davis', '1989-03-13', 'F', '8901234567', '654 Willow Ave', 'Riverside', 'CityB');
INSERT INTO HMS.Patient VALUES ('P000009', '8475620193', 'William', 'Henry', 'Moore', '2002-02-25', 'M', '9012345678', '321 Pine Rd', 'Lakeside', 'CityC');
INSERT INTO HMS.Patient VALUES ('P000010', '2738491012', 'Olivia', 'Lynn', 'Garcia', '1994-06-30', 'F', '0123456789', '987 Birch Ln', 'Valley', 'CityA');
INSERT INTO HMS.Patient VALUES ('P000011', '1827364556', 'James', 'Edward', 'Anderson', '1988-08-18', 'M', '2233445566', '789 Walnut St', 'Hillside', 'CityD');
INSERT INTO HMS.Patient VALUES ('P000012', '3344556677', 'Charlotte', 'May', 'Thomas', '1996-11-22', 'F', '3344556677', '123 Cypress Rd', 'Woodside', 'CityE');
INSERT INTO HMS.Patient VALUES ('P000013', '4455667788', 'Benjamin', 'Paul', 'Jackson', '1983-03-12', 'M', '4455667788', '456 Magnolia Blvd', 'Downtown', 'CityF');
INSERT INTO HMS.Patient VALUES ('P000014', '5566778899', 'Isabella', 'Marie', 'Martin', '1999-07-07', 'F', '5566778899', '987 Aspen Ave', 'Eastside', 'CityG');
INSERT INTO HMS.Patient VALUES ('P000015', '6677889900', 'Alexander', 'John', 'Thompson', '1977-05-25', 'M', '6677889900', '654 Alder St', 'Northside', 'CityH');
INSERT INTO HMS.Patient VALUES ('P000016', '7788990011', 'Amelia', 'Jane', 'White', '1981-01-15', 'F', '7788990011', '321 Redwood Ct', 'Southside', 'CityI');
INSERT INTO HMS.Patient VALUES ('P000017', '8899001122', 'Lucas', 'Scott', 'Harris', '2001-09-03', 'M', '8899001122', '123 Hickory Ln', 'Valley', 'CityJ');
INSERT INTO HMS.Patient VALUES ('P000018', '9900112233', 'Mia', 'Sophia', 'Clark', '1993-02-19', 'F', '9900112233', '456 Sycamore Dr', 'Riverside', 'CityK');
INSERT INTO HMS.Patient VALUES ('P000019', '0011223344', 'Matthew', 'George', 'Lewis', '1998-12-11', 'M', '0011223344', '789 Fir Ct', 'Suburb', 'CityL');
INSERT INTO HMS.Patient VALUES ('P000020', '1122334455', 'Harper', 'Anne', 'Lee', '1986-10-28', 'F', '1122334455', '654 Poplar St', 'Downtown', 'CityM');
INSERT INTO HMS.Patient VALUES ('P000021', '2233445566', 'Elijah', 'Patrick', 'Walker', '1979-06-16', 'M', '2233445566', '321 Ash Blvd', 'Westside', 'CityN');
INSERT INTO HMS.Patient VALUES ('P000022', '3344556678', 'Abigail', 'Claire', 'Hall', '1995-08-14', 'F', '3344556677', '987 Spruce Rd', 'Uptown', 'CityO');
INSERT INTO HMS.Patient VALUES ('P000023', '4455667789', 'Ethan', 'Charles', 'Young', '1990-04-02', 'M', '4455667788', '123 Beech Ln', 'Hillside', 'CityP');
INSERT INTO HMS.Patient VALUES ('P000024', '5566778890', 'Sofia', 'Elizabeth', 'Allen', '1984-11-29', 'F', '5566778899', '456 Cherry Ave', 'Woodside', 'CityQ');
INSERT INTO HMS.Patient VALUES ('P000025', '6677889901', 'Logan', 'David', 'King', '2003-05-07', 'M', '6677889900', '789 Palm Ct', 'Lakeside', 'CityR');
INSERT INTO HMS.Patient VALUES ('P000026', '7788990012', 'Ava', 'Emily', 'Scott', '1997-09-21', 'F', '7788990011', '654 Dogwood Rd', 'Northside', 'CityS');
INSERT INTO HMS.Patient VALUES ('P000027', '8899001123', 'Mason', 'Henry', 'Wright', '1991-03-09', 'M', '8899001122', '321 Juniper St', 'Southside', 'CityT');
INSERT INTO HMS.Patient VALUES ('P000028', '9900112234', 'Grace', 'Isabelle', 'Green', '1982-02-13', 'F', '9900112233', '123 Willow Dr', 'Eastside', 'CityU');
INSERT INTO HMS.Patient VALUES ('P000029', '0011223345', 'Oliver', 'Nathan', 'Adams', '1987-12-30', 'M', '0011223344', '456 Maple Ct', 'Downtown', 'CityV');
INSERT INTO HMS.Patient VALUES ('P000030', '1122334456', 'Emily', 'Victoria', 'Baker', '1992-08-18', 'F', '1122334455', '789 Elm Blvd', 'Suburb', 'CityW');



CREATE TABLE HMS.Patients_Family (
    familyID INT,
    patientID CHAR(7) NOT NULL,
    relationship VARCHAR(50),
    phoneNumber CHAR(10),
    
    PRIMARY KEY (patientID, familyID),
    FOREIGN KEY (patientID) REFERENCES Patient (patientID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO HMS.Patients_Family VALUES (1, 'P000001', 'Mother', '1234567890');
INSERT INTO HMS.Patients_Family VALUES (2, 'P000001', 'Father', '2345678901');
INSERT INTO HMS.Patients_Family VALUES (1, 'P000002', 'Husband', '3456789012');
INSERT INTO HMS.Patients_Family VALUES (2, 'P000002', 'Mother', '4567890123');
INSERT INTO HMS.Patients_Family VALUES (1, 'P000003', 'Sister', '5678901234');
INSERT INTO HMS.Patients_Family VALUES (2, 'P000003', 'Father', '6789012345');
INSERT INTO HMS.Patients_Family VALUES (1, 'P000004', 'Father', '7890123456');
INSERT INTO HMS.Patients_Family VALUES (2, 'P000004', 'Brother', '8901234567');
INSERT INTO HMS.Patients_Family VALUES (1, 'P000005', 'Wife', '9012345678');
INSERT INTO HMS.Patients_Family VALUES (2, 'P000005', 'Mother', '0123456789');
INSERT INTO HMS.Patients_Family VALUES (1, 'P000006', 'Brother', '1234567890');
INSERT INTO HMS.Patients_Family VALUES (2, 'P000006', 'Father', '2345678901');
INSERT INTO HMS.Patients_Family VALUES (1, 'P000007', 'Mother', '3456789012');
INSERT INTO HMS.Patients_Family VALUES (2, 'P000007', 'Father', '4567890123');
INSERT INTO HMS.Patients_Family VALUES (1, 'P000008', 'Sister', '5678901234');
INSERT INTO HMS.Patients_Family VALUES (2, 'P000008', 'Father', '6789012345');
INSERT INTO HMS.Patients_Family VALUES (1, 'P000009', 'Mother', '7890123456');
INSERT INTO HMS.Patients_Family VALUES (2, 'P000009', 'Brother', '8901234567');
INSERT INTO HMS.Patients_Family VALUES (1, 'P000010', 'Husband', '9012345678');
INSERT INTO HMS.Patients_Family VALUES (2, 'P000010', 'Father', '0123456789');

CREATE TABLE HMS.Admitted_to (
    patientID CHAR(7),
    roomID CHAR(3),
    admittedDate DATE,
    dischargedDate DATE,
    
    PRIMARY KEY (patientID, roomID, admittedDate),
    FOREIGN KEY (patientID) REFERENCES Patient (patientID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (roomID) REFERENCES Room (roomID) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE HMS.Admitted_to
ADD CONSTRAINT CheckDateValidity
CHECK (dischargedDate >= admittedDate);


INSERT INTO HMS.Admitted_to VALUES ('P000001', '101', '2024-12-01', '2024-12-07');
INSERT INTO HMS.Admitted_to VALUES ('P000011', '101', '2024-12-02', '2024-12-08');
INSERT INTO HMS.Admitted_to VALUES ('P000002', '102', '2024-12-05', '2024-12-12');
INSERT INTO HMS.Admitted_to VALUES ('P000003', '103', '2024-12-10', '2024-12-15');
INSERT INTO HMS.Admitted_to VALUES ('P000005', '103', '2024-12-03', '2024-12-09');
INSERT INTO HMS.Admitted_to VALUES ('P000018', '104', '2024-12-01', '2024-12-07');
INSERT INTO HMS.Admitted_to VALUES ('P000012', '105', '2024-12-06', '2024-12-13');
INSERT INTO HMS.Admitted_to VALUES ('P000019', '105', '2024-12-12', '2024-12-19');
INSERT INTO HMS.Admitted_to VALUES ('P000004', '106', '2024-12-01', '2024-12-10');
INSERT INTO HMS.Admitted_to VALUES ('P000006', '106', '2024-12-05', '2024-12-12');
INSERT INTO HMS.Admitted_to VALUES ('P000029', '106', '2024-12-09', '2024-12-15');
INSERT INTO HMS.Admitted_to VALUES ('P000013', '107', '2024-12-10', '2024-12-17');
INSERT INTO HMS.Admitted_to VALUES ('P000008', '108', '2024-12-01', '2024-12-05');
INSERT INTO HMS.Admitted_to VALUES ('P000021', '108', '2024-12-03', '2024-12-09');
INSERT INTO HMS.Admitted_to VALUES ('P000014', '109', '2024-12-01', '2024-12-07');
INSERT INTO HMS.Admitted_to VALUES ('P000027', '109', '2024-12-02', '2024-12-08');
INSERT INTO HMS.Admitted_to VALUES ('P000015', '110', '2024-12-05', '2024-12-12');




CREATE TABLE HMS.Appointment (
    appointmentID INT,
    patientID CHAR(7),
    doctorID CHAR(7),
    appointmentDate DATE,
    appointmentTime TIME,
    
    PRIMARY KEY (appointmentID),
    FOREIGN KEY (patientID) REFERENCES Patient (patientID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (doctorID) REFERENCES Doctor (doctorID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO HMS.Appointment VALUES (1, 'P000003', 'D100003', '2024-12-01', '10:00:00');
INSERT INTO HMS.Appointment VALUES (2, 'P000002', 'D100002', '2024-12-01', '09:30:00');

INSERT INTO HMS.Appointment VALUES (3, 'P000001', 'D100001', '2024-12-01', '09:00:00');
INSERT INTO HMS.Appointment VALUES (4, 'P000007', 'D100002', '2024-12-10', '11:30:00');
INSERT INTO HMS.Appointment VALUES (5, 'P000004', 'D100003', '2024-12-09', '10:00:00');
INSERT INTO HMS.Appointment VALUES (6, 'P000004', 'D100004', '2024-12-02', '10:30:00');
INSERT INTO HMS.Appointment VALUES (7, 'P000005', 'D100005', '2024-12-02', '11:00:00');
INSERT INTO HMS.Appointment VALUES (8, 'P000006', 'D100006', '2024-12-03', '11:30:00');
INSERT INTO HMS.Appointment VALUES (9, 'P000007', 'D100007', '2024-12-03', '12:00:00');
INSERT INTO HMS.Appointment VALUES (10, 'P000008', 'D100008', '2024-12-04', '12:30:00');
INSERT INTO HMS.Appointment VALUES (11, 'P000009', 'D100009', '2024-12-04', '13:00:00');
INSERT INTO HMS.Appointment VALUES (12, 'P000010', 'D100010', '2024-12-05', '13:30:00');
INSERT INTO HMS.Appointment VALUES (13, 'P000011', 'D100011', '2024-12-05', '14:00:00');
INSERT INTO HMS.Appointment VALUES (14, 'P000012', 'D100012', '2024-12-06', '14:30:00');
INSERT INTO HMS.Appointment VALUES (15, 'P000013', 'D100013', '2024-12-06', '15:00:00');
INSERT INTO HMS.Appointment VALUES (16, 'P000014', 'D100014', '2024-12-07', '15:30:00');
INSERT INTO HMS.Appointment VALUES (17, 'P000015', 'D100015', '2024-12-07', '16:00:00');
INSERT INTO HMS.Appointment VALUES (18, 'P000016', 'D100016', '2024-12-08', '16:30:00');
INSERT INTO HMS.Appointment VALUES (19, 'P000017', 'D100017', '2024-12-08', '17:00:00');
INSERT INTO HMS.Appointment VALUES (20, 'P000018', 'D100018', '2024-12-09', '17:30:00');
INSERT INTO HMS.Appointment VALUES (21, 'P000019', 'D100019', '2024-12-10', '08:00:00');
INSERT INTO HMS.Appointment VALUES (22, 'P000020', 'D100020', '2024-12-10', '08:30:00');
INSERT INTO HMS.Appointment VALUES (23, 'P000021', 'D100001', '2024-12-11', '09:00:00');
INSERT INTO HMS.Appointment VALUES (24, 'P000022', 'D100002', '2024-12-11', '09:30:00');
INSERT INTO HMS.Appointment VALUES (25, 'P000023', 'D100003', '2024-12-12', '10:00:00');
INSERT INTO HMS.Appointment VALUES (26, 'P000024', 'D100004', '2024-12-12', '10:30:00');
INSERT INTO HMS.Appointment VALUES (27, 'P000025', 'D100005', '2024-12-13', '11:00:00');
INSERT INTO HMS.Appointment VALUES (28, 'P000026', 'D100006', '2024-12-13', '11:30:00');
INSERT INTO HMS.Appointment VALUES (29, 'P000027', 'D100007', '2024-12-14', '12:00:00');
INSERT INTO HMS.Appointment VALUES (30, 'P000028', 'D100008', '2024-12-14', '12:30:00');
INSERT INTO HMS.Appointment VALUES (31, 'P000029', 'D100009', '2024-12-15', '13:00:00');
INSERT INTO HMS.Appointment VALUES (32, 'P000030', 'D100010', '2024-12-15', '13:30:00');
INSERT INTO HMS.Appointment VALUES (33, 'P000001', 'D100011', '2024-12-16', '08:00:00');
INSERT INTO HMS.Appointment VALUES (34, 'P000002', 'D100012', '2024-12-16', '08:30:00');

INSERT INTO HMS.Appointment VALUES (35, 'P000003', 'D100013', '2024-12-17', '09:00:00');
INSERT INTO HMS.Appointment VALUES (36, 'P000004', 'D100014', '2024-12-17', '09:30:00');
INSERT INTO HMS.Appointment VALUES (37, 'P000005', 'D100015', '2024-12-18', '10:00:00');
INSERT INTO HMS.Appointment VALUES (38, 'P000006', 'D100016', '2024-12-18', '10:30:00');
INSERT INTO HMS.Appointment VALUES (39, 'P000007', 'D100017', '2024-12-19', '11:00:00');
INSERT INTO HMS.Appointment VALUES (40, 'P000008', 'D100018', '2024-12-19', '11:30:00');
INSERT INTO HMS.Appointment VALUES (41, 'P000009', 'D100019', '2024-12-20', '12:00:00');
INSERT INTO HMS.Appointment VALUES (42, 'P000010', 'D100020', '2024-12-20', '12:30:00');
INSERT INTO HMS.Appointment VALUES (43, 'P000011', 'D100001', '2024-12-21', '13:00:00');
INSERT INTO HMS.Appointment VALUES (44, 'P000012', 'D100002', '2024-12-21', '13:30:00');
INSERT INTO HMS.Appointment VALUES (45, 'P000013', 'D100003', '2024-12-22', '14:00:00');
INSERT INTO HMS.Appointment VALUES (46, 'P000014', 'D100004', '2024-12-22', '14:30:00');
INSERT INTO HMS.Appointment VALUES (47, 'P000015', 'D100005', '2024-12-23', '15:00:00');
INSERT INTO HMS.Appointment VALUES (48, 'P000016', 'D100006', '2024-12-23', '15:30:00');
INSERT INTO HMS.Appointment VALUES (49, 'P000017', 'D100007', '2024-12-24', '16:00:00');
INSERT INTO HMS.Appointment VALUES (50, 'P000018', 'D100008', '2024-12-24', '16:30:00');
INSERT INTO HMS.Appointment VALUES (51, 'P000019', 'D100009', '2024-12-25', '17:00:00');
INSERT INTO HMS.Appointment VALUES (52, 'P000020', 'D100010', '2024-12-25', '17:30:00');



CREATE TABLE HMS.Pharmacy (
    pharmacyID CHAR(2),
    pharmacyName VARCHAR(50),
    
    PRIMARY KEY (pharmacyID)
);
INSERT INTO HMS.Pharmacy VALUES ('01', 'City Pharmacy');
INSERT INTO HMS.Pharmacy VALUES ('02', 'Green Leaf Pharmacy');
INSERT INTO HMS.Pharmacy VALUES ('03', 'Wellness Pharmacy');

CREATE TABLE HMS.Medicine (
    medicineID CHAR(11),
    medicineName VARCHAR(50),
    dosage VARCHAR(1000),
    pharmacyID CHAR(2) NOT NULL,
    
    PRIMARY KEY (medicineID),
    FOREIGN KEY (pharmacyID) REFERENCES Pharmacy (pharmacyID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO HMS.Medicine VALUES ('M000000001', 'Paracetamol', '500mg, Take 1 tablet every 6 hours', '01');
INSERT INTO HMS.Medicine VALUES ('M000000002', 'Aspirin', '100mg, Take 1 tablet once daily', '01');
INSERT INTO HMS.Medicine VALUES ('M000000003', 'Ibuprofen', '200mg, Take 1 tablet every 4-6 hours', '01');
INSERT INTO HMS.Medicine VALUES ('M000000004', 'Amoxicillin', '500mg, Take 1 capsule twice daily', '01');
INSERT INTO HMS.Medicine VALUES ('M000000005', 'Cetirizine', '10mg, Take 1 tablet daily', '01');
INSERT INTO HMS.Medicine VALUES ('M000000006', 'Metformin', '500mg, Take 1 tablet twice daily with meals', '02');
INSERT INTO HMS.Medicine VALUES ('M000000007', 'Lisinopril', '10mg, Take 1 tablet once daily', '02');
INSERT INTO HMS.Medicine VALUES ('M000000008', 'Losartan', '50mg, Take 1 tablet once daily', '02');
INSERT INTO HMS.Medicine VALUES ('M000000009', 'Prednisone', '5mg, Take 1 tablet daily for 5 days', '02');
INSERT INTO HMS.Medicine VALUES ('M000000010', 'Atorvastatin', '20mg, Take 1 tablet at night', '02');
INSERT INTO HMS.Medicine VALUES ('M000000011', 'Clindamycin', '300mg, Take 1 capsule 3 times daily', '03');
INSERT INTO HMS.Medicine VALUES ('M000000012', 'Metronidazole', '500mg, Take 1 tablet twice daily', '03');
INSERT INTO HMS.Medicine VALUES ('M000000013', 'Hydrochlorothiazide', '25mg, Take 1 tablet daily', '03');
INSERT INTO HMS.Medicine VALUES ('M000000014', 'Simvastatin', '40mg, Take 1 tablet before bedtime', '03');
INSERT INTO HMS.Medicine VALUES ('M000000015', 'Alprazolam', '0.5mg, Take 1 tablet 3 times daily', '01');
INSERT INTO HMS.Medicine VALUES ('M000000016', 'Diphenhydramine', '25mg, Take 1 tablet before bed', '01');
INSERT INTO HMS.Medicine VALUES ('M000000017', 'Doxycycline', '100mg, Take 1 tablet twice daily', '02');
INSERT INTO HMS.Medicine VALUES ('M000000018', 'Gabapentin', '300mg, Take 1 tablet three times a day', '02');
INSERT INTO HMS.Medicine VALUES ('M000000019', 'Omeprazole', '20mg, Take 1 tablet before breakfast', '03');
INSERT INTO HMS.Medicine VALUES ('M000000020', 'Levothyroxine', '50mcg, Take 1 tablet in the morning', '03');

CREATE TABLE HMS.Payment_Approach (
    PAID CHAR(4),    
    PRIMARY KEY (PAID)
);

INSERT INTO HMS.Payment_Approach VALUES ('C001');
INSERT INTO HMS.Payment_Approach VALUES ('C002');
INSERT INTO HMS.Payment_Approach VALUES ('C003');
INSERT INTO HMS.Payment_Approach VALUES ('B001');
INSERT INTO HMS.Payment_Approach VALUES ('B002');
INSERT INTO HMS.Payment_Approach VALUES ('B003');
INSERT INTO HMS.Payment_Approach VALUES ('E001');
INSERT INTO HMS.Payment_Approach VALUES ('E002');
INSERT INTO HMS.Payment_Approach VALUES ('E003');

CREATE TABLE HMS.Cash (
    cashierID CHAR(3),
    cashierName	VARCHAR(50),
    PAID CHAR(4) NOT NULL,
    
    PRIMARY KEY (cashierID),
    FOREIGN KEY (PAID) REFERENCES Payment_Approach (PAID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO HMS.Cash VALUES ('001', 'John Doe', 'C001');
INSERT INTO HMS.Cash VALUES ('002', 'Alice Smith', 'C002');
INSERT INTO HMS.Cash VALUES ('003', 'Bob Johnson', 'C003');

CREATE TABLE HMS.Bank (
    bankID CHAR(3),
    bankName VARCHAR(50),
    PAID CHAR(4) NOT NULL,
    
    PRIMARY KEY (bankID),
    FOREIGN KEY (PAID) REFERENCES Payment_Approach (PAID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO HMS.Bank VALUES ('001', 'City Bank', 'B001');
INSERT INTO HMS.Bank VALUES ('002', 'Green Valley Bank', 'B002');
INSERT INTO HMS.Bank VALUES ('003', 'Trust Bank', 'B003');

CREATE TABLE HMS.Ewallet (
    ewalletID CHAR(3),
    ewalletName	VARCHAR(50),
    PAID CHAR(4) NOT NULL,
    
    PRIMARY KEY (ewalletID),
    FOREIGN KEY (PAID) REFERENCES Payment_Approach (PAID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO HMS.Ewallet VALUES ('001', 'PayPal', 'E001');
INSERT INTO HMS.Ewallet VALUES ('002', 'Venmo', 'E001');
INSERT INTO HMS.Ewallet VALUES ('003', 'Google Pay', 'E001');

CREATE TABLE HMS.Bill (
    billID INT,
    patientID CHAR(7) NOT NULL,
    amount INT UNSIGNED,
    createdDate	DATE,
    paymentStatus BOOLEAN,
    PAID CHAR(4),
    paidDate DATE,
    
    PRIMARY KEY (billID),
    FOREIGN KEY (patientID) REFERENCES Patient (patientID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (PAID) REFERENCES Payment_Approach (PAID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO HMS.Bill VALUES (1, 'P000001', 150, '2024-12-29', TRUE, 'C002', '2024-11-29');
INSERT INTO HMS.Bill VALUES (2, 'P000002', 200, '2024-11-28', FALSE, 'B003', NULL);
INSERT INTO HMS.Bill VALUES (3, 'P000003', 350, '2024-11-27', TRUE, 'E001', '2024-11-27');
INSERT INTO HMS.Bill VALUES (4, 'P000004', 500, '2024-11-26', FALSE, 'C003', NULL);
INSERT INTO HMS.Bill VALUES (5, 'P000005', 250, '2024-11-25', TRUE, 'B001', '2024-11-25');

CREATE TABLE HMS.Treatment (
    treatmentID INT,
    patientID CHAR(7) NOT NULL,
    treatmentDate DATE,
    treatmentProcedure VARCHAR(1000),
    
    PRIMARY KEY (treatmentID),
    FOREIGN KEY (patientID) REFERENCES Patient (patientID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO HMS.Treatment (treatmentID, patientID, treatmentDate, treatmentProcedure)
VALUES
(1, 'P000001', '2024-11-01', 'X-ray for chest examination'),
(2, 'P000002', '2024-11-02', 'Blood test for diabetes screening'),
(3, 'P000003', '2024-11-03', 'MRI for knee injury'),
(4, 'P000004', '2024-11-04', 'ECG for heart health check-up'),
(5, 'P000005', '2024-11-05', 'Ultrasound for abdominal pain'),
(6, 'P000006', '2024-11-06', 'Endoscopy for gastrointestinal examination'),
(7, 'P000007', '2024-11-07', 'X-ray for fractured arm'),
(8, 'P000008', '2024-11-08', 'CT scan for head trauma'),
(9, 'P000009', '2024-11-09', 'Blood test for cholesterol level'),
(10, 'P000010', '2024-11-10', 'Physical therapy for back pain'),
(11, 'P000011', '2024-11-11', 'Skin test for allergy detection'),
(12, 'P000012', '2024-11-12', 'Blood pressure monitoring'),
(13, 'P000013', '2024-11-13', 'MRI for ankle sprain assessment'),
(14, 'P000014', '2024-11-14', 'Blood test for anemia diagnosis'),
(15, 'P000015', '2024-11-15', 'Eye examination for vision test'),
(16, 'P000016', '2024-11-16', 'Urine test for infection screening'),
(17, 'P000017', '2024-11-17', 'Pulmonary function test for asthma evaluation'),
(18, 'P000018', '2024-11-18', 'CT scan for kidney stone detection'),
(19, 'P000019', '2024-11-19', 'Symptom-based diagnosis for migraine treatment'),
(20, 'P000020', '2024-11-20', 'Colonoscopy for gastrointestinal health check'),
(21, 'P000021', '2024-11-21', 'Chest X-ray for pneumonia diagnosis'),
(22, 'P000022', '2024-11-22', 'Blood test for thyroid function assessment'),
(23, 'P000023', '2024-11-23', 'Bone density scan for osteoporosis evaluation'),
(24, 'P000024', '2024-11-24', 'CT scan for sinus infection analysis'),
(25, 'P000025', '2024-11-25', 'Audiometry test for hearing evaluation'),
(26, 'P000026', '2024-11-26', 'Endoscopy for acid reflux examination'),
(27, 'P000027', '2024-11-27', 'Comprehensive evaluation for chronic fatigue syndrome'),
(28, 'P000028', '2024-11-28', 'X-ray for clavicle fracture diagnosis'),
(29, 'P000029', '2024-11-29', 'Blood test for diabetes confirmation'),
(30, 'P000030', '2024-11-30', 'Allergy test for skin rash diagnosis');


CREATE TABLE HMS.Medical_Record (
    recordID INT,
    patientID CHAR(7) NOT NULL,
    recordDate DATE,
    treatmentID	INT NOT NULL,
    diagnosis VARCHAR(1000),
    testResult VARCHAR(1000),
    
    PRIMARY KEY (patientID, recordID),
    FOREIGN KEY (patientID) REFERENCES Patient (patientID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (treatmentID) REFERENCES Treatment (treatmentID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO HMS.Medical_Record (recordID, patientID, recordDate, treatmentID, diagnosis, testResult)
VALUES
(1, 'P000001', '2024-11-02', 1, 'Normal chest X-ray', 'No abnormalities detected'),
(2, 'P000002', '2024-11-03', 2, 'Pre-diabetes', 'Blood sugar levels elevated'),
(3, 'P000003', '2024-11-04', 3, 'Torn meniscus', 'MRI confirmed damage'),
(4, 'P000004', '2024-11-05', 4, 'Normal ECG', 'No irregular heartbeats'),
(5, 'P000005', '2024-11-06', 5, 'No significant findings', 'Ultrasound showed no issues'),
(6, 'P000006', '2024-11-07', 6, 'Gastritis', 'Endoscopy revealed inflammation'),
(7, 'P000007', '2024-11-08', 7, 'Fractured radius', 'X-ray confirmed fracture'),
(8, 'P000008', '2024-11-09', 8, 'Concussion', 'CT scan showed mild brain injury'),
(9, 'P000009', '2024-11-10', 9, 'High cholesterol', 'Blood test showed elevated levels'),
(10, 'P000010', '2024-11-11', 10, 'Chronic back pain', 'Physical therapy recommended'),
(11, 'P000011', '2024-11-12', 11, 'Seasonal allergy', 'Skin test confirmed pollen allergy'),
(12, 'P000012', '2024-11-13', 12, 'Hypertension', 'Blood pressure consistently elevated'),
(13, 'P000013', '2024-11-14', 13, 'Sprained ankle', 'MRI showed ligament strain'),
(14, 'P000014', '2024-11-15', 14, 'Mild anemia', 'Blood test showed low hemoglobin'),
(15, 'P000015', '2024-11-16', 15, 'Normal vision', 'Eye test results within normal range'),
(16, 'P000016', '2024-11-17', 16, 'Urinary tract infection', 'Urine test confirmed bacteria'),
(17, 'P000017', '2024-11-18', 17, 'Asthma', 'Pulmonary function test showed reduced airflow'),
(18, 'P000018', '2024-11-19', 18, 'Kidney stones', 'CT scan confirmed presence of stones'),
(19, 'P000019', '2024-11-20', 19, 'Migraine', 'Diagnosis based on symptom assessment'),
(20, 'P000020', '2024-11-21', 20, 'Normal colonoscopy', 'No polyps or abnormalities found'),
(21, 'P000021', '2024-11-22', 21, 'Pneumonia', 'Chest X-ray confirmed lung infection'),
(22, 'P000022', '2024-11-23', 22, 'Hyperthyroidism', 'Blood test showed elevated T4 levels'),
(23, 'P000023', '2024-11-24', 23, 'Osteoporosis', 'Bone density scan confirmed diagnosis'),
(24, 'P000024', '2024-11-25', 24, 'Sinus infection', 'CT scan showed sinus inflammation'),
(25, 'P000025', '2024-11-26', 25, 'Normal hearing', 'Audiometry test results normal'),
(26, 'P000026', '2024-11-27', 26, 'Acid reflux', 'Endoscopy confirmed esophageal irritation'),
(27, 'P000027', '2024-11-28', 27, 'Chronic fatigue', 'Diagnosis based on symptom evaluation'),
(28, 'P000028', '2024-11-29', 28, 'Broken clavicle', 'X-ray confirmed fracture'),
(29, 'P000029', '2024-11-30', 29, 'Diabetes type 2', 'Blood sugar levels above threshold'),
(30, 'P000030', '2024-12-01', 30, 'Skin rash', 'Allergy test confirmed contact dermatitis');


CREATE TABLE HMS.Performs (
    doctorID CHAR(7) NOT NULL,
    treatmentID	INT NOT NULL,
    
    PRIMARY KEY (doctorID, treatmentID),
    FOREIGN KEY (doctorID) REFERENCES Doctor (doctorID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (treatmentID) REFERENCES Treatment (treatmentID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO HMS.Performs (doctorID, treatmentID)
VALUES
('D100001', 1),
('D100002', 2),
('D100003', 3),
('D100004', 4),
('D100005', 5),
('D100006', 6),
('D100007', 7),
('D100008', 8),
('D100009', 9),
('D100010', 10);


CREATE TABLE HMS.Assists (
    nurseID	CHAR(7) NOT NULL,
    treatmentID	INT	NOT NULL,
    
    PRIMARY KEY (nurseID, treatmentID),
    FOREIGN KEY (nurseID) REFERENCES Nurse (nurseID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (treatmentID) REFERENCES Treatment (treatmentID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO HMS.Assists (nurseID, treatmentID)
VALUES
('N100001', 1),
('N100002', 2),
('N100003', 3),
('N100004', 4),
('N100005', 5),
('N100006', 6),
('N100007', 7),
('N100008', 8),
('N100009', 9),
('N100010', 10);

CREATE TABLE HMS.Takes_care (
    nurseID	CHAR(7)	NOT NULL,
    roomID CHAR(3) NOT NULL,
    
    PRIMARY KEY (nurseID, roomID),
    FOREIGN KEY (nurseID) REFERENCES Nurse (nurseID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (roomID) REFERENCES Room (roomID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO HMS.Takes_care (nurseID, roomID) 
VALUES
('N100001', '101'),
('N100002', '102'),
('N100003', '103'),
('N100004', '104'),
('N100005', '105'),
('N100006', '106'),
('N100007', '107'),
('N100008', '108'),
('N100009', '109'),
('N100010', '110');



CREATE TABLE HMS.Prescribes (
    medicineID CHAR(11)	NOT NULL,
    patientID CHAR(7) NOT NULL,
    doctorID CHAR(7) NOT NULL,
    prescribesDate DATE,
    
    PRIMARY KEY (patientID, medicineID, doctorID),
    FOREIGN KEY (patientID) REFERENCES Patient (patientID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (doctorID) REFERENCES Doctor (doctorID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (medicineID) REFERENCES Medicine (medicineID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO HMS.Prescribes (medicineID, patientID, doctorID, prescribesDate)
VALUES
('M000000001', 'P000001', 'D100001', '2024-11-01'),
('M000000002', 'P000002', 'D100002', '2024-11-02'),
('M000000003', 'P000003', 'D100003', '2024-11-03'),
('M000000004', 'P000004', 'D100004', '2024-11-04'),
('M000000005', 'P000005', 'D100005', '2024-11-05'),
('M000000006', 'P000006', 'D100006', '2024-11-06'),
('M000000007', 'P000007', 'D100007', '2024-11-07'),
('M000000008', 'P000008', 'D100008', '2024-11-08'),
('M000000009', 'P000009', 'D100009', '2024-11-09'),
('M000000010', 'P000010', 'D100010', '2024-11-10');


DROP ROLE IF EXISTS admin_role, doctor_role, nurse_role, receptionist_role, patient_role;

CREATE ROLE 'admin_role';
GRANT ALL PRIVILEGES ON HMS.* TO 'admin_role';

CREATE ROLE 'doctor_role';
GRANT SELECT, INSERT, UPDATE, DELETE ON HMS.Appointment TO 'doctor_role';
GRANT SELECT, INSERT, UPDATE, DELETE ON HMS.Medical_Record TO 'doctor_role';
GRANT SELECT, INSERT, UPDATE, DELETE ON HMS.Treatment TO 'doctor_role';
GRANT SELECT, INSERT, UPDATE, DELETE ON HMS.Prescribes TO 'doctor_role';
GRANT SELECT ON HMS.Patient TO 'doctor_role';
GRANT SELECT ON HMS.Doctor TO 'doctor_role';
GRANT SELECT ON HMS.Nurse TO 'doctor_role';
GRANT SELECT ON HMS.Room TO 'doctor_role';
GRANT SELECT ON HMS.Admitted_to TO 'doctor_role';
GRANT SELECT ON HMS.Medicine TO 'doctor_role';

CREATE ROLE 'nurse_role';
GRANT SELECT, UPDATE ON HMS.Patient TO 'nurse_role';
GRANT SELECT ON HMS.Room TO 'nurse_role';
GRANT SELECT ON HMS.Admitted_to TO 'nurse_role';
GRANT SELECT ON HMS.Treatment TO 'nurse_role';
GRANT SELECT ON HMS.Prescribes TO 'nurse_role';

CREATE ROLE 'receptionist_role';
GRANT SELECT, INSERT, UPDATE, DELETE ON HMS.Patient TO 'receptionist_role';
GRANT SELECT, INSERT, UPDATE, DELETE ON HMS.Patients_Family TO 'receptionist_role';
GRANT SELECT, INSERT, UPDATE, DELETE ON HMS.Appointment TO 'receptionist_role';
GRANT SELECT, INSERT, UPDATE, DELETE ON HMS.Admitted_to TO 'receptionist_role';
GRANT SELECT, INSERT, UPDATE, DELETE ON HMS.Bill TO 'receptionist_role';

CREATE ROLE 'patient_role';
CREATE VIEW HMS.Patient_View AS
    SELECT * FROM HMS.Patient WHERE patientID = SUBSTRING_INDEX(USER(), '@', 1);
CREATE VIEW HMS.Patients_Family_View AS
    SELECT * FROM HMS.Patients_Family WHERE patientID = SUBSTRING_INDEX(USER(), '@', 1);
CREATE VIEW HMS.Appointment_View AS
    SELECT * FROM HMS.Appointment WHERE patientID = SUBSTRING_INDEX(USER(), '@', 1);
CREATE VIEW HMS.Medical_Record_View AS
    SELECT * FROM HMS.Medical_Record WHERE patientID = SUBSTRING_INDEX(USER(), '@', 1);
CREATE VIEW HMS.Prescribes_View AS
    SELECT * FROM HMS.Prescribes WHERE patientID = SUBSTRING_INDEX(USER(), '@', 1);
CREATE VIEW HMS.Bill_View AS
    SELECT * FROM HMS.Bill WHERE patientID = SUBSTRING_INDEX(USER(), '@', 1);
GRANT SELECT ON HMS.Patient_View TO 'patient_role';
GRANT SELECT ON HMS.Patients_Family_View TO 'patient_role';
GRANT SELECT ON HMS.Appointment_View TO 'patient_role';
GRANT SELECT ON HMS.Medical_Record_View TO 'patient_role';
GRANT SELECT ON HMS.Prescribes_View TO 'patient_role';
GRANT SELECT ON HMS.Bill_View TO 'patient_role';

FLUSH PRIVILEGES;

-- FUNCTION

DELIMITER $$

CREATE FUNCTION HMS.GetPatientCountAtRoom(roomIDInput CHAR(3))
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE patientCount INT;

    -- Calculate the number of patients currently in the room
    SELECT 
        COUNT(patientID) 
    INTO 
        patientCount
    FROM 
        HMS.Admitted_to
    WHERE 
        roomID = roomIDInput 
        AND admittedDate <= NOW()
        AND (dischargedDate > NOW() OR dischargedDate IS NULL);

    RETURN patientCount;
END$$

DELIMITER ;

DELIMITER $$

CREATE FUNCTION getRoomIDByPatientID(inPatientID CHAR(7))
RETURNS CHAR(3)
DETERMINISTIC
BEGIN
    DECLARE roomID CHAR(3);

    SELECT a.roomID
    INTO roomID
    FROM HMS.Admitted_to a
    WHERE a.patientID = inPatientID
      AND CURRENT_DATE BETWEEN a.admittedDate AND a.dischargedDate
    LIMIT 1;

    RETURN roomID;
END $$

DELIMITER ;

DELIMITER $$

CREATE FUNCTION HMS.GetDoctorCountInDepartment(departmentNameInput VARCHAR(50))
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE doctorCount INT;

    -- Calculate the number of doctor in the department
    SELECT COUNT(*)
    INTO doctorCount
    FROM HMS.Medical_Staff, HMS.Department
    WHERE departmentName = departmentNameInput AND Medical_Staff.departmentID = Department.departmentID AND staffID LIKE 'D%';
    RETURN doctorCount;
END$$

DELIMITER ;

DELIMITER $$

CREATE FUNCTION HMS.GetNurseCountInDepartment(departmentNameInput VARCHAR(50))
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE nurseCount INT;

    -- Calculate the number of doctor in the department
    SELECT COUNT(*)
    INTO nurseCount
    FROM HMS.Medical_Staff, HMS.Department
    WHERE departmentName = departmentNameInput AND Medical_Staff.departmentID = Department.departmentID AND staffID LIKE 'N%';
    RETURN nurseCount;
END$$

DELIMITER ;

DELIMITER $$

CREATE FUNCTION GetPatientIDByName(
    inFirstName VARCHAR(20), 
    inMidName VARCHAR(50), 
    inLastName VARCHAR(20)
) RETURNS CHAR(7)
DETERMINISTIC
BEGIN
    DECLARE patientID CHAR(7);

    SELECT p.patientID 
    INTO patientID
    FROM HMS.Patient p
    WHERE p.firstName = inFirstName 
      AND (p.midName = inMidName OR (inMidName IS NULL AND p.midName IS NULL))
      AND p.lastName = inLastName
    LIMIT 1;

    RETURN patientID;
END $$

DELIMITER ;







-- PROCEDURE

DELIMITER $$

CREATE PROCEDURE HMS.CountMedicalStaffGroupbyDepartment()
BEGIN
    SELECT 
        Department.departmentName, 
        SUM(CASE WHEN Medical_Staff.staffID LIKE 'D%' THEN 1 ELSE 0 END) AS numberDoctor,
        SUM(CASE WHEN Medical_Staff.staffID LIKE 'N%' THEN 1 ELSE 0 END) AS numberNurse
    FROM HMS.Medical_Staff
    JOIN HMS.Department ON Medical_Staff.departmentID = Department.departmentID
    GROUP BY Department.departmentName;
END$$

DELIMITER ;


DELIMITER $$

CREATE PROCEDURE HMS.GetDoctorInDepartment(departmentNameInput VARCHAR(50))
BEGIN
    SELECT staffID, firstName, midName, lastName, gender, staffDoB, phoneNumber, salary, departmentName 
    FROM HMS.Medical_Staff, HMS.Department
    WHERE departmentName = departmentNameInput AND Medical_Staff.departmentID = Department.departmentID AND staffID LIKE 'D%';
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE HMS.GetNurseInDepartment(departmentNameInput VARCHAR(50))
BEGIN
    SELECT staffID, firstName, midName, lastName, gender, staffDoB, phoneNumber, salary, departmentName 
    FROM HMS.Medical_Staff, HMS.Department
    WHERE departmentName = departmentNameInput AND Medical_Staff.departmentID = Department.departmentID AND staffID LIKE 'N%';
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE HMS.GetPatientCountInRoomAtDate(atDate DATE)
BEGIN
    SELECT 
        a.roomID, 
        COUNT(patientID) AS patientCount,
        capacity
    FROM HMS.Admitted_to a, HMS.Room r
    WHERE a.roomID = r.roomID
		AND admittedDate <= atDate 
		AND (dischargedDate > atDate OR dischargedDate IS NULL)
    GROUP BY a.roomID
	ORDER BY a.roomID;
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE ShowDoctorAppointments(IN doctorIDInput CHAR(7))
BEGIN
    SELECT 
        appointmentID,
        patientID,
        doctorID,
        appointmentDate,
        appointmentTime
    FROM HMS.Appointment
    WHERE doctorID = doctorIDInput
    ORDER BY appointmentDate, appointmentTime;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE ShowPatientAppointments(IN patientIDInput CHAR(7))
BEGIN
    SELECT 
        appointmentID,
        patientID,
        doctorID,
        appointmentDate,
        appointmentTime
    FROM HMS.Appointment
    WHERE patientID = patientIDInput
    ORDER BY appointmentDate, appointmentTime;
END $$

DELIMITER ;


-- TRIGGER

DELIMITER $$

CREATE TRIGGER HMS.CheckRoomCapacity
BEFORE INSERT ON HMS.Admitted_to
FOR EACH ROW
BEGIN
    DECLARE currentCount INT;
    DECLARE roomCapacity INT;

    -- Get the current number of patients in the room
    SELECT COUNT(patientID)
    INTO currentCount
    FROM HMS.Admitted_to
    WHERE roomID = NEW.roomID 
      AND admittedDate <= NEW.admittedDate 
      AND (dischargedDate > NEW.admittedDate OR dischargedDate IS NULL);

    -- Get the room's capacity
    SELECT capacity
    INTO roomCapacity
    FROM HMS.Room
    WHERE roomID = NEW.roomID;

    -- Check if adding the new patient exceeds the capacity
    IF currentCount >= roomCapacity THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Room capacity exceeded';
    END IF;
END$$

DELIMITER ;



DELIMITER $$

CREATE TRIGGER HMS.EnsureUniqueRoomForPatient
BEFORE INSERT ON HMS.Admitted_to
FOR EACH ROW
BEGIN
    DECLARE overlappingAdmissions INT;

    -- Check if the patient is already admitted to another room during the new admission period
    SELECT 
        COUNT(*)
    INTO 
        overlappingAdmissions
    FROM 
        HMS.Admitted_to
    WHERE 
        patientID = NEW.patientID
        AND (
            (NEW.admittedDate BETWEEN admittedDate AND IFNULL(dischargedDate, NOW())) -- Overlap with an existing admission
            OR (admittedDate BETWEEN NEW.admittedDate AND IFNULL(NEW.dischargedDate, NOW()))
        );

    -- If overlapping admissions exist, raise an error
    IF overlappingAdmissions > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Patient is already admitted to another room during this time period';
    END IF;
END$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER BeforeInsertDoctorManages
BEFORE INSERT ON HMS.Manages
FOR EACH ROW
BEGIN
    DECLARE existingCount INT;

    -- Check if the doctor already manages another department
    SELECT COUNT(*)
    INTO existingCount
    FROM HMS.Manages
    WHERE doctorID = NEW.doctorID;

    IF existingCount > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'A doctor can only manage one department.';
    END IF;
END$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER BeforeUpdateDoctorManages
BEFORE UPDATE ON HMS.Manages
FOR EACH ROW
BEGIN
    DECLARE existingCount INT;

    -- Check if the doctor already manages another department
    SELECT COUNT(*)
    INTO existingCount
    FROM HMS.Manages
    WHERE doctorID = NEW.doctorID AND departmentID != OLD.departmentID;

    IF existingCount > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'A doctor can only manage one department.';
    END IF;
END$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER Prevent_HeadDoctor_Delete
BEFORE DELETE ON Doctor
FOR EACH ROW
BEGIN
    -- Check if the doctor being deleted is managing a department
    IF EXISTS (SELECT 1 FROM Manages WHERE doctorID = OLD.doctorID) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot delete a doctor who is currently managing a department.';
    END IF;
END$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER HMS.EnsureDoctorAvailability
BEFORE INSERT ON HMS.Appointment
FOR EACH ROW
BEGIN
    DECLARE conflictingCount INT;

    -- Check if the doctor already has an overlapping appointment
    SELECT 
        COUNT(*)
    INTO 
        conflictingCount
    FROM 
        HMS.Appointment
    WHERE 
        doctorID = NEW.doctorID
        AND appointmentDate = NEW.appointmentDate
        AND (
            (NEW.appointmentTime >= appointmentTime AND NEW.appointmentTime < ADDTIME(appointmentTime, '00:10:00')) 
            OR 
            (ADDTIME(NEW.appointmentTime, '00:10:00') > appointmentTime AND ADDTIME(NEW.appointmentTime, '00:10:00') <= ADDTIME(appointmentTime, '00:10:00'))
        );

    -- If there is a conflict, raise an error
    IF conflictingCount > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'A doctor can be scheduled for at most one appointment every 10 minutes.';
    END IF;
END$$

DELIMITER ;

DELIMITER $$


CREATE TRIGGER HMS.EnsurePatientAvailability
BEFORE INSERT ON HMS.Appointment
FOR EACH ROW
BEGIN
    DECLARE overlappingAppointments INT;

    -- Check if there are any overlapping appointments for the patient
    SELECT 
        COUNT(*)
    INTO 
        overlappingAppointments
    FROM 
        HMS.Appointment
    WHERE 
        patientID = NEW.patientID
        AND appointmentDate = NEW.appointmentDate
        AND (
            (NEW.appointmentTime BETWEEN appointmentTime AND ADDTIME(appointmentTime, '00:30:00'))
            OR (appointmentTime BETWEEN NEW.appointmentTime AND ADDTIME(NEW.appointmentTime, '00:30:00'))
        );

    -- If overlapping appointments exist, raise an error
    IF overlappingAppointments > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Patient is already scheduled for another appointment at this time';
    END IF;
END$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER EnsureFutureAppointment
BEFORE INSERT ON HMS.Appointment
FOR EACH ROW
BEGIN
    -- Check if the appointment date and time are in the future
    IF NEW.appointmentDate < CURDATE() OR 
       (NEW.appointmentDate = CURDATE() AND NEW.appointmentTime <= CURTIME()) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Appointment date and time must be in the future.';
    END IF;
END$$

DELIMITER ;


