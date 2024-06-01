from flask import Flask, render_template

app = Flask(__name__)

# Crop data
crops = {
    'wheat': {
        'name': 'Wheat',
        'about': 'Wheat is a cereal grain originally from the Levant region but now cultivated worldwide.',
        'species': 'Triticum spp.',
        'type': 'Cereal grain',
        'optimum_plantation': 'Wheat grows best in temperatures between 12°C to 25°C (54°F to 77°F) with annual rainfall of 30-100 cm.',
        'optimum_storage': 'Wheat should be stored in cool, dry conditions with a temperature below 15°C and relative humidity below 65%.',
        'soil_type': 'Loam or clay loam soils with a pH range of 6.0 to 7.5 are ideal for wheat cultivation.',
        'yield_per_hectare': 'The potential yield of wheat can vary from 2.5 to 8 tons per hectare depending on the variety and growing conditions.'
    },
    'corn': {
        'name': 'Corn',
        'about': 'Corn is a large grain plant first domesticated by indigenous peoples in southern Mexico.',
        'species': 'Zea mays',
        'type': 'Cereal grain',
        'optimum_plantation': 'Corn grows best in temperatures between 18°C to 27°C (64°F to 81°F) with annual rainfall of 60-120 cm.',
        'optimum_storage': 'Corn should be stored in cool, dry conditions with a temperature below 15°C and relative humidity below 60%.',
        'soil_type': 'Well-drained loamy soil with a pH range of 5.8 to 7.0 is ideal for corn cultivation.',
        'yield_per_hectare': 'The potential yield of corn can vary from 4 to 10 tons per hectare depending on the variety and growing conditions.'
    }
    # Add more crops as needed
}

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/crops')
def crops_page():
    return render_template('crops.html', crops=crops)

@app.route('/crops/<crop_name>')
def crop_detail(crop_name):
    crop = crops.get(crop_name)
    if crop:
        return render_template('crop_detail.html', crop=crop)
    else:
        return "Crop not found", 404

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    app.run(debug=True)

