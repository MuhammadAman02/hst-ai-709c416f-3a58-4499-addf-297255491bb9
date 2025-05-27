from nicegui import app, ui

# Import components
from .pages.home import create_home_page
from .pages.product_detail import create_product_detail_page
from .pages.cart import create_cart_page
from .services.cart_service import CartService
from .services.product_service import ProductService

# Initialize services
product_service = ProductService()
cart_service = CartService()

# Setup routes
@ui.page('/')
def home_page():
    create_home_page(product_service, cart_service)

@ui.page('/product/{product_id}')
def product_detail_page(product_id: str):
    create_product_detail_page(product_id, product_service, cart_service)

@ui.page('/cart')
def cart_page():
    create_cart_page(cart_service, product_service)

# Make services available to the app
app.product_service = product_service
app.cart_service = cart_service