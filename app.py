"""DELIBERATELY VULNERABLE — BreachLens SAST test target. Do NOT deploy."""
import hashlib
import sqlite3
import subprocess

from flask import Flask, request

from config import DB_PASSWORD  # noqa: F401  (hardcoded secret imported for realism)

app = Flask(__name__)


@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    # SAST: OS command injection — untrusted input concatenated into a shell command.
    return subprocess.check_output("ping -c 1 " + host, shell=True)


@app.route("/calc")
def calc():
    expr = request.args.get("expr", "1+1")
    # SAST: code injection — eval() on untrusted input.
    return str(eval(expr))


@app.route("/user")
def user():
    uid = request.args.get("id", "1")
    conn = sqlite3.connect("app.db")
    # SAST: SQL injection — query built by string concatenation.
    return str(conn.execute("SELECT * FROM users WHERE id = '" + uid + "'").fetchall())


def hash_password(pw: str) -> str:
    # SAST: weak/insecure hash (MD5) used for a password.
    return hashlib.md5(pw.encode()).hexdigest()


if __name__ == "__main__":
    # SAST: Flask debug server (interactive Werkzeug console = RCE) bound to all interfaces.
    app.run(host="0.0.0.0", port=5000, debug=True)
