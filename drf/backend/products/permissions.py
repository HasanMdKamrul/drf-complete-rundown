from rest_framework.permissions import DjangoModelPermissions

    # def has_permission(self, request, view):
    #     # Workaround to ensure DjangoModelPermissions are not applied
    #     # to the root view when using DefaultRouter.
    #     if getattr(view, '_ignore_model_permissions', False):
    #         return True

    #     if not request.user or (
    #        not request.user.is_authenticated and self.authenticated_users_only):
    #         return False

    #     queryset = self._queryset(view)
    #     perms = self.get_required_permissions(request.method, queryset.model)

    #     return request.user.has_perms(perms)

class IsStaffEditorPermission(DjangoModelPermissions):
    
    
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    
    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)
    
    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm('products.view_product'): #** app_name.action_model
    #             return True
    #         if user.has_perm('products.add_product'): #** app_name.action_model
    #             return True
    #         if user.has_perm('products.change_product'): #** app_name.action_model
    #             return True
    #         if user.has_perm('products.delete_product'): #** app_name.action_model
    #             return True
    #         return False
    #     return False
    
  