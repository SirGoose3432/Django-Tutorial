SWEN-261 Advice


- When first starting the project, code together as a group and learn Django together. 
That way everyone is on the same page when it comes to Django and everyone can contribute equally.


- Meet with the client/professor often and early. It helps give a better picture of what the project should be like.


- Have the group create it's own deadlines and make sure everyone is committing to them.


- Be sure to be done early with deliverables. Bugs will pop up and it's best to tackle them long before presentations.


- Rehearse presentations ahead of time, especially with what is going to be done in the site demo.


- Always make migrations after making changes to models like below
    - $ manage.py makemigrations <app name>
    - $ manage.py migrate

- Take care when committing the database to the vcs repo
    - After making migrations, make sure to update the repo with the new database
    - Sometimes, it's best not to update the repo with a database unless migrations are being made

