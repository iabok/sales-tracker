FROM alpine

# Initialize
RUN mkdir -p /data/web
WORKDIR /data/web
COPY requirements.txt /data/web/
COPY package.json /data/web/

# Setup
RUN apk update
RUN apk upgrade
RUN apk add --update python3 python3-dev postgresql-client postgresql-dev build-base gettext

# Install node from NodeSource
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get install -y nodejs

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

#install front-end dependencies
RUN npm install

# Clean
RUN apk del -r python3-dev postgresql

# Prepare
COPY . /data/web/
RUN mkdir -p sales_app/static/admin
