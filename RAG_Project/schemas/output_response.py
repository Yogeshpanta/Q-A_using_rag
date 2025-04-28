from pydantic import BaseModel


# from RAG_Project.schemas.output_response import ResponseOutput
class ResponseOutput(BaseModel):
    out: str
