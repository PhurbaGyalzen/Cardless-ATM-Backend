from transaction.api.serializers import WithdrawSerializer
from rest_framework.viewsets import ModelViewSet
from transaction.models import Withdraw




class WithdrawView(ModelViewSet):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer
    

