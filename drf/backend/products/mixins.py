from rest_framework import permissions

from .models import Product
from .permissions import IsStaffEditorPermission


class IsStaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

class QuerySetMixin():
    queryset = Product.objects.all()
    
class GetQuerySetMixin():
    user_field = "user"
    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        defaul_queryset = super().get_queryset(*args, **kwargs)
        lookup_data[self.user_field] = self.request.user
        # print(defaul_queryset)
        # print(lookup_data)
        
      
        
        return defaul_queryset.filter(**lookup_data) 