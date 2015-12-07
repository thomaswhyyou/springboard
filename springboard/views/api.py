from pyramid.view import view_config, view_defaults

from springboard.models import sess, Product, Vendor


DEFAULT_BATCH_AMOUNT = 35;


@view_defaults(renderer="json")
class APIViews:
    def __init__(self, request):
        self.request = request

    # api/products
    @view_config(route_name="products")
    def products_list(self):
        # XXX: Better to use form schema to validate params, but for simplicity
        # just do it manually.
        offset = int(self.request.params.get("offset", 0))

        products = (
            sess.query(Product)
                .join(Vendor, Product.vendor_id == Vendor.id)
                .order_by(Product.created_at.desc())
                .offset(offset * DEFAULT_BATCH_AMOUNT)
                .limit(DEFAULT_BATCH_AMOUNT)
        ).all()

        resp = {
            "offset": offset,
            "filtered": {},
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
