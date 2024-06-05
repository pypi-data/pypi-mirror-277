# License tool for yFiles Graphs for Jupyter

## Requirements

You need the private key to create licenses. 
Ask Fabian or Jasmine for the private key.

Then create a `/server/.env` file with the private key as `PKCS8_PRIVATE_KEY` content. For example:
```text
PKCS8_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----
                   MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDm5RmTfVFc88WU
                   ...
                   ZpI98JWvTmJPUkEeiRbW3Z7f
                   -----END PRIVATE KEY-----"
```
The header, footer, newlines and spaces are removed upon usage in the server.

## Start license server

This Express.js server signs the license objects with the given private key.

Start the server with
```shell
npm run start-server
```

## Start the license creation frontend

This simple Vite.js frontend provide an input form for the license data 
and connects to the running license server to signe the license with the
private key.

Start the frontend with
```shell
npm run start-frontend
```