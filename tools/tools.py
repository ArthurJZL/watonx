"""
Tools for Customer Support Agent
Uses DummyJSON API for mock data
"""

import requests
from ibm_watsonx_orchestrate.agent_builder.tools import tool
from typing import Dict, Any


@tool
def get_order_status(order_id: str) -> Dict[str, Any]:
    """
    Check order status and details

    Args:
        order_id: The order ID to look up (use cart ID from DummyJSON)

    Returns:
        Order details including status, items, and total
    """
    try:
        response = requests.get(f"https://dummyjson.com/carts/{order_id}")
        if response.status_code == 200:
            cart = response.json()
            return {
                "order_id": order_id,
                "status": "Shipped" if int(order_id) % 2 == 0 else "Processing",
                "total": cart.get("total", 0),
                "items_count": len(cart.get("products", [])),
                "items": cart.get("products", [])[:3],  # First 3 items
                "tracking_number": f"TRK{order_id}9876" if int(order_id) % 2 == 0 else None
            }
        return {"error": "Order not found"}
    except Exception as e:
        return {"error": str(e)}


@tool
def search_product(query: str) -> Dict[str, Any]:
    """
    Search for products by name or keyword

    Args:
        query: Search term for product

    Returns:
        List of matching products with details
    """
    try:
        response = requests.get(f"https://dummyjson.com/products/search?q={query}")
        if response.status_code == 200:
            data = response.json()
            products = data.get("products", [])[:3]  # Top 3 results
            return {
                "found": len(products),
                "products": [
                    {
                        "id": p.get("id"),
                        "name": p.get("title"),
                        "price": p.get("price"),
                        "stock": p.get("stock"),
                        "rating": p.get("rating")
                    }
                    for p in products
                ]
            }
        return {"error": "Search failed"}
    except Exception as e:
        return {"error": str(e)}


