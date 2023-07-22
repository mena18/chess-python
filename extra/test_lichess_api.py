import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()


LICHESS_HOST = os.getenv("LICHESS_HOST", "https://lichess.org")
bearer = os.getenv("BEARER")
headers = {}
headers["Authorization"] = f"Bearer {bearer}"
headers["Accept"] = "*/*"
# headers["Content-type"] = "application/json"
api = requests.session()
api.headers.update(headers)


def test_database():
    body_data = {
        "fen": "rnbqk2r/pp2bp1p/4p1p1/2ppP3/6nP/2P2BP1/PP1P1P2/RNBQK1NR b KQkq - 2 8"
    }
    body_data["fen"] = "rnbqkbnr/ppp1pppp/8/3pP3/8/8/PPPP1PPP/RNBQKBNR b KQkq - 0 2"

    response = api.get(
        f"{LICHESS_HOST}/api/cloud-eval", headers=headers, params=body_data
    )
    print(response.status_code)
    print(response.json())


def list_chess_engines():
    return api.get("https://lichess.org/api/external-engine")


def generate_chess_engine_id():
    payload = {
        "name": "Stockfish 15",
        "maxThreads": 8,
        "maxHash": 2048,
        "defaultDepth": 24,
        "variants": ["chess"],
        "providerSecret": "Dee3uwieZei9ahpaici9bee2yahsai0K",
        "providerData": "string",
    }
    response = requests.post(
        f"{LICHESS_HOST}/api/external-engine", headers=headers, data=payload
    )
    return response.json()["id"]


def test_engine_analysis():
    id = os.getenv("CHESS_ENGINE_ID")
    clientSecret = os.getenv("CHESS_ENGINE_CLIENT_SECRET")
    print(id, clientSecret)

    payload = {
        "clientSecret": clientSecret,
        "work": {
            "sessionId": "abcd1234",
            "threads": 4,
            "hash": 128,
            "infinite": False,
            "multiPv": 1,
            "variant": "chess",
            "initialFen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
            "moves": [],
        },
    }

    return requests.post(
        f"https://engine.lichess.ovh/api/external-engine/{id}/analyse",
        headers=headers,
        data=json.dumps(payload),
    )


res = test_engine_analysis()
print(res.status_code)
print(res.json())
