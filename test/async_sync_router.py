import asyncio
import logging
from fastapi import APIRouter

class TaskIdFilter(logging.Filter):
    def filter(self, record):
        try:
            task = asyncio.current_task()
            record.task_id = id(task) if task else "N/A"
        except RuntimeError:
            # No running event loop (e.g., sync function in threadpool)
            record.task_id = "N/A"

        return True

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d [Thread:%(thread)d] [Task:%(task_id)s] [%(levelname)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.getLogger().addFilter(TaskIdFilter())
async_sync_router = APIRouter()

@async_sync_router.get("/sync-sleep")
def sync_sleep():
    import time
    logging.info("Sync sleep...")
    time.sleep(5)
    logging.info("Sync woke")
    return {"msg": "done after sync sleep"}


@async_sync_router.get("/async-sleep")
async def async_sleep():
    logging.info("ASync sleep...")
    await asyncio.sleep(5)
    logging.info("ASync woke")
    return {"msg": "done after async sleep"}