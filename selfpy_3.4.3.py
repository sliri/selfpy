# 3.4.3
#################
encrypted_message = input('Please enter a string:')
encrypted_message_length = len(encrypted_message)
print(encrypted_message[:encrypted_message_length//2].lower() +
      encrypted_message[encrypted_message_length//2:].upper())


