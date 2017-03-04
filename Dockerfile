FROM dperson/moinmoin

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
      python-ldap \
      && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ADD ./wikiconfig.py /usr/local/share/moin/wikiconfig.py

