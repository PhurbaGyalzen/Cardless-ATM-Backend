from ast import With
from rest_framework import serializers

from transaction.models import Withdraw


class WithdrawSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Withdraw
        fields = ('id', 'amount', 'date', 'account_number', 'account_name', 'account_type', 'account_bank', 'account_branch', 'remarks', 'purpose', 'bank_code', 'atm_code', 'atm_location')