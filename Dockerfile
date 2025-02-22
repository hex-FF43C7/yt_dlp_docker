FROM python:3.11

RUN apt update
RUN apt install -y nano
RUN apt install -y ffmpeg
# RUN set -x \
#     && add-apt-repository ppa:mc3man/trusty-media \
#     && apt-get update \
#     && apt-get dist-upgrade \
#     && apt-get install -y --no-install-recommends ffmpeg

WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app/code
CMD [ "python3", "nrm_entry.py" ]