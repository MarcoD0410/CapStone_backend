""" A ZooController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Zoo import Zoo


class ZooController(Controller):
    """Class Docstring Description
    """

    def __init__(self, request: Request):
        self.request = request


    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", ZooController)
        """
        id = self.request.param("id")
        return Zoo.find(id)

        pass

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", ZooController)
        """
        return Zoo.all()

        pass

    def create(self):
        country = self.request.input("country")
        animal = self.request.input("animal")
        zoo = Zoo.create({"country": country, "animal": animal})
        return zoo

        pass

    

    def update(self):
        country = self.request.input("country")
        animal = self.request.input("animal")
        id = self.request.param("id")
        Zoo.where("id", id).update({"country": country, "animal": animal})
        return Zoo.where("id", id).get()

        pass

    def destroy(self):
        id = self.request.param("id")
        zoo = Zoo.where("id", id).get()
        Zoo.where("id", id).delete()
        return zoo

        pass