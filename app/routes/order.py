from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import order, cart, product
from app.core.security import get_current_user

router = APIRouter()

@router.post("/place-order")
def place_order(db: Session = Depends(get_db),
                current_user: dict = Depends(get_current_user)): 

    # 1️ Get user's cart items
    cart_items = db.query(cart.Cart).filter(
        cart.Cart.user_id == current_user["id"]   
    ).all()

    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    # 2️ Calculate total price
    total = 0
    for item in cart_items:
        prod = db.query(product.Product).filter(
            product.Product.id == item.product_id
        ).first()

        if not prod:
            raise HTTPException(status_code=404, detail="Product not found")

        total += prod.price * item.quantity

    # 3️ Create Order
    new_order = order.Order(
        user_id=current_user["id"],  
        total_price=total,
        status="pending"
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    # 4️ Clear Cart
    for item in cart_items:
        db.delete(item)

    db.commit()

    return {
        "message": "Order placed successfully",
        "order_id": new_order.id
    }