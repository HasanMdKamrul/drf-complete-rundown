from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                "whole_url": "http://localhost:8000/api/products/",
            },
            'count': self.page.paginator.count,
            'results': data,
            'page': self.page.number,
            
        })
