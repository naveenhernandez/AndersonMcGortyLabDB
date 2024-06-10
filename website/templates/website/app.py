from flask import Flask, request, render_template

app = Flask(__name__)

# Sample data
materials = [
    {"name": "Material 1", "description": "Description of Material 1"},
    {"name": "Material 2", "description": "Description of Material 2"},
    {"name": "Material 3", "description": "Description of Material 3"},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query', '')
    results = [material for material in materials if query.lower() in material['name'].lower()]
    return render_template('search_results.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
