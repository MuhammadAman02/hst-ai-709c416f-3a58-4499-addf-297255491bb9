from typing import Dict, Any

class CartService:
    """Service for managing the shopping cart"""
    
    def __init__(self):
        # Initialize an empty cart
        # Dictionary with product_id as key and quantity as value
        self._cart_items: Dict[str, int] = {}
    
    def add_item(self, product_id: str, quantity: int = 1) -> None:
        """Add an item to the cart or increase quantity if already exists"""
        if product_id in self._cart_items:
            self._cart_items[product_id] += quantity
        else:
            self._cart_items[product_id] = quantity
    
    def remove_item(self, product_id: str) -> None:
        """Remove an item from the cart"""
        if product_id in self._cart_items:
            del self._cart_items[product_id]
    
    def update_quantity(self, product_id: str, quantity: int) -> None:
        """Update the quantity of an item in the cart"""
        if quantity <= 0:
            self.remove_item(product_id)
        else:
            self._cart_items[product_id] = quantity
    
    def get_cart_items(self) -> Dict[str, int]:
        """Get all items in the cart"""
        return self._cart_items
    
    def get_item_count(self, product_id: str) -> int:
        """Get the quantity of a specific item in the cart"""
        return self._cart_items.get(product_id, 0)
    
    def get_total_items(self) -> int:
        """Get the total number of items in the cart"""
        return sum(self._cart_items.values())
    
    def clear_cart(self) -> None:
        """Clear all items from the cart"""
        self._cart_items = {}