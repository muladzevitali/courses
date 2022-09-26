

CREATE_BRAND_TABLE = """
create table if not exists brand(
    brand_id serial primary key,
    brand_name text not null
    );
"""
CREATE_PRODUCT_TABLE = """
create table if not exists product(
    product_id serial primary key,
    product_name text not null,
    brand_id int not null,
    foreign key (brand_id) references brand(brand_id)
    );
"""
CREATE_PRODUCT_COLOR_TABLE = """
create table if not exists product_color(
    product_color_id serial primary key,
    product_color_name text not null
    );
"""
CREATE_PRODUCT_SIZE_TABLE = """
create table if not exists product_size(
    product_size_id serial primary key,
    product_size_name text not null
);
"""

CREATE_SKU_TABLE = """
create table if not exists sku(
    sku_id serial primary key,
    product_id int not null,
    product_size_id int not null,
    product_color int not null,
    foreign key (product_id) references product(product_id),
    foreign key (product_size_id) references product_size(product_size_id),
    foreign key (product_color) references product_color(product_color_id)
);
"""

SIZE_INSERT = """
insert into product_size values (1, 'small');
insert into product_size values (2, 'medium');
insert into product_size values (3, 'large');
"""

COLOR_INSERT = """
insert into product_color values (1, 'blue');
insert into product_color values (2, 'red')
"""


PRODUCT_STATEMENT = """
    select
    p.product_id, p.product_name, p.brand_id, s.sku_id, pc.product_color_name, ps.product_size_name
    from product p 
    join sku s on s.product_id=p.product_id
    join product_color pc on pc.product_color_id=s.product_color
    join product_size ps on ps.product_size_id=s.product_size_id
    
    where p.product_id=100
    """