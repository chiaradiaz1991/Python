

userVariable = ""

userMessage = input(f"insert text: {userVariable}")
userMessageLength = len(userMessage)

print(userMessageLength)
print(userMessage)

if userMessageLength > 100:
    print(userMessage)
if userMessageLength > 50 and userMessageLength < 100:
    print(userMessage[::-1])
else:
    print("Su mensaje es demasiado corto.")
