from flask import Flask, request, send_file
from flask_cors import CORS
from cvFunc import TransformVideo
import io
from logging.config import dictConfig
import logging
from dotenv import load_dotenv
from jwt_midl import check_token

load_dotenv()

# logging.basicConfig(filename='record.log', level=logging.INFO, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'formatters': {
        'Simple_Format': {
            'format': 'Level: {levelname},  {message}',
            'style': '{',
        }
    },

    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'Simple_Format',
            'filename': "data.log",
        }
    },

    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}


dictConfig(LOGGING)

app = Flask(__name__)
CORS(app)

@app.before_request
def Middleware():
    print('Incomming request')
    resp = check_token()
    try: 
        if not resp[1]:
            return resp[0]
    except:
        pass

@app.route('/', methods = ['POST', 'GET'])
def main():
    print("Access to the API granted")
    app.logger.info("New request")

    if request.method == 'POST':
        app.logger.info("----- Incomming Post request -----")
        data = request.files["image"]
        fileName = request.form.get('name')
        fileExtension = request.form.get('fileExtension')

        print(request.form)

        content = data.read()

        with open("videos/"+fileExtension, 'wb') as _file:
            _file.write(content)

        TransformVideo("videos/"+fileExtension, fileName)

        path = f"gifs/{fileName}.gif"

        # with open(path, 'rb') as _file:
        #     If we dont handle the MultiPartFormData, an error will pop up
        #     content = _file.read()
        #     print("Type of data", type(content))
        #     print(content)
        #     return _file.read()

        return send_file(path, as_attachment=True)

    # source = request.args.get("user")
    print("Icomming request")
    # return "Flask running"
    path = "{fileName}.gif"
    return "Done"


app.run(debug=True)