# # from RAG_Project.models.rag_retrieve import RagImplementation
# # from RAG_Project.models.text_generator import TunedChatGeneration
# # from RAG_Project.schemas.output_response import ResponseOutput
# # from fastapi import APIRouter

# # router = APIRouter()


# # @router.post("/rag", response_class=ResponseOutput)
# # def rag_output(req:RagImplementation, use_rank:bool=False):
# #     if not use_rank:
# #         output = TunedChatGeneration.generate_tuned_output(use_ranked=False, question="What is attention in transformer?")

# #     return output


# # routes/rag_routes.py (and rerank_routes.py - should be combined)
# from fastapi import APIRouter, UploadFile, File
# from RAG_Project.models.rag_retrieve import RagImplementation
# from RAG_Project.models.text_generator import TunedChatGeneration
# from RAG_Project.schemas.output_response import ResponseOutput

# router = APIRouter()

# @router.post("/query", response_model=ResponseOutput)
# async def handle_query(
#     # file: UploadFile = File(...),
#     filename = "C:/Users/Acer/OneDrive/Desktop/veel_internship_final/transformer.pdf",
#     question: str = "What is attention in transformer?",
#     use_rank: bool = False
# ):
#     # Save uploaded file temporarily
#     # with open(file.filename, "wb") as buffer:
#     #     buffer.write( file.read())
#     with open(filename, "r") as file:
#         file = file.read()
#     # rag_system = RagImplementation(file.filename)
#     rag_system = RagImplementation(file=file)
#     chat_bot = TunedChatGeneration(rag_system, "gpt2")

#     if use_rank:
#         response = await  chat_bot.generate_tuned_output(question, use_ranked=True)
#     else:
#         response = await  chat_bot.generate_tuned_output(question, use_ranked=False)

#     return ResponseOutput(out=response)


from fastapi import APIRouter
from RAG_Project.models.rag_retrieve import RagImplementation
from RAG_Project.models.text_generator import TunedChatGeneration
from RAG_Project.schemas.output_response import ResponseOutput

router = APIRouter()

# Static file path
STATIC_FILE = "C:/Users/Acer/OneDrive/Desktop/veel_internship_final/transformer.pdf"


@router.post("/query", response_model=ResponseOutput)
async def handle_query(
    question: str = "What is attention in transformer?", use_rank: bool = False
):
    # Initialize RAG system with static file
    rag_system = RagImplementation(file=STATIC_FILE)

    # Initialize chat bot
    chat_bot = TunedChatGeneration(rag_system, "gpt2")

    # Generate response
    if use_rank:
        response = chat_bot.generate_tuned_output(question, use_ranked=True)
    else:
        response = chat_bot.generate_tuned_output(question, use_ranked=False)

    print(ResourceWarning(out=str(response)))
    return ResponseOutput(out=str(response))
