from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests

class ActionSearchProduct(Action):
    def name(self) -> str:
        return "action_search_product"

    def run(self, dispatcher, tracker, domain):
        product = tracker.get_slot("product")
        # In a real scenario, call your product API
        results = self.search_products(product)
        
        if results:
            response = f"Found these {product}:\n" + "\n".join(results[:3])
        else:
            response = f"Sorry, no {product} found in stock."
            
        dispatcher.utter_message(text=response)
        return [SlotSet("product", None)]

    def search_products(self, query):
        # Mock product database - replace with real API call
        mock_products = {
            "laptop": ["Dell XPS 13", "MacBook Air", "Lenovo ThinkPad"],
            "headphones": ["Sony WH-1000XM4", "Apple AirPods Pro", "Bose QuietComfort"],
            "shoes": ["Nike Air Zoom", "Adidas Ultraboost", "New Balance 990"]
        }
        return mock_products.get(query.lower(), [])

class ActionCheckOrder(Action):
    def name(self) -> str:
        return "action_check_order"

    def run(self, dispatcher, tracker, domain):
        order_id = tracker.get_slot("order_id")
        # In real implementation, call order tracking API
        status = self.get_order_status(order_id)
        dispatcher.utter_message(text=status)
        return [SlotSet("order_id", None)]

    def get_order_status(self, order_id):
        # Mock order database
        mock_orders = {
            "ORD-12345": "Shipped (ETA: Nov 10)",
            "ORD-67890": "Processing",
            "ORD-55555": "Delivered"
        }
        return mock_orders.get(order_id, "Order not found. Please check your ID.")
