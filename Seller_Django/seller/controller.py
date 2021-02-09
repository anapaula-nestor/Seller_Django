from typing import List
from person.models import Person


class PersonController:
    def create(self, name: str, num_doc: str, cnpj: str, phone: str, address: int) -> Person:
        per = Person(name=name, num_doc=num_doc, cnpj=cnpj, phone=phone, address=address)
        per.save()
        return per

    def update(self, id_: int,  name: str, num_doc: str, cnpj: str, phone: str, address: int) -> Person:
        per = self.get_by_id(id_)
        per.name = name
        per.num_doc = num_doc
        per.cnpj = cnpj
        per.phone = phone
        per.address = address
        per.save()
        return per

    def delete(self, id_: int) -> None:
        per = self.get_by_id(id_)
        per.delete()

    def get_all(self) -> List[Person]:
        return Person.objects.all()

    def get_by_id(self, id_: int) -> Person:
        return Person.objects.filter(id=id_).get()
