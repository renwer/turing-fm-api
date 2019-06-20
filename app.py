import os
from flask_cors import CORS

from flask import Flask
from scale_graph_walking_no_pitch import scale_graph_walking_no_pitch

app = Flask(__name__)
app.debug = True
CORS(app)


# edit the API endpoint structure to allow for multiple algorithms
@app.route('/sequence')
def sequence():
    return scale_graph_walking_no_pitch.get_sequence()


if __name__ == '__main__':
    app.run()
    # pp.run(host='0.0.0.0', port=os.environ.get('PORT'))
