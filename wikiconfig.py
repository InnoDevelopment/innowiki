# -*- coding: iso-8859-1 -*-
# IMPORTANT! This encoding (charset) setting MUST be correct! If you live in a
# western country and you don't know that you use utf-8, you probably want to
# use iso-8859-1 (or some other iso charset). If you use utf-8 (a Unicode
# encoding) you MUST use: coding: utf-8
# That setting must match the encoding your editor uses when you modify the
# settings below. If it does not, special non-ASCII chars will be wrong.

"""
    MoinMoin - Configuration for a single wiki

    If you run a single wiki only, you can omit the farmconfig.py config
    file and just use wikiconfig.py - it will be used for every request
    we get in that case.

    Note that there are more config options than you'll find in
    the version of this file that is installed by default; see
    the module MoinMoin.config.multiconfig for a full list of names and their
    default values.

    Also, the URL http://moinmo.in/HelpOnConfiguration has
    a list of config options.

    ** Please do not use this file for a wiki farm. Use the sample file
    from the wikifarm directory instead! **
"""

import os

from MoinMoin.config import multiconfig, url_prefix_static


class Config(multiconfig.DefaultConfig):

    # Critical setup  ---------------------------------------------------

    # Directory containing THIS wikiconfig:
    wikiconfig_dir = os.path.abspath(os.path.dirname(__file__))

    # We assume that this config file is located in the instance directory, like:
    # instance_dir/
    #              wikiconfig.py
    #              data/
    #              underlay/
    # If that's not true, feel free to just set instance_dir to the real path
    # where data/ and underlay/ is located:
    #instance_dir = '/where/ever/your/instance/is'
    instance_dir = wikiconfig_dir

    # Where your own wiki pages are (make regular backups of this directory):
    data_dir = os.path.join(instance_dir, 'data', '') # path with trailing /

    # Where system and help pages are (you may exclude this from backup):
    data_underlay_dir = os.path.join(instance_dir, 'underlay', '') # path with trailing /

    # The URL prefix we use to access the static stuff (img, css, js).
    # Note: moin runs a static file server at url_prefix_static path (relative
    # to the script url).
    # If you run your wiki script at the root of your site (/), just do NOT
    # use this setting and it will automatically work.
    # If you run your wiki script at /mywiki, you need to use this:
    url_prefix_static = '/wiki' + url_prefix_static


    # Wiki identity ----------------------------------------------------

    # Site name, used by default for wiki name-logo [Unicode]
    sitename = u'Inno Wiki'

    # Wiki logo. You can use an image, text or both. [Unicode]
    # For no logo or text, use '' - the default is to show the sitename.
    # See also url_prefix setting below!
    logo_string = u'<img src="%s/common/logo.png" alt="Innopolis Logo" style="margin-top: -5px">' % url_prefix_static

    # name of entry page / front page [Unicode], choose one of those:

    # a) if most wiki content is in a single language
    #page_front_page = u"MyStartingPage"

    # b) if wiki content is maintained in many languages
    page_front_page = u"FrontPage"

    # The interwiki name used in interwiki links
    #interwikiname = u'UntitledWiki'
    # Show the interwiki name (and link it to page_front_page) in the Theme,
    # nice for farm setups or when your logo does not show the wiki's name.
    #show_interwiki = 1


    # Security ----------------------------------------------------------

    # This is checked by some rather critical and potentially harmful actions,
    # like despam or PackageInstaller action:
    superuser = [u"i.tkachenko", u"m.skoriukov"]

    # IMPORTANT: grant yourself admin rights! replace YourName with
    # your user name. See HelpOnAccessControlLists for more help.
    # All acl_rights_xxx options must use unicode [Unicode]
    acl_rights_default = u"+AdminGroup:delete,revert Known:read,write All:"
    acl_rights_before = u"i.tkachenko,m.skoriukov:read,write,delete,revert,admin"
    acl_hierarchic = True
    acl_rights_valid = ["read", "write", "delete", "revert", "admin"]


    # The default (ENABLED) password_checker will keep users from choosing too
    # short or too easy passwords. If you don't like this and your site has
    # rather low security requirements, feel free to DISABLE the checker by:
    #password_checker = None # None means "don't do any password strength checks"

    # Link spam protection for public wikis (Uncomment to enable)
    # Needs a reliable internet connection.
    #from MoinMoin.security.antispam import SecurityPolicy


    # Mail --------------------------------------------------------------

    # Configure to enable subscribing to pages (disabled by default)
    # or sending forgotten passwords.

    # SMTP server, e.g. "mail.provider.com" (None to disable mail)
    #mail_smarthost = ""

    # The return address, e.g u"Jürgen Wiki <noreply@mywiki.org>" [Unicode]
    #mail_from = u""

    # "user pwd" if you need to use SMTP AUTH
    #mail_login = ""


    # User interface ----------------------------------------------------

    # Add your wikis important pages at the end. It is not recommended to
    # remove the default links.  Leave room for user links - don't use
    # more than 6 short items.
    # You MUST use Unicode strings here, but you need not use localized
    # page names for system and help pages, those will be used automatically
    # according to the user selected language. [Unicode]
    navi_bar = [
        # If you want to show your page_front_page here:
        u'%(page_front_page)s',
        u'RecentChanges',
        u'FindPage',
        u'HelpContents',
    ]

    # The default theme anonymous or new users get
    theme_default = 'memodump'


    # Language options --------------------------------------------------


    # The main wiki language, set the direction of the wiki pages
    language_default = 'ru'

    page_category_regex = ur'(?P<all>(Категория|Category)(?P<key>\S+))'
    page_dict_regex     = ur'(?P<all>(?P<key>\S+)(Словарь|Dict))'
    page_group_regex    = ur'(?P<all>((?!.*Group)(?P<ru>Группа))?(?P<key>\S+)(?(ru)|Group))'
    page_template_regex = ur'(?P<all>((?!.*Template)(?P<ru>Шаблон))?(?P<key>\S+)(?(ru)|Template))'

    # Content options ---------------------------------------------------

    # Show users hostnames in RecentChanges
    show_hosts = 1

    # Enable graphical charts, requires gdchart.
    #chart_options = {'width': 600, 'height': 300}

    # Auth/LDAP ---------------------------------------------------------

    # This is a sample configuration snippet that shows how to use the ldap auth plugin.
    # See HelpOnAuthentication and HelpOnConfiguration for more infos.

    from MoinMoin.auth.ldap_login import LDAPAuth
    ldap_authenticator1 = LDAPAuth(
        # the values shown below are the DEFAULT values (you may remove them if you are happy with them),
        # the examples shown in the comments are typical for Active Directory (AD) or OpenLDAP.
        server_uri=os.environ.get('LDAP_URI'),
            # ldap / active directory server URI
            # use ldaps://server:636 url for ldaps,
            # use  ldap://server for ldap without tls (and set start_tls to 0),
            # use  ldap://server for ldap with tls (and set start_tls to 1 or 2).
        bind_dn=os.environ.get('BIND_DN'),
            # We can either use some fixed user and password for binding to LDAP.
            # Be careful if you need a % char in those strings - as they are used as
            # a format string, you have to write %% to get a single % in the end.
            #bind_dn = 'binduser@example.org' # (AD)
            #bind_dn = 'cn=admin,dc=example,dc=org' # (OpenLDAP)
            #bind_pw = 'secret'
            # or we can use the username and password we got from the user:
            #bind_dn = '%(username)s@example.org' # DN we use for first bind (AD)
            #bind_pw = '%(password)s' # password we use for first bind
            # or we can bind anonymously (if that is supported by your directory).
            # In any case, bind_dn and bind_pw must be defined.
        bind_pw=os.environ.get('BIND_PW'),
        base_dn='DC=edu,DC=innopolis,DC=ru',
            # base DN we use for searching
            #base_dn = 'ou=SOMEUNIT,dc=example,dc=org'
            #base_dn = 'uid=%(username)s,ou=people,dc=company,dc=com'

        scope=2, # scope of the search we do (2 == ldap.SCOPE_SUBTREE)
        referrals=0, # LDAP REFERRALS (0 needed for AD)
        search_filter='(sAMAccountName=%(username)s)',
            # ldap filter used for searching:
            #search_filter = '(sAMAccountName=%(username)s)' # (AD)
            #search_filter = '(uid=%(username)s)' # (OpenLDAP)
            # you can also do more complex filtering like:
            # "(&(cn=%(username)s)(memberOf=CN=WikiUsers,OU=Groups,DC=example,DC=org))"

        # some attribute names we use to extract information from LDAP (if not None,
        # if None, the attribute won't be extracted from LDAP):
        givenname_attribute='givenName', # often 'givenName' - ldap attribute we get the first name from
        surname_attribute='sn', # often 'sn' - ldap attribute we get the family name from
        aliasname_attribute='mailNickname', # often 'displayName' - ldap attribute we get the aliasname from
        email_attribute='mail', # often 'mail' - ldap attribute we get the email address from
        email_callback=None, # callback function called to make up email address
        coding='utf-8', # coding used for ldap queries and result values
        timeout=10, # how long we wait for the ldap server [s]
        start_tls=2, # usage of Transport Layer Security 0 = No, 1 = Try, 2 = Required
        tls_cacertdir=None,
        tls_cacertfile='/etc/ssl/certs/ca-certificates.crt',
        tls_certfile=None,
        tls_keyfile=None,
        tls_require_cert=0, # 0 == ldap.OPT_X_TLS_NEVER (needed for self-signed certs)
        bind_once=False, # set to True to only do one bind - useful if configured to bind as the user on the first attempt
        autocreate=True, # set to True to automatically create/update user profiles
        name='ldap', # use e.g. 'ldap_pdc' and 'ldap_bdc' (or 'ldap1' and 'ldap2') if you auth against 2 ldap servers
        report_invalid_credentials=True, # whether to emit "invalid username or password" msg at login time or not
    )

    auth = [ldap_authenticator1, ] # this is a list, you may have multiple ldap authenticators
                                   # as well as other authenticators

    cookie_lifetime = (0, 1) # no anon user sessions, 1h session lifetime for logged-in users

    # customize user preferences (optional, see MoinMoin/config/multiconfig for internal defaults)
    # you maybe want to use user_checkbox_remove, user_checkbox_defaults, user_form_defaults,
    # user_form_disable, user_form_remove.

