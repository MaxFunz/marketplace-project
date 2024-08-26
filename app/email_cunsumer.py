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
            email_data = message.value.decode("utf-8").split(',')
            email = email_data[0]
            action = email_data[1]

            if action == "register":
                subject = "Registration successful"
                body = "You have successfully registered."
            elif action == "login":
                subject = "Login successful"
                body = "You have successfully logged in."
            elif action == "reset_password":
                subject = "Password reset successful"
                body = "Your password has been successfully reset."
            else:
                continue

            await send_email(to_email=email, subject=subject, body=body)
    finally:
        await consumer.stop()

if __name__ == "__main__":
    asyncio.run(consume())
