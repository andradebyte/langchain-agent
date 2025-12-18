import weaviate
from app.schemas.project import ProjectUpload, ProjectResponse
from app.services.logger import logger

class WeaviateService:
    def __init__(self):
        self.client = weaviate.connect_to_local(
            host="weaviate",  # Nome do serviço no docker-compose
            port=8080,
            grpc_port=50051
        )
        self._create_collection_if_not_exists()
    
    def _create_collection_if_not_exists(self):
        """Create the Project collection schema if it doesn't exist."""
        try:
            if not self.client.collections.exists("Project"):
                self.client.collections.create(
                    name="Project",
                    vectorizer_config=weaviate.classes.config.Configure.Vectorizer.text2vec_transformers(),
                    properties=[
                        weaviate.classes.config.Property(
                            name="title",
                            data_type=weaviate.classes.config.DataType.TEXT
                        ),
                        weaviate.classes.config.Property(
                            name="description",
                            data_type=weaviate.classes.config.DataType.TEXT
                        ),
                        weaviate.classes.config.Property(
                            name="tags",
                            data_type=weaviate.classes.config.DataType.TEXT_ARRAY
                        ),
                    ]
                )
                logger.info("Project collection created successfully")
        except Exception as e:
            logger.error(f"Error creating collection: {e}")
    
    async def insert_project(self, project: ProjectUpload) -> ProjectResponse:
        """Insert a single project into Weaviate."""
        try:
            projects = self.client.collections.get("Project")
            
            uuid = projects.data.insert(
                properties={
                    "title": project.title,
                    "description": project.description,
                    "tags": project.tags or [],
                }
            )
            
            logger.info(f"Project inserted with UUID: {uuid}")
            
            return ProjectResponse(
                title=project.title,
                description=project.description,
                tags=project.tags or []
            )
        except Exception as e:
            logger.error(f"Error inserting project: {e}")
            raise
        
    async def list_all_projects(self, limit: int = 100) -> list[ProjectResponse]:
        """List all projects from Weaviate."""
        try:
            projects = self.client.collections.get("Project")
            
            # Fetch objects with limit
            response = projects.query.fetch_objects(limit=limit)
            
            results = []
            for obj in response.objects:
                results.append(ProjectResponse(
                    title=obj.properties.get("title", ""),
                    description=obj.properties.get("description", ""),
                    tags=obj.properties.get("tags", [])
                ))
            
            logger.info(f"Retrieved {len(results)} projects")
            return results
        except Exception as e:
            logger.error(f"Error listing projects: {e}")
            raise

    def close(self):
        """Close Weaviate connection."""
        self.client.close()

weaviate_service = WeaviateService()