from fastapi import APIRouter
from RAG_Project.models.rag_retrieve import RagImplementation
from RAG_Project.models.text_generator import TunedChatGeneration
from RAG_Project.schemas.output_response import ResponseOutput
from RAG_Project.redis.redis_cache import RedisImplementation
import os
from dotenv import load_dotenv
load_dotenv()

router = APIRouter()

# Static file path
# STATIC_FILE = "/home/yogesh/Desktop/veel_internship_final/Q-A_using_rag/transformer.pdf"
# STATIC_FILE = "/app/data/transformer.pdf"
# STATIC_FILE = os.getenv("PDF_PATH")


# @router.post("/query", response_model=ResponseOutput)
# async def handle_query(
#     question: str = "What is attention in transformer?", use_rank: bool = False
#     # question: str, use_rank: bool
# ):
#     # Initialize RAG system with static file
#     rag_system = RagImplementation(file=STATIC_FILE)

#     # Initialize chat bot
#     chat_bot = TunedChatGeneration(rag_system, "gpt2")

#     # Generate response
#     if use_rank:
#         response = chat_bot.generate_tuned_output(question, use_ranked=True)
#     else:
#         response = chat_bot.generate_tuned_output(question, use_ranked=False)

#     # print(ResourceWarning(out=str(response)))
#     return ResponseOutput(out=str(response))



# ### FOR REDIS
# @router.post("/query", response_model=ResponseOutput)
# async def handle_query(
#     question: str = "What is attention in transformer?", use_rank: bool = False
# ):
#     # Initialize RAG system
#     rag_system = RagImplementation(file=STATIC_FILE)

#     # Initialize chatbot
#     chat_bot = TunedChatGeneration(rag_system, "gpt2")

#     # Initialize Redis and fetch/generate response
#     redis_cache = RedisImplementation(chat_bot, query=question, use_ranked=use_rank)
#     response = redis_cache.get_response()

#     return ResponseOutput(out=response)

# ### FOR PARAGRAPH
# @router.post("/multi_line", response_model=ResponseOutput)
# async def handle_query(
#     question: str = "What is attention in transformer?", style_define="multi_line"
# ):
#     # Initialize RAG system
#     rag_system = RagImplementation(file=STATIC_FILE)

#     # Initialize chatbot
#     chat_bot = TunedChatGeneration(rag_system, "gpt2", style=style_define)
#     # chat_bot.define_prompt(style=style_define)

#     # Initialize Redis and fetch/generate response

#     redis_cache = RedisImplementation(chat_bot, query=question, style=style_define)
#     response = redis_cache.multi_line_redis()

#     return ResponseOutput(out=response)

# ### FOR Single Line
# @router.post("/single_line", response_model=ResponseOutput)
# async def handle_query(
#     question: str = "What is attention in transformer?", style_define="single_line"
# ):
#     # Initialize RAG system
#     rag_system = RagImplementation(file=STATIC_FILE)

#     # Initialize chatbot
#     chat_bot = TunedChatGeneration(rag_system, "gpt2", style=style_define)
#     # chat_bot.define_prompt(style=style_define)

#     # Initialize Redis and fetch/generate response

#     redis_cache = RedisImplementation(chat_bot, query=question, style=style_define)
#     response = redis_cache.single_line_redis()

#     return ResponseOutput(out=response)


### FOR PARAGRAPH
@router.post("/multi_line", response_model=ResponseOutput)
async def handle_query(
    question: str = "What is attention in transformer?", style_define="multi_line"
):
    # Initialize RAG system
    # rag_system = RagImplementation(file=STATIC_FILE)
    rag_system = RagImplementation()

    # Initialize chatbot
    chat_bot = TunedChatGeneration(rag_system, style=style_define)
    # chat_bot.define_prompt(style=style_define)

    # Initialize Redis and fetch/generate response

    redis_cache = RedisImplementation(chat_bot, query=question, style=style_define)
    response = redis_cache.multi_line_redis()

    return ResponseOutput(Answer=response)

### FOR Single Line
@router.post("/single_line", response_model=ResponseOutput)
async def handle_query(
    question: str = "What is attention in transformer?", style_define="single_line"
):
    # Initialize RAG system
    rag_system = RagImplementation()

    # Initialize chatbot
    chat_bot = TunedChatGeneration(rag_system,style=style_define)
    # chat_bot.define_prompt(style=style_define)

    # Initialize Redis and fetch/generate response

    redis_cache = RedisImplementation(chat_bot, query=question, style=style_define)
    response = redis_cache.single_line_redis()

    return ResponseOutput(Answer=response)
