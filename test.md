
C:\Users\Dev\OneDrive\Desktop\box_selector\box_selector>python manage.py test     
Found 7 test(s).
System check identified no issues (0 silenced).
.......
----------------------------------------------------------------------
Ran 7 tests in 0.010s

OK

## Code Logic
<!-- class BoxSelectionTests(SimpleTestCase):
    def setUp(self):
        self.client = APIClient()

    def test_single_product_fits(self):
        payload = {"items": [
            {"name": "Mug", "length": 8, "width": 8, "height": 6, "weight": 0.4, "quantity": 1}
        ]}
        response = self.client.post(URL, payload, format="json")
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertIsNotNone(body["selected_box"])
        self.assertEqual(body["selected_box"]["name"], "XS")

    def test_multiple_products_fit(self):
        payload = {"items": [
            {"name": "Mug", "length": 10, "width": 10, "height": 12, "weight": 0.4, "quantity": 2},
            {"name": "Book", "length": 20, "width": 15, "height": 3, "weight": 0.5, "quantity": 3},
        ]}
        response = self.client.post(URL, payload, format="json")
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertIsNotNone(body["selected_box"])
        self.assertAlmostEqual(body["order_summary"]["total_weight"], 2.3)

    def test_exact_weight_limit(self):
        # XS box max_weight is exactly 1.0kg - an order weighing exactly
        # 1.0kg should still qualify (boundary is inclusive).
        payload = {"items": [
            {"name": "Item", "length": 5, "width": 5, "height": 5, "weight": 1.0, "quantity": 1}
        ]}
        response = self.client.post(URL, payload, format="json")
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertIsNotNone(body["selected_box"])
        self.assertEqual(body["selected_box"]["name"], "XS")

    def test_weight_exceeds_box_capacity(self):
        payload = {"items": [
            {"name": "Anvil", "length": 10, "width": 10, "height": 10, "weight": 9999, "quantity": 1}
        ]}
        response = self.client.post(URL, payload, format="json")
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertIsNone(body["selected_box"])
        self.assertIn("weight", body["reason"])

    def test_dimensions_exceed_all_boxes(self):
        payload = {"items": [
            {"name": "Surfboard", "length": 250, "width": 10, "height": 5, "weight": 2, "quantity": 1}
        ]}
        response = self.client.post(URL, payload, format="json")
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertIsNone(body["selected_box"])
        self.assertIn("Surfboard", body["reason"])

    def test_empty_order(self):
        response = self.client.post(URL, {"items": []}, format="json")
        self.assertEqual(response.status_code, 400)

    def test_invalid_request(self):
        # Missing required fields and a negative dimension.
        payload = {"items": [{"name": "Bad", "length": -5, "width": 10}]}
        response = self.client.post(URL, payload, format="json")
        self.assertEqual(response.status_code, 400) -->
