from flask import Flask

from xml_creator import XmlCreator

app = Flask(__name__)


@app.route('/create_xml')
def xml_creator():
    creator = XmlCreator()
    creator.creator()
    return "Product xml created."


@app.route('/product_xml')
def get_product_xml():
    products_xml = open('products.xml', 'r')
    return products_xml.read()

if __name__ == '__main__':
    app.run(port=8080)
