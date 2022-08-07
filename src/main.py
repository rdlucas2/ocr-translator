import argparse
import textract
from translate import Translator

parser = argparse.ArgumentParser(description="Perform OCR on file.")
parser.add_argument("file", type=str, help="path to the file to run OCR against")
parser.add_argument(
    "language",
    type=str,
    help="language to read for OCR (a valid tesseract language - see https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html)",
)

args = parser.parse_args()
print(args.__dict__)

text = textract.process(args.file, method="tesseract", language=args.language)

decoded = text.decode()

print(decoded.strip())

#TODO: the translator piece needs work, and doing this with this library gets you rate limited - but sending small chunks was better as longer ones seem to error
translator = Translator(from_lang="Russian", to_lang="English")
for line in decoded.splitlines():
    print(line)
    try:
        translation = translator.translate(line)
        print(translation)
    except:
        print(f'Trouble translating: {line}')
