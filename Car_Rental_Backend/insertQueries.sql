-- Delete rows if already exits
DELETE FROM Customer;
DELETE FROM Owner;
DELETE FROM Car;
DELETE FROM Availability;

-- Insert into Customer table
INSERT INTO Customer (customerID, name, phone, customerType) VALUES
(1,'J.Doe','123-456-7890','Business'),
(2,'J.Smith','987-654-3210','Individual'),
(3,'M.Brown','555-555-5555','Business'),
(4,'E.Johnson','111-222-3333','Individual'),
(5,'D.Lee','444-555-6666','Business'),
(6,'O.Taylor','777-888-9999','Individual'),
(7,'S.Anderson','333-444-5555','Individual'),
(8,'D.Martinez','666-777-8888','Business'),
(9,'E.Wilson','111-111-1111','Individual'),
(10,'A.Harris','222-222-2222','Business');

-- Insert into Owner table
INSERT INTO Owner (Id, name, ownerType) VALUES
  (1, 'John Smith', 'Rental'),
  (2, 'Jane Brown', 'Bank'),
  (3, 'Michael Johnson', 'Individual'),
  (4, 'Emily Davis', 'Rental'),
  (5, 'David Wilson', 'Individual'),
  (6, 'Olivia Taylor', 'Bank'),
  (7, 'Sophia Anderson', 'Rental'),
  (8, 'Daniel Martinez', 'Individual'),
  (9, 'Emma Thompson', 'Bank'),
  (10, 'Alexander Harris', 'Rental');

-- Insert into Car table
INSERT INTO Car (vehicleID, ownerId, model, year, location, carType, carCategory, dailyRate, weeklyRate) VALUES
(1, 1, 'Honda Civic', 2018, 'New York', 'Compact', 'Regular',  30.00, 150.00),
(2, 2, 'Corolla', 2019, 'San Francisco', 'Compact', 'Regular',  30.00, 150.00),
(3, 3, 'Camry', 2020, 'Los Angeles', 'Compact', 'Luxury',  36.00, 180.00),
(4, 4, 'A4', 2017, 'Chicago', 'Compact', 'Luxury', 36.00, 180.00),
(5, 5, 'Model S', 2019, 'San Francisco', 'Truck', 'Luxury',  100.00, 600.00),
(6, 1, 'GT-R', 2020, 'Miami', 'Van', 'Regular',  70.00, 450.00),
(7, 2, 'Q7', 2018, 'New York', 'SUV', 'Luxury',  72.00, 476.00),
(8, 3, 'CX-5', 2019, 'Los Angeles', 'SUV', 'Regular',  60.00, 380.00),
(9, 4, 'Model Y', 2020, 'San Francisco', 'Compact', 'Luxury', 36.00, 180.00),
(10, 5, 'Cherokee', 2019, 'Las Vegas', 'Large', 'Regular', 50.00, 350.00);

-- Insert into Availability table
INSERT INTO Availability (carID, avaliabilityID, startDate, endDate) VALUES
(1,1,'2023-05-01', '2023-05-05'),
(2,1,'2023-05-10', '2023-05-15'),
(3,1,'2023-05-01', '2023-05-05'),
(4,1,'2023-05-10', '2023-05-15'),
(5,1,'2023-05-01', '2023-05-05'),
(6,1,'2023-05-10', '2023-05-15'),
(7,1,'2023-05-01', '2023-05-05'),
(8,1,'2023-05-10', '2023-05-15'),
(9,1,'2023-05-01', '2023-05-05'),
(10,1,'2023-05-10', '2023-05-15');


