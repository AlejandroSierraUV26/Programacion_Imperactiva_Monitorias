from flask import Flask, render_template, request
import proyecto

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Obtener datos del formulario
    graph_data = request.form['graph_data']
    
    # Procesar datos y guardar en archivo sin saltos de línea adicionales
    graph_lines = [line.strip() for line in graph_data.strip().split('\n') if line.strip()]
    with open('archivo.txt', 'w') as file:
        for line in range(len(graph_lines)):
            if line == len(graph_lines) - 1:
                file.write(graph_lines[line])
            else:
                file.write(graph_lines[line] + '\n')
    
    # Procesar el archivo y obtener la matriz resultante
    graph = proyecto.obtener_datos_txt('archivo.txt')
    colors, current_color = proyecto.coloreo(graph)
    villa_matrix = proyecto.generar_matrix(colors, current_color)

    villas = {}
    for i, color in enumerate(colors):
        if color + 1 not in villas:
            villas[color + 1] = []
        villas[color + 1].append(f'Equipo {i + 1}')  

    sorted_villas = dict(sorted(villas.items()))

    villas_str = '\n'.join([f'Villa {villa}: {", ".join(teams)}' for villa, teams in sorted_villas.items()])

    result_str = '\n'.join([','.join(map(str, row)) for row in villa_matrix])

    return render_template('result.html', result=result_str, villas=villas_str)

if __name__ == '__main__':
    app.run(debug=True)
