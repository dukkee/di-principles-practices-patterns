import uvicorn
from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from user_util import User, user_role
from db.config import async_session
from product_service import ProductService

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get('/', response_class=HTMLResponse)
async def get_products(request: Request, user: User = Depends(user_role)):
    is_preferred_customer = user.is_in_role('preferred_customer')
    view_data = {'request': request}

    async with async_session() as session:
        async with session.begin():
            service = ProductService(session)
            products = await service.get_featured_products(is_preferred_customer)
            view_data['products'] = products

    return templates.TemplateResponse('products.html', view_data)


if __name__ == '__main__':
    uvicorn.run(app)
