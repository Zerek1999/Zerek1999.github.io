from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/aboutMe')
def about_me():
    return render_template('aboutMe.html')


@app.route('/woolworth&colesSystem')
def woolworth_coles_system():
    return render_template('woolworth&colesSystem.html')


@app.route('/efficientSimilarityJoin')
def efficient_similarity_join():
    return render_template('efficientSimilarityJoin.html')


@app.route('/kaggleDataAnalysisModeling')
def kaggle_data_analysis_modeling():
    return render_template('kaggleDataAnalysisModeling.html')

if __name__ == '__main__':
    app.run(debug=True)
