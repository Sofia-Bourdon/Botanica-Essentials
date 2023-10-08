

def bag_contents(request):
    
    bag_items = []
    total = 0
    product_count = 0
    delivery = 0


    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
    }

    return context
