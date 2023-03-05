import os

from fastapi.openapi.utils import get_openapi

from model.training.Config import Config


def initializeSwagger(app):
    configPath = os.path.join(os.path.dirname(__file__), "../config.yaml")
    config = Config(configPath)

    openApiSchema = app.openapi_schema = get_openapi(
        title=config.get("swagger.title"),
        version=config.get("swagger.version"),
        description=config.get("swagger.description"),
        routes=app.routes,
    )
    openApiSchema["info"]["x-logo"] = {
        "url": config.get("swagger.logoUrl")
    }
    # add contact info
    openApiSchema["info"]["contact"] = {
        "name": config.get("swagger.contact.name"),
    }

    app.openapi_schema = openApiSchema
