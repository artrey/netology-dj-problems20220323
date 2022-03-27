from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from demo.models import Product, Order, OrderPosition


class PositionInlineFormset(BaseInlineFormSet):
    def clean(self):
        pids = {form.cleaned_data['product'].id for form in self.forms}
        if len(pids) != len([f for f in self.forms if f.cleaned_data['DELETE'] is False]):
            raise ValidationError('У вас наблюдаются дубликаты')
        return super().clean()


class PositionInline(admin.TabularInline):
    formset = PositionInlineFormset
    model = OrderPosition
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [PositionInline]
