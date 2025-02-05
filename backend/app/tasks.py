import numpy as np
from celery import Celery
import time

celery_app = Celery("tasks", broker="redis://redis:6379/0", backend="redis://redis:6379/0")


# celery handles where the tasks should be sent to the workers
# celery handles distrubition of work between multiple workers for us
@celery_app.task
def cpu_intensive_task(n: int):
    """Simulate a CPU-intensive task"""
    matrix = np.random.rand(n, n)
    result = np.linalg.matrix_power(matrix, 5)
    return f"Completed CPU-intensive task with size {n}x{n}"



@celery_app.task
def cpu_intensive_task(n: int):
    """A CPU-intensive task that runs long enough to trigger autoscaling"""

    start_time = time.time()
    
    while time.time() - start_time < 200:  # Run for at least 60 seconds
        matrix = np.random.rand(1000, 1000)
        _ = np.linalg.det(matrix)  # Heavy CPU operation

    return "Task complete"

