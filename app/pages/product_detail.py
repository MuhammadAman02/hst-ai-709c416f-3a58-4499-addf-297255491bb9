from nicegui import ui
from ..services.product_service import ProductService
from ..services.cart_service import CartService
from ..ui_components.header import create_header
from ..ui_components.footer import create_footer

def create_product_detail_page(product_id: str, product_service: ProductService, cart_service: CartService) -> None:
    """Create the product detail page"""
    create_header(cart_service)
    
    product = product_service.get_product_by_id(product_id)
    
    if not product:
        with ui.column().classes('w-full max-w-screen-xl mx-auto p-4'):
            ui.label('Product not found').classes('text-2xl text-red-500')
            ui.button('Back to Home', on_click=lambda: ui.navigate('/')).classes('mt-4')
        return
    
    with ui.column().classes('w-full max-w-screen-xl mx-auto p-4'):
        # Breadcrumb navigation
        with ui.row().classes('text-sm mb-6'):
            ui.link('Home', '/').classes('text-blue-500')
            ui.label('›').classes('mx-2')
            ui.link(product['category'], '/').classes('text-blue-500')
            ui.label('›').classes('mx-2')
            ui.label(product['name']).classes('font-medium')
        
        with ui.row().classes('gap-8 flex-wrap md:flex-nowrap'):
            # Product images
            with ui.column().classes('w-full md:w-1/2'):
                ui.image(product['image']).classes('w-full h-auto rounded-lg shadow-lg')
                
                # Thumbnail gallery
                with ui.row().classes('mt-4 gap-2 justify-center'):
                    for i in range(1, 4):
                        ui.image(product['image']).classes('w-16 h-16 rounded cursor-pointer hover:opacity-80')
            
            # Product details
            with ui.column().classes('w-full md:w-1/2'):
                ui.label(product['name']).classes('text-3xl font-bold')
                ui.label(f"${product['price']:.2f}").classes('text-2xl text-blue-600 font-bold mt-2')
                
                # Rating
                with ui.row().classes('items-center mt-2'):
                    for _ in range(int(product['rating'])):
                        ui.icon('star', color='amber').classes('text-amber-400')
                    for _ in range(5 - int(product['rating'])):
                        ui.icon('star_border', color='amber').classes('text-amber-400')
                    ui.label(f"({product['reviews']} reviews)").classes('ml-2 text-gray-600')
                
                ui.separator().classes('my-4')
                
                # Description
                ui.label('Description').classes('text-xl font-semibold')
                ui.label(product['description']).classes('mt-2 text-gray-700')
                
                ui.separator().classes('my-4')
                
                # Specifications
                ui.label('Specifications').classes('text-xl font-semibold')
                with ui.grid(columns=2).classes('gap-y-2 mt-2'):
                    ui.label('Brand:').classes('font-medium')
                    ui.label(product['brand'])
                    ui.label('Movement:').classes('font-medium')
                    ui.label(product.get('movement', 'Automatic'))
                    ui.label('Case Material:').classes('font-medium')
                    ui.label(product.get('case_material', 'Stainless Steel'))
                    ui.label('Water Resistance:').classes('font-medium')
                    ui.label(product.get('water_resistance', '30m'))
                
                ui.separator().classes('my-4')
                
                # Add to cart section
                with ui.row().classes('items-center gap-4 mt-4'):
                    quantity = ui.number(value=1, min=1, max=10).classes('w-20')
                    ui.button('Add to Cart', icon='shopping_cart', on_click=lambda: add_to_cart(product, quantity.value, cart_service)).classes('bg-blue-600')
                
                # Availability
                with ui.row().classes('mt-4 items-center'):
                    ui.icon('check_circle', color='green').classes('text-green-500')
                    ui.label('In Stock - Ready to Ship').classes('text-green-600 ml-1')
    
    # Related products section
    with ui.column().classes('w-full max-w-screen-xl mx-auto p-4 mt-8'):
        ui.label('You May Also Like').classes('text-2xl font-bold mb-4')
        
        with ui.row().classes('gap-4 overflow-x-auto pb-4'):
            related_products = product_service.get_related_products(product_id)
            for related in related_products:
                with ui.card().classes('w-64 flex-shrink-0'):
                    ui.image(related['image']).classes('w-full h-48 object-cover')
                    with ui.card_section():
                        ui.label(related['name']).classes('font-bold')
                        ui.label(f"${related['price']:.2f}").classes('text-blue-600')
                        ui.button('View Details', on_click=lambda p=related['id']: ui.navigate(f'/product/{p}')).classes('mt-2')
    
    create_footer()

def add_to_cart(product, quantity, cart_service):
    cart_service.add_item(product['id'], quantity)
    ui.notify(f"{quantity} x {product['name']} added to cart", color='positive')