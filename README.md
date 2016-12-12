## Changes in this fork

### New Django! Tested with 1.8.17 and 1.10

I'm not an expert in django let alone migrating from 1.6 to 1.8. It's very likely that I've done it in a very wrong way. Be my guest and point it out or, better, fix it. Some things definitely need extra care, e.g. tests. Plus, files are stored in the database using https://github.com/bfirsh/django-database-files which is not mainteined for years. Perhaps it makes sense migrating to something like http://django-db-file-storage.readthedocs.io/en/master/.

### Extra Fields

Now each tag can have Extra Fields. Credentials get a set of Extra Fields from tags.
For example, if you have credentials with tag "email_account" you can add some Extra Fields to this tag, say, "Aliases" and "Distribution lists". When you edit a particular password entry with tag email_accounts it'll get these fields: 

Access tag's extra fields:
![tag_list](https://cloud.githubusercontent.com/assets/13673718/21100388/10fb8510-c074-11e6-8486-c8e3c960c6fa.jpg)

Edit them:
![extra_add](https://cloud.githubusercontent.com/assets/13673718/21100386/10fae394-c074-11e6-88ee-1f59597ba5ee.jpg)

Delete extra fields from a tag:
![extra_delete](https://cloud.githubusercontent.com/assets/13673718/21100387/10fb24f8-c074-11e6-8763-444dc409a022.jpg)

Edit password entry:

![cred_edit](https://cloud.githubusercontent.com/assets/13673718/21100385/10faedf8-c074-11e6-8d09-97078483a182.jpg)

View password entry:
![cred_details](https://cloud.githubusercontent.com/assets/13673718/21100384/10fa3278-c074-11e6-8020-de096f90cabe.jpg)

### Issues

* Tests need fixing
* social_auth did not fly well, so it's commented out in settings.py
* requirements files are not to be trusted. You should be good to go if you can lay hands on versions from the requirements-base.txt
* Extra fields do not appear in cred_edit and cred_detail views in web2.0 way. Click "edit" in cred_detail and extra fields from current tags are added with empty values. "submit" in cred_edit does the same if tags were added/deleted duting editing.

RatticWeb
=========

RatticWeb is the website part of the Rattic password management solution, which allows you to easily manage your users and passwords.

If you decide to use RatticWeb you should take the following into account:
* The webpage should be served over HTTPS only, apart from a redirect from normal HTTP.
* The filesystem in which the database is stored should be protected with encryption.
* The access logs should be protected.
* The machine which serves RatticWeb should be protected from access.
* Tools like <a href=="http://www.ossec.net/">OSSEC</a> are your friend.

Support and Known Issues:
* Through <a href="http://twitter.com/RatticDB">twitter</a> or <a href="https://github.com/tildaslash/RatticWeb/issues?state=open">Github Issues</a>
* Apache config needs to have "WSGIPassAuthorization On" for the API keys to work  

Dev Setup: <https://github.com/tildaslash/RatticWeb/wiki/Development>

