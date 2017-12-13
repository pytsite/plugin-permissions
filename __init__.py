"""PytSite Permissions Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import plugman as _plugman

if _plugman.is_installed(__name__):
    # Public API
    from . import _error as error
    from ._api import define_permission, define_group, get_permission, is_permission_group_defined, \
        get_permission_groups, get_permissions, is_permission_defined


def plugin_load():
    define_group('app', 'app_name')
