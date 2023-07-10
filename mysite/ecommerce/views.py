from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators import cache
from .models import User,Dealer,AmazonProductData,AsinCategory,Order,CreditCard,Temp1,Temp2,Temp3
from django.db.models import Count


@csrf_exempt
@cache.cache_page(30*15)
def main(request):
    if request.method == "GET":
        login_user = None
        if 'User_is_login' in request.session:
            login_user = User.objects.get(username=request.session['User_username'])

        TopSaled_products = AmazonProductData.objects.filter(sale_rank__in=[1, 2])
        Special_offer_products = AmazonProductData.objects.filter(price__gt=500)
        Recommendation_Products = AmazonProductData.objects.filter(sale_rank__in=[3, 4, 5])

        ###### create "shop_by_category" dict
        shop_by_category = {}
        first_category = AsinCategory.objects.all().values('category1').annotate(category1_count=Count('category1')).order_by('-category1_count')
        first_category_list = []
        for ele in first_category[:10]:
            first_category_list.append(ele['category1'])
            shop_by_category[ele['category1']] = None

        for k,v in shop_by_category.items():
            category2_list_by_single_category1= Temp2.objects.filter(category1=k).values("category2")
            temp_category2_to_category3_dict = {}
            for ele in category2_list_by_single_category1:
                category2_list_by_single_category1_and__single_category2 = Temp3.objects.filter(category1=k,category2=ele['category2'])
                temp_category2_to_category3_dict[ele['category2']] =category2_list_by_single_category1_and__single_category2
            shop_by_category[k] = temp_category2_to_category3_dict

        for k1,v1 in shop_by_category.items():
            for k2,v2 in v1.items():
                for ele in v2:
                    print(ele.category3)

        ###### end of create "shop_by_category" dict

        category_1 = Temp1.objects.all().order_by("category1_count")

        category_list1 = category_1[0:2]
        target_dict1 = {}
        for ele in category_list1:
            temp = Temp2.objects.filter(category1=ele.category1).values("category2")
            target_dict1[ele.category1] = temp

        category_list2 = category_1[2:4]
        target_dict2 = {}
        for ele in category_list2:
            temp = Temp2.objects.filter(category1=ele.category1).values("category2")
            target_dict2[ele.category1] = temp

        category_list3 = category_1[4:6]
        target_dict3 = {}
        for ele in category_list3:
            temp = Temp2.objects.filter(category1=ele.category1).values("category2")
            target_dict3[ele.category1] = temp

        category_list4 = category_1[6:8]
        target_dict4 = {}
        for ele in category_list4:
            temp = Temp2.objects.filter(category1=ele.category1).values("category2")
            target_dict4[ele.category1] = temp

        category_list5 = category_1[6:8]
        target_dict5 = {}
        for ele in category_list5:
            temp = Temp2.objects.filter(category1=ele.category1).values("category2")
            target_dict5[ele.category1] = temp




        return render(request, 'ecommerce/index.html',{"TopSaled_products":TopSaled_products[:20],
                                                       "login_user":login_user,
                                                       "Special_offer_products":Special_offer_products[:20],
                                                       "Recommendation_Products":Recommendation_Products[:20],
                                                       "TopSaled_products_one":TopSaled_products[0],
                                                       "TopSaled_products_rest":TopSaled_products[1:7],
                                                       "main_category_list":first_category[:10],
                                                       "target_dict1":target_dict1,
                                                       "target_dict2":target_dict2,
                                                       "target_dict3":target_dict3,
                                                       "target_dict4":target_dict4,
                                                       "target_dict5":target_dict5,
                                                       "shop_by_category":shop_by_category},
                                                        )



@csrf_exempt
def UserRegistration(request):
    if request.method == 'POST':
        username = request.POST['username']
        existed_user = User.objects.filter(username=username)
        if existed_user:
            return render(request, 'ecommerce/account-login.html')
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        phone_number = request.POST['phonenumber']
        #### check username is unique or not
        user = User(first_name=firstname,last_name=lastname,email=email,username=username,password=password,user_address=address,user_phone_number=phone_number)
        user.save(force_insert=False,force_update=False)
        return redirect("editProfile")
    else:
        return render(request, 'ecommerce/account-login.html')

