from flask import Flask, Response
import os

app = Flask(__name__)

@app.get("/")
def root():
    return "<!doctype html><html><head><meta charset='utf-8'><title>Hola</title></head>" \
           "<body style='font-family: system-ui; text-align:center; margin-top:10vh'>" \
           "<h1>Hola mundo desde Python 🐍</h1>" \
           "<p>Refresca para ver el balanceo por HAProxy.</p>" \
           "</body></html>"

@app.get("/health")
def health():
    return Response("OK", mimetype="text/plain")

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
