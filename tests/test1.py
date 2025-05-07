# import redis

# r = redis.Redis(host="localhost", port=6379, db=0)

# # query = input("enter the query")

# # if query in r.keys():
# #     r.get("query")
# # else:
# #     r.set("query",input("enter answer"))
# #     r.get("qwery")

# style = input("Enter the style ")
# query = input("enter the query")

# if style=="single_line":
#     if query in r.keys():
#         r.hget(style, query)
#     else:
#         r.hset(style, query,input("enter answer"))

# elif style == "multi_line":
#     if query in r.keys():
#         r.hget(style, query)
#     else:
#         r.hset(style, query,input("enter answer"))
    
# from RAG_Project.configs.logging_config import setup_logging
# setup_logging.info("Testing logger file")

import os

path = "/home/yogesh/Desktop/veel_internship_final/Q-A_using_rag/chroma_db"

# if os.path.exists(path=path):
#     print("file exist")

# else:
#     print("file doesn't exist")

if os.path.isdir(path):
    print("folder exist")

else:
    print("folder doesn't exist")

