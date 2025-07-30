from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

import sys
import os

# Add your app directory to sys.path if needed so imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from sqlmodel import SQLModel

from app.models.user import User
from app.models.category import Category
from app.models.cart_item import Cart_Item
from app.models.product import Product
from app.models.product_category import Product_Category
from app.models.order import Order
from app.models.order_item import Order_Item
from app.models.coupon_usage import Coupon_Usage
from app.models.coupon import Coupon
from app.models.product_discount import Product_Discount
from app.models.category_discount import Category_Discount
from app.models.shipment_discount import Shipment_Discount
from app.models.user_profile import User_Profile
from app.models.seller_profile import Seller_Profile
from app.models.address import Address
from app.models.shipment import Shipment
from app.models.product_review import Product_Review






config = context.config
fileConfig(config.config_file_name)

target_metadata = SQLModel.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"}
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
