from app import app
from flask import render_template, request


@app.errorhandler(404)
def notFound(e):
    print(e)
    return render_template("public/404.html")

@app.errorhandler(500)
def serverError(e):
    app.logger.error(f"Server error: {e}, route: {request.url}")
   

    return render_template("public/500.html")


@app.errorhandler(403)
def forbidden(e):
    app.logger.error(f"Forbidden: {e}, route: {request.url}")
   

    return render_template("public/403.html")

