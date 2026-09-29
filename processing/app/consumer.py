from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'validated-market-data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='fsip-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("🚀 Waiting for messages...")

for message in consumer:
    event = message.value
    print("📥 Received event:", event)