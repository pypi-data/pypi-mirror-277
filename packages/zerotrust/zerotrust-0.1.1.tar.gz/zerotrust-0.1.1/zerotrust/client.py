import requests
from fastapi.encoders import jsonable_encoder

get_stream_url = "https://zt-ml-llm-new-arch.azurewebsites.net/zt-llm-get-stream/V4"

def call_zt_llm_get_stream_V4(llm, prompt, pii_array="", client_api_key="", user_query="", uploaded_file=None, fallback_llm=False, authorization=None):
    
    headers = {
        "Authorization": f"Bearer {authorization}"
    }
    
    data = {
        "llm": llm,
        "prompt": prompt,
        "pii_array": pii_array,
        "client_api_key": client_api_key,
        "user_query": user_query,
        "fallback_llm": fallback_llm
    }
    
    files = None
    if uploaded_file:
        files = {'uploaded_file': uploaded_file}
    
    response = requests.post(get_stream_url, headers=headers, data=data, files=files)
    
    # Return the JSON response
    return response.json()
