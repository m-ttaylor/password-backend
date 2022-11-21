from flask import Flask, Response, jsonify, request
from flask_cors import CORS, cross_origin
from services.generation import generate_password

# app = Flask(__name__)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


incomes = [
    { 'description': 'salary', 'amount': 5000 }
]


@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204

@app.route('/generate')
def get_password():
  length = int(request.args.get('length')) or 4
  titlecase = request.args.get('titlecase') or False
  separators = request.args.get('separators').lower() == 'true' or False
  numbers = int(request.args.get('numbers')) or False
  print()
  print("separators value: ", separators)
  app.logger.debug(type(separators))
  app.logger.debug(f"separators value: {separators}")
  password = generate_password(
        titlecase=titlecase,
        separators=separators,
        length=length,
        numbers=numbers
      )
#   return Response(password, mimetype='text/plain')
  return {
        "passphrase": password, 
        "titlecase": titlecase, 
        "separators": separators, 
        "length": length, 
        "numbers": numbers
    }