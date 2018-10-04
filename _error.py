"""PytSite Permissions Plugin Errors
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class PermissionGroupNotDefined(Exception):
    pass


class PermissionGroupAlreadyDefined(Exception):
    pass


class PermissionNotDefined(Exception):
    pass


class PermissionAlreadyDefined(Exception):
    pass
