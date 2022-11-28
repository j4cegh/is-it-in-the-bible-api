from quart import Quart, request, jsonify
from quart_rate_limiter import rate_limit, RateLimiter
from datetime import timedelta
from bible_loader import load_verses
from quart_cors import cors

app = Quart(__name__)
app = cors(app, allow_origin="*")
rate_limiter = RateLimiter(app)
bible_verses = load_verses()


@rate_limit(1, timedelta(seconds=2))
@app.get("/bible")
async def bible():
    # TODO: maybe one day include the testament
    search = request.args["search"]

    verse = next((verse for verse in bible_verses if search in verse),
                 None)

    if verse is None:
        return jsonify({"error": "Not found"})

    return jsonify({"verse": verse})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
