from flask import Flask, jsonify, request,render_template
from flask_cors import CORS, cross_origin
from file_handler import FileHandler

app = Flask(__name__)
cors = CORS(app)

is_api = False


@app.route('/', methods = ['GET'])
def home():
    file_data = None
    file_name = request.args.get('file_name')
    start_line = request.args.get('start_line')
    end_line = request.args.get('end_line')
    file_obj = FileHandler(file_name,start_line,end_line)
    file_data = file_obj.fileProcess()
    if not is_api:
        return render_template(
            'index.html',
            file_data= file_data['file_data']
        )
    else:

        return jsonify({'file_data':file_data})


if __name__ == '__main__':
	app.run(debug = True)
