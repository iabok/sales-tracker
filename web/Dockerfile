FROM alpine

# Initialize
RUN mkdir -p /data/web
WORKDIR /data/web
COPY requirements.txt /data/web/
COPY package.json /data/web/

# Setup
RUN apk update
RUN apk upgrade
RUN apk add --update python3 python3-dev postgresql-client postgresql-dev \
                     build-base libffi-dev gettext bash curl nodejs \
                     nodejs-npm && npm install npm@latest -g
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

#install front-end dependencies
RUN npm install

# Clean
#RUN apk del -r python3-dev postgresql

# Prepare
COPY . /data/web/
RUN mkdir -p sales_app/static/admin
