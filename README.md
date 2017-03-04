# innowiki

# set up

create volume `wiki-data`:

`$ docker volume create --name wiki-data`

place these files:

`wiki.env`:

```
BIND_DN=...
BIND_PW=...
```

ssl:

* ./ssl/cert.pem
* ./ssl/privkey.pem
