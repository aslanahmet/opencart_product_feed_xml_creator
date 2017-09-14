import xml.etree.cElementTree as Et
import MySQLdb
import html


class XmlCreator:
    def __init__(self):
        db = MySQLdb.connect('54.171.60.117', 'bn_opencart',
                             '8a2238ca91', 'bitnami_opencart')
        cursor = db.cursor()
        cursor.execute(
            'select oc.product_id, oc_d.name, oc_d.description, oc.image, oc.price from oc_product oc inner join'
            ' oc_product_description oc_d on oc.product_id = oc_d.product_id ')
        self.all_product_data = cursor.fetchall()

    def creator(self):
        root = Et.Element("xml", version="1.0", encoding="UTF-8")
        for product_detail in self.all_product_data:
            doc = Et.SubElement(root, "product", id=str(product_detail[0]))
            Et.SubElement(doc, "name").text = product_detail[1]
            Et.SubElement(doc, "producturl").text = "http://shoppbagg.com/index.php?route=product/product&" \
                                                    "product_id={product_id}".format(product_id=product_detail[0])
            Et.SubElement(doc, "description").text = html.unescape(product_detail[2])
            Et.SubElement(doc, "bigimage").text = "http://shoppbagg.com/image/{image_name}"\
                .format(image_name=product_detail[3])
            Et.SubElement(doc, "price").text = str(product_detail[4])
            Et.SubElement(doc, "stock").text = 'true'
        tree = Et.ElementTree(root)
        tree.write("products.xml")
test = XmlCreator()
test.creator()
