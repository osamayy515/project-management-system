To start the project locally first install dependencies by command pip install -r requirements.txt and also python version would be preferably 3.10.10

Then, for running the server python manage.py runserver

For migrations, python manage.py makemigrations and after that python manage.py migrate

All API have restricted access so first create superuser in new integrated terminal with command python manage.py createsuperuser
Demo user for production:
Username: Osama
Psw: Osama12345.

Then hit url http://127.0.0.1:8001/auth/login/ locally and for live project hit url https://project-management-system-eeas-3j72r9zse-osamayy515s-projects.vercel.app/auth/login/ and login with the username and password given above and it will redirect you to the token generation page https://project-management-system-eeas-3j72r9zse-osamayy515s-projects.vercel.app/api/token/
Obtain the access token with the username and password. 

Then, use the Token in the DRF Interface
The Django REST Framework browsable API does not automatically handle JWT tokens. However, you can manually include the token in your requests using browser extensions like "ModHeader" for Chrome or similar tools.

Using ModHeader (or similar extension)
Install ModHeader:
Install the ModHeader extension from the Chrome Web Store.

Add Authorization Header:

Open the ModHeader extension.
Add a new header with the key `Authorization` and the value `Bearer <your_access_token>`.


And now you can check all APIs and the header added by ModHeader will automatically include the JWT token with your requests, allowing you to interact with the APIs:
https://project-management-system-eeas-3j72r9zse-osamayy515s-projects.vercel.app/api/
https://project-management-system-eeas-3j72r9zse-osamayy515s-projects.vercel.app/api/projects/
https://project-management-system-eeas-3j72r9zse-osamayy515s-projects.vercel.app/api/tasks/
