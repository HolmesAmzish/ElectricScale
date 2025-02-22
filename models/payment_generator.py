from io import BytesIO

import barcode
import qrcode
import json
import time
import random

from PyQt6.QtGui import QPixmap
from barcode.writer import ImageWriter

"""
File: models/payment_generator.py
Date: 2025-02-22
"""


def generate_order_id():
    """Generate a unique order ID"""
    timestamp = int(time.time())
    order_id = f"{timestamp}"
    return order_id


def generate_qrcode(cart_items, total_price):
    try:
        order_info = {
            "cart_items": [{"label": item.label, "weight": item.weight, "price": item.price} for item in cart_items],
            "total_price": total_price
        }

        order_json = json.dumps(order_info, ensure_ascii=False)
        qr_code = qrcode.make(order_json)

        # Convert QR code to QPixmap
        qr_byte_array = BytesIO()
        qr_code.save(qr_byte_array, format='PNG')
        qr_byte_array.seek(0)

        qr_pixmap = QPixmap()
        qr_pixmap.loadFromData(qr_byte_array.getvalue())
        return qr_pixmap
    except Exception as e:
        print(f"Error generating QR code: {e}")
        return QPixmap()  # Return an empty QPixmap on error


def generate_barcode(order_id):
    try:
        code128 = barcode.get_barcode_class('code128')
        order_barcode = code128(order_id, writer=ImageWriter())

        barcode_byte_array = BytesIO()
        order_barcode.write(barcode_byte_array, {'module_width': 0.4, 'module_height': 15})  # 调整条形码宽度和高度
        barcode_byte_array.seek(0)

        barcode_pixmap = QPixmap()
        barcode_pixmap.loadFromData(barcode_byte_array.read())

        return barcode_pixmap
    except Exception as e:
        print(f"Error generating barcode: {e}")
        return QPixmap()



