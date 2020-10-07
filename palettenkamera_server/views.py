from django.shortcuts import render
import picamera
import os


def home(request):
    with picamera.PiCamera() as camera:
        camera.resolution = (3280, 2464)
        camera.capture("/var/www/palettenkamera/media/bild.jpg")
    return render(request, 'home.html', {'bild': 'bild.jpg'})


def home_no(request, no):
    with picamera.PiCamera() as camera:
        camera.resolution = (3280, 2464)
        camera.capture("/var/www/palettenkamera/media/" + no + ".jpg")
    return render(request, 'home.html', {'bild': no + '.jpg'})


def delete(request, no):
    path = "/var/www/palettenkamera/media/" + no + ".jpg"
    if os.path.isfile(path):
        os.remove(path)
    return render(request, 'home.html', {})


def status(request):
    return render(request, 'home.html', {})
