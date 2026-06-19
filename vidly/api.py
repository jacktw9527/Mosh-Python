from ninja import NinjaAPI
from movies.api import router as movies_router

api = NinjaAPI(title='Vidly API', version='1.0.0', description='API for the Vidly movie rental system')
api.add_router('v1', movies_router)
