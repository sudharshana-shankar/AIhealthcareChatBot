
from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer


chatBot = ChatBot('ChatBot')


trainer = ChatterBotCorpusTrainer(chatBot)


trainer.train("chatterbot.corpus.english")


print("Hi, I am ChatBot")


while True:
    
    query = input(">>>")
   
    print(chatBot.get_response(Statement(text=query, search_text=query)))