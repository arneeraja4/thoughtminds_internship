CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credits INT
);

CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    
    CONSTRAINT fk_student
        FOREIGN KEY (student_id)
        REFERENCES Students(student_id),

    CONSTRAINT fk_course
        FOREIGN KEY (course_id)
        REFERENCES Courses(course_id)
);
-- Students
INSERT INTO students (name, email)
VALUES
('Neeraja', 'neeraja@gmail.com'),
('Anu', 'anu@gmail.com'),
('Rahul', 'rahul@gmail.com');

-- Courses
INSERT INTO courses (course_name, credits)
VALUES
('Database Management', 4),
('Python Programming', 3),
('Artificial Intelligence', 4);


INSERT INTO enrollments (student_id, course_id, enrollment_date)
VALUES
(1, 1, '2026-06-24'),
(1, 2, '2026-06-24'),
(2, 3, '2026-06-24'),
(3, 1, '2026-06-24');

SELECT s.student_id, s.name,c.course_name,e.enrollment_date FROM enrollments e JOIN students s ON e.student_id = s.student_id JOIN courses c ON e.course_id = c.course_id;