@csrf_exempt
def DealerRegistration(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        brand = request.POST['brand']
        id_number = request.POST['id_number']
        temp_dealder = Dealer.objects.filter(email=email,id_number=id_number)
        if temp_dealder:
            return render(request, 'ecommerce/404.html')
        dealer = Dealer(first_name=firstname,last_name=lastname,email=email,username=username,password=password,brand=brand,id_number=id_number)
        dealer.save()
        return HttpResponse("Dealer Registration Successful")
    else:
        return render(request, 'ecommerce/404.html')

@csrf_exempt
def UserLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        temp_user = User.objects.filter(username=username,password=password)
        if temp_user:
            request.session['User_is_login'] = True
            request.session['User_username'] = username
            request.session['User_password'] = password
            return redirect('ShowUserinformation')
        else:
            return render(request, 'ecommerce/account-login.html',{"login_error_info":
                                                                       "Your login information is not correct"})
    else:
        return render(request, 'ecommerce/account-login.html')

@csrf_exempt
def DealerLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        id_number = request.POST['id_number']
        temp_dealer = Dealer.objects.filter(username=username, password=password, id_number=id_number)
        if temp_dealer:
            return HttpResponse("Dealer Login Successful ! ")
        else:
            return render(request, 'ecommerce/DealerLogin.html')
    else:
        return render(request, 'ecommerce/DealerLogin.html')

@csrf_exempt
def ShowUserinformation(request):
    if request.method == 'GET':##### show user info
        if 'User_username' not in request.session:
            return redirect('UserLogin')
        User_username = request.session['User_username']
        target_user = User.objects.get(username=User_username)
        orders = Order.objects.filter(username=User_username)
        return render(request, 'ecommerce/account-dashboard.html',{"target_user":target_user,"orders":orders})
    else:
        return HttpResponse(22233333)

@csrf_exempt
def editProfile(request):

    if request.method == 'GET':  ##### show user info
        if "User_is_login" not in request.session:
            return redirect('UserLogin')
        else:
            return render(request,'ecommerce/account-profile.html')
    else:
        User_is_login = request.session['User_is_login']
        if User_is_login:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            address = request.POST['address']
            phone_number = request.POST['phone_number']
            target_user = User.objects.get(username=request.session['User_username'])
            target_user.first_name = firstname
            target_user.last_name = lastname
            target_user.email = email
            target_user.user_address = address
            target_user.user_phone_number = phone_number
            target_user.save()

            return render(request, 'ecommerce/account-profile.html',{"success_info":"Your information changed successfully!"})
        else:
            return redirect('UserLogin')

@csrf_exempt
def UserLogOut(request):
    try:
        request.session.pop('User_is_login')
        request.session.pop('User_password')
        request.session.pop('User_username')
        return render(request,'ecommerce/account-login.html')
    except Exception as e:
        return render(request, 'ecommerce/account-login.html')

@csrf_exempt
def ProductInformation(request):
    if request.method == "GET":
        if request.GET['product_asin']:
            product = AmazonProductData.objects.get(asin=request.GET['product_asin'])

            also_bought_asins = product.also_bought
            also_viewed_asins = product.also_viewed
            bought_together_asins = product.bought_together
            buy_after_viewing_asins = product.buy_after_viewing

            also_bought_product_list = []
            also_viewed_product_list = []
            bought_together_product_list = []
            buy_after_viewing_product_list = []

            if also_bought_asins is None:
                pass
            else:
                for asin in also_bought_asins.split(","):
                    try:
                        temp_product = AmazonProductData.objects.get(asin=asin)
                        also_bought_product_list.append(temp_product)
                    except:
                        continue

            if also_viewed_asins is None:
                pass
            else:
                for asin in also_viewed_asins.split(","):
                    try:
                        temp_product = AmazonProductData.objects.get(asin=asin)
                        also_viewed_product_list.append(temp_product)
                    except:
                        continue


            if bought_together_asins is None:
                pass
            else:
                for asin in bought_together_asins.split(","):
                    try:
                        temp_product = AmazonProductData.objects.get(asin=asin)
                        bought_together_product_list.append(temp_product)
                    except:
                        continue

            if buy_after_viewing_asins is None:
                pass
            else:
                for asin in buy_after_viewing_asins.split(","):
                    try:
                        temp_product = AmazonProductData.objects.get(asin=asin)
                        buy_after_viewing_product_list.append(temp_product)
                    except:
                        continue
            return render(request,'ecommerce/product.html',{"product":product,
                                                            'also_bought_product_list':also_bought_product_list,
                                                            'also_viewed_product_list':also_viewed_product_list,
                                                            'bought_together_product_list':bought_together_product_list,
                                                            'buy_after_viewing_product_list':buy_after_viewing_product_list,})
        else:
            return HttpResponse("product_asin Error")
    else:
        return HttpResponse("Method Error")

@csrf_exempt
def AddProductToCart(request):
    if request.method == "POST":
        ### User did not login
        if "User_is_login" not in request.session:
            return redirect('UserLogin')
        ### User has logged
        else:
            user = User.objects.get(username=request.session['User_username'])
            asin = AmazonProductData.objects.get(asin=request.POST['asin_for_submit'])
            order = Order(username=user,quantity=request.POST['quantity'],asin=asin)
            order.paidorunpaid = False
            order.save()
            return redirect("getAllOrderByUsername")
    else:
        if "User_is_login" not in request.session:
            return redirect('UserLogin')
        else:
            return HttpResponse("main")

@csrf_exempt
def getAllOrderByUsername(request):
    if request.method == "GET":
        if "User_is_login" not in request.session:
            return redirect('UserLogin')
        else:
            username = request.session['User_username']
            Order_list = Order.objects.filter(username=username)
            Order_list_totals = 0
            for ele in Order_list:
                ele.total = ele.quantity*ele.asin.price
                Order_list_totals = Order_list_totals + ele.total
            return render(request,"ecommerce/cart.html",{"Order_list":Order_list,"Order_list_totals":Order_list_totals})
    else:
        return HttpResponse("getAllOrderByUsername POST")

@csrf_exempt
def CheckOut(request):
    if request.method == "GET":
        if "User_is_login" not in request.session:
            return redirect('UserLogin')
        else:
            username = request.session['User_username']
            Order_list = Order.objects.filter(username=username)
            Order_list_totals = 0
            for ele in Order_list:
                ele.total = ele.quantity * ele.asin.price
                Order_list_totals = Order_list_totals + ele.total
            return render(request,'ecommerce/checkout.html',{'Order_list_totals':Order_list_totals})
    else:

        return HttpResponse("Check Out Post")

@csrf_exempt
def PlaceOrder(request):

    if request.method == "POST":
        if "User_is_login" not in request.session:
            return redirect('UserLogin')
        else:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            credit_card = request.POST['Credit Card Number']
            sec_code = request.POST['Security Code']
            total_fees = float(request.POST['total_fees'])
            credit_card = CreditCard.objects.get(credit_card_id=credit_card,security_code = sec_code,firstname=firstname,lastname=lastname)
            if (credit_card.money > float(total_fees)):
                credit_card.money = credit_card.money - total_fees
                credit_card.save()
                username = request.session['User_username']
                Order_list = Order.objects.filter(username=username)
                for ele in Order_list:
                    ele.paidorunpaid = True
                    ele.save()
                return render(request,"ecommerce/PurchaseSuccessfull.html")
            else:
                return render(request,"ecommerce/PurchaseFailed.html")
    else:
        return redirect('CheckOut')

@csrf_exempt
def searchByCategory(request):
        target_category = request.POST.get("search")
        if target_category == None:
            target_category = request.GET.get("search")

        if "asin" in target_category:

            asin = target_category.split(":")[1]
            product = AmazonProductData.objects.get(asin=asin)
            also_bought_asins = product.also_bought
            also_viewed_asins = product.also_viewed
            bought_together_asins = product.bought_together
            buy_after_viewing_asins = product.buy_after_viewing

            also_bought_product_list = []
            also_viewed_product_list = []
            bought_together_product_list = []
            buy_after_viewing_product_list = []

            if also_bought_asins is None:
                pass
            else:
                for asin in also_bought_asins.split(","):
                    try:
                        temp_product = AmazonProductData.objects.get(asin=asin)
                        also_bought_product_list.append(temp_product)
                    except:
                        continue

            if also_viewed_asins is None:
                pass
            else:
                for asin in also_viewed_asins.split(","):
                    try:
                        temp_product = AmazonProductData.objects.get(asin=asin)
                        also_viewed_product_list.append(temp_product)
                    except:
                        continue

            if bought_together_asins is None:
                pass
            else:
                for asin in bought_together_asins.split(","):
                    try:
                        temp_product = AmazonProductData.objects.get(asin=asin)
                        bought_together_product_list.append(temp_product)
                    except:
                        continue

            if buy_after_viewing_asins is None:
                pass
            else:
                for asin in buy_after_viewing_asins.split(","):
                    try:
                        temp_product = AmazonProductData.objects.get(asin=asin)
                        buy_after_viewing_product_list.append(temp_product)
                    except:
                        continue
            return render(request, 'ecommerce/product.html', {"product": product,
                                                              'also_bought_product_list': also_bought_product_list,
                                                              'also_viewed_product_list': also_viewed_product_list,
                                                              'bought_together_product_list': bought_together_product_list,
                                                              'buy_after_viewing_product_list': buy_after_viewing_product_list, })
        if target_category!= "End_of_Category":
            products1 = AsinCategory.objects.filter(category1__contains=target_category).values("asin")
            products2 = AsinCategory.objects.filter(category2__contains=target_category).values("asin")
            products3 = AsinCategory.objects.filter(category3__contains=target_category).values("asin")
            if products1:
                products = products1
            elif products2:
                products = products2
            else:
                products = products3
        else:
                products = None
        target_products = None
        if products:
                target_products = AmazonProductData.objects.filter(asin__in=products)
        return render(request,"ecommerce/shop-list.html",{"target_products":target_products[:150]})
