from nicegui import ui
from ..services.cart_service import CartService

def create_header(cart_service: CartService) -> None:
    """Create the site header with navigation and cart icon"""
    with ui.header().classes('bg-white shadow-md'):
        with ui.row().classes('w-full max-w-screen-xl mx-auto p-4 items-center justify-between'):
            # Logo and site name
            with ui.row().classes('items-center gap-2 cursor-pointer').on('click', lambda: ui.navigate('/')):
                ui.icon('watch', size='lg').classes('text-blue-600')
                ui.label('LuxWatch').classes('text-2xl font-bold text-blue-600')
            
            # Navigation menu
            with ui.row().classes('gap-6'):
                ui.link('Home', '/').classes('text-gray-700 hover:text-blue-600')
                ui.link('Luxury', '/').classes('text-gray-700 hover:text-blue-600')
                ui.link('Sport', '/').classes('text-gray-700 hover:text-blue-600')
                ui.link('Smart', '/').classes('text-gray-700 hover:text-blue-600')
                ui.link('Sale', '/').classes('text-gray-700 hover:text-blue-600')
            
            # User actions
            with ui.row().classes('gap-4 items-center'):
                ui.button(icon='search').props('flat')
                
                # Cart with item count
                with ui.button(icon='shopping_cart', on_click=lambda: ui.navigate('/cart')).props('flat').classes('relative'):
                    cart_count = sum(cart_service.get_cart_items().values())
                    if cart_count > 0:
                        with ui.badge(str(cart_count)).classes('bg-red-500 absolute -top-1 -right-1'):
                            pass
                
                ui.button(icon='person').props('flat')