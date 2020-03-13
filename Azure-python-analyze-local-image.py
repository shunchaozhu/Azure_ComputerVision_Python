import requests
# If you are using a Jupyter notebook, uncomment the following line.
# %matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# Add your Computer Vision subscription key and endpoint to your environment variables.
# You need to update the SUBSCRIPTION_KEY to
# they key for your Computer Vision Service
SUBSCRIPTION_KEY = "xxxxxxxxxxxxxxxxxx"

# You need to update the vision_service_address to the address of
# your Computer Vision Service
vision_service_address = "https://pythonimagelearning.cognitiveservices.azure.com/vision/v2.1/"

analyze_url = vision_service_address + "analyze"

# Set image_path to the local path of an image that you want to analyze.
image_path = "C:/Users/Administrator/Desktop/1.png"

# Read the image into a byte array
image_data = open(image_path, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
           'Content-Type': 'application/octet-stream'}
params = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(
    analyze_url, headers=headers, params=params, data=image_data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
analysis = response.json()
print(analysis)
image_caption = analysis["description"]["captions"][0]["text"].capitalize()

# Display the image and overlay it with the caption.
image = Image.open(BytesIO(image_data))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)
