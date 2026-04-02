import openai
import base64
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_image(image_bytes):
    image_base64 = base64.b64encode(image_bytes).decode()

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this automobile engineering diagram clearly for students."},
                    {"type": "image_url", "image_url": f"data:image/png;base64,{image_base64}"}
                ],
            }
        ],
    )

    return response.choices[0].message.content