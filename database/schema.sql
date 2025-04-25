CREATE TABLE submissions (
    id SERIAL PRIMARY KEY,
    student_id VARCHAR(64),
    submission_text TEXT,
    score INTEGER,
    feedback TEXT,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
