from rolepermissions.roles import AbstractUserRole

class Editor(AbstractUserRole):
    available_permissions = {
        'create_category': True,
        'create_page': True,
    }