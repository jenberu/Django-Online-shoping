from .models import Product,ProductRecommandation
from django.db.models import Q
class Recommender:
    def products_bought(self,products):
        product_ids=[p.id for p in products ]
        for product_id in product_ids:
            for with_id in product_ids:
                if product_id!=with_id:
                   recommender,created=ProductRecommandation.objects.get_or_create(product_id=product_id,
                                                                                   purchased_with_product_id=with_id,
                                                                                   purchased_with_times =1)
                  
                   if not created: 
                      recommender.purchased_with_times +=1
                      recommender.save()
    def get_purchased_products(self,products,max_result=5):
        product_ids=[p.id for p in products]
        purchased_with_products=ProductRecommandation.objects.filter(Q(product_id__in=product_ids)| Q( purchased_with_product_id__in=product_ids)).order_by('-purchased_with_times')[:max_result]
        
        if len(purchased_with_products)==1:
            suggestions_id=[purchased_with_products[0].purchased_with_product_id]
            if suggestions_id[0] in product_ids:
               suggestions_id=[purchased_with_products[0].product_id]      

        else:
            purchased_with_ids=[]
            for p_with in purchased_with_products:
                purchased_with_ids.append(p_with.purchased_with_product_id)
                purchased_with_ids.append(p_with.product_id)
            suggestions_id=[ids for ids in purchased_with_ids if ids not in product_ids]
        suggestions_products=list(Product.objects.filter(id__in=suggestions_id) )
        return suggestions_products   

            



            
                

