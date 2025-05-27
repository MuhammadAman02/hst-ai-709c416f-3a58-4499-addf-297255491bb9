from nicegui import ui
from ..services.cart_service import CartService
from ..services.product_service import ProductService
from ..ui_components.header import create_header
from ..ui_components.footer import create_footer

def create_cart_page(cart_service: CartService, product_service: ProductService) -> None:
    """Create the shopping cart page"""
    create_header(cart_service)
    
    with ui.column().classes('w-full max-w-screen-xl mx-auto p-4'):
        ui.label('Your Shopping Cart').classes('text-3xl font-bold mb-6')
        
        cart_items = cart_service.get_cart_items()
        
        if not cart_items:
            with ui.card().classes('w-full p-8 text-center'):
                ui.icon('shopping_cart', size='5em').classes('text-gray-400 mx-auto')
                ui.label('Your cart is empty').classes('text-2xl mt-4')
                ui.label('Add some beautiful watches to your cart').classes('text-gray-600 mt-2')
                ui.button('Continue Shopping', on_click=lambda: ui.navigate('/')).classes('mt-6 mx-auto')
            return
        
        # Cart items
        with ui.column().classes('w-full gap-4'):
            total_price = 0
            
            for item_id, quantity in cart_items.items():
                product = product_service.get_product_by_id(item_id)
                if not product:
                    continue
                
                item_total = product['price'] * quantity
                total_price += item_total
                
                with ui.card().classes('w-full'):
                    with ui.row().classes('items-center p-4 gap-4'):
                        # Product image
                        ui.image(product['image']).classes('w-24 h-24 object-cover rounded')
                        
                        # Product details
                        with ui.column().classes('flex-grow gap-1'):
                            ui.link(product['name'], f'/product/{product["id"]}').classes('text-lg font-bold')
                            ui.label(f"${product['price']:.2f}").classes('text-blue-600')
                        
                        # Quantity controls
                        with ui.number(value=quantity, min=1, max=10, on_change=lambda e, p=product['id']: update_quantity(cart_service, p, e.value)).classes('w-20'):
                            pass
                        
                        # Item total
                        ui.label(f"${item_total:.2f}").classes('text-lg font-bold')
                        
                        # Remove button
                        ui.button(icon='delete', on_click=lambda p=product['id']: remove_item(cart_service, p)).props('flat color=red')
            
            # Order summary
            with ui.card().classes('w-full mt-6'):
                with ui.column().classes('p-4 gap-2'):
                    ui.label('Order Summary').classes('text-xl font-bold')
                    
                    with ui.row().classes('justify-between'):
                        ui.label('Subtotal:')
                        ui.label(f"${total_price:.2f}")
                    
                    with ui.row().classes('justify-between'):
                        ui.label('Shipping:')
                        shipping = 0 if total_price > 100 else 10
                        ui.label(f"${shipping:.2f}")
                    
                    with ui.row().classes('justify-between'):
                        ui.label('Tax:')
                        tax = total_price * 0.08
                        ui.label(f"${tax:.2f}")
                    
                    ui.separator()
                    
                    with ui.row().classes('justify-between font-bold text-lg'):
                        ui.label('Total:')
                        ui.label(f"${(total_price + shipping + tax):.2f}")
                    
                    # Checkout button
                    ui.button('Proceed to Checkout', icon='shopping_bag', on_click=lambda: checkout()).classes('mt-4 w-full bg-blue-600')
            
            # Continue shopping button
            ui.button('Continue Shopping', on_click=lambda: ui.navigate('/')).classes('mt-4')
    
    create_footer()

def update_quantity(cart_service, product_id, quantity):
    cart_service.update_quantity(product_id, quantity)
    ui.notify('Cart updated', color='positive')
    ui.refresh()

def remove_item(cart_service, product_id):
    cart_service.remove_item(product_id)
    ui.notify('Item removed from cart', color='positive')
    ui.refresh()

def checkout():
    ui.notify('Checkout functionality would be implemented here', type='info')