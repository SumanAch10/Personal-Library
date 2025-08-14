from sqlalchemy import Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship,mapped_column,Mapped
from app.db.base_class import Base
from app.core.config import settings

class User(Base):
    
    __tablename__ = "users"
    user_id:Mapped[int] = mapped_column(Integer,primary_key = True,autoincrement = True)
    user_name:Mapped[str] = mapped_column(String(25),nullable = False,unique = True)
    user_email:Mapped[str] = mapped_column(String,nullable = False,unique = True)
    user_pwd:Mapped[str] = mapped_column(String,nullable=False)
    




