# chatMimic
A NLP app which uses textgenrnn &amp; twitchAPI modules to go to a specific VOD (designated by VOD ID), collects all messages, and trains itself on that chat to try and mimic chat for said VOD. I made this after noticing how different chats react to certain things, I wanted to see different chats could be used to generate different types of text. 

For this project I utilized two different github projects:

textgenrnn

https://github.com/minimaxir/textgenrnn

twitchAPI

https://github.com/PetterKraabol/Twitch-Python

## VOD ID example 
https://www.twitch.tv/videos/**1083683886**
In this example, the VOD id here would be 1083683886

## Example Use
```
# Using 1083683886 from earlier example

from chatMimic import ChatMimic
shroudMimic = ChatMimic("client-id", "client-secret") 
shroudMimic.trainOnVOD(1083683886)
text = shroudMimic.generateTextFromVOD()
print(text)
```

## Credits

minimaxir - textgenrnn

https://github.com/minimaxir/textgenrnn

PetterKraabol - twitchAPI

https://github.com/PetterKraabol/Twitch-Python
