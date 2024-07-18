from telethon import TelegramClient
from configs.settings.Settings import Settings
from transformers import pipeline


settings = Settings()
client = TelegramClient('anon', settings.telethon.api_id, settings.telethon.api_hash)

async def main():
    qa_model = pipeline("question-answering", "timpal0l/mdeberta-v3-base-squad2")
    question = "What is the tech stack of this job?"
    context = "Analyst 1" \
    "Essential Knowledge:" \
    "VueJs Tailwind JScript HTML, CSS Storybook" \
    "Additional Knowledge:"\
    " Ruby on Rails MongoDB Postgres Postman / Insomnia React Native Material UI Styled Component"
    qa_model(question = question, context = context)




with client:
    client.loop.run_until_complete(main())
