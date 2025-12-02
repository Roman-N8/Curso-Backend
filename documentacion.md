# Gestión de Roles y Permisos

Este proyecto implementa autenticación con **JWT** y un sistema de roles basado en un modelo de usuario personalizado (`CustomUser`) en Django.

## Roles disponibles

Actualmente existen dos roles:

- `ADMIN`
- `USER` (valor por defecto)

```python
class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        USER = 'USER', 'User'

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.USER,
    )
