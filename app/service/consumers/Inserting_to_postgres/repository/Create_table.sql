-- Create table for 'email'
CREATE TABLE email (
    id SERIAL PRIMARY KEY,
    email VARCHAR NOT NULL UNIQUE,
    username VARCHAR NOT NULL,
    ip_address VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for 'location'
CREATE TABLE location (
    id SERIAL PRIMARY KEY,
    latitude VARCHAR NOT NULL,
    longitude VARCHAR NOT NULL,
    city VARCHAR NOT NULL,
    country VARCHAR NOT NULL,
    email_id INTEGER NOT NULL,
    FOREIGN KEY (email_id) REFERENCES email (id) ON DELETE CASCADE
);

-- Create table for 'device_info'
CREATE TABLE device_info (
    id SERIAL PRIMARY KEY,
    browser VARCHAR NOT NULL,
    os VARCHAR NOT NULL,
    device_id VARCHAR NOT NULL,
    email_id INTEGER NOT NULL,
    FOREIGN KEY (email_id) REFERENCES email (id) ON DELETE CASCADE
);

-- Create table for 'sentences_hostage'
CREATE TABLE sentences_hostage (
    id SERIAL PRIMARY KEY,
    word VARCHAR NOT NULL,
    email_id INTEGER NOT NULL,
    FOREIGN KEY (email_id) REFERENCES email (id) ON DELETE CASCADE
);

-- Create table for 'sentences_explos'
CREATE TABLE sentences_explos (
    id SERIAL PRIMARY KEY,
    word VARCHAR NOT NULL,
    email_id INTEGER NOT NULL,
    FOREIGN KEY (email_id) REFERENCES email (id) ON DELETE CASCADE
);

-- Create table for 'sentences_not_suspicious'
CREATE TABLE sentences_not_suspicious (
    id SERIAL PRIMARY KEY,
    word VARCHAR NOT NULL,
    email_id INTEGER NOT NULL,
    FOREIGN KEY (email_id) REFERENCES email (id) ON DELETE CASCADE
);
