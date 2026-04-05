CREATE TABLE signals (
    signal_id UUID PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL,
    signal_type VARCHAR(50) NOT NULL,
    sentiment_score DECIMAL(5,2),
    confidence DECIMAL(5,2),
    reason TEXT,
    generated_at TIMESTAMP NOT NULL
);