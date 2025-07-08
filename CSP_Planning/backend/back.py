from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from scheduler_repetition import RepetitionScheduler



app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8000"}})

UPLOAD_FOLDER = "uploads"
RESULT_FILE = "planning_repetitions.xlsx"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        dispo_file = request.files['disponibilites']
        repart_file = request.files['repartition']
        maybe_penalty = int(request.form['maybe_penalty'])
        max_load = int(request.form['max_load'])
        load_penalty = int(request.form['load_penalty'])
        group_bonus = int(request.form['group_bonus'])

        dispo_path = os.path.join(UPLOAD_FOLDER, dispo_file.filename)
        repart_path = os.path.join(UPLOAD_FOLDER, repart_file.filename)

        dispo_file.save(dispo_path)
        repart_file.save(repart_path)
        #print("debug: Fichiers reçus :", dispo_path, repart_path)
        #print("debug: Paramètres :", maybe_penalty, max_load, load_penalty, group_bonus)


        # Instanciation de ton planificateur
        planner = RepetitionScheduler(
            repart_path, dispo_path,
            maybe_penalty, max_load, load_penalty, group_bonus
        )

        planner.generer_planning()
        planner.export_planning(RESULT_FILE)
        json_data = planner.get_json_data()
        return jsonify(json_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/download', methods=['GET'])
def download():
    try:
        return send_file(RESULT_FILE, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5050)
