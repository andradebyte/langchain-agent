from app.services import weaviate_service
from app.schemas.project import ProjectUpload
from app.services.logger import logger
import json
import asyncio

async def main():
    with open('data/projects.json', 'r', encoding='utf-8') as file:
        projects_data = json.load(file)
        for project in projects_data:
            try:
                project = ProjectUpload(project)
                result = weaviate_service.insert_project(project)
                logger.info(f"Inserted: {result}")
            except Exception as e:
                logger.error(f"Error inserting project {project['title']}: {e}")
    weaviate_service.close()

if __name__ == "__main__":
    asyncio.run(main())

