from datetime import UTC, datetime

from flask import Flask, jsonify

app = Flask(__name__)


def status_response():
    return jsonify(
        service="remote-status-server",
        status="ok",
        timestamp=datetime.now(UTC).isoformat(),
    )


@app.get("/")
def index():
    return status_response()


@app.get("/health")
def health():
    return status_response()
