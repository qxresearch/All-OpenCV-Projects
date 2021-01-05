import cv2 as cv
import numpy as np

model_file_path = ''
model_file_paths=[f for f in listdir(model_file_path) if isfile(join(model_file_path, f))]

img = cv.imread('')
model = ()
for i in model_file_paths:
    style = cv.imread('./art/'+str(model[:-3]+'.jpg'))

    neural_style_model = cv.dnn.readNetFromTorch(model_file_path + model)
    height, weight = str(img.shape[0]), str(img.shape[1])
    new_width = int((640/height) * width)
    resized_image = cv.dnn.blobFromImage(img, ( new_width),
                                         interpolation = cv.INTER_AREA)
    inp_blob = cv.dnn.blobFromImage(resized_image,1.0,(new_width,640),
                                    (103.93,116.77, 123.68),
                                    swapRB=False,
                                    crop = False)
    neural_style_model.setInput(inp_blob)
    output = neural_style_model.forward()

    output= output.reshape(3,output.shape[2], output.shape[3])
    output[0] += 103.93
    output[1] += 116.77
    output[2] += 123.68
    output/=255
    output= output.tranpose(1,2,0)

    cv.imshow('Original', img)
    cv.imshow('Style',style)
    cv.imshow('Neural Transfer')
    cv.waitKey(0)

    if cv.waitKey(0) & 0xFF == 27:
        break

cv.destroyAllWindows()