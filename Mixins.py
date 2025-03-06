class RoleMixin:
    """Mixin for user roles."""
    def __init__(self):
        self.roles = set()

    def add_role(self, role):
        """Assign a role to the user."""
        self.roles.add(role)
        print(f"Role {role} added.")

    def remove_role(self, role):
        """Remove a role from the user."""
        if role in self.roles:
            self.roles.remove(role)
            print(f"Role {role} removed.")
        else:
            print(f"You don't have the role {role}")

    def show_roles(self):
        """Display all roles assigned to the user."""
        if self.roles:
            print(f"{self.roles}")
        else:
            print(f"no roles")


class PermissionMixin:
    """Mixin for user permissions."""
    def __init__(self):
        self.permissions = set()

    def grant_permission(self, action):
        """Grant a specific permission to the user."""
        self.permissions.add(action)
        print(f"Granted permission for {action}.")

    def revoke_permission(self, action):
        """Revoke a permission from the user."""
        if action in self.permissions:
            self.permissions.remove(action)
            print(f"Revoked permission for {action}.")
        else:
            print(f"You don't have this permission {action} in the first place.")

    def check_permission(self, action):
        """Check if the user has a specific permission."""
        if action in self.permissions:
            print(f"You have permission for '{action}'.")
            return True
        else:
            print(f"You don't have permission for '{action}'.")
            return False

class User:
    """Base user class."""
    def __init__(self, name):
        self.name = name
        super().__init__()


class AdminUser(User, RoleMixin, PermissionMixin):
    """Admin user with full control over roles and permissions."""
    def __init__(self, name):
        super().__init__(name)


class EditorUser(User, RoleMixin, PermissionMixin):
    """Editor user with limited permissions."""
    def __init__(self, name):
        super().__init__(name)


class ViewerUser(User, RoleMixin):
    """Viewer user with read-only access."""
    def __init__(self, name):
        super().__init__(name)