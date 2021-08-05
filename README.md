# bingo_with_django
Internet Technology team project
As limited time frame for the project, framework is based on Rango and Bootstrap 5 template as basis.
1) Packagse needed refering to requirements.txt.
  Django - web framework
  django-registration-redux - for registration
  django-role-permissions - for role based control
  Pillow - for image processing
  social-auth-app-django - social network authentication
  
2) To run site with content
  - run migrate command to create sqlite db
  - run createsuperuser command to create super user account
  - run populate_rango.py to populate content
      three users created
        editor/editor1234 (editor role)
        peter/peter1234
        david/david1234

3) rango/test_bingo.py for the testing script
4) website do support twitter login. Corresponding keys in setting file are deleted for security reason & need to be updated manually in order to resume function.  
