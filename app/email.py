import aiohttp

async def send_email(to_email: str, subject: str, body: str):
    async with aiohttp.ClientSession() as session:
        await session.post(
            "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
            auth=("api", "YOUR_API_KEY"),
            data={"from": "kurn0sovm@yandex.ru",
                  "to": to_email,
                  "subject": subject,
                  "text": body}
        )
