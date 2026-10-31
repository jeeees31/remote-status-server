# remote-status-server

Eine kleine, öffentliche Status-API fuer Lernzwecke.

## Endpunkte

- `GET /` liefert den aktuellen API-Status als JSON.
- `GET /health` ist der Gesundheitscheck fuer Render.

Die API nimmt keine Befehle entgegen, fuehrt keine Programme aus und speichert keine Daten.

## Auf Render bereitstellen

1. In Render **New** > **Blueprint** waehlen und dieses GitHub-Repository verbinden.
2. Render liest `render.yaml` und erstellt einen kostenlosen Web-Service.
3. Nach dem Deploy die Adresse mit `/health` aufrufen.

Alternativ bei einem manuellen Web-Service diese Werte eintragen:

- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- Health Check Path: `/health`
