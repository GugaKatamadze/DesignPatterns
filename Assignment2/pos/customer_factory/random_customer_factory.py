from pos.customer.customer import Customer
from pos.customer.icustomer import ICustomer
from pos.payment_method_picker.random_payment_method_picker import (
    RandomPaymentMethodPicker,
)
from pos.product_picker.random_product_picker import RandomProductPicker
from pos.repository.repository import Repository


class RandomCustomerFactory:
    def create(self, repository: Repository) -> ICustomer:
        random_product_picker = RandomProductPicker(repository)
        random_payment_method_picker = RandomPaymentMethodPicker()

        return Customer(random_product_picker, random_payment_method_picker)
