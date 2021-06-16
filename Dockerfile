FROM python:3.9


WORKDIR /youtube-fetcher .

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./ ./ 

EXPOSE 5000

EXPOSE 8000

COPY runner.sh /scripts/runner.sh
RUN ["chmod", "+x", "/scripts/runner.sh"]
ENTRYPOINT [ "/scripts/runner.sh" ]