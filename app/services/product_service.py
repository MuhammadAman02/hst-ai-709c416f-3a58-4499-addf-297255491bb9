from typing import List, Dict, Any, Optional

class ProductService:
    """Service for managing product data"""
    
    def __init__(self):
        # Initialize with sample product data
        self._products = self._get_sample_products()
    
    def get_all_products(self) -> List[Dict[str, Any]]:
        """Get all products"""
        return self._products
    
    def get_product_by_id(self, product_id: str) -> Optional[Dict[str, Any]]:
        """Get a product by its ID"""
        for product in self._products:
            if product['id'] == product_id:
                return product
        return None
    
    def get_products_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Get products filtered by category"""
        return [p for p in self._products if p['category'].lower() == category.lower()]
    
    def get_related_products(self, product_id: str, limit: int = 4) -> List[Dict[str, Any]]:
        """Get related products based on the same category"""
        product = self.get_product_by_id(product_id)
        if not product:
            return []
        
        category = product['category']
        related = [p for p in self._products if p['category'] == category and p['id'] != product_id]
        
        # If not enough related products in the same category, add some from other categories
        if len(related) < limit:
            other_products = [p for p in self._products if p['id'] != product_id and p not in related]
            related.extend(other_products[:limit - len(related)])
        
        return related[:limit]
    
    def search_products(self, query: str) -> List[Dict[str, Any]]:
        """Search products by name or description"""
        query = query.lower()
        return [p for p in self._products if query in p['name'].lower() or query in p['description'].lower()]
    
    def _get_sample_products(self) -> List[Dict[str, Any]]:
        """Generate sample product data"""
        return [
            {
                'id': '1',
                'name': 'Rolex Submariner',
                'category': 'Luxury',
                'price': 9999.99,
                'rating': 5,
                'reviews': 128,
                'image': 'https://images.unsplash.com/photo-1547996160-81dfa63595aa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80',
                'description': 'The Rolex Submariner is a classic diving watch known for its durability and timeless design. Water-resistant to 300 meters, it features a unidirectional rotatable bezel and luminescent display for underwater legibility.',
                'brand': 'Rolex',
                'movement': 'Automatic',
                'case_material': 'Stainless Steel',
                'water_resistance': '300m'
            },
            {
                'id': '2',
                'name': 'Omega Speedmaster',
                'category': 'Luxury',
                'price': 6799.99,
                'original_price': 7500.00,
                'rating': 5,
                'reviews': 94,
                'image': 'https://images.unsplash.com/photo-1614164185128-e4ec99c436d7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80',
                'description': 'The Omega Speedmaster, also known as the "Moonwatch," was the first watch worn on the moon. This chronograph features a tachymeter scale and is powered by Omega\'s precision mechanical movement.',
                'brand': 'Omega',
                'movement': 'Manual-winding',
                'case_material': 'Stainless Steel',
                'water_resistance': '50m'
            },
            {
                'id': '3',
                'name': 'Seiko Prospex Diver',
                'category': 'Sport',
                'price': 499.99,
                'rating': 4,
                'reviews': 215,
                'image': 'https://images.unsplash.com/photo-1612817159949-195b6eb9e31a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80',
                'description': 'The Seiko Prospex Diver is a professional-grade diving watch with 200m water resistance. It features Seiko\'s reliable automatic movement and LumiBrite hands and markers for excellent visibility in low-light conditions.',
                'brand': 'Seiko',
                'movement': 'Automatic',
                'case_material': 'Stainless Steel',
                'water_resistance': '200m'
            },
            {
                'id': '4',
                'name': 'Apple Watch Series 8',
                'category': 'Smart',
                'price': 399.99,
                'rating': 4,
                'reviews': 342,
                'image': 'https://images.unsplash.com/photo-1551816230-ef5deaed4a26?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80',
                'description': 'The Apple Watch Series 8 features advanced health monitoring including ECG and blood oxygen measurement. With a stunning always-on Retina display and powerful apps, it helps you stay connected, active, and healthy.',
                'brand': 'Apple',
                'movement': 'Digital',
                'case_material': 'Aluminum',
                'water_resistance': '50m'
            },
            {
                'id': '5',
                'name': 'Casio G-Shock',
                'category': 'Sport',
                'price': 99.99,
                'rating': 4,
                'reviews': 520,
                'image': 'https://images.unsplash.com/photo-1595520407624-66b84ae7314f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80',
                'description': 'The Casio G-Shock is built to withstand mechanical shock and vibration. With its rugged construction and 200m water resistance, it\'s perfect for outdoor activities and extreme sports.',
                'brand': 'Casio',
                'movement': 'Quartz',
                'case_material': 'Resin',
                'water_resistance': '200m'
            },
            {
                'id': '6',
                'name': 'Tissot PRX',
                'category': 'Casual',
                'price': 375.00,
                'rating': 4,
                'reviews': 183,
                'image': 'https://images.unsplash.com/photo-1548171915-e79a1fe12ae2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80',
                'description': 'The Tissot PRX features a sleek integrated bracelet design inspired by 1970s aesthetics. With its slim profile and versatile style, it transitions effortlessly from casual to formal occasions.',
                'brand': 'Tissot',
                'movement': 'Quartz',
                'case_material': 'Stainless Steel',
                'water_resistance': '100m'
            },
            {
                'id': '7',
                'name': 'Samsung Galaxy Watch 5',
                'category': 'Smart',
                'price': 279.99,
                'original_price': 329.99,
                'rating': 4,
                'reviews': 267,
                'image': 'https://images.unsplash.com/photo-1579586337278-3befd40fd17a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80',
                'description': 'The Samsung Galaxy Watch 5 offers comprehensive health monitoring including body composition analysis. With Wear OS, it provides seamless integration with Android devices and access to a wide range of apps.',
                'brand': 'Samsung',
                'movement': 'Digital',
                'case_material': 'Aluminum',
                'water_resistance': '50m'
            },
            {
                'id': '8',
                'name': 'Tag Heuer Carrera',
                'category': 'Luxury',
                'price': 5450.00,
                'rating': 5,
                'reviews': 76,
                'image': 'https://images.unsplash.com/photo-1524592094714-0f0654e20314?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80',
                'description': 'The Tag Heuer Carrera is a legendary chronograph inspired by motorsport. With its sophisticated design and precise movement, it embodies the spirit of speed and elegance that defines the Tag Heuer brand.',
                'brand': 'Tag Heuer',
                'movement': 'Automatic',
                'case_material': 'Stainless Steel',
                'water_resistance': '100m'
            },
            {
                'id': '9',
                'name': 'Timex Weekender',
                'category': 'Casual',
                'price': 49.99,
                'rating': 4,
                'reviews': 412,
                'image': 'https://images.unsplash.com/photo-1533139502658-0198f920d8e8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1000&q=80',
                'description': 'The Timex Weekender is a versatile and affordable watch with interchangeable straps. Its clean design and Indiglo night-light make it a practical choice for everyday wear.',
                'brand': 'Timex',
                'movement': 'Quartz',
                'case_material': 'Brass',
                'water_resistance': '30m'
            }
        ]