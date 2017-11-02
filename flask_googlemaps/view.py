import flask
import logging

import config
import dataraw


app = flask.Flask(__name__)
if __name__ == "__main__":
    configuration = config.configuration()
else:
    # If we aren't main, the command line doesn't belong to us
    configuration = config.configuration(proxied=True)


restaurant = dataraw.process(open("data/eugene.txt"))
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY



@app.route("/")

@app.route("/index")
def index():
    app.logger.debug("main page entry")
    flask.g.restaurant = restaurant
    return flask.render_template("googlemapapi.html")
    # creating a map in the view

@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] =  flask.url_for("index")
    return flask.render_template('page_not_found.html'), 404

@app.route("/_listfy")
def listfy():
    app.logger.debug("Got a JSON request")
    #여기서부터 json html에서 써서 써야함
    global restaurant
    restaurant = dataraw.process(open("data/eugene.txt"))
    return flask.jsonify(restaurant = restaurant)
#returns like[{'address': ' 44.0442509,-123.0829474', 'name': ' Pegasus Pizza'}, ....]


if __name__ == "__main__":
    app.run(debug=True)