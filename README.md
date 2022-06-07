# Automatic License Plate Reader Application

## Overview

## Method

## Results

## Usage
### Installation
```bash
https://github.com/KapilM26/license-plate-reader.git
cd license-plate-reader
pip3 install -r requirements.txt
```
It is recommended to create a virtual environment for this project.
### Preliminary application setup
#### Email.config
The application uses a file called `email.config` to get the Email ID and password of the account to send the email to the offender.
Create the file `email.config` inside the `alpr/` folder.
The first line of this file should have the email ID and the second line should have the password.
Make sure not to push this file to Github!

#### Download/train model
The pretrained YOLOv3 model can be downloaded from here: https://drive.google.com/file/d/14sR8yAX-ByUxUGARqr3YU5vmnuaNeSbZ/view?usp=sharing
Download this file and put it inside `alpr/models`.
Alternatively, you can refer to the `train_yolo_alpr` notebook to train a custom model.

YOLO implementation used: https://github.com/eriklindernoren/PyTorch-YOLOv3

Dataset used for training: https://web.inf.ufpr.br/vri/databases/ufpr-alpr/

### Running the application
```bash
cd alpr
python3 manage.py runserver
```
This will run a local server on http://127.0.0.1:8000/
You can also run a server on a particular IP address by specifying it (along with the port) in the runserver command.
```bash
python3 manage.py runserver <IP>:<PORT>
```

## Ref:
Pipeline: Object Detection (YOLO) -> Crop & Preprocess -> OCR -> Database Search


## To do:
- [ ] Overview
- [ ] Method and Block diagram
- [ ] Results
- [x] Usage
- [x] Add pipfile/requirements.txt
