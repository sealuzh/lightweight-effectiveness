FROM ubuntu:16.04

RUN apt-get update && \
  apt-get install -y --no-install-recommends locales && \
  locale-gen en_US.UTF-8 && \
  apt-get dist-upgrade -y && \
  apt-get --purge remove openjdk* && \
  echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections && \
  echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" > /etc/apt/sources.list.d/webupd8team-java-trusty.list && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \
  apt-get update && \
  apt-get install -y --no-install-recommends oracle-java8-installer oracle-java8-set-default && \
  apt-get clean all

RUN apt-get -y install maven

RUN apt-get update
RUN apt-get -y install git

RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv && \
  rm -rf /var/lib/apt/lists/*

RUN pip install pip --upgrade
RUN pip install wheel
RUN pip install pandas
RUN pip install GitPython
RUN pip install htmlparser

RUN apt-get update
RUN apt-get install -y python3-pip
RUN python3 -m pip install pip --upgrade
RUN python3 -m pip install GitPython
RUN python3 -m pip install pandas
RUN python3 -m pip install htmlparser

# Install Ruby.
RUN \
  apt-get update && \
  apt-get install -y ruby

RUN apt-get update
RUN apt-get install vim -y

RUN mkdir /home/ubuntu/
RUN mkdir /home/ubuntu/experiments
COPY *.py /home/ubuntu/experiments/
COPY run.sh /home/ubuntu/experiments
COPY projects.csv /home/ubuntu/experiments
# copy dir with stats and code for metrics
RUN mkdir /home/ubuntu/experiments/metrics
COPY metrics /home/ubuntu/experiments/metrics

# Define working directory.
WORKDIR /home/ubuntu/experiments

# Define default command.
CMD ["bash"]