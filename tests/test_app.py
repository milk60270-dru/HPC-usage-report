"""
SpeedyPizza 單元測試
測試應用程式的主要路由與功能。
"""


class TestIndex:
    """首頁相關測試"""

    def test_index_returns_200(self, client):
        """首頁應回傳 HTTP 200"""
        response = client.get("/")
        assert response.status_code == 200

    def test_index_shows_menu(self, client):
        """首頁應顯示披薩菜單"""
        response = client.get("/")
        data = response.data.decode("utf-8")
        assert "瑪格麗特" in data
        assert "夏威夷" in data
        assert "辣味臘腸" in data

    def test_index_shows_prices(self, client):
        """首頁應顯示披薩價格"""
        response = client.get("/")
        data = response.data.decode("utf-8")
        assert "280" in data
        assert "300" in data


class TestOrder:
    """訂購功能相關測試"""

    def test_order_page_returns_200(self, client):
        """訂購頁面應回傳 HTTP 200"""
        response = client.get("/order")
        assert response.status_code == 200

    def test_order_page_shows_form(self, client):
        """訂購頁面應顯示表單"""
        response = client.get("/order")
        data = response.data.decode("utf-8")
        assert "customer_name" in data
        assert "pizza_id" in data

    def test_create_order(self, client):
        """提交訂單應重導至成功頁面"""
        response = client.post(
            "/order",
            data={
                "customer_name": "測試用戶",
                "pizza_id": "1",
                "quantity": "2",
            },
            follow_redirects=True,
        )
        assert response.status_code == 200
        data = response.data.decode("utf-8")
        assert "訂購成功" in data


class TestOrderStatus:
    """訂單查詢相關測試"""

    def test_order_status_page_returns_200(self, client):
        """查詢頁面應回傳 HTTP 200"""
        response = client.get("/order_status")
        assert response.status_code == 200

    def test_query_existing_order(self, client):
        """查詢存在的訂單應顯示訂單資訊"""
        response = client.get("/order_status?order_id=1")
        data = response.data.decode("utf-8")
        assert response.status_code == 200
        assert "王小明" in data

    def test_query_nonexistent_order(self, client):
        """查詢不存在的訂單應顯示錯誤訊息"""
        response = client.get("/order_status?order_id=999")
        data = response.data.decode("utf-8")
        assert "找不到" in data

    def test_order_status_without_id(self, client):
        """未輸入訂單編號時應正常顯示查詢頁面"""
        response = client.get("/order_status")
        assert response.status_code == 200


class TestOrderSuccess:
    """訂購成功頁面測試"""

    def test_success_page_returns_200(self, client):
        """成功頁面應回傳 HTTP 200"""
        response = client.get("/order_success")
        assert response.status_code == 200

    def test_success_page_content(self, client):
        """成功頁面應顯示成功訊息"""
        response = client.get("/order_success")
        data = response.data.decode("utf-8")
        assert "訂購成功" in data
