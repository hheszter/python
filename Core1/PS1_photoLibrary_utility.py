import os, shutil, json
from PIL import Image, ExifTags

# folderPath = input("Enter the folder name:")
folderPath = "c:/Users/Pictures/"
destinationFolder = folderPath + "DATE_"
finalText = ""
if os.path.exists(folderPath):
    files = [ photo for photo in os.listdir(folderPath) if photo.lower().endswith(".jpg") or photo.lower().endswith(".png")]        #a mappában jpg és png file-ok vannak

    for imagePath in files:
        fullPath = os.path.join(folderPath, imagePath)
        img = Image.open( fullPath )
        photoData = img._getexif()                                  #fotok adatai kimentve dictionary-be
        if not photoData: continue
        date, cam1, cam2, iso, w, l = None, None, None, None, None, None        #alapertelmezetten None

        for key, value in photoData.items():                        #itt kiszedjük az exifből az adatokat es feltöltődnek a változók
            if not key in ExifTags.TAGS: continue
            # print(ExifTags.TAGS[key])                               # ?

            if ExifTags.TAGS[key] == "DateTime":
                date = value
                dateFolder = destinationFolder + (value[0:7]).replace(":", "_")  # datum alapjan mappakba masolja a fotokat
                if not os.path.exists( dateFolder ):
                    os.mkdir( dateFolder )
                shutil.copy2(folderPath + imagePath, dateFolder + "/" + imagePath)

            if ExifTags.TAGS[key] == "Make": cam1 = value
            if ExifTags.TAGS[key] == "Model": cam2 = value
            if ExifTags.TAGS[key] == "ISOSpeedRatings": iso = value
            if ExifTags.TAGS[key] == "ImageWidth": w = value
            if ExifTags.TAGS[key] == "ImageLength": l = value

        finalText += "Filename: {}\n-----\nDate: {}\nCamera: {} {}\nISO: {}\nDimension: {} x {}\n\n-----\n".format(imagePath, date,cam1,cam2,iso,w,l)

else:print ("no result")

with open(folderPath + "exif_data.txt","w") as f:
    f.write(finalText)

with open(folderPath + "exif_data.json","w") as f:
    json.dump(finalText,f)

print (finalText)