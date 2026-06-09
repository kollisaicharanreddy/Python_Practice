def process_api_response(status_code, json_payload):
    if status_code==200:
        data = json_payload
        print(data.get("user_id"))
    else:
        print("Connection failed")
process_api_response(200, {"user_id": 12345})
