CREATE TABLE IF NOT EXISTS productos (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(100) NOT NULL,
    sku         VARCHAR(30)  NOT NULL UNIQUE,
    precio      NUMERIC(12,2) NOT NULL CHECK (precio >= 0),
    stock       INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),
    categoria   VARCHAR(20) NOT NULL CHECK (categoria IN ('ropa', 'tecnologia', 'hogar')),
    creado_en   TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT nombre_no_vacio CHECK (length(trim(nombre)) > 0)
);      
