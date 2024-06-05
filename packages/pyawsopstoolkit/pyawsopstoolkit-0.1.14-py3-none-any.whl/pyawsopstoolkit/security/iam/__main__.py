import re

from pyawsopstoolkit.__interfaces__ import ISession
from pyawsopstoolkit.__validations__ import Validation


class Role:
    """
    A class representing security risks and vulnerabilities related with IAM roles.
    """

    def __init__(self, session: ISession) -> None:
        """
        Initializes the constructor of the Role class.
        :param session: An ISession object providing access to AWS services.
        :type session: ISession
        """
        Validation.validate_type(session, ISession, 'session should be of Session type.')

        self._session = session

    @property
    def session(self) -> ISession:
        """
        Gets the ISession object which provides access to AWS services.
        :return: The ISession object which provide access to AWS services.
        :rtype: ISession
        """
        return self._session

    @session.setter
    def session(self, value: ISession) -> None:
        """
        Sets the ISession object which provides access to AWS services.
        :param value: The ISession object which provides access to AWS services.
        :type value: ISession
        """
        Validation.validate_type(value, ISession, 'session should be of Session type.')

        self._session = value

    def roles_without_permissions_boundary(self) -> list:
        """
        Returns a list of IAM roles that do not have an associated permissions boundary.
        :return: A list of IAM roles without an associated permissions boundary.
        :rtype: list
        """
        from pyawsopstoolkit.advsearch.iam import Role

        role_object = Role(self.session)
        iam_roles = role_object.search_roles(include_details=True)

        if iam_roles is None:
            return []

        roles_without_permissions_boundary = []

        for role in iam_roles:
            if not re.search(r'/aws-service-role/', role.path, re.IGNORECASE):
                if role.permissions_boundary is None:
                    roles_without_permissions_boundary.append(role)

        return roles_without_permissions_boundary


class User:
    """
    A class representing security risks and vulnerabilities related with IAM users.
    """

    def __init__(self, session: ISession) -> None:
        """
        Initializes the constructor of the User class.
        :param session: An ISession object providing access to AWS services.
        :type session: ISession
        """
        Validation.validate_type(session, ISession, 'session should be of Session type.')

        self._session = session

    @property
    def session(self) -> ISession:
        """
        Gets the ISession object which provides access to AWS services.
        :return: The ISession object which provide access to AWS services.
        :rtype: ISession
        """
        return self._session

    @session.setter
    def session(self, value: ISession) -> None:
        """
        Sets the ISession object which provides access to AWS services.
        :param value: The ISession object which provides access to AWS services.
        :type value: ISession
        """
        Validation.validate_type(value, ISession, 'session should be of Session type.')

        self._session = value

    def users_without_permissions_boundary(self) -> list:
        """
        Returns a list of IAM users that do not have an associated permissions boundary.
        :return: A list of IAM users without an associated permissions boundary.
        :rtype: list
        """
        from pyawsopstoolkit.advsearch.iam import User

        user_object = User(self.session)
        iam_users = user_object.search_users(include_details=True)

        if iam_users is None:
            return []

        return [
            user for user in iam_users
            if user.permissions_boundary is None
        ]
