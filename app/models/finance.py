
from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class FinanceRecord(Base):
    __tablename__ = "finance_records"

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    type = Column(String)
    category = Column(String)
    date = Column(String)
    notes = Column(String)
