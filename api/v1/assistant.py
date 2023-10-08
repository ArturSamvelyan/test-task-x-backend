from celery.result import AsyncResult
from fastapi import APIRouter, HTTPException

from tasks import ask_assistant_task, worker
from schemas.assistant import QuestionSchema


router = APIRouter()


@router.post("/ask")
async def question_ask(question: QuestionSchema):
    """"""

    task = ask_assistant_task.delay(question.api_token, question.question,)

    return {"task_id": task.id}


@router.get("/status/{task_id}")
async def task_status(task_id: str):
    task = ask_assistant_task.AsyncResult(task_id, app=worker)

    return {"status": task.state}


@router.get("/result/{task_id}")
async def get_result(task_id: str):

    result = AsyncResult(task_id, app=worker)

    if result.state == "SUCCESS":
        response = {"status": result.state, "data": result.get()}
    else:
        response = {"status": result.state, "data": None}

    return response
