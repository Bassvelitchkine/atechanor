FROM python:3

WORKDIR /usr/src/app

COPY packages.txt ./
RUN pip install --no-cache-dir -r packages.txt

COPY . .

CMD [ "python", "app.py" ]