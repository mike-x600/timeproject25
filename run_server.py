import uvicorn

from timeproject25.celery import app as celery_app 

if __name__ == "__main__":
    uvicorn.run("asgi:application", port=8000, log_level="info", reload=True)

    # app = current_app._get_current_object()
    # worker = worker.worker(app=app)

    # celery_app.worker_main([
    #     'worker',
    #     '--loglevel=DEBUG',
    # ])

    # worker = celery_app.Worker()
    # worker.start()