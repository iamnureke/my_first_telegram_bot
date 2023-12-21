from FakeStore import FakeStoreAPI

fake_store_api = FakeStoreAPI()


def do_format():
    lis = ''
    for i in fake_store_api.get_all_products():
        lis += f'''
ID: {i['id']}
Продукт: {i['title']}
Цена: {i['price']}
Категория: {i['category']}
            '''
    return lis


def show_categories():
    a = 1
    categories = ''
    for category in fake_store_api.get_all_categories():
        categories += f'{a}){category}\n'
        a += 1
    return categories

def do_format_list():
    lis = []
    for i in fake_store_api.get_all_products():
        lis.append(f'''
ID: {i['id']}
Продукт: {i['title']}
Цена: {i['price']}
Категория: {i['category']}
                ''')
    return lis


def category_jewelery():
    lis = ''
    for i in fake_store_api.get_product_in_specific_category('jewelery'):
        lis += f'''
ID: {i['id']}
Продукт: {i['title']}
Цена: {i['price']}
Категория: {i['category']}
                        '''
    return lis

def category_electronics():
    lis = ''
    for i in fake_store_api.get_product_in_specific_category('electronics'):
        lis += f'''
ID: {i['id']}
Продукт: {i['title']}
Цена: {i['price']}
Категория: {i['category']}
                        '''
    return lis

def category_men_clothing():
    lis = ''
    for i in fake_store_api.get_product_in_specific_category("men's clothing"):
        lis += f'''
ID: {i['id']}
Продукт: {i['title']}
Цена: {i['price']}
Категория: {i['category']}
                            '''
    return lis

def category_women_clothing():
    lis = ''
    for i in fake_store_api.get_product_in_specific_category("women's clothing"):
        lis += f'''
ID: {i['id']}
Продукт: {i['title']}
Цена: {i['price']}
Категория: {i['category']}
                                '''
    return lis