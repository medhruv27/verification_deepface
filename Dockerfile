FROM python:3.8

# RUN apt-get update && apt-get install -y \
#     libgl1-mesa-glx \
#     libglib2.0-0

ADD main.py .
ADD haarcascade_frontalface_default.xml .
ADD input/ ./input/

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install deepface opencv-python numpy

RUN mkdir output

CMD ["python","./main.py"]