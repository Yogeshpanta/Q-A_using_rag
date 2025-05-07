from RAG_Project.models.rag_retrieve import RagImplementation
from RAG_Project.configs.logging_config import setup_logging
import logging
from RAG_Project.models.reranked import Reranker
import redis
import os
from dotenv import load_dotenv
load_dotenv()

setup_logging()

host = os.getenv("REDIS_HOST", "localhost")
port = int(os.getenv("REDIS_PORT", 6379))

# class RedisImplementation:
#     def __init__(self, chat_bot, query: str, use_ranked: bool = False):
#         self.query = query
#         self.use_ranked = use_ranked
#         self.chat_bot = chat_bot
#         self.redis_client = redis.Redis(host="localhost", port=6379, db=0)

#     def get_response(self):
#         # Try to fetch from Redis
#         cached_answer = self.redis_client.get(self.query)

#         if cached_answer:
#             logging.info("Output from redis cache")
#             return cached_answer.decode("utf-8")  # Redis returns bytes

#         # If not in cache, compute using the chatbot
#         logging.info("query is not found in cache, generating response...")
#         response = self.chat_bot.generate_tuned_output(
#             question=self.query, use_ranked=self.use_ranked
#         )

#         # Cache it as string
#         self.redis_client.set(self.query, str(response))

#         return str(response)

class RedisImplementation:
    def __init__(self, chat_bot, query:str, style:str):
        self.chat_bot = chat_bot
        self.query = query
        self.style = style
        # self.redis_client = redis.Redis(host="0.0.0.0", port=6379, db=0)
        self.redis_client = redis.Redis(host=host, port=port, db=0)


    def single_line_redis(self):
        # self.style = style
        cached_answer = self.redis_client.hget(self.style, self.query)
        # if self.style:
        if cached_answer:
            logging.info("Displaying the cached result in single line")
            return cached_answer.decode("utf-8")
        response = self.chat_bot.generate_tuned_output(
                question = self.query
            )
        logging.info("Displaying result by generating in single line ")
        self.redis_client.hset(self.style, self.query, str(response))
        self.redis_client.expire(self.style, 1800)

        return str(response)
        
    def multi_line_redis(self):
        # self.style = style
        cached_answer = self.redis_client.hget(self.style, self.query)
        # if self.style:
        if cached_answer:
            logging.info("Displaying result from cache in multiple line")
            return cached_answer.decode("utf-8")
        response = self.chat_bot.generate_tuned_output(
                question = self.query
            )
        logging.info("Displaying result by generating in multiple lines")
        self.redis_client.hset(self.style, self.query, str(response))
        self.redis_client.expire(self.style, 1800)
        

        return str(response)
    # def get_response(self):
    #     if self.style == "single_line":
    #         return self.single_line_redis()
        
    #     elif self.style == "multi_line":
    #         return self.multi_line_redis()
    #     else:
    #         return Exception 

