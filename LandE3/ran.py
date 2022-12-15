# Write your code here :-)
import base64

message_bytes = b'zpXOmc6jzpHOmSDOnM6ZzpEgzqDOkc6bzpnOn86SzqXOls6fzqUgKM6VzqDOmc6jzpfOoyDOo86WzqApIM6RzpvOm86RIM6VzpnOo86RzpkgzpzOmc6RIM6azqnOm86fzpLOpc6Wzp/OpQ=='

message = base64.b64decode(message_bytes).decode('utf-8')

print(message)
