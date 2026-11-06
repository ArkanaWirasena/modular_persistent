from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from subscription_product import SubscriptionProduct

PRODUCT_TYPES = {
    PhysicalProduct.TYPE: (PhysicalProduct, "Physical Product",
                           [("weight", "weight (kg): ", float)]),
    DigitalProduct.TYPE: (DigitalProduct, "Digital Product",
                           [("download_size", "Download size (MB): ", float)]),
    SubscriptionProduct.TYPE: (SubscriptionProduct, "Subscription Product",
                                [("duration_months", "duration (months): ", int)]),
}

def get_type_keys():
    return list(PRODUCT_TYPES.keys())

def get_label(type_key: str) -> str:
    return PRODUCT_TYPES[type_key][1]

def get_extra_fields(type_key: str):
    return PRODUCT_TYPES[type_key][2]

def create_product(type_key: str, product_id: str, name: str, 
                   price: float, stock: int, **extra):
    if type_key not in PRODUCT_TYPES:
        raise ValueError(f"Invalid product type: {type_key}")
    cls = PRODUCT_TYPES[type_key][0]
    return cls(product_id, name, price, stock, **extra)

def from_dict(item: dict):
    type_key = item.get("type")
    if type_key not in PRODUCT_TYPES:
        raise ValueError(f"Invalid product type: {type_key}")
    extra = {field: conv(item[field]) for field, _, conv in get_extra_fields(type_key)}
    return create_product(type_key, item["id"], item["name"],
                          float(item["price"]), int(item["stock"]), **extra)