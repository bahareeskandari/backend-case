from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from celery.result import AsyncResult
from tasks import cpu_intensive_task, celery_app

app = FastAPI()

# Allow frontend to access FastAPI backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/start-task/")
def start_task(n: int = 1000):
    """Start a CPU-intensive Celery task and return the task ID."""
    task = cpu_intensive_task.delay(n)
    return {"task_id": task.id}

@app.get("/task-status/{task_id}")
def get_task_status(task_id: str):
    """Check the status of a Celery task with all possible statuses."""
    
    task_result = AsyncResult(task_id, app=celery_app)  # Fetch task info
    
    response = {
        "task_id": task_id,
        "status": task_result.state,  # Current state (PENDING, STARTED, etc.)
        "progress": None,  # Placeholder for progress (if available)
        "result": None,  # Final result (if task is done)
        "error": None  # Error message (if task failed)
    }

    # Check if the task is still running and reporting progress
    if task_result.state == "PROGRESS" and task_result.info:
        response["progress"] = task_result.info  # Example: {"current": 30, "total": 100}

    # If the task is completed, fetch the result
    if task_result.ready():
        if task_result.successful():
            response["result"] = task_result.result  # Final return value
        elif task_result.failed():
            response["error"] = str(task_result.result)  # Error message if failed
    
    return response
