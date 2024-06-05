from __future__ import annotations

from datetime import datetime
import json
import logging
from typing import Dict, List, Optional, Tuple, Union
import uuid

from flask import current_app, has_app_context
from flask_appbuilder import const as c
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.security.manager import BaseSecurityManager
from flask_appbuilder.security.sqla.apis import (
    PermissionApi,
    PermissionViewMenuApi,
    RoleApi,
    UserApi,
    ViewMenuApi,
)
from flask_appbuilder.security.sqla.models import (
    assoc_permissionview_role,
    Permission,
    PermissionView,
    RegisterUser,
    Role,
    User,
    ViewMenu,
)
from sqlalchemy import and_, func, literal, update
from sqlalchemy import inspect
from sqlalchemy.orm import contains_eager
from sqlalchemy.orm.exc import MultipleResultsFound
from werkzeug.security import generate_password_hash


log = logging.getLogger(__name__)


class SecurityManager(BaseSecurityManager):
    """
    Responsible for authentication, registering security views,
    role and permission auto management

    If you want to change anything just inherit and override, then
    pass your own security manager to AppBuilder.
    """

    user_model = User
    """ Override to set your own User Model """
    role_model = Role
    """ Override to set your own Role Model """
    permission_model = Permission
    viewmenu_model = ViewMenu
    permissionview_model = PermissionView
    registeruser_model = RegisterUser

    # APIs
    permission_api = PermissionApi
    role_api = RoleApi
    user_api = UserApi
    view_menu_api = ViewMenuApi
    permission_view_menu_api = PermissionViewMenuApi

    def __init__(self, appbuilder):
        """
        SecurityManager contructor
        param appbuilder:
            F.A.B AppBuilder main object
        """
        super(SecurityManager, self).__init__(appbuilder)
        user_datamodel = SQLAInterface(self.user_model)
        if self.auth_type == c.AUTH_DB:
            self.userdbmodelview.datamodel = user_datamodel
        elif self.auth_type == c.AUTH_LDAP:
            self.userldapmodelview.datamodel = user_datamodel
        elif self.auth_type == c.AUTH_OID:
            self.useroidmodelview.datamodel = user_datamodel
        elif self.auth_type == c.AUTH_OAUTH:
            self.useroauthmodelview.datamodel = user_datamodel
        elif self.auth_type == c.AUTH_REMOTE_USER:
            self.userremoteusermodelview.datamodel = user_datamodel

        if self.userstatschartview:
            self.userstatschartview.datamodel = user_datamodel
        if self.auth_user_registration:
            self.registerusermodelview.datamodel = SQLAInterface(
                self.registeruser_model
            )

        self.rolemodelview.datamodel = SQLAInterface(self.role_model)
        self.permissionmodelview.datamodel = SQLAInterface(self.permission_model)
        self.viewmenumodelview.datamodel = SQLAInterface(self.viewmenu_model)
        self.permissionviewmodelview.datamodel = SQLAInterface(
            self.permissionview_model
        )
        self.create_db()

    @property
    def session(self):
        return self.appbuilder.session

    def register_views(self) -> None:
        super().register_views()

        if not current_app.config.get("FAB_ADD_SECURITY_API", False):
            return

        self.appbuilder.add_api(self.permission_api)
        self.appbuilder.add_api(self.role_api)
        self.appbuilder.add_api(self.user_api)
        self.appbuilder.add_api(self.view_menu_api)
        self.appbuilder.add_api(self.permission_view_menu_api)

    def create_db(self) -> None:
        if not current_app.config.get("FAB_CREATE_DB", True):
            return
        try:
            # Check if an application context does not exist
            if not has_app_context():
                # Create a new application context
                with self.appbuilder.app.app_context():
                    self._create_db()
            else:
                self._create_db()
        except Exception as e:
            log.error(c.LOGMSG_ERR_SEC_CREATE_DB, e)
            exit(1)

    def _create_db(self) -> None:
        from flask_appbuilder.extensions import db

        inspector = inspector = inspect(db.engine)
        if "ab_user" not in inspector.get_table_names():
            log.info(c.LOGMSG_INF_SEC_NO_DB)
            db.create_all()
            log.info(c.LOGMSG_INF_SEC_ADD_DB)
        super().create_db()

    def find_register_user(self, registration_hash: str) -> Optional[RegisterUser]:
        return (
            self.appbuilder.session.query(self.registeruser_model)
            .filter(self.registeruser_model.registration_hash == registration_hash)
            .scalar()
        )

    def add_register_user(
        self,
        username: str,
        first_name: str,
        last_name: str,
        email: str,
        password: str = "",
        hashed_password: str = "",
    ) -> User:
        """
        Add a registration request for the user.

        :rtype : RegisterUser
        """
        register_user = self.registeruser_model()
        register_user.username = username
        register_user.email = email
        register_user.first_name = first_name
        register_user.last_name = last_name
        if hashed_password:
            register_user.password = hashed_password
        else:
            register_user.password = generate_password_hash(password)
        register_user.registration_hash = str(uuid.uuid1())
        try:
            self.appbuilder.session.add(register_user)
            self.appbuilder.session.commit()
            return register_user
        except Exception as e:
            log.error(c.LOGMSG_ERR_SEC_ADD_REGISTER_USER, e)
            self.appbuilder.session.rollback()
            return None

    def del_register_user(self, register_user):
        """
        Deletes registration object from database

        :param register_user: RegisterUser object to delete
        """
        try:
            self.appbuilder.session.delete(register_user)
            self.appbuilder.session.commit()
            return True
        except Exception as e:
            log.error(c.LOGMSG_ERR_SEC_DEL_REGISTER_USER, e)
            self.appbuilder.session.rollback()
            return False

    def find_user(self, username=None, email=None):
        """
        Finds user by username or email
        """
        if username:
            try:
                if self.auth_username_ci:
                    return (
                        self.appbuilder.session.query(self.user_model)
                        .filter(
                            func.lower(self.user_model.username) == func.lower(username)
                        )
                        .one_or_none()
                    )
                else:
                    return (
                        self.appbuilder.session.query(self.user_model)
                        .filter(self.user_model.username == username)
                        .one_or_none()
                    )
            except MultipleResultsFound:
                log.error("Multiple results found for user %s", username)
                return None
        elif email:
            try:
                return (
                    self.appbuilder.session.query(self.user_model)
                    .filter_by(email=email)
                    .one_or_none()
                )
            except MultipleResultsFound:
                log.error("Multiple results found for user with email %s", email)
                return None

    def get_all_users(self):
        return self.appbuilder.session.query(self.user_model).all()

    def add_user(
        self,
        username: str,
        first_name: str,
        last_name: str,
        email: str,
        role: Role | list[Role],
        password="",
        hashed_password="",
    ):
        """
        Generic function to create user
        """
        try:
            user = self.user_model()
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.active = True
            user.roles = role if isinstance(role, list) else [role]
            if hashed_password:
                user.password = hashed_password
            else:
                user.password = generate_password_hash(password)
            self.appbuilder.session.add(user)
            self.appbuilder.session.commit()
            log.info(c.LOGMSG_INF_SEC_ADD_USER, username)
            return user
        except Exception as e:
            log.error(c.LOGMSG_ERR_SEC_ADD_USER, e)
            self.appbuilder.session.rollback()
            return False

    def count_users(self):
        return self.appbuilder.session.query(func.count(self.user_model.id)).scalar()

    def update_user(self, user):
        try:
            self.appbuilder.session.merge(user)
            self.appbuilder.session.commit()
            log.info(c.LOGMSG_INF_SEC_UPD_USER, user)
        except Exception as e:
            log.error(c.LOGMSG_ERR_SEC_UPD_USER, e)
            self.appbuilder.session.rollback()
            return False

    def get_user_by_id(self, pk):
        return self.appbuilder.session.get(self.user_model, pk)

    def get_first_user(self) -> "User":
        return self.appbuilder.session.query(self.user_model).first()

    def noop_user_update(self, user: "User") -> None:
        stmt = (
            update(self.user_model)
            .where(self.user_model.id == user.id)
            .values(login_count=user.login_count)
        )
        self.appbuilder.session.execute(stmt)
        self.appbuilder.session.commit()

    """
    -----------------------
     PERMISSION MANAGEMENT
    -----------------------
    """

    def add_role(
        self, name: str, permissions: Optional[List[PermissionView]] = None
    ) -> Optional[Role]:
        if not permissions:
            permissions = []

        role = self.find_role(name)
        if role is None:
            try:
                role = self.role_model()
                role.name = name
                role.permissions = permissions
                self.appbuilder.session.add(role)
                self.appbuilder.session.commit()
                log.info(c.LOGMSG_INF_SEC_ADD_ROLE, name)
                return role
            except Exception as e:
                log.error(c.LOGMSG_ERR_SEC_ADD_ROLE, e)
                self.appbuilder.session.rollback()
        return role

    def update_role(self, pk, name: str) -> Optional[Role]:
        role = self.appbuilder.session.query(self.role_model).get(pk)
        if not role:
            return
        try:
            role.name = name
            self.appbuilder.session.merge(role)
            self.appbuilder.session.commit()
            log.info(c.LOGMSG_INF_SEC_UPD_ROLE, role)
        except Exception as e:
            log.error(c.LOGMSG_ERR_SEC_UPD_ROLE, e)
            self.appbuilder.session.rollback()
            return

    def find_role(self, name):
        return (
            self.appbuilder.session.query(self.role_model)
            .filter_by(name=name)
            .one_or_none()
        )

    def get_all_roles(self):
        return self.appbuilder.session.query(self.role_model).all()

    def get_public_role(self):
        return (
            self.appbuilder.session.query(self.role_model)
            .filter_by(name=self.auth_role_public)
            .one_or_none()
        )

    def get_public_permissions(self):
        role = self.get_public_role()
        if role:
            return role.permissions
        return []

    def find_permission(self, name):
        """
        Finds and returns a Permission by name
        """
        return (
            self.appbuilder.session.query(self.permission_model)
            .filter_by(name=name)
            .one_or_none()
        )

    def exist_permission_on_roles(
        self, view_name: str, permission_name: str, role_ids: List[int]
    ) -> bool:
        """
            Method to efficiently check if a certain permission exists
            on a list of role id's. This is used by `has_access`

        :param view_name: The view's name to check if exists on one of the roles
        :param permission_name: The permission name to check if exists
        :param role_ids: a list of Role ids
        :return: Boolean
        """
        q = (
            self.appbuilder.session.query(self.permissionview_model)
            .join(
                assoc_permissionview_role,
                and_(
                    (
                        self.permissionview_model.id
                        == assoc_permissionview_role.c.permission_view_id
                    )
                ),
            )
            .join(self.role_model)
            .join(self.permission_model)
            .join(self.viewmenu_model)
            .filter(
                self.viewmenu_model.name == view_name,
                self.permission_model.name == permission_name,
                self.role_model.id.in_(role_ids),
            )
            .exists()
        )
        # Special case for MSSQL/Oracle (works on PG and MySQL > 8)
        if self.appbuilder.session.get_bind().name in ("mssql", "oracle"):
            return self.appbuilder.session.query(literal(True)).filter(q).scalar()
        return self.appbuilder.session.query(q).scalar()

    def find_roles_permission_view_menus(
        self, permission_name: str, role_ids: List[int]
    ):
        return (
            self.appbuilder.session.query(self.permissionview_model)
            .join(
                assoc_permissionview_role,
                and_(
                    (
                        self.permissionview_model.id
                        == assoc_permissionview_role.c.permission_view_id
                    )
                ),
            )
            .join(self.role_model)
            .join(self.permission_model)
            .join(self.viewmenu_model)
            .filter(
                self.permission_model.name == permission_name,
                self.role_model.id.in_(role_ids),
            )
        ).all()

    def get_user_roles_permissions(self, user) -> Dict[str, List[Tuple[str, str]]]:
        """
        Utility method for fetching all roles and permissions for a specific user.
        Example of the returned data:
        ```
        {
            'Admin': [
                ('can_this_form_get', 'ResetPasswordView'),
                ('can_this_form_post', 'ResetPasswordView'),
                ...
            ]
             'EmptyRole': [],
        }
        ```
        """
        if not user.roles:
            raise AttributeError("User object does not have roles")

        result: Dict[str, List[Tuple[str, str]]] = {}
        db_roles_ids = []
        for role in user.roles:
            # Make sure all db roles are included on the result
            result[role.name] = []
            if role.name in self.builtin_roles:
                for permission in self.builtin_roles[role.name]:
                    result[role.name].append((permission[1], permission[0]))
            else:
                db_roles_ids.append(role.id)

        permission_views = (
            self.appbuilder.session.query(PermissionView)
            .join(Permission)
            .join(ViewMenu)
            .join(PermissionView.role)
            .filter(Role.id.in_(db_roles_ids))
            .options(contains_eager(PermissionView.permission))
            .options(contains_eager(PermissionView.view_menu))
            .options(contains_eager(PermissionView.role))
        ).all()

        for permission_view in permission_views:
            for role_item in permission_view.role:
                if role_item.name in result:
                    result[role_item.name].append(
                        (
                            permission_view.permission.name,
                            permission_view.view_menu.name,
                        )
                    )
        return result

    def get_db_role_permissions(self, role_id: int) -> List[PermissionView]:
        """
        Get all DB permissions from a role (one single query)
        """
        return (
            self.appbuilder.session.query(PermissionView)
            .join(Permission)
            .join(ViewMenu)
            .join(PermissionView.role)
            .filter(Role.id == role_id)
            .options(contains_eager(PermissionView.permission))
            .options(contains_eager(PermissionView.view_menu))
            .all()
        )

    def add_permission(self, name):
        """
        Adds a permission to the backend, model permission

        :param name:
            name of the permission: 'can_add','can_edit' etc...
        """
        perm = self.find_permission(name)
        if perm is None:
            try:
                perm = self.permission_model()
                perm.name = name
                self.appbuilder.session.add(perm)
                self.appbuilder.session.commit()
                return perm
            except Exception as e:
                log.error(c.LOGMSG_ERR_SEC_ADD_PERMISSION, e)
                self.appbuilder.session.rollback()
        return perm

    def del_permission(self, name: str) -> bool:
        """
        Deletes a permission from the backend, model permission

        :param name:
            name of the permission: 'can_add','can_edit' etc...
        """
        perm = self.find_permission(name)
        if not perm:
            log.warning(c.LOGMSG_WAR_SEC_DEL_PERMISSION, name)
            return False
        try:
            pvms = (
                self.appbuilder.session.query(self.permissionview_model)
                .filter(self.permissionview_model.permission == perm)
                .all()
            )
            if pvms:
                log.warning(c.LOGMSG_WAR_SEC_DEL_PERM_PVM, perm, pvms)
                return False
            self.appbuilder.session.delete(perm)
            self.appbuilder.session.commit()
            return True
        except Exception as e:
            log.error(c.LOGMSG_ERR_SEC_DEL_PERMISSION, e)
            self.appbuilder.session.rollback()
            return False

    """
    ----------------------
     PRIMITIVES VIEW MENU
    ----------------------
    """

    def find_view_menu(self, name):
        """
        Finds and returns a ViewMenu by name
        """
        return (
            self.appbuilder.session.query(self.viewmenu_model)
            .filter_by(name=name)
            .one_or_none()
        )

    def get_all_view_menu(self):
        return self.appbuilder.session.query(self.viewmenu_model).all()

    def add_view_menu(self, name):
        """
        Adds a view or menu to the backend, model view_menu
        param name:
            name of the view menu to add
        """
        view_menu = self.find_view_menu(name)
        if view_menu is None:
            try:
                view_menu = self.viewmenu_model()
                view_menu.name = name
                self.appbuilder.session.add(view_menu)
                self.appbuilder.session.commit()
                return view_menu
            except Exception as e:
                log.error(c.LOGMSG_ERR_SEC_ADD_VIEWMENU, e)
                self.appbuilder.session.rollback()
        return view_menu

    def del_view_menu(self, name: str) -> bool:
        """
        Deletes a ViewMenu from the backend

        :param name:
            name of the ViewMenu
        """
        view_menu = self.find_view_menu(name)
        if not view_menu:
            log.warning(c.LOGMSG_WAR_SEC_DEL_VIEWMENU, name)
            return False
        try:
            pvms = (
                self.appbuilder.session.query(self.permissionview_model)
                .filter(self.permissionview_model.view_menu == view_menu)
                .all()
            )
            if pvms:
                log.warning(c.LOGMSG_WAR_SEC_DEL_VIEWMENU_PVM, view_menu, pvms)
                return False
            self.appbuilder.session.delete(view_menu)
            self.appbuilder.session.commit()
            return True
        except Exception as e:
            log.error(c.LOGMSG_ERR_SEC_DEL_PERMISSION, e)
            self.appbuilder.session.rollback()
            return False

    """
    ----------------------
     PERMISSION VIEW MENU
    ----------------------
    """

    def find_permission_view_menu(self, permission_name, view_menu_name):
        """
        Finds and returns a PermissionView by names
        """
        permission = self.find_permission(permission_name)
        view_menu = self.find_view_menu(view_menu_name)
        if permission and view_menu:
            return (
                self.appbuilder.session.query(self.permissionview_model)
                .filter_by(permission=permission, view_menu=view_menu)
                .one_or_none()
            )

    def find_permissions_view_menu(self, view_menu):
        """
        Finds all permissions from ViewMenu, returns list of PermissionView

        :param view_menu: ViewMenu object
        :return: list of PermissionView objects
        """
        return (
            self.appbuilder.session.query(self.permissionview_model)
            .filter_by(view_menu_id=view_menu.id)
            .all()
        )

    def add_permission_view_menu(self, permission_name, view_menu_name):
        """
        Adds a permission on a view or menu to the backend

        :param permission_name:
            name of the permission to add: 'can_add','can_edit' etc...
        :param view_menu_name:
            name of the view menu to add
        """
        if not (permission_name and view_menu_name):
            return None
        pv = self.find_permission_view_menu(permission_name, view_menu_name)
        if pv:
            return pv
        vm = self.add_view_menu(view_menu_name)
        perm = self.add_permission(permission_name)
        pv = self.permissionview_model()
        pv.view_menu, pv.permission = vm, perm
        try:
            self.appbuilder.session.add(pv)
            self.appbuilder.session.commit()
            log.info(c.LOGMSG_INF_SEC_ADD_PERMVIEW, pv)
            return pv
        except Exception as e:
            log.error(c.LOGMSG_ERR_SEC_ADD_PERMVIEW, e)
            self.appbuilder.session.rollback()

    def del_permission_view_menu(self, permission_name, view_menu_name, cascade=True):
        if not (permission_name and view_menu_name):
            return
        pv = self.find_permission_view_menu(permission_name, view_menu_name)
        if not pv:
            return
        roles_pvs = (
            self.appbuilder.session.query(self.role_model)
            .filter(self.role_model.permissions.contains(pv))
            .first()
        )
        if roles_pvs:
            log.warning(
                c.LOGMSG_WAR_SEC_DEL_PERMVIEW,
                view_menu_name,
                permission_name,
                roles_pvs,
            )
            return
        try:
            # delete permission on view
            self.appbuilder.session.delete(pv)
            self.appbuilder.session.commit()
            # if no more permission on permission view, delete permission
            if not cascade:
                return
            if (
                not self.appbuilder.session.query(self.permissionview_model)
                .filter_by(permission=pv.permission)
                .all()
            ):
                self.del_permission(pv.permission.name)
            log.info(c.LOGMSG_INF_SEC_DEL_PERMVIEW, permission_name, view_menu_name)
        except Exception as e:
            log.error(c.LOGMSG_ERR_SEC_DEL_PERMVIEW, e)
            self.appbuilder.session.rollback()

    def exist_permission_on_views(self, lst, item):
        for i in lst:
            if i.permission and i.permission.name == item:
                return True
        return False

    def exist_permission_on_view(self, lst, permission, view_menu):
        for i in lst:
            if i.permission.name == permission and i.view_menu.name == view_menu:
                return True
        return False

    def add_permission_role(self, role, perm_view):
        """
        Add permission-ViewMenu object to Role

        :param role:
            The role object
        :param perm_view:
            The PermissionViewMenu object
        """
        if perm_view and perm_view not in role.permissions:
            try:
                role.permissions.append(perm_view)
                self.appbuilder.session.merge(role)
                self.appbuilder.session.commit()
                log.info(c.LOGMSG_INF_SEC_ADD_PERMROLE, perm_view, role.name)
            except Exception as e:
                log.error(c.LOGMSG_ERR_SEC_ADD_PERMROLE, e)
                self.appbuilder.session.rollback()

    def del_permission_role(self, role, perm_view):
        """
        Remove permission-ViewMenu object to Role

        :param role:
            The role object
        :param perm_view:
            The PermissionViewMenu object
        """
        if perm_view in role.permissions:
            try:
                role.permissions.remove(perm_view)
                self.appbuilder.session.merge(role)
                self.appbuilder.session.commit()
                log.info(c.LOGMSG_INF_SEC_DEL_PERMROLE, perm_view, role.name)
            except Exception as e:
                log.error(c.LOGMSG_ERR_SEC_DEL_PERMROLE, e)
                self.appbuilder.session.rollback()

    def export_roles(
        self, path: Optional[str] = None, indent: Optional[Union[int, str]] = None
    ) -> None:
        """Exports roles to JSON file."""
        timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
        filename = path or f"roles_export_{timestamp}.json"

        serialized_roles = []

        for role in self.get_all_roles():
            serialized_role = {"name": role.name, "permissions": []}
            for pvm in role.permissions:
                permission = pvm.permission
                view_menu = pvm.view_menu
                permission_view_menu = {
                    "permission": {"name": permission.name},
                    "view_menu": {"name": view_menu.name},
                }
                serialized_role["permissions"].append(permission_view_menu)
            serialized_roles.append(serialized_role)

        with open(filename, "w") as fd:
            fd.write(json.dumps(serialized_roles, indent=indent))

    def import_roles(self, path: str) -> None:
        """Imports roles from JSON file."""

        session = self.appbuilder.session()

        with open(path, "r") as fd:
            roles_json = json.loads(fd.read())

        roles = []

        for role_kwargs in roles_json:
            role = self.add_role(role_kwargs["name"])
            permission_view_menus = [
                self.add_permission_view_menu(
                    permission_name=pvm_kwargs["permission"]["name"],
                    view_menu_name=pvm_kwargs["view_menu"]["name"],
                )
                for pvm_kwargs in role_kwargs["permissions"]
            ]

            for permission_view_menu in permission_view_menus:
                if permission_view_menu not in role.permissions:
                    role.permissions.append(permission_view_menu)
            roles.append(role)

        session.add_all(roles)
        session.commit()
