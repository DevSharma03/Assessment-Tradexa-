from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from boxes.selector import select_box


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    length = serializers.FloatField(min_value=0.01)
    width = serializers.FloatField(min_value=0.01)
    height = serializers.FloatField(min_value=0.01)
    weight = serializers.FloatField(min_value=0.01)
    quantity = serializers.IntegerField(min_value=1)


class OrderSerializer(serializers.Serializer):
    items = ItemSerializer(many=True)

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("An order must contain at least one item.")
        return value


class SelectBoxView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = select_box(serializer.validated_data["items"])

        return Response({
            "selected_box": result["selected_box"],
            "order_summary": {
                "total_weight": result["total_weight"],
                "total_volume": result["total_volume"],
            },
            "reason": result["reason"],
        }, status=200)
