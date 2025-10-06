# Customer Support Agent - watsonx Orchestrate

A simple AI-powered customer support agent built with watsonx Orchestrate that helps customers with:
- 📦 Order tracking and status
- 🛍️ Product search and information
- 📚 Knowledge base queries and FAQs

## Features

### Multi-Agent Architecture
- **Customer Support Agent** (Orchestrator) - Handles general inquiries and delegates to specialists
- **Returns Agent** (Specialist) - Dedicated returns and refunds processing

### Customer Support Agent Tools
1. **get_order_status** - Check order status, tracking info, and items
2. **search_product** - Search products by name with pricing and availability

### Returns Agent Tools
1. **initiate_return** - Process return requests and issue RAN numbers
2. **generate_return_label** - Create prepaid return shipping labels
3. **check_return_status** - Track return package status
4. **calculate_refund_amount** - Calculate and explain refund amounts

### Knowledge Base
- Comprehensive customer support knowledge base (PDF)
- Return policies, shipping info, warranty details, FAQs
- Shared by both agents for consistent answers

### Data Source
Uses [DummyJSON](https://dummyjson.com) free API for realistic mock e-commerce data

## Quick Start

### 1. Test the Tools
```bash
source watonx-env/bin/activate
python test_tools.py
```

### 2. Deploy the Agent
```bash
./deploy.sh
```

### 3. Chat with the Agent
```bash
orchestrate chat start
```

## Example Questions

Try these with your agent:
- "What's the status of order #1?"
- "Do you have any phones available?"
- "How do I return an item?"
- "Show me order #5 details"
- "Search for laptop"

## Project Structure

```
.
├── agents/
│   ├── customer_support_agent.yaml   # Orchestrator agent config
│   ├── returns_agent.yaml            # Returns specialist agent config
│   └── customer_support_kb.yaml      # Knowledge base config
├── tools/
│   ├── tools.py                      # Customer support tools
│   └── returns_tools.py              # Returns specialist tools
├── knowledge_base/
│   └── customer_support_kb.pdf       # Policies and FAQs
├── test_tools.py                     # Tool testing script
└── README.md                         # This file
```

## Files

### Agents
- **customer_support_agent.yaml** - Orchestrator agent with collaboration
- **returns_agent.yaml** - Specialist agent for returns processing
- **customer_support_kb.yaml** - Knowledge base configuration

### Tools
- **tools.py** - Customer support tools (order status, product search)
- **returns_tools.py** - Returns tools (initiate, label, status, refund)

### Other
- **test_tools.py** - Test tools before deploying

## Requirements

- Python 3.11-3.13
- ibm-watsonx-orchestrate SDK
- watsonx Orchestrate instance credentials (in .env)
