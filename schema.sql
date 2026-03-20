-- SpeedyPizza 資料庫結構定義
-- 披薩菜單

CREATE TABLE IF NOT EXISTS pizzas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
);

-- 訂單紀錄
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    pizza_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1,
    status TEXT DEFAULT 'preparing',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (pizza_id) REFERENCES pizzas(id)
);

-- 預填範例資料：披薩菜單
INSERT INTO pizzas (name, description, price) VALUES
    ('瑪格麗特', '經典番茄醬、莫札瑞拉起司、新鮮羅勒', 280),
    ('夏威夷', '火腿、鳳梨、莫札瑞拉起司', 300),
    ('辣味臘腸', '義式辣腸、莫札瑞拉起司、辣椒片', 320),
    ('海鮮總匯', '蝦仁、花枝、蛤蜊、蒜味白醬', 380),
    ('田園蔬菜', '甜椒、蘑菇、洋蔥、黑橄欖、番茄醬', 260);

-- 預填範例資料：訂單紀錄
INSERT INTO orders (customer_name, pizza_id, quantity, status) VALUES
    ('王小明', 1, 2, 'delivered'),
    ('李大華', 3, 1, 'preparing'),
    ('張美玲', 2, 3, 'delivering'),
    ('陳志偉', 4, 1, 'preparing'),
    ('林淑芬', 5, 2, 'delivered');
