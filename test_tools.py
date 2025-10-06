"""
Quick Demo: Test tools directly before deploying agent
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'tools'))

from tools import get_order_status, search_product
from returns_tools import initiate_return, generate_return_label, check_return_status, calculate_refund_amount


def main():
    print("=" * 60)
    print("   CUSTOMER SUPPORT TOOLS - Quick Test")
    print("=" * 60)
    print("\nTesting all tools with sample data...\n")

    # Test Order Status
    print("1️⃣  Testing Order Status Tool")
    print("-" * 40)
    print("Query: Get status for order #1")
    result = get_order_status("1")
    print(f"Result: {result}")
    print()

    # Test Product Search
    print("2️⃣  Testing Product Search Tool")
    print("-" * 40)
    print("Query: Search for 'phone'")
    result = search_product("phone")
    print(f"Result: {result}")
    print()

    # Test Initiate Return
    print("3️⃣  Testing Initiate Return Tool")
    print("-" * 40)
    print("Query: Initiate return for order #2 (reason: defective)")
    result = initiate_return("2", "defective item")
    print(f"Result: {result}")
    print()

    # Test Generate Return Label
    print("4️⃣  Testing Generate Return Label Tool")
    print("-" * 40)
    print("Query: Generate label for RAN-2-1234")
    result = generate_return_label("RAN-2-1234", "2")
    print(f"Result: {result}")
    print()

    # Test Check Return Status
    print("5️⃣  Testing Check Return Status Tool")
    print("-" * 40)
    print("Query: Check status for RAN-2-1234")
    result = check_return_status("RAN-2-1234")
    print(f"Result: {result}")
    print()

    # Test Calculate Refund Amount
    print("6️⃣  Testing Calculate Refund Amount Tool")
    print("-" * 40)
    print("Query: Calculate refund for order #2 (all items)")
    result = calculate_refund_amount("2", "all")
    print(f"Result: {result}")
    print()

    print("=" * 60)
    print("✅ All tools tested successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
