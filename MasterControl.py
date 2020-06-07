import multiprocessing
import WebsiteControl, BotResponse

for Code in ('WebsiteControl', 'BotResponse'):
    p = multiprocessing.Process(target=lambda: __import__(bot))
    p.start()