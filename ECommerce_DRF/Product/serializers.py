
class ProductSerializer(serializers.Serializer):
    # category = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        models = Product
        fields = "__all__"

