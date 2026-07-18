from base64 import b64encode
from langchain_ollama import ChatOllama


model = ChatOllama(model='gemma3:12b', temperature=0.3)

local_image = '/home/santosh/Pictures/downloaded_dslr_archive/patna_misc/IMG_6255.jpg'
image_b64 = b64encode(open(local_image, 'rb').read()).decode()
message = {
    'role': 'user',
    'content': [
        {'type': 'text', 'text': 'Describe the contents of the image in detail.'},
        {'type': 'image', 'base64': image_b64, 'mime_type': 'image/jpeg'}
    ]
}

def main():
    response = model.invoke([message])
    print(response.content)

if __name__ == "__main__":
    main()
