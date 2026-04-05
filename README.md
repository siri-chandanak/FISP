# Financial Signal Intelligence Platform (FSIP)

## Overview
FSIP is a microservices-based platform that ingests market and news data, validates and processes events, generates financial signals, and exposes low-latency APIs for analysts.

## Core Services
- ingestion-service (Python)
- processing-service (Python)
- api-service (Java Spring Boot)

## Tech Stack
- Python
- Java / Spring Boot
- Kafka
- PostgreSQL
- Redis
- Docker
- GitHub Actions
- Terraform

## Data Flow
Input sources -> ingestion-service -> Kafka -> processing-service -> PostgreSQL/Redis -> api-service

## Architectural Flow

```
[CSV / Mock Stock API / Mock News API]
              |
              v
    [ingestion-service | Python]
      - validate
      - normalize
      - publish
              |
              v
     Kafka topic: validated-market-data
              |
              v
   [processing-service | Python]
      - consume event
      - compute sentiment/risk signal
      - save to PostgreSQL
      - cache latest signal in Redis
      - publish generated-signals
              |
              +----------------------+
              |                      |
              v                      v
        PostgreSQL               Redis Cache
              |                      |
              +----------+-----------+
                         |
                         v
            [api-service | Java Spring Boot]
                  - GET /signals
                  - GET /risk-alerts
```

## Repositories

```
FSIP/
├── README.md
├── docker-compose.yml
├── .gitignore
├── common/
│   ├── schemas/
│   │   ├── market_event.schema.json
│   │   └── signal_event.schema.json
│   └── sample_data/
│       ├── stock_prices.csv
│       └── news_feed.json
├── ingestion/
│   ├── app/
│   │   ├── main.py
│   │   ├── producer.py
│   │   ├── validator.py
│   │   ├── normalizer.py
│   │   └── config.py
│   ├── tests/
│   │   └── test_validator.py
│   ├── requirements.txt
│   └── Dockerfile
├── processing/
│   ├── app/
│   │   ├── main.py
│   │   ├── consumer.py
│   │   ├── signal_engine.py
│   │   ├── sentiment.py
│   │   ├── db.py
│   │   ├── cache.py
│   │   └── config.py
│   ├── tests/
│   │   └── test_signal_engine.py
│   ├── requirements.txt
│   └── Dockerfile
├── api/
│   ├── src/
│   │   └── main/
│   │       ├── java/com/fsip/api/
│   │       │   ├── controller/
│   │       │   ├── service/
│   │       │   ├── repository/
│   │       │   ├── model/
│   │       │   └── ApiApplication.java
│   │       └── resources/
│   │           └── application.yml
│   ├── src/test/
│   ├── pom.xml
│   └── Dockerfile
└── infra/
    ├── local/
    │   └── docker-compose.override.yml
    └── terraform/
```

## Example Use Cases
- Sentiment-based buy/sell signals
- Risk alerts from negative news spikes
- Historical signal retrieval for analysts

## Future Enhancements
- Real NLP model integration
- Kubernetes deployment
- Terraform infrastructure
- Observability with Prometheus/Grafana