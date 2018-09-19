from rest_framework import serializers
from blockchain.models import Blockchain
class BlockchainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blockchain
        fields = ('__all__')

    def create(self, validated_data):
        last_transaction = Blockchain.objects.filter(processed=True).order_by('-created_at').first()
        return Blockchain.objects.create(
            **validated_data, 
            total=last_transaction.total if last_transaction else 0)
            