About : This virtual CV allows the user to create their own virtual CV tour, where employers can view your life summary, the most important information that interests them, not just in PDF format but also with visualizations created using programming languages. This provides uniqueness and the opportunity to be noticed and stand out from other job applicants.




Functionalities:

    The user, logged in as an administrator, has the ability to modify and edit the entire life description, manage images, and edit the most important information directly through a text editor in a convenient way with just a few clicks.
    The website features a translation functionality for LT-ENG languages, which can be performed with a single click, instantly translating the entire website into the selected language.
    The game also includes an integrated Rock, Paper, Scissors game for differentiation, showing the employer that you are familiar with programming languages and capable of performing a simple task such as creating this game.
    Additionally, a graphical pie chart is included, reflecting your experience.





Requirements:

django==5.1.4

django-modeltranslation==0.19.12

django-tinymce==4.1.0

pillow==11.1.0






Steps to Set Up the Virtual CV Project

    Add all the files from the repository you see here: https://github.com/DeividasBaliutis/virtual_CV to your newly created project.

    Read the requirements.txt file to see all the libraries you need to install in order to run the project.

    After installing the necessary libraries, open your terminal and run the following commands:
        python manage.py makemigrations
        python manage.py migrate

    This will automatically create the database file.

    Create a superuser account (admin) so you can edit the content of the Virtual CV. Run the command:
        python manage.py createsuperuser

    You will be prompted to enter the necessary details for the superuser account.

    After completing the above steps, start the server using the command:
        python manage.py runserver

    Ensure that there are no errors and try accessing the website by navigating to:
        http://127.0.0.1:8000/admin/

    Here, you can log in with the superuser account you created earlier.

    You will now be able to edit the content through the admin interface. The website itself can be accessed at:
        http://127.0.0.1:8000




Contacts : Contacts:
If you have any questions, feel free to contact the developer at the email address DeividasBaliutis@gmail.com. Please ensure that your questions are in English and clear.
