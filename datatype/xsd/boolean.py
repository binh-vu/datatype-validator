from .xsd import Xsd

class XsdBoolean(Xsd):
    def label(self):
        return "xsd:boolean"

    def uri(self):
        return "http://www.w3.org/2001/XMLSchema#boolean"