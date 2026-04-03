# Inventory Management System

A command-line inventory management application built in Python, developed as part of a recruiting assignment for Autodesk.

## Project Structure
IMS/    
├── main.py          # Entry point, CLI menu    
├── inventory.py     # Inventory class      
├── decorators.py    # @log_operation decorator     
├── exceptions.py    # Custom exception hierarchy      
├── utils.py         # Filtering and sorting functions      
└── models/     
├── init.py     
└── item.py      # Item (abstract), Electronics, Grocery   

## Features

- OOP design with abstract base class and two concrete item types
- Full CRUD operations via interactive CLI menu
- CSV file I/O with context managers
- Custom exception hierarchy with meaningful error messages
- Generator-based category filtering
- Decorator logging with timestamps and execution time
- Filtering and sorting using Python built-ins (`filter`, `sorted`, `max`)