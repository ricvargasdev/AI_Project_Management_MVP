from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.customer import Customer
from app.schemas.customer import CustomerResponse

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.get(
    "",
    response_model=list[CustomerResponse]
)
def get_customers(
    db: Session = Depends(get_db)
):

    customers = (
        db.query(Customer)
        .order_by(Customer.name)
        .all()
    )

    return customers