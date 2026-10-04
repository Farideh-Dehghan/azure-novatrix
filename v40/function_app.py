import azure.functions as func

import html

import uuid

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="arende", methods=["GET", "POST"])

def arende(req: func.HttpRequest) -> func.HttpResponse:

    if req.method == "POST":

        namn = html.escape(req.form.get("namn", "Okänd kund"))

        epost = html.escape(req.form.get("epost", ""))

        meddelande = html.escape(req.form.get("meddelande", ""))

        arendenummer = str(uuid.uuid4())[:8].upper()

        svar = f"""

        <html>

        <body style="font-family:Arial; max-width:650px; margin:40px auto;">

            <h1>Ärendet har registrerats</h1>

            <p><strong>Ärendenummer:</strong> {arendenummer}</p>

            <p><strong>Namn:</strong> {namn}</p>

            <p><strong>E-post:</strong> {epost}</p>

            <p><strong>Meddelande:</strong> {meddelande}</p>

            <a href="/api/arende">Skicka ett nytt ärende</a>

        </body>

        </html>

        """

        return func.HttpResponse(svar, mimetype="text/html", status_code=200)

    formular = """

    <html>

    <body style="font-family:Arial; max-width:650px; margin:40px auto;">

        <h1>Novatrix kundtjänst</h1>

        <p>Skicka in ett nytt kundärende.</p>

        <form method="post">

            <label>Namn</label><br>

            <input name="namn" required style="width:100%; padding:8px;"><br><br>

            <label>E-post</label><br>

            <input name="epost" type="email" required style="width:100%; padding:8px;"><br><br>

            <label>Meddelande</label><br>

            <textarea name="meddelande" required

                      style="width:100%; height:120px; padding:8px;"></textarea><br><br>

            <button type="submit" style="padding:10px 20px;">

                Skicka ärende

            </button>

        </form>

    </body>

    </html>

    """

    return func.HttpResponse(formular, mimetype="text/html", status_code=200)

