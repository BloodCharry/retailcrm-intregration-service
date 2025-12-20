class DummyCRM:
    async def list_customers(self, filters, page, limit):
        return {"ok": True, "filters": filters}

    async def create_customer(self, data):
        return {"ok": True, "customer": data}

    async def create_payment(self, data):
        return {"ok": True, "payment": data}

    async def create_order(self, data):
        return {"ok": True, "order": data}
