CREATE DATABASE hostel_management;
USE hostel_management;

CREATE TABLE students (
    student_id VARCHAR(20) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    father_name VARCHAR(50),
    mother_name VARCHAR(50),
    dob DATE,
    contact VARCHAR(15) UNIQUE NOT NULL,
    email VARCHAR(100),
    address TEXT,
    room_no VARCHAR(10),
    gender ENUM('Male', 'Female', 'Other'),
    date_added DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE rooms (
    room_number VARCHAR(10) PRIMARY KEY,  -- Unique Room Number
    gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Gender of occupants
    date_added DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE in_out_time (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(20) NOT NULL,
    action ENUM('IN', 'OUT') NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE visitors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    visitor_name VARCHAR(100) NOT NULL,
    visitor_contact VARCHAR(15),
    reason TEXT,
    student_id VARCHAR(20) NOT NULL,
    date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE leave_applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(20) NOT NULL,
    reason TEXT NOT NULL,
    return_date DATE,
    date_added DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

select * from students;
select * from rooms;
select * from in_out_time;
select * from visitors;
select * from leave_applications;