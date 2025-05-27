from nicegui import ui

def create_footer() -> None:
    """Create the site footer"""
    with ui.footer().classes('bg-gray-800 text-white mt-12'):
        with ui.column().classes('w-full max-w-screen-xl mx-auto p-8'):
            with ui.row().classes('w-full justify-between flex-wrap gap-8'):
                # Company info
                with ui.column().classes('gap-2 w-full md:w-1/4'):
                    with ui.row().classes('items-center gap-2'):
                        ui.icon('watch', size='lg').classes('text-blue-400')
                        ui.label('LuxWatch').classes('text-xl font-bold')
                    ui.label('Your destination for luxury timepieces. Discover the perfect watch to match your style and elevate your collection.').classes('text-gray-400 text-sm mt-2')
                
                # Quick links
                with ui.column().classes('gap-2 w-full md:w-1/4'):
                    ui.label('Quick Links').classes('font-bold mb-2')
                    ui.link('About Us', '/').classes('text-gray-400 hover:text-white')
                    ui.link('Contact Us', '/').classes('text-gray-400 hover:text-white')
                    ui.link('FAQ', '/').classes('text-gray-400 hover:text-white')
                    ui.link('Shipping & Returns', '/').classes('text-gray-400 hover:text-white')
                
                # Categories
                with ui.column().classes('gap-2 w-full md:w-1/4'):
                    ui.label('Categories').classes('font-bold mb-2')
                    ui.link('Luxury Watches', '/').classes('text-gray-400 hover:text-white')
                    ui.link('Sport Watches', '/').classes('text-gray-400 hover:text-white')
                    ui.link('Smart Watches', '/').classes('text-gray-400 hover:text-white')
                    ui.link('Accessories', '/').classes('text-gray-400 hover:text-white')
                
                # Newsletter
                with ui.column().classes('gap-2 w-full md:w-1/4'):
                    ui.label('Stay Updated').classes('font-bold mb-2')
                    ui.label('Subscribe to our newsletter for exclusive offers').classes('text-gray-400 text-sm')
                    with ui.row().classes('mt-2 gap-2'):
                        ui.input(placeholder='Your email').classes('w-full')
                        ui.button('Subscribe', icon='send').classes('bg-blue-600')
            
            ui.separator().classes('my-6 bg-gray-700')
            
            with ui.row().classes('w-full justify-between items-center flex-wrap gap-4'):
                ui.label('© 2023 LuxWatch. All rights reserved.').classes('text-gray-400 text-sm')
                
                with ui.row().classes('gap-4'):
                    ui.button(icon='facebook').props('flat round').classes('text-gray-400 hover:text-white')
                    ui.button(icon='instagram').props('flat round').classes('text-gray-400 hover:text-white')
                    ui.button(icon='twitter').props('flat round').classes('text-gray-400 hover:text-white')
                    ui.button(icon='pinterest').props('flat round').classes('text-gray-400 hover:text-white')