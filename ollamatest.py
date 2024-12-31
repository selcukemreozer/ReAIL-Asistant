import ollama
from time import time
import pyautogui as pag


# resolution of the screen
screenWidth, screenHeight = pag.size()
print("Screen resolution: ", screenWidth, screenHeight)
#start
start = time()
response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': f'''This image is a screenshot from my computer. The top left corner is (0,0). The bottom right corner is (1440,900).
        On some points of the image, there are their coordinate info. Use them as reference points. 
        Give me pixel coordinates of the mocomtool file
        in the image resolution of {screenWidth}x{screenHeight}.
        I do not need explanation, just the one coordinate. Example response: (100, 200)''',
        'images': ['image.png']
    }]
)

end = time()
# two decimal places
print("Time taken: ", round(end-start, 2))
print(response)

'''This image is a screenshot from my computer. Give me pixel coordinates of the apple logo
                                           in the image resolution of {screenWidth}x{screenHeight}.
                                           I do not need explanation, just the one coordinate. Example response: (100, 200)''',