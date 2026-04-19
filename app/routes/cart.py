from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.cart import Cart
from app.models.product import Product
from app.schemas.cart_schema import CartCreate, CartUpdate, CartResponse
from app.core.security import get_current_user

router = APIRouter(prefix="/cart", tags=["Cart"])


# Create (POST) - Add item to cart
@router.post("/add", response_model=CartResponse)
def add_to_cart(
    cart: CartCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    product = db.query(Product).filter(Product.id == cart.product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    cart_item = db.query(Cart).filter(
        Cart.user_id == current_user["id"],
        Cart.product_id == cart.product_id
    ).first()

    if cart_item:
        cart_item.quantity += cart.quantity
    else:
        cart_item = Cart(
            user_id=current_user["id"],
            product_id=cart.product_id,
            quantity=cart.quantity
        )
        db.add(cart_item)

    db.commit()
    db.refresh(cart_item)

    return cart_item


# Read (GET) - View cart
@router.get("/", response_model=list[CartResponse])
def view_cart(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    cart_items = db.query(Cart).filter(
        Cart.user_id == current_user["id"]
    ).all()

    return cart_items


# Update (PUT) - Update cart item
@router.put("/{cart_id}")
def update_cart(
    cart_id: int,
    cart: CartUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    cart_item = db.query(Cart).filter(
        Cart.id == cart_id,
        Cart.user_id == current_user["id"]
    ).first()

    if not cart_item:
        raise HTTPException(status_code=404, detail="Item not found")

    cart_item.quantity = cart.quantity

    db.commit()

    return {"message": "Cart updated"}


# Delete (DELETE) - Remove item
@router.delete("/{cart_id}")
def remove_cart_item(
    cart_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    cart_item = db.query(Cart).filter(
        Cart.id == cart_id,
        Cart.user_id == current_user["id"]
    ).first()

    if not cart_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(cart_item)
    db.commit()

    return {"message": "Item removed from cart"}