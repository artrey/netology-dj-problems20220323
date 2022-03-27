from rest_framework import serializers

from demo.models import Product, OrderPosition


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPosition
        fields = ['id', 'qty', 'order']


class ProductSerializer(serializers.ModelSerializer):
    positions = PositionSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'orders', 'positions']
        read_only_fields = ['orders']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        product = super().create(validated_data)
        for p in positions:
            OrderPosition.objects.create(
                product=product, order=p['order'], qty=p['qty']
            )
        return product

    # def update(self, instance, validated_data):
    #     pass

