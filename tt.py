import datetime
from PIL import Image
from PIL.ExifTags import TAGS
import piexif

def set_exif_date_taken(image_path, new_date_taken):
    # Open the image
    img = Image.open(image_path)
    
    # Get the existing Exif metadata
    exif_data = img._getexif()
    
    # Tag for the "Date and Time (Original)" Exif property
    exif_date_tag = 0x9003
    
    # Convert the new date taken to the Exif format (string)
    new_exif_date = new_date_taken.strftime("%Y:%m:%d %H:%M:%S")
    
    # Update the Exif metadata with the new date taken
    if exif_data is not None and exif_date_tag in exif_data:
        exif_data[exif_date_tag] = new_exif_date
        img.save(image_path, exif=exif_data)
        print("Date taken updated successfully.")
    else:
        print("No Exif metadata found or no date tag.")

if __name__ == "__main__":
    image_path = r'C:\Users\Omer\Desktop\444.jpg'
    new_date_taken = datetime.datetime(2020, 1, 20, 11, 1, 0)  # Replace with your desired date and time
    set_exif_date_taken(image_path, new_date_taken)
    print("done")
