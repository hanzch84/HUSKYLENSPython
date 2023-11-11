import smbus
import time

bus = smbus.SMBus(1)

HURSKY_ADRESS = 0x32

def read_data(adress):
    try:
        data = bus.read_i2c_block_data(adress,0x32, 16)
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def get_face_recognition_data():
    data = read_data(HURSKY_ADRESS)
    if data:
        number_of_faces = data[0]
        if number_of_faces > 0:
            print(f"detected {number_of_faces} face(s)")
        else:
            print("No faces detected")
    else:
        print("Fail to read data")



while True:
    get_face_recognition_data()
    time.sleep(1)