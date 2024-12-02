use stock_db;

-- ユーザー
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(512) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 支出
CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    item VARCHAR(16),
    category INT ,
    description VARCHAR(255),
    price INT,
    expense_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -- FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (category) REFERENCES common_expenses_category(id)
);

-- 支出カテゴリ
CREATE TABLE common_expenses_category(
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(16) NOT NULL
);

-- 収入
CREATE TABLE income (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(16) NOT NULL,
    item VARCHAR(16),
    category INT ,
    description VARCHAR(255),
    expense_date DATE NOT NULL,
    created_at TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (category) REFERENCES common_income_category(id)
);

-- 収入カテゴリ
CREATE TABLE common_income_category(
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(16) NOT NULL
);

-- 現預金
CREATE TABLE bank(
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT ,
    bank_name VARCHAR(32),
    balance INT, 
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- 個別株
CREATE TABLE stock(
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(8),
    name, VARCHAR(64),
    user_id INT, 
    acquisition_price INT, -- 取得単価
    quantity INT ,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- 配当金管理
CREATE TABLE yeild(
    id INT AUTO_INCREMENT PRIMARY KEY,
    stock_id INT,
    cumulative_dividend INT,
    FOREIGN KEY (stock_id) REFERENCES stock(id)
);

-- 投資信託
CREATE TABLE invest_trust(
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(32),
    found_name VARCHAR(64), 
    acquisition_price INT, -- 取得単価(基準評価額)
    now_price INT, -- 原罪の単価
    quantity INT , -- 保有口数
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO common_expenses_category(id,category_name) 
    VALUES(1,"食費");
INSERT INTO common_expenses_category(id,category_name) 
    VALUES(2,"交通費");
INSERT INTO common_expenses_category(id,category_name) 
    VALUES(3,"日用品");
INSERT INTO common_expenses_category(id,category_name) 
    VALUES(4,"家賃");
INSERT INTO common_expenses_category(id,category_name) 
    VALUES(5,"教育");
INSERT INTO common_expenses_category(id,category_name) 
    VALUES(6,"趣味");
INSERT INTO common_expenses_category(id,category_name) 
    VALUES(7,"通信費");
INSERT INTO common_expenses_category(id,category_name) 
    VALUES(8,"その他");

INSERT INTO common_income_category(category_name) VALUES("給料");
INSERT INTO common_income_category(category_name) VALUES("立替");
INSERT INTO common_income_category(category_name) VALUES("資産");
INSERT INTO common_income_category(category_name) VALUES("その他");