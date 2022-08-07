# ocr-translator

a quick demo, reading a russian image with OCR, and translating it to english

### build the container:
```
docker build -t pyocrrus .
```

### run the image (formatted for powershell with $(pwd) - may need adjustment for linux)
```
docker run --rm -it -v "$(pwd)\files:/files" --name=pyocrrus pyocrrus /files/rus.png rus
```

###  debug/code in the container (be sure to go to the src dir, as the original during build goes to WORKDIR app)
```
docker run --rm -it -v "$(pwd)\files:/files" -v "$(pwd)\src:/src" --entrypoint /bin/bash --name=pyocrrus pyocrrus
```
