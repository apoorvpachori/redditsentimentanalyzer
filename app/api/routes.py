import asyncio
import logging
from time import perf_counter

from fastapi import APIRouter, HTTPException
from app.api.schemas import AnalyzeRequest, AnalyzeResponse

from app.agent.service import get_agent
from app.core.config import get_settings

logger = logging.getLogger(__name__)
router = APIRouter()




@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    started = perf_counter()
    try:
        settings = get_settings()
        agent = get_agent()
        result = await asyncio.wait_for(
            agent.ainvoke(
                {"messages": [{"role": "user", "content": request.query}]},
                config={"recursion_limit": settings.agent_recursion_limit},
            ),
            timeout=settings.request_timeout_seconds,
        )
        message = result["messages"][-1]
        answer = message.text
        if not answer:
            raise ValueError("Agent returned no answer")
    except TimeoutError as exc:
        raise HTTPException(504, "Analysis timed out. Try a more specific query.") from exc
    except Exception as exc:
        logger.exception("Analysis failed")
        raise HTTPException(503, "Analysis unavailable. Check server configuration and provider logs.") from exc
    return AnalyzeResponse(answer=answer, elapsed_seconds=round(perf_counter() - started, 3))
