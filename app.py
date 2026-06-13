import pickle
import json
from pathlib import Path

import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Carga del modelo al arrancar (una sola vez)
# ---------------------------------------------------------------------------
MODEL_PATH = Path('models') / 'lightgbm_california.pkl'
META_PATH  = Path('models') / 'lightgbm_california_metadata.json'

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

with open(META_PATH) as f:
    metadata = json.load(f)

FEATURES = metadata['features']

# ---------------------------------------------------------------------------
# Rutas
# ---------------------------------------------------------------------------
@app.route('/')
def index():
    return jsonify({'status': 'ok', 'model': metadata['model'], 'version': metadata['exported_at']})


@app.route('/health')
def health():
    return jsonify({'status': 'ok'})


@app.route('/predict', methods=['POST'])
def predict():
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({'error': 'Se esperaba JSON en el cuerpo de la petición'}), 400

    missing = [f for f in FEATURES if f not in body]
    if missing:
        return jsonify({'error': f'Faltan features: {missing}'}), 422

    try:
        values = np.array([[float(body[f]) for f in FEATURES]])
    except (TypeError, ValueError) as e:
        return jsonify({'error': f'Valor no numérico: {e}'}), 422

    prediction = model.predict(values)[0]
    return jsonify({
        'prediction': round(float(prediction), 4),
        'unit': '100k USD',
        'features_used': FEATURES,
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
