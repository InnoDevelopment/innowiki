FROM dperson/moinmoin

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
      ca-certificates \
      python-ldap \
      && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ADD ./wikiconfig.py /usr/local/share/moin/wikiconfig.py

ADD ./moinmoin-memodump/memodump.py /usr/local/share/moin/data/plugin/theme
ADD ./moinmoin-memodump/memodump    /usr/local/lib/python2.7/dist-packages/MoinMoin/web/static/htdocs/memodump

VOLUME ["/usr/local/share/moin/data"]
