from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework import status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view, extend_schema


class TenPerDayUserThrottle(UserRateThrottle):
    rate = '10/day'


@extend_schema_view(
    retrieve=extend_schema(
        summary="",
        responses={
            status.HTTP_200_OK: "",
        },
    ),
)
@api_view(['GET'])
@throttle_classes([TenPerDayUserThrottle])
def minimal_view(request):
    return Response({"message": "Hello"})
