from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    The UserManager class inherits from the BaseUserManager class from the django.contrib.auth.models module.
    Overrides the functionality of the base class to interact with instances of the modified User model.
    """
    use_in_migrations = True

    def create_user(self, email: str, first_name: str, last_name: str, phone: str, password: str = None):
        """
        The create_user function overrides the method of the base class. Accepts as arguments the instance itself,
        the value of the fields email, first_name, last_name, phone and password. Creates and saves an instance
        of the User model with the user role in the database. Returns the created instance.
        """
        if not email:
            raise ValueError('Users must have an email address')

        username = email.split('@')[0]

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role="user"
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, first_name: str, last_name: str, phone: str, password: str = None):
        """
        The create_superuser function overrides the method of the base class. Accepts as arguments the instance itself,
        the value of the fields email, first_name, last_name, phone and password. Creates and saves an instance
        of the User model with the admin role in the database. Returns the created instance.
        """
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password
        )
        user.role = "admin"
        user.save(using=self._db)

        return user
