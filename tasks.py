from celery import Celery

from domain.assistant.utils import get_answer

worker = Celery(
    backend="redis://redis:6379/1",
    broker="redis://redis:6379/2",
)


@worker.task
def ask_assistant_task(api_token: str, question: str) -> str:
    """"""

    answer = get_answer(api_token=api_token, question=question)

    return answer.content
