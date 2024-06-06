import requests
import json

def generate_image(key, prompt, negative_prompt=None, width=512, height=512, safety_checker=False, seed=None, samples=1, base64=False, webhook=None, track_id=None):
    url = "https://modelslab.com/api/v6/realtime/text2img"
    payload = {
        "key": key,
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "width": str(width),
        "height": str(height),
        "safety_checker": safety_checker,
        "seed": seed,
        "samples": samples,
        "base64": base64,
        "webhook": webhook,
        "track_id": track_id
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.text