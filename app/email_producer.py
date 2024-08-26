from aiokafka import AIOKafkaProducer
import asyncio

async def send_email_to_kafka(email: str, action: str):
    producer = AIOKafkaProducer(bootstrap_servers='kafka:9092')
    await producer.start()
    try:
        message = f"{email},{action}"
        await producer.send_and_wait("email_notifications", message.encode("utf-8"))
    finally:
        await producer.stop()
