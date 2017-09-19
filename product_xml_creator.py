from flask import Flask, render_template

from xml_creator import XmlCreator

app = Flask(__name__)


@app.route('/create_xml')
def xml_creator():
    creator = XmlCreator()
    creator.creator()
    return "Product xml created."


@app.route('/product_xml.xml')
def get_product_xml():
    return render_template("products.xml")

if __name__ == '__main__':
    app.run(port=8080)
