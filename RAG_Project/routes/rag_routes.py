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
