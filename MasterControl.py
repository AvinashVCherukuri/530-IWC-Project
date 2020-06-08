import multiprocessing
import BotCode

for Code in ('BotCode'):
    print("Program ", Code, " Start")
    p = multiprocessing.Process(target=lambda: __import__(Code))
    p.start()

print("Project Complete")