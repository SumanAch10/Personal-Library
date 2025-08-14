from sqlalchemy import Integer,String,DateTime,ForeignKey,Text
from sqlalchemy.orm import relationship,mapped_column,Mapped
from app.db.base_class import Base

class Books(Base):
    __tablename__ = "books"
    bk_id:Mapped[int] = mapped_column(Integer,primary_key = True,autoincrement = True)
    bk_name:Mapped[str] = mapped_column(String,nullable = False)
    author_name:Mapped[str] = mapped_column(String,nullable = False)
    bk_summary:Mapped[str] = mapped_column(Text,nullable = False)