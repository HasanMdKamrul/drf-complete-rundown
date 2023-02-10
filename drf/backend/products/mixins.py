from rest_framework import permissions

from .models import Product
from .permissions import IsStaffEditorPermission


class IsStaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

class QuerySetMixin():
    queryset = Product.objects.all()