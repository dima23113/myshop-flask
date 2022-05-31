from model import Product, Category, Subcategory, Subcategory_type, Brand, ProductSize


def sort_brand_list_into_2_columns():
    """Создаем список для сортировки брендов по алфавиту и группировки их по первой букве. Делим список на 2 для
    вывода списка брендов в 2 колонки """
    lst = []
    brand = Brand.query.all()
    for i in brand:
        s = {
            'symbol': i.name[0].upper(),
            'name': i.name,
            'slug': i.slug
        }
        lst.append(s)
    lst1 = lst[(len(lst) // 2) + 1:]
    lst = lst[:(len(lst) // 2) + 1]
    context = {
        'brand_cl': lst,
        'brand_cl_1': lst1
    }
    return context


def get_product_list(obj, slug):
    print(obj)
    """Выдаем товары и submenu для выбранной категории/подкатегории/типа подкатегории"""
    if obj == 'category':
        products = Product.query.filter(Product.category_slug == slug,
                                        Product.available == True)
    if obj == 'brand':
        products = Product.query.filter(Product.brand_slug == slug, Product.available == True)

    if obj == 'subcategory':
        products = Product.objects.filter(
            subcategory__slug=slug,
            available=True)

    if obj == 'subcategorytype':
        products = Product.objects.filter(Product.subcategory_type_slug == slug,
                                          Product.available == True)
    category, subcategory, subcategory_type, sizes, brand = get_left_filter_submenu(products)
    return products, brand, category, subcategory, subcategory_type, sizes


def get_left_filter_submenu(product):
    """Получаем submenu для набора товаров"""
    category = Category.query.join(Category.products).filter(Product.id.in_(i.id for i in product)).all()
    subcategory = Subcategory.query.join(Subcategory.products).filter(Product.id.in_(i.id for i in product)).all()
    subcategory_type = Subcategory_type.query.join(Subcategory_type.products).filter(
        Product.id.in_(i.id for i in product)).all()
    sizes = ProductSize.query.join(ProductSize.prouduct_sizes).filter(Product.id.in_(i.id for i in product)).all()
    brands = Brand.query.join(Brand.products).filter(Product.id.in_(i.id for i in product)).all()
    return category, subcategory, subcategory_type, sizes, brands
