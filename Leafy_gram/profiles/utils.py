import uuid #universal unique identifier

def get_random_code():
    code = str(uuid.uuid4())[:10].replace('-','.').lower()
    return code