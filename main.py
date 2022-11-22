import aiml
import os


kernel = aiml.Kernel()
# kernel.setPredicate("botmaster", "Rishub")

if os.path.isfile("brain.brn"):
    kernel.bootstrap(brainFile = "brain.brn")
else:
    kernel.bootstrap(learnFiles = "model.aiml", commands = "load aiml")
    kernel.saveBrain("brain.brn")

while True:
    print(kernel.respond(input(">> ")))


# import aiml

# kernel = aiml.Kernel()
# kernel.learn("model.aiml")
# kernel.respond("load aiml")

# while True:
#     print(kernel.respond(input(">> ")))