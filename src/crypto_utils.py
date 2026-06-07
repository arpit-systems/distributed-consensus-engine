import hashlib

def sign_message(message):
    return hashlib.sha256(message.encode()).hexdigest()

def verify_signature(message, signature):
    return hashlib.sha256(message.encode()).hexdigest() == signature
