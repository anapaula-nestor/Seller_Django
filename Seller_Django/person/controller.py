from typing import List
from seller.models import Seller


class SellerController:
    def create(self, active: bool, person: object) -> Seller:
        seller = Seller(active=active, person=person)
        seller.save()
        return seller

    def update(self, id_: int, active: bool, person: object) -> Seller:
        seller = self.get_by_id(id_)
        seller.active = active
        seller.person = person
        seller.save()
        return seller

    def delete(self, id_: int) -> None:
        seller = self.get_by_id(id_)
        seller.delete()

    def get_all(self) -> List[Seller]:
        return Seller.objects.all()

    def get_by_id(self, id_: int) -> Seller:
        return Seller.objects.filter(id=id_).get()
