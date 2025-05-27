from nicegui import ui
from typing import List, Dict, Any
from ..services.product_service import ProductService
from ..services.cart_service import CartService
from ..ui_components.header import create_header
from ..ui_components.product_card import create_product_card
from ..ui_components.footer import create_footer

def create_home_page(product_service: ProductService, cart_service: CartService) -> None:
    """Create the home page with product listings"""
    create_header(cart_service)
    
    with ui.column().classes('w-full max-w-screen-xl mx-auto p-4'):
        ui.label('Luxury Watches Collection').classes('text-3xl font-bold mb-6 text-center')
        
        # Filter controls
        with ui.row().classes('w-full justify-between items-center mb-6'):
            ui.label('Filter by:').classes('text-lg')
            
            category = ui.select(
                options=['All Categories', 'Luxury', 'Sport', 'Casual', 'Smart'],
                value='All Categories'
            ).classes('w-40')
            
            price_range = ui.select(
                options=['All Prices', 'Under $100', '$100-$500', '$500-$1000', 'Over $1000'],
                value='All Prices'
            ).classes('w-40')
            
            sort_by = ui.select(
                options=['Newest', 'Price: Low to High', 'Price: High to Low', 'Popularity'],
                value='Newest'
            ).classes('w-40')
            
            # Search box
            ui.input(placeholder='Search watches...').classes('w-64')
        
        # Product grid
        with ui.grid(columns=3).classes('gap-6 w-full'):
            products = product_service.get_all_products()
            for product in products:
                create_product_card(product, cart_service)
    
    create_footer()