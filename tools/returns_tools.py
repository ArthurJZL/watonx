"""
Tools for Returns & Refunds Agent
Specialized agent for handling product returns and refunds
"""

import random
from ibm_watsonx_orchestrate.agent_builder.tools import tool
from typing import Dict, Any


@tool
def initiate_return(order_id: str, reason: str) -> Dict[str, Any]:
    """
    Initiate a return for an order

    Args:
        order_id: The order ID to return
        reason: Reason for return (e.g., "defective", "wrong item", "changed mind", "not as described")

    Returns:
        Return authorization details including RAN number and next steps
    """
    # Generate Return Authorization Number
    ran = f"RAN-{order_id}-{random.randint(1000, 9999)}"

    # Determine if return is eligible
    eligible_reasons = ["defective", "wrong item", "not as described", "changed mind", "damaged"]
    is_eligible = any(r in reason.lower() for r in eligible_reasons)

    if not is_eligible:
        return {
            "success": False,
            "error": "Invalid return reason. Please provide a valid reason such as defective, wrong item, changed mind, or damaged."
        }

    # Check if free return shipping applies
    free_shipping = "defective" in reason.lower() or "wrong" in reason.lower() or "damaged" in reason.lower()

    return {
        "success": True,
        "ran": ran,
        "order_id": order_id,
        "reason": reason,
        "free_return_shipping": free_shipping,
        "return_window": "30 days from purchase",
        "next_steps": [
            "Pack item in original packaging with all tags attached",
            "Print return label (will be emailed separately)",
            "Drop off at any authorized shipping location",
            "Refund will be processed within 5-7 business days after receipt"
        ],
        "message": f"Return authorized! Your Return Authorization Number is {ran}. A prepaid return label will be emailed to you within 1 hour."
    }


@tool
def generate_return_label(ran: str, order_id: str) -> Dict[str, Any]:
    """
    Generate a prepaid return shipping label

    Args:
        ran: Return Authorization Number from initiate_return
        order_id: The order ID

    Returns:
        Return label details and tracking information
    """
    # Generate tracking number for return
    tracking_number = f"RTN{random.randint(100000, 999999)}"

    return {
        "success": True,
        "ran": ran,
        "order_id": order_id,
        "tracking_number": tracking_number,
        "label_url": f"https://returns.example.com/labels/{ran}.pdf",
        "carrier": "UPS",
        "drop_off_locations": [
            "UPS Store - 123 Main St",
            "UPS Store - 456 Oak Ave",
            "Any UPS drop box"
        ],
        "message": f"Return label generated! Download at the provided URL. Use tracking number {tracking_number} to monitor your return shipment."
    }


@tool
def check_return_status(ran: str) -> Dict[str, Any]:
    """
    Check the status of a return

    Args:
        ran: Return Authorization Number

    Returns:
        Current status of the return and refund
    """
    # Simulate different return statuses
    statuses = [
        {
            "status": "Label Generated",
            "description": "Return label has been created and emailed to you",
            "refund_status": "Pending - awaiting returned item",
            "estimated_refund_date": "7-14 days after we receive the item"
        },
        {
            "status": "In Transit",
            "description": "Return package is on its way to our warehouse",
            "refund_status": "Pending - item in transit",
            "estimated_refund_date": "5-7 days after receipt"
        },
        {
            "status": "Received",
            "description": "We've received your return and are processing it",
            "refund_status": "Processing - item received and being inspected",
            "estimated_refund_date": "3-5 business days"
        },
        {
            "status": "Refund Issued",
            "description": "Refund has been processed to your original payment method",
            "refund_status": "Complete",
            "estimated_refund_date": "Refund completed"
        }
    ]

    # Pick a random status for demo
    status_info = random.choice(statuses)

    return {
        "success": True,
        "ran": ran,
        **status_info,
        "message": f"Return status: {status_info['status']}. {status_info['description']}"
    }


@tool
def calculate_refund_amount(order_id: str, items_to_return: str = "all") -> Dict[str, Any]:
    """
    Calculate the refund amount for a return

    Args:
        order_id: The order ID
        items_to_return: Which items to return (default: "all", or specify item names)

    Returns:
        Breakdown of refund amount
    """
    # Mock order totals (in real app, would fetch from order system)
    base_total = random.uniform(50, 500)
    shipping_cost = 4.99 if base_total < 50 else 0.0
    tax = base_total * 0.08

    # Calculate refund
    if items_to_return.lower() == "all":
        item_refund = base_total
        refund_shipping = shipping_cost
    else:
        # Partial return - refund 50% as example
        item_refund = base_total * 0.5
        refund_shipping = 0.0  # No shipping refund on partial returns

    total_refund = item_refund + refund_shipping

    return {
        "success": True,
        "order_id": order_id,
        "items_to_return": items_to_return,
        "breakdown": {
            "item_refund": round(item_refund, 2),
            "shipping_refund": round(refund_shipping, 2),
            "tax_refund": round(tax, 2),
            "total_refund": round(total_refund + tax, 2)
        },
        "refund_method": "Original payment method",
        "processing_time": "5-7 business days after receipt",
        "message": f"Estimated refund: ${round(total_refund + tax, 2)}"
    }


# Test the tools
if __name__ == "__main__":
    print("Testing Returns Tools:")
    print("\n1. Initiate Return:")
    print(initiate_return("123", "defective item"))

    print("\n2. Generate Return Label:")
    print(generate_return_label("RAN-123-5678", "123"))

    print("\n3. Check Return Status:")
    print(check_return_status("RAN-123-5678"))

    print("\n4. Calculate Refund:")
    print(calculate_refund_amount("123"))
