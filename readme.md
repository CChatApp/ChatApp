#### _Documentation for ChatApp v1_
Typical Request:

A typical request might look like:
```
encrypted = authkey + ":" + Encrypt(methodID + ":" + encryptedData)

send ( pack("Q", len(encrypted)) + ecrypted )
```

in order to get your own auth key for that session you need to use the default temporary key.

as soon as you got your own authkey, you need to execute the method GetPG to get p,g for Diffie Hellman exchange protocol.

