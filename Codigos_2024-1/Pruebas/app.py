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
    
    
    # Convertir la matriz a una cadena para mostrarla
    result_str = '\n'.join([','.join(map(str, row)) for row in villa_matrix])
    for i in range(len(graph)):
        print(graph[i])
    
    print()
    print(villa_matrix)
    print()
    print(result_str)
    
    return render_template('result.html', result=result_str)

if __name__ == '__main__':
    app.run(debug=True)
