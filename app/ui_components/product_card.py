from nicegui import ui
from typing import Dict, Any
from ..services.cart_service import CartService

def create_product_card(product: Dict[str, Any], cart_service: CartService) -> None:
    """Create a product card for the product listing"""
    with ui.card().classes('w-full hover:shadow-lg transition-shadow duration-300'):
        # Product image with quick view overlay
        with ui.element('div').classes('relative'):
            ui.image(product['image']).classes('w-full h-64 object-cover')
            
            # Quick actions overlay (visible on hover)
            with ui.element('div').classes('absolute inset-0 bg-black bg-opacity-50 opacity-0 hover:opacity-100 transition-opacity duration-300 flex items-center justify-center'):
                with ui.row().classes('gap-2'):
                    ui.button('Quick View', icon='visibility', on_click=lambda: ui.navigate(f'/product/{product["id"]}')).classes('bg-white text-black')
                    ui.button(icon='favorite_border').props('flat round').classes('bg-white text-black')
        
        with ui.card_section():
            # Product category
            ui.label(product['category']).classes('text-xs text-blue-600 uppercase tracking-wide')
            
            # Product name (linked to detail page)
            ui.link(product['name'], f'/product/{product["id"]}').classes('font-bold text-lg line-clamp-1 hover:text-blue-600')
            
            # Rating stars
            with ui.row().classes('items-center mt-1'):
                for _ in range(int(product['rating'])):
                    ui.icon('star', size='xs').classes('text-amber-400')
                for _ in range(5 - int(product['rating'])):
                    ui.icon('star_border', size='xs').classes('text-amber-400')
                ui.label(f"({product['reviews']})").classes('text-xs text-gray-500 ml-1')
            
            # Price
            with ui.row().classes('items-center justify-between mt-2'):
                if product.get('original_price'):
                    with ui.row().classes('items-center gap-2'):
                        ui.label(f"${product['price']:.2f}").classes('font-bold text-lg')
                        ui.label(f"${product['original_price']:.2f}").classes('text-gray-500 line-through text-sm')
                else:
                    ui.label(f"${product['price']:.2f}").classes('font-bold text-lg')
                
                # Add to cart button
                ui.button(icon='add_shopping_cart', on_click=lambda: add_to_cart(product, cart_service)).props('flat round')

def add_to_cart(product, cart_service):
    cart_service.add_item(product['id'], 1)
    ui.notify(f"{product['name']} added to cart", color='positive')