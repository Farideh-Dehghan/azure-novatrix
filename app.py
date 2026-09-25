from datetime import datetime, timezone

from email.utils import format_datetime

import json
import os
import uuid

from urllib.parse import quote

import requests

from flask import Flask, request

from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

STORAGE_ACCOUNT = "stnovatrixfarideh37"

CONTAINER = "novatrix-arenden"
POWER_AUTOMATE_URL = os.getenv("POWER_AUTOMATE_URL", "")
MI_RESOURCE_ID = (

    "/subscriptions/5d5e0f20-c148-42c8-9596-6a4764ddcefb/"

    "resourceGroups/rg-novatrix/providers/"

    "Microsoft.ManagedIdentity/userAssignedIdentities/id-novatrix-app"

)

def get_access_token():

    response = requests.get(

        "http://169.254.169.254/metadata/identity/oauth2/token",

        headers={"Metadata": "true"},

        params={

            "api-version": "2019-08-01",

            "resource": "https://storage.azure.com/",

            "mi_res_id": MI_RESOURCE_ID,

        },

        timeout=10,

    )

    response.raise_for_status()

    return response.json()["access_token"]

def upload_blob(blob_name, data, content_type):

    token = get_access_token()

    encoded_name = quote(blob_name, safe="/")

    url = (

        f"https://{STORAGE_ACCOUNT}.blob.core.windows.net/"

        f"{CONTAINER}/{encoded_name}"

    )

    response = requests.put(

        url,

        data=data,

        headers={

            "Authorization": f"Bearer {token}",

            "x-ms-version": "2023-11-03",

            "x-ms-date": format_datetime(

                datetime.now(timezone.utc), usegmt=True

            ),

            "x-ms-blob-type": "BlockBlob",

            "Content-Type": content_type,

        },

        timeout=30,

    )

    response.raise_for_status()



@app.post("/submit")

def submit():

    name = request.form.get("name", "").strip()

    email = request.form.get("email", "").strip()

    message = request.form.get("message", "").strip()

    if not name or not email or not message:

        return "Namn, e-post och meddelande måste fyllas i.", 400

    timestamp = datetime.now(timezone.utc)

    case_id = (

        timestamp.strftime("%Y%m%d-%H%M%S")

        + "-"

        + uuid.uuid4().hex[:8]

    )

    case_data = {

        "case_id": case_id,

        "name": name,

        "email": email,

        "message": message,

        "created_utc": timestamp.isoformat(),

    }

    upload_blob(

        f"arenden/{case_id}.json",

        json.dumps(case_data, ensure_ascii=False, indent=2).encode("utf-8"),

        "application/json; charset=utf-8",

    )
if POWER_AUTOMATE_URL:

        flow_response = requests.post(

            POWER_AUTOMATE_URL,

            json={

                "name": name,

                "email": email,

                "message": message,

            },

            timeout=15,

        )

        flow_response.raise_for_status()


    attachment = request.files.get("attachment")

    if attachment and attachment.filename:

        filename = secure_filename(attachment.filename)

        if filename:

            upload_blob(

                f"bilagor/{case_id}-{filename}",

                attachment.read(),

                attachment.mimetype or "application/octet-stream",

            )

    return f"""

    <!doctype html>

    <html lang="sv">

    <head>

        <meta charset="utf-8">

        <title>Ärendet sparades</title>

    </head>

    <body>

        <main>

            <h1>Tack!</h1>

            <p>Ditt ärende har sparats säkert.</p>

            <p><strong>Ärendenummer:</strong> {case_id}</p>

            <a href="/">Skicka ett nytt ärende</a>

        </main>

    </body>

    </html>

    """

@app.errorhandler(413)

def file_too_large(error):

    return "Bilagan är för stor. Maximal filstorlek är 5 MB.", 413

if __name__ == "__main__":

    app.run(host="127.0.0.1", port=5000)



