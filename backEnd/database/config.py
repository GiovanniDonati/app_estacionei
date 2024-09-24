import sqlite3

conn = sqlite3.connect('backend/database/database.db')

cursor = conn.cursor()
def create_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS `veiculo` (
    `id_veiculo` INTEGER PRIMARY KEY NOT NULL UNIQUE,
    `placa` TEXT NOT NULL,
    `modelo` TEXT NOT NULL,
    `dono` TEXT NOT NULL,
    `tipo_veiculo` TEXT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS `estacionamento` (
    `id_vaga` INTEGER PRIMARY KEY NOT NULL UNIQUE,
    `vaga` TEXT,
    `tipo_vaga` TEXT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS `historico` (
    `id_historico` INTEGER PRIMARY KEY NOT NULL UNIQUE,
    `data_entrada` INTEGER NOT NULL,
    `data_saida` REAL NOT NULL,
    `veiculo_id_veiculo` INTEGER NOT NULL,
    `est_id_vaga` INTEGER NOT NULL,
    `valor_a_receber` REAL,
    FOREIGN KEY(`veiculo_id_veiculo`) REFERENCES `veiculo`(`id_veiculo`),
    FOREIGN KEY(`est_id_vaga`) REFERENCES `estacionamento`(`id_vaga`)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS `cliente` (
    `id_cliente` INTEGER PRIMARY KEY NOT NULL UNIQUE,
    `nome` TEXT NOT NULL,
    `cpf` TEXT NOT NULL UNIQUE,
    `telefone` TEXT NOT NULL
    );
    ''')
    conn.commit()

create_table()