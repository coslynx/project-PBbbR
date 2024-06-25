import os
from flask import Flask, request, jsonify
import pandas as pd
from room_allocation import allocate_rooms
from email_notifications import send_email_notification

app = Flask(__name__)

UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['csv']

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'group_file' not in request.files or 'hostel_file' not in request.files:
        return jsonify({'error': 'Missing files in the request'})

    group_file = request.files['group_file']
    hostel_file = request.files['hostel_file']

    if group_file.filename == '' or hostel_file.filename == '':
        return jsonify({'error': 'No selected files'})

    if group_file and allowed_file(group_file.filename) and hostel_file and allowed_file(hostel_file.filename):
        group_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'group.csv')
        hostel_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'hostel.csv')
        
        group_file.save(group_filename)
        hostel_file.save(hostel_filename)
        
        group_data = pd.read_csv(group_filename)
        hostel_data = pd.read_csv(hostel_filename)
        
        allocated_rooms = allocate_rooms(group_data, hostel_data)
        
        allocated_rooms.to_csv('output/allocated_rooms.csv', index=False)
        
        send_email_notification()
        
        return jsonify({'message': 'Files uploaded successfully and rooms allocated'})

    return jsonify({'error': 'File format not supported. Please upload CSV files only'})

if __name__ == '__main__':
    app.run(debug=True)