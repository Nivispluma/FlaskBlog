from flask import Flask, render_template, url_for,flash,redirect,session

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/hexpage')
def show_hex():
    return render_template("hexpage.html")
# ------------------------------- Error Handler ------------------------------------------------------------

# Error 404 - URL not found
@app.errorhandler(404)
def error_handler_page_404(e):
    return render_template("Errorpages/err404.html"), 404


# Error 500 - Internal Server Error
@app.errorhandler(500)
def error_handler_page_500(e):
    return render_template("Errorpages/err500.html"), 500


# -------------------------------------------------------------------------------
# run program


if __name__ == '__main__':
    app.run()
