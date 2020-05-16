from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')
# Create a new Trainer
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
"chatterbot.corpus.korean"
)
