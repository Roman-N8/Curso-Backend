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
```
## Ejemplos de uso
Ejemplos de como hacer peticiones a todas las APIs del proyecto
### 1. Registro de usuario (rol USER por defecto)
Endpoint: /api/users/register/
Metodo: POST
body: 
´´´JSON
{
  "username": "roman",
  "password": "mi_clave_segura",
  "first_name": "Roman",
  "last_name": "Chavez",
  "country": "MX",
  "city": "Morelia",
  "phoneNumber"; "+52 9854375648"
}
´´´

