
class Van:
    def __init__(self, van_id, name, price, description, image_url, van_type):
        self._id = van_id
        self._name = name
        self._price = price
        self._description = description
        self._image_url = image_url
        self._van_type = van_type

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_description(self):
        return self._description

    def get_image_url(self):
        return self._image_url

    def get_type(self):
        return self._van_type
