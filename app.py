from flask import Flask
from prometheus_client import make_wsgi_app, Counter
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

# Configurar métricas
REQUEST_COUNT = Counter('app_requests_total', 'Total web app requests')

@app.route('/')
def hello_world():
    REQUEST_COUNT.inc()
    return '¡Hola Mundo con python realizando un despliegue continuo v2!'

# Añadir endpoint para métricas
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
