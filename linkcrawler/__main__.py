from crawler import Crawler
with Crawler("https://www.google.com", LOG=Crawler.INFO_LOG) as crawler:
     crawler.crawl()

#import asyncio
#import concurrent.futures
#import requests
#import threading
#from timeit import default_timer

#def test():
#    print("requested")
#    return requests.get('http://localhost:8888/tree')

#async def main():

#    c =0 

#    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:

#        loop = asyncio.get_event_loop()
#        futures = [
#            loop.run_in_executor(
#                executor, 
#                test
#            )
#            for i in range(100)
#        ]
#        for response in await asyncio.gather(*futures): 
#            pass

#async def main2():
#    loop = asyncio.get_event_loop()
#    futures = [
#        loop.run_in_executor(
#            None, 
#            test
#        )
#        for i in range(100)
#    ]
#    for response in await asyncio.gather(*futures):
#        pass

#num_requests = 100
#start = default_timer()
#responses = [
#    requests.get('http://localhost:8888/tree')
#    for i in range(num_requests)
#]
#print(default_timer()-start)
#start = default_timer()
#loop = asyncio.get_event_loop()
#loop.run_until_complete(main2())
#print(default_timer()-start)
#start = default_timer()
#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())
#print(default_timer()-start)

# need to remove this line after testing
