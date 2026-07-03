-- Ingredientes
CREATE TABLE ingredients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    unit TEXT NOT NULL,              -- ej: 'kg', 'g', 'lb', 'liter'
    price_per_unit DECIMAL(10,2) NOT NULL
);

-- Donuts
CREATE TABLE donuts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    gluten_free TEXT NOT NULL CHECK (gluten_free IN ('YES','NO')),
    price_per_donut DECIMAL(10,2) NOT NULL
);

-- Relación Donuts - Ingredientes (muchos a muchos)
CREATE TABLE donut_ingredients (
    donut_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    quantity DECIMAL(10,2) NOT NULL, -- ej: 200 g de harina
    PRIMARY KEY (donut_id, ingredient_id),
    FOREIGN KEY (donut_id) REFERENCES donuts(id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
);

-- Clientes
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

-- Pedidos
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- Donuts dentro de cada pedido
CREATE TABLE order_items (
    order_id INTEGER NOT NULL,
    donut_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    PRIMARY KEY (order_id, donut_id),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (donut_id) REFERENCES donuts(id)
);
