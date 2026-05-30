from fastapi import APIRouter

from backend.agents.router_agent import router_agent

router = APIRouter()

@router.get("/ask-agent")
def ask_agent(question: str):

    response = router_agent(question)

    return {
        "question": question,
        "response": response
    }