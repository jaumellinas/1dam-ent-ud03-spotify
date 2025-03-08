from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
DATABASE_PATH = "/tmp/canciones.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DATABASE_PATH}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    artista = db.Column(db.String(100), nullable=False)
    duracion = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f'<Cancion {self.titulo}>'

# Función para inicializar la base de datos si no existe
def init_db():
    if not os.path.exists(DATABASE_PATH):
        with app.app_context():
            db.create_all()

# Inicializa la base de datos al arrancar
init_db()
      
@app.route('/')
def get_canciones():
    canciones = Cancion.query.all()
    return render_template('canciones.html', canciones = canciones)
  
@app.route('/canciones/add', methods=['GET', 'POST'])
def add_cancion():
    if request.method == 'POST':
        titulo = request.form['titulo']
        artista = request.form['artista']
        duracion = request.form['duracion']
        link = request.form['link']

        if link.startswith("https://youtu.be"): 
            link = link.replace("https://youtu.be/", "https://www.youtube.com/embed/")
        else: 
            if link.startswith("https://www.youtube.com/watch?v="):
                link = link.replace("/watch?v=", "/embed/")
        # -------------------------------------------------------------------
        
        new_cancion = Cancion(titulo = titulo, artista = artista, duracion = duracion, link = link)
        db.session.add(new_cancion)
        db.session.commit()
        
        return redirect(url_for('get_canciones'))
    
    return render_template('add.html', cancion=None)
  
@app.route('/canciones/get')
def get_cancion_by_id():

    return render_template('get.html')
    
@app.route('/canciones/delete/<int:cancion_id>', methods=['POST'])
def delete_cancion(cancion_id):
    cancion = Cancion.query.get(cancion_id)
    if cancion:
        db.session.delete(cancion)
        db.session.commit()
        return redirect(url_for('get_canciones'))
    else:
        return jsonify({"error": "Canción no encontrada."}), 404
    
@app.route('/canciones/edit/<int:cancion_id>', methods=['GET', 'POST'])
def edit_cancion(cancion_id):
    cancion = Cancion.query.get(cancion_id)
    if not cancion:
        return "Canción no encontrada.", 404

    if request.method == 'POST':
        cancion.titulo = request.form.get('titulo')
        cancion.artista = request.form.get('artista')
        cancion.duracion = request.form.get('duracion')
        cancion.link = request.form.get('link')
        db.session.commit()
        return redirect(url_for('get_canciones'))

    return render_template('edit.html', cancion = cancion)

@app.route('/play/<int:cancion_id>', methods=['GET'])
def play_cancion(cancion_id):
    if cancion_id==0:
        cancion_id = request.args.get('cancion_id')
    canciones = Cancion.query.all()
    cancion = Cancion.query.get(cancion_id)
    return render_template('play.html', cancion=cancion, canciones=canciones)

if __name__ == '__main__':
    app.run(debug=True)