from fastapi import FastAPI
from celery import Celery
from celery.result import AsyncResult
from tasks import cpu_intensive_task

app = FastAPI()

@app.post("/start-task/")
def start_task(n: int = 1000):
    """Start a CPU-intensive Celery task and return the task ID."""
    task = cpu_intensive_task.delay(n)
    return {"task_id": task.id}


@app.get("/task-status/{task_id}")
def get_task_status(task_id: str):
    """Check the status of a Celery task."""
    from tasks import celery_app
    task_result = celery_app.AsyncResult(task_id)
    return {"task_id": task_id, "status": task_result.state, "result": task_result.result}



@app.post("/testtask/")
def testtask(n: int = 1000):
    """Start a CPU-intensive Celery task and return the task ID with error handling."""
    try:
        # Start Celery task
        task = cpu_intensive_task.delay(n)

        # Check if task was successfully enqueued
        if not isinstance(task, AsyncResult):
            raise RuntimeError("Failed to enqueue Celery task")

        return {"task_id": task.id}

    except Exception as e:
        # Log the exception (optional: you can use logging)
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

