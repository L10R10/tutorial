from flask import Flask, request, make_response, render_template_string

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
    # Obtener el valor de la cookie
    username = request.cookies.get('username')
    
    # HTML para mostrar la página
    html = '''
    <!doctype html>
    <title>Gestión de Cookies</title>
    <h1>Bienvenido a la página de gestión de cookies</h1>
    {% if username %}
        <p>Hola, {{ username }}! Has visitado esta página antes.</p>
    {% else %}
        <p>¡Hola! Por favor, ingresa tu nombre para que podamos recordarlo.</p>
        <form action="/setcookie" method="post">
            <input type="text" name="username" placeholder="Ingresa tu nombre" required>
            <input type="submit" value="Enviar">
        </form>
    {% endif %}
    '''

    return render_template_string(html, username=username)

# Ruta para establecer la cookie
@app.route('/setcookie', methods=['POST'])
def setcookie():
    username = request.form['username']
    resp = make_response(f'Cookie establecida para {username}!')
    resp.set_cookie('username', username)
    return resp

# Ruta para eliminar la cookie
@app.route('/deletecookie')
def deletecookie():
    resp = make_response('Cookie eliminada!')
    resp.set_cookie('username', '', expires=0)
    return resp

if __name__ == '__main__':
    app.run(debug=True)