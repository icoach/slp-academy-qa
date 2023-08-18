from flask import Flask, jsonify, request
from flask_cors import CORS
import ssl
from qa import setup, query
import markdown

app = Flask(__name__)
CORS(app) 
chain = setup()

@app.route('/ai', methods=['POST'])
def ai_endpoint():
    question = request.json.get('question')
    if not question:
        return jsonify({"error": "Question not provided"}), 400
    response = query(chain, question)

    if response and response['answer']:
        response['answer'] = markdown.markdown(response['answer'])

    if response and response['sources']:
        response['sources'] = markdown.markdown(response['sources'])

    return jsonify(response)

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_cert_chain(certfile='./cert/localhost.crt', keyfile='./cert/localhost.key')
    app.run(host='localhost', port=8008, ssl_context=context)
