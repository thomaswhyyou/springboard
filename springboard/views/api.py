from pyramid.view import view_config, view_defaults

from springboard.models import sess, Product, Vendor


@view_defaults(renderer="json")
class APIViews:
    def __init__(self, request):
        self.request = request

    # api/products
    @view_config(route_name="products")
    def products_list(self):
        products = (
            sess.query(Product)
                .join(Vendor, Product.vendor_id == Vendor.id)
                .order_by(Product.created_at.desc())
                .limit(50)
                .offset(0)
        ).all()

        resp = {
            "offeset": 0,
            "filters": {},
            "data": [],
        }
        for product in products:
            resp["data"].append({
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "photo_url": product.photo_url,
                "price": float(product.price),
                "is_on_sale": product.is_on_sale,
                "target_gender": product.target_gender,
                "category": product.category,
                "created_at": product.created_at.isoformat(),
                "vendor_id": product.vendor_id,
                "vendor_name": product.vendor.name,
            })

        return resp
