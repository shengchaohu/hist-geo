import address
import adaptor
import queries

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/administrative-divisions", status_code=200)
async def get_administrative_divisions(year: int = 1368, dynasty_id: int = 4329):
    administrative_divisions_query = queries.AdministrativeDivisionQuery(dynasty_id).sql
    address_loader = address.AddressLoader(administrative_divisions_query)
    addresses = address_loader.get_address()[year]
    geo_json_addresses = adaptor.MingAdaptor().dict_to_geo_json(addresses)
    return geo_json_addresses
