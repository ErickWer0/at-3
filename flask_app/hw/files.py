#!/usr/bin/env python3

import os.path
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from flask_autoindex import AutoIndex
from werkzeug.utils import secure_filename

files = Blueprint('files', __name__)

UPLOAD_FOLDER = os.path.join(os.path.curdir, "hw/files")
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'}

files_index = AutoIndex(files, os.path.curdir + '/hw/files', add_url_rules=False)
@files.route('/files')
def autoindex(path='.'):
    return files_index.render_autoindex(path)

@files.route('/download')
@login_required
def download():
    #print(os.path.exists(UPLOAD_FOLDER))
    #return UPLOAD_FOLDER
    return redirect(url_for('files.autoindex'))
##########################################
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@files.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('files.upload', filename=filename))
    return render_template('upload.html')