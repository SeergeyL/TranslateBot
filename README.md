# TranslateBot

## List of available commands:
Telegram Bot can perform following commands:

/switch - there are two available translation mods: synchronous translation (**sync**) and selective (**selective**). Selective mode translates messages if they are marked by `MESSASAGE_MARKER` in any place in the text. Synchronous translation translates all messages.

/status - show current state of variables

/help - show help message

## Environment Variables
`MESSASAGE_MARKER` - In selective mode marked message will be translated. List of markers can be provided with comma divider

`DESTINATION_LANGUAGE` - The 2 character language code into which the translation will be carried out. More in [googletrans](https://pypi.org/project/googletrans/) docs

`TELEGRAM_TOKEN` - Bot token which can be obtained from BotFather

`CONFIDENCE_THRESHOLD` - confidence level that the received message already translated to destination language. Messages with confidence higher than threshold won't be translated

## Run Container
Copy environment variables from example file and add `TELEGRAM_TOKEN`
```
cp .env.example .env
```

Build the image
```
docker build -t bot .
```
Run container
```
docker run bot
```

