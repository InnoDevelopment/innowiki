# innowiki

# set up

create volume `wiki-data`:

`$ docker volume create --name wiki-data`

place these files:

`wiki.env`:

```
LDAP_URI=ldap://...
BIND_DN=...
BIND_PW=...
```

ssl:

* ./ssl/cert.pem
* ./ssl/privkey.pem
