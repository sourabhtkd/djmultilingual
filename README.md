# Tasks
 - Create Multilingual Blog application to store articles
 - Addition/removal of new language should not require schema change


# Assumptions
- Default language will never be changed 
- Content should be added for default language first
- if default language content is deleted then all of it's child content should also be deleted
- No error handling,logging and production grade configurations are used since this is just a POC
- There are two urls for article list, one without language code and one with language code,in production 
  we may want to redirect users to default language url if language is not provided but here it is skipped
  eg:-  if user types {{url}}/articles it should be redirected to
  {{url}}/articles/en
- Assuming we cannot use any translator services which will automatically translates the content to different
  languages.
- Here we are using hard delete but in production we may want to use soft delete

# Installation
- clone repo
- navigate to root folder
- pip install -r requirements.txt
- sqlite database and migrations are not added in .gitignore so that you can see dummy data(to make it fast)


# Flow
- Run application :- python manage.py runserver
- go to http://localhost:8000/admin
- Login to admin panel, **username**-admin,**password**-admin
- Add Article in default language that is english
- Add Article in different languages by selecting parent article
- to check  article list go to http://localhost:8000/articles/,http://localhost:8000/articles/hi/(for hindi language)
- In case you want to add support for new language
  go to core/constants/LanguageChoice and add support for new language

# Screenshots
![Alt text](screenshots/1.png?raw=true "")<br>
![Alt text](screenshots/2.png?raw=true "")<br>
![Alt text](screenshots/3.png?raw=true "")<br>
![Alt text](screenshots/4.png?raw=true "")<br>