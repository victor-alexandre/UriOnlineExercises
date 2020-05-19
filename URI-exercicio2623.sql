/* CONSTRUINDO OS SCHEMAS */
CREATE TABLE categories(
	id NUMERIC PRIMARY KEY,
	name VARCHAR (255) NOT NULL
);

CREATE TABLE products(
	id NUMERIC PRIMARY KEY,
	name VARCHAR (255) NOT NULL,
	amount NUMERIC NOT NULL,
	price NUMERIC NOT NULL,
    id_categories NUMERIC,
	FOREIGN KEY (id_categories) REFERENCES categories (id)
);

/* INSERINDO VALORES NAS TABELAS */
INSERT INTO categories (id, name)
VALUES
	(1,	'Superior'),
    (2,	'Super Luxury'),
    (3,	'Modern'),
    (4,	'Nerd'),
    (5,	'Infantile'),
    (6,	'Robust'),
    (9,	'Wood');

INSERT INTO products (id, name, amount, price, id_categories)
VALUES 
    (1, 'Blue Chair', 30, 300.00, 9),
    (2, 'Red Chair', 200, 2150.00, 2),
    (3, 'Disney Wardrobe', 400, 829.50,	4),
    (4, 'Blue Toaster', 20, 9.90, 3),
    (5, 'Solar Panel', 30, 3000.25, 4);




/* FAZENDO A BUSCA */
SELECT P.name, C.name
FROM categories AS C
INNER JOIN products AS P
ON P.id_categories = C.id 
WHERE P.amount > 100 
  AND (C.id = 1 or C.id = 2 or C.id = 3 or C.id = 6 or C.id = 9)
ORDER BY
	C.id ASC;