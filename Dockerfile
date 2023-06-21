FROM python:3.9

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . tgbot
WORKDIR tgbot 

ENTRYPOINT ["/usr/local/bin/python"] 
CMD ["/tgbot/bot.py"]