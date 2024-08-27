f = open('Files/IMG_KLGNG.jpg', 'rb')

f1 = open('Files/IMG_KLGNG_CPY.jpg', 'wb')

for data in f:
    f1.write(data)
