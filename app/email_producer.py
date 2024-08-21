from aiokafka import AIOKafkaProducer
import asyncio

async def send_email_to_kafka(email: str):
    producer = AIOKafkaProducer(bootstrap_servers='kafka:9092')
    await producer.start()
    try:
        await producer.send_and_wait("email_notifications", email.encode("utf-8"))
    finally:
        await producer.stop()
