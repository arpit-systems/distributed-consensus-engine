from crypto_utils import sign_message, verify_signature

msg = "TX001 : Pay Rs 100"

sig = sign_message(msg)

print("Verification:",
      verify_signature(msg, sig))
