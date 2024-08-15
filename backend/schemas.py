from pydantic import BaseModel, PositiveFloat, EmailStr, validator, Field
from enum import Enum
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    filial: str
    postes:  bool
    ligacao: bool
    inauguracao: str 
    obra: str 
    responsavel: str
    link: str 
    projetos: str
    orcamento: str
    material: str
    ti: bool
    equipe: str
    orcamento_final: str
    status: str

    class ProductCreate(ProductBase):
        pass

    class ProductResponse(ProductBase):
        id: int
        created: datetime

        class Config:
            from_atributes = True

    class ProductUpdate(ProductBase):
        filial: Optional[str] =None
        postes: Optional[bool] =None
        ligacao: Optional[bool] =None
        inauguracao: Optional[str] =None
        obra: Optional[str] =None 
        responsavel: Optional[str] =None
        link: Optional[str] = None
        projetos: Optional[str] =None
        orcamento: Optional[str] =None
        material: Optional[str] =None
        ti: Optional[bool] =None
        equipe: Optional[str] =None
        orcamento_final: Optional[str] =None
        status: Optional[str] =None
