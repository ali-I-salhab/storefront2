from django.urls import path,include
from . import views
from rest_framework_nested import routers
router=routers.DefaultRouter()

# -------------------------------
router.register('products',viewset=views.Productviewset,basename='products')
router.register('customers',viewset=views.CustomerViewSet,basename='customers')

router.register('carts',viewset=views.Cartviewset,basename='carts')
# -------------
cartitems=routers.NestedDefaultRouter(router,'carts',lookup='cart')
cartitems.register('items',viewset=views.Itemsviewset,basename='iteffms')
# ------------------------,vi--
reviewrouter=routers.NestedDefaultRouter(router,'products',lookup='review')
reviewrouter.register('reviews',viewset=views.Reviewviewset,basename="ali-salhab")
# URLConf
# urlpatterns = [
#     path("",include(router.urls)),
#         path("",include(reviewrouter.urls))
#     # path('products/', views.ProductList.as_view()),
#     # path('products/<int:id>', views.ProductDetails.as_view()),
#     #   path('collections/', views.CollectionList.as_view()),
#     #     path('collections/<int:pk>', views.collection_details,name="collection-details"),

  
# ]
urlpatterns=router.urls+reviewrouter.urls+cartitems.urls
