# Flask Image Processing App Documentation

This documentation provides an overview of a Flask web application for image processing. The app includes features to apply a transparent filter, change image background, and enhance image quality.

## Table of Contents
1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Endpoints](#endpoints)
   - [1. Apply Transparent Filter (`/apply_filter`)](#1-apply-transparent-filter-apply_filter)
   - [2. Change Image Background (`/image_bg`)](#2-change-image-background-image_bg)
   - [3. Enhance Image Quality (`/enhance`)](#3-enhance-image-quality-enhance)
4. [Docker Container](#docker-container)
5. [Usage](#usage)

## Introduction

The Flask Image Processing App is a web application built with Flask, allowing users to perform various image processing operations. It includes features to apply a transparent filter, change image background, and enhance image quality.

## Setup

To set up the app, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required packages by running `pip install Flask Pillow requests rembg`.
3. Clone the repository or download the source code.
4. Navigate to the project directory in the terminal.
5. Run the app using the command `python app.py`.
6. Access the app in your web browser at `http://127.0.0.1:5000/`.

## Endpoints

### 1. Apply Transparent Filter (`/apply_filter`)

- **Method:** POST
- **Parameters:**
  - `key`: Authentication key (must be 'alphabravocharlie1998').
  - `image`: Uploaded image file.
  - `img_url`: URL of an image to be used as a filter.

**Functionality:**
- Applies a transparent filter to the uploaded image.
- Supports the use of an external image as a filter.

### 2. Change Image Background (`/image_bg`)

- **Method:** POST
- **Parameters:**
  - `key`: Authentication key (must be 'alphabravocharlie1998').
  - `image`: Uploaded image file.
  - `img_bg_index`: Index specifying the background image to be used.

**Functionality:**
- Changes the background of the uploaded image using a specified background image.
- Background images are assumed to be in the 'Backgrounds' folder, named as '1.png', '2.png', etc.

### 3. Enhance Image Quality (`/enhance`)

- **Method:** POST
- **Parameters:**
  - `key`: Authentication key (must be 'alphabravocharlie1998').
  - `image`: Uploaded image file.

**Functionality:**
- Enhances the quality of the uploaded image by increasing sharpness and contrast.
- Returns the processed image.

## Docker Container

This Flask app is also available as a Dockerized container on Docker Hub. You can pull the image using:

```bash
docker pull usamarehmantararml/photolabzv1:v1.1
```

## Usage

1. Access the app through the web browser.
2. Follow the provided UI to perform image processing tasks.
3. Ensure the correct authentication key is provided for each operation.
4. Review the response for the processed image.


Feel free to contribute to the project by submitting issues or pull requests.

**Note:** Ensure proper security measures are in place when deploying this application in a production environment.
