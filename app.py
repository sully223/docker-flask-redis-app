import os
from flask import Flask, render_template, jsonify
import redis

app = Flask(__name__)
redis_client = redis.Redis(
    host=os.environ.get('REDIS_HOST', 'redis'),
    port=int(os.environ.get('REDIS_PORT', 6379)),
    decode_responses=True,
)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/count')
def count():
    visits = redis_client.incr('visit_count')
    return render_template('count.html', visits=visits)

@app.route('/count/api')
def count_api():
    visits = redis_client.incr('visit_count')
    return jsonify(visits=visits)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
