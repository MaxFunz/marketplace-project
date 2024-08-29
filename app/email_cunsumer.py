from aiokafka import AIOKafkaConsumer
import asyncio
from app.email import send_email

async def consume():
    consumer = AIOKafkaConsumer(
        'email_notifications',
        bootstrap_servers='kafka:9092',
        group_id="email_group"
    )
    await consumer.start()
    try:
        async for message in consumer:
            email = message.value.decode("utf-8")
            await send_email(to_email=email, subject="Registration successful",
                             body="You have successfully registered.")
    finally:
        await consumer.stop()

if __name__ == "__main__":
    asyncio.run(consume())
