import multiprocessing
import application, BotCode

print("Starting all Programs!")

for Code in ('application', 'BotCode'):
    p = multiprocessing.Process(target=lambda: __import__(Code))
    p.start()

print("Project Complete")