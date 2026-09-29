from kafka import KafkaProducer
import json
import uuid
from datetime import datetime, timezone

producer = KafkaProducer(
    bootstrap_servers='localhost:9092', 
    value_serializer=lambda v: json.dumps(v).encode('utf-8'))

TOPIC = "validated-market-data"

def send_event():
    event = {
        "id": str(uuid.uuid4()),
        "source_type": "news",
        "ticker": "TSLA",
        "headline": "Tesla faces production issues",
        "content": "Negative sentiment around supply chain",
        "price": 167.23,
        "volume": 1200345,
        "published_at": datetime.now(timezone.utc).isoformat(),
        "ingested_at": datetime.now(timezone.utc).isoformat()
    }

    producer.send(TOPIC, value=event)
    producer.flush()

    print(f"✅ Event sent to Kafka: {event}")

if __name__ == "__main__":
    send_event()