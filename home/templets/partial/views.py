from django.shortcuts import render

def home(request):
    return render(request, "home.html", {
            "breadcrumbs": [
                        {"title": "Home", "url": "/"},
                                ]
                                    })

                                    def menu(request):
                                        return render(request, "menu.html", {
                                                "breadcrumbs": [
                                                            {"title": "Home", "url": "/"},
                                                                        {"title": "Menu", "url": "/menu/"},
                                                                                ]
                                                                                    })

                                                                                    def order_confirmation(request, order_id):
                                                                                        return render(request, "order_confirmation.html", {
                                                                                                "breadcrumbs": [
                                                                                                            {"title": "Home", "url": "/"},
                                                                                                                        {"title": "Menu", "url": "/menu/"},
                                                                                                                                    {"title": "Order Confirmation", "url": f"/order/{order_id}/confirmation/"},
                                                                                                                                            ]
                                                                                                                                                })
                                                                                                                                                