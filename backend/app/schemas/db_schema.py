from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class WebpageTemplate(Base):
    __tablename__ = "webpage_templates"

    id = Column(Integer, primary_key=True, index=True)
    market = Column(String, index=True)          # e.g., healthcare, finance
    description = Column(String)                 # what this template is for
    webpage_code = Column(Text)                  # full HTML + CSS + JS
