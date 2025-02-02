import os
import json
from pathlib import Path


def list_reader(directory_path):
    listFile = directory_path
    try:
        listPath = Path(__file__).parent.resolve()/listFile
        if listPath.exists():
            with open(listPath, 'r') as file:
                return json.load(file)

    except json.decoder.JSONDecodeError as e:
        return {"error": str(e)}

