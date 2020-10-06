#!/usr/bin/env python3
# coding: utf-8

"""Bandwidth calculation for streaming server."""

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from pydantic import BaseModel

tags_metadata = [
    {
        'name': 'bwserver',
        'description': 'Determine necessary server bandwidth'
    },
    {
        'name': 'serverusagebw',
        'description': 'Determine the amount of data used for the streaming; '
    }
]

app = FastAPI(title='streaming calc fastapi - scf',
              description='Bandwidth calculation for streaming server - '
                          'webservice',
              docs_url='/', openapi_tags=tags_metadata
              )


class BwserverJsonReq(BaseModel):
    """Define element (with type) needed inside the json."""

    bitrate: float
    nblisteners: float


class BwserverJsonRes(BaseModel):
    """Define element (with type) that you get inside the response."""

    result: float


class ServerusagebwJsonReq(BaseModel):
    """Define element (with type) needed inside the json."""

    bitrate: float
    nblisteners: float
    nbdays: float
    nbhours: float


class ServerusagebwJsonRes(BaseModel):
    """Define element (with type) that you get inside the response."""

    result: float


def compute_bwserver(bitrate: float, nblisteners: float) -> float:
    """Determine necessary server bandwidth."""
    return 125 * nblisteners * bitrate / 128


def compute_serverusagebw(bitrate: float, nbdays: float, nbhours: float,
                          nblisteners: float) -> float:
    """Determine the amount of data used for the streaming."""
    return 28125 * nbdays * nbhours * bitrate * nblisteners / 65536


@app.post('/bwserver', tags=['bwserver'], response_model=BwserverJsonRes,
          response_class=ORJSONResponse,
          response_description='result -> Mib/s')
async def bwserver(body: BwserverJsonReq):
    """
    Endpoint to determine necessary server bandwidth.

    Bitrate in kb/s.
    """
    bitrate: float = body.bitrate
    nblisteners: float = body.nblisteners
    result: float = compute_bwserver(bitrate=bitrate, nblisteners=nblisteners)
    return {'result': result}


@app.post('/serverusagebw', tags=['serverusagebw'],
          response_model=ServerusagebwJsonRes, response_class=ORJSONResponse,
          response_description='result -> GiB')
async def serverusagebw(body: ServerusagebwJsonReq):
    """
    Endpoint to determine the amount of data used for the streaming.

    Bitrate in kb/s.
    """
    bitrate: float = body.bitrate
    nbdays: float = body.nbdays
    nbhours: float = body.nbhours
    nblisteners: float = body.nblisteners
    result: float = compute_serverusagebw(bitrate=bitrate, nbdays=nbdays,
                                          nbhours=nbhours,
                                          nblisteners=nblisteners)
    return {'result': result}
