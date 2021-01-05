import cv2 as cv
import numpy as np

def neural_style_transfer(img, size=320,upscale=1):
    model_file_path='models/'
    style=cv.imread('art/' + str(model)[:-3] + '.jpg')
    neural_style_model = cv.dnn.readNetFromTorch(model_file_path + model + '.t7')

    height, weight = int(img.shape[0], int(img.shape[1]))
    new_width = int((size/height) * width)
    resized_image = cv.resize(img, (new_width, size), interpolation=cv.INTER_AREA)

    inp_blob = cv.dnn.blobFromImage((resized_image, 1.0, (new_width, size),(103.93,116.77, 123.68),
                                     swapRB=False),
                                    crop=False)
    neural_style_model.setInput(inp_blob)
    output = neural_style_model.forward()
    output= output.reshape(3,output.shape[2], output.shape[3])
    output[0] += 103.93
    output[1] += 116.77
    output[2] += 123.68
    output/=255
    output= output.tranpose(1,2,0)
    output = cv.resize(output, None , fx= upscale, interpolation=cv.INTER_LINEAR)

cap.VideoCapture('')
while True:
    ret, frame = cap.read()
    cv.imshow('Neural Style Transfer Video',
              neural_style_transfer(frame,'starry_night'),
              320,2)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.releast()
cv.destroyAllWindows()