import uuid
from django.db import models


class CustomField(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    data_type = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class ProposalCustomField(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    custom_field = models.ForeignKey(CustomField, on_delete=models.CASCADE)
    value_char = models.CharField(max_length=200, blank=True, null=True)
    value_decimal = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10)

    def __str__(self):
        return f"{self.custom_field.name} - {self.value_char or self.value_decimal}"


class Proposal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    custom_fields = models.ManyToManyField(ProposalCustomField, related_name='proposals')
