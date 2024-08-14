USE estudos
--Criação das tabelas
CREATE TABLE vendedores (
	table_id		INT IDENTITY(1,1),
	id_vendedor		VARCHAR(5) PRIMARY KEY,
	nome_vendedor	VARCHAR(20) NOT NULL,
	nivel_cargo		VARCHAR(50)
)

INSERT INTO vendedores (id_vendedor,nome_vendedor,nivel_cargo)
VALUES 
('vv001','Mauro Rodrigues','pleno'),
('vv002','Lídia Vasques','junior'),
('vv003','Romero Brito','pleno'),
('vv004','Ícaro José','senior')


CREATE TABLE clientes (
	table_id		INT IDENTITY(1,1),
	id_cliente		VARCHAR(5) PRIMARY KEY,
	nome_cliente	VARCHAR(20) NOT NULL,
	idade			TINYINT NOT NULL,
	UF				CHAR(2),
	cidade			VARCHAR(50)
)

INSERT INTO clientes (id_cliente,nome_cliente,idade,UF,cidade)
VALUES 
('cl001','Juliana Tavares',32,'SP','São Paulo'),
('cl002','Mariana Oliveira',25,'SP','Jundiaí'),
('cl003','Mario Silva',52,'SP','São Carlos'),
('cl004','José Costa',72,'SP','Jundiaí'),
('cl005','Nadia Silva',18,'SP','São Paulo'),
('cl006','Igor Onofre',92,'SP','Jundiaí'),
('cl007','Dani Florzinha',34,'SP','Jundiaí'),
('cl008','Pedro Alvares',35,'SP','São Paulo'),
('cl009','Mariane Freitas',45,'SP','São Paulo')

CREATE TABLE produtos (

	table_id		INT IDENTITY(1,1),
	id_produto		VARCHAR(5) PRIMARY KEY,
	categoria		VARCHAR(20) NOT NULL,
	nome_produto	VARCHAR(20) NOT NULL,
	fornecedor		VARCHAR(20) NOT NULL,
	custo			DECIMAL(6,2) NOT NULL,
	margem_lucro	DECIMAL(6,2) NOT NULL,
	data_cadastro	DATETIME NOT NULL,
	expira_em		DATETIME NULL
	
)

INSERT INTO produtos (id_produto,categoria,nome_produto,fornecedor,custo,margem_lucro,data_cadastro)
VALUES 
('pr001','vestuario','camiseta básica','fornecedor alpha',23,1.6,'2024-01-01'),
('pr002','vestuario','camiseta básica','fornecedor beta',25,1.7,'2024-01-01'),
('pr003','vestuario','camiseta básica','fornecedor gama',30,1.5,'2024-01-01'),
('pr004','vestuario','bermuda jeans','fornecedor alpha',35,1.8,'2024-01-01'),
('pr005','vestuario','calça jeans','fornecedor alpha',35,1.9,'2024-01-01'),
('pr006','vestuario','jaqueta','fornecedor alpha',100,2,'2024-01-01'),
('pr007','acessorios','boné','fornecedor alpha',12,2.6,'2024-01-01'),
('pr008','acessorios','bucket','fornecedor alpha',30,2.6,'2024-01-01'),
('pr009','acessorios','relogio','fornecedor alpha',50,1.7,'2024-01-01'),
('pr010','acessorios','brinco','fornecedor alpha',30,2.6,'2024-01-01'),
('pr011','acessorios','bracelete','fornecedor alpha',50,1.7,'2024-01-01'),
('pr012','acessorios','faixa','fornecedor alpha',30,2.6,'2024-01-01'),
('pr013','acessorios','touca','fornecedor alpha',50,1.7,'2024-01-01')


CREATE TABLE vendas (

	table_id		INT IDENTITY(1,1),
	id_venda		VARCHAR(5) PRIMARY KEY,
	id_produto		VARCHAR(5) FOREIGN KEY REFERENCES produtos(id_produto)  NOT NULL,
	id_cliente		VARCHAR(5) FOREIGN KEY REFERENCES clientes(id_cliente)  NOT NULL,
	quantidade		INT NOT NULL,
	preco			DECIMAL(6,2) NOT NULL DEFAULT 0.00,
	valor			DECIMAL(6,2) NOT NULL DEFAULT 0.00,
	data_venda		DATETIME NOT NULL,
	id_vendedor		VARCHAR(5) FOREIGN KEY REFERENCES vendedores(id_vendedor)  NOT NULL,
)

INSERT INTO vendas (id_venda,id_produto,id_cliente,quantidade,data_venda,id_vendedor)
VALUES
('vn001','pr001','cl001',2,'2024-05-01 09:32:00','vv001'),
('vn002','pr002','cl002',2,'2024-05-01 12:32:00','vv002'),
('vn003','pr003','cl003',2,'2024-05-01 13:12:00','vv001'),
('vn004','pr007','cl007',2,'2024-05-01 09:02:00','vv001'),
('vn005','pr005','cl005',2,'2024-05-01 10:30:00','vv002'),
('vn006','pr005','cl006',2,'2024-05-01 17:42:00','vv002'),
('vn007','pr002','cl002',2,'2024-05-01 08:42:00','vv001'),
('vn008','pr001','cl001',2,'2024-05-01 16:32:00','vv002'),
('vn009','pr001','cl005',2,'2024-05-01 16:55:00','vv003'),
('vn010','pr003','cl003',2,'2024-05-01 16:21:00','vv004'),
('vn011','pr007','cl004',2,'2024-05-01 15:20:00','vv004'),
('vn012','pr008','cl001',2,'2024-05-01 09:32:00','vv003'),
('vn013','pr009','cl002',2,'2024-05-01 12:32:00','vv003'),
('vn014','pr009','cl003',2,'2024-05-01 13:12:00','vv001'),
('vn015','pr007','cl007',2,'2024-05-01 09:02:00','vv003'),
('vn016','pr010','cl005',2,'2024-05-01 10:30:00','vv003'),
('vn017','pr011','cl006',2,'2024-05-01 17:42:00','vv004'),
('vn018','pr012','cl002',2,'2024-05-01 08:42:00','vv002'),
('vn019','pr013','cl001',2,'2024-05-01 16:32:00','vv002'),
('vn020','pr012','cl005',2,'2024-05-01 16:55:00','vv002'),
('vn021','pr012','cl003',2,'2024-05-01 16:21:00','vv001'),
('vn022','pr011','cl004',2,'2024-05-01 15:20:00','vv004')

--Aqui atualiza-se a coluna preço e valor, considerando a margem_lucro de cada produto

UPDATE vendas
SET valor = (produtos.custo * quantidade * produtos.margem_lucro)
FROM vendas
INNER JOIN produtos
ON vendas.id_produto = produtos.id_produto

UPDATE vendas
SET preco = (produtos.custo * produtos.margem_lucro)
FROM vendas
INNER JOIN produtos
ON vendas.id_produto = produtos.id_produto