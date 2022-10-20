# TranslateBot

## List of available commands:

/switch - there are two available translation mods: synchronous translation (**sync**) and selective (**selective**). Selective mode translates messages if they are marked by emoji in any place in the text. Synchronous translation translates all messages.

/status - show current state of variables

/help - show help message

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

