from sqlalchemy.orm import Session
from schemas import ProductUpdate, ProductCreate
from models import ProductModel

# funcao que faz a leitura de todos os itens do banco
def get_products(db: Session):
    return db.query(ProductModel).all()

def get_product(db: Session):
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()


def create_product(db: Session, product: ProductCreate):
    db_product = ProductModel(**product.model_dump())

    db.add(db_product)

    db.commit()

    db.refresh(db_product)

    return db_product

def delete_product(db: Session, product_id: int):
    db.product(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db.product)
    db.commit()
    return db.product

def update_product(db: Session, product_id: int, product: ProductUpdate):
    db.product(ProductModel).filter(ProductModel.id == product_id).first()

    if db.product is None:
        return None
    
    if product.description is not None:
        db.filial = product.filial

    if product.postes is not None:
        db.postes = product.postes

    if product.ligacao is not None:
        db.ligacao = product.ligacao
           
    if product.inauguracao is not None:
      db.inauguracao = product.inauguracao
    
    if product.obra is not None:
        db.obra = product.obra

    if product.responsavel is not None:
        db.responsavel = product.responsavel
    
    if product.link is not None:
        db.link = product.link

    if product.projetos is not None:   
       db.projetos = product.projetos
    
    if product.orcamento is not None:
       db.orcamento = product.orcamento
    
    if product.material is not None:
        db.material = product.material

    if product.ti is not None:
        db.ti = product.ti
   
    if product.equipe is not None:
        db.equipe = product.equipe

    if product.orcamento_final is not None:
        db.orcamento_final = product.orcamento_final

    if product.status is not None:
        db.status = product.status 

    db.commit()
    return db    
    
    
    




    