FROM dawn001/z_mirror:main

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

COPY requirements.txt .
RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt
EXPOSE 8000
COPY . .

CMD ["bash", "start.sh"]
