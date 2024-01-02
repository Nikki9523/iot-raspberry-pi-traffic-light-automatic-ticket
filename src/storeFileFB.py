import firebase_admin
from firebase_admin import credentials, firestore, storage, db
import os

cred=credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'iot-project-compsci.appspot.com',
    'databaseURL': 'https://iot-project-compsci-default-rtdb.europe-west1.firebasedatabase.app/'
})

bucket = storage.bucket()

ref = db.reference('/')
home_ref = ref.child('file')
def store_file(fileLoc):

    filename=os.path.basename(fileLoc)

    # Store File in FB Bucket
    blob = bucket.blob(filename)
    outfile=fileLoc
    blob.upload_from_filename(outfile)
    print(blob.public_url)

def push_db(fileLoc, time):

  filename=os.path.basename(fileLoc)

  # Push file reference to image in Realtime DB
  home_ref.push({
      'image': filename,
      'timestamp': time}
  )

#update boolean to track if red light is active or not
def update_firebase_red_light_boolean(value):
    ref = db.reference("/red_light_value")
    ref.set(value)

#read value of boolean in firebase
def read_firebase_boolean(path):
    ref = db.reference(path)
    boolean_value = ref.get(path)
    return boolean_value

if __name__ == "__main__":
 update_firebase_red_light_boolean(True)