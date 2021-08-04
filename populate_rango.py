import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page, Comment
from django.contrib.auth.models import User, Group
from rolepermissions.roles import AbstractUserRole
from rolepermissions.roles import assign_role

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    Rolex1 = [
        {'title': 'Cosmograph Daytona',
        'url':'https://www.rolex.com/watches/cosmograph-daytona.html', 'views': 1500}]
    Rolex2 = [
        {'title':'Submariner',
        'url':'https://www.rolex.com/watches/submariner.html', 'views': 2000}]
    Rolex3 = [
        {'title':'GMT Master',
        'url':'https://www.rolex.com/watches/gmt-master-ii.html', 'views': 1800} ]

    Patek1 = [
        {'title':'Nautilus',
        'url':'https://www.patek.com/en/collection/nautilus', 'views': 5000}]
    Patek2 = [
        {'title':'Aquanaut',
        'url':'https://www.patek.com/en/collection/aquanaut', 'views': 900} ]   
      
    AD = [
        {'title':'Royal Oak',
        'url':'https://www.audemarspiguet.com/com/en/collections/royal-oak.html', 'views': 1000}
         ]

    Hublot1 = [
        {'title':'Big Bang',
        'url':'https://www.hublot.com/en-gb/watches/big-bang', 'views': 100}]
    Hublot2 = [
        {'title':'Classic Fusion',
        'url':'https://www.hublot.com/en-gb/watches/classic-fusion', 'views': 150} ]
        
    
    Samsung1 = [
        {'title':'Galaxy Watch 3',
        'url':'https://www.samsung.com/uk/watches/galaxy-watch/galaxy-watch3-45mm-mystic-black-sm-r840nzkaeua/', 'views': 250}]
    Samsung2 = [
        {'title':'Galaxy Fit 2',
        'url':'https://www.samsung.com/uk/watches/galaxy-fit/galaxy-fit2-scarlet-sm-r220nzraeua/', 'views': 150} ]
        
    
    Apple = [
        {'title':'Apple Watch 6',
        'url':'https://www.apple.com/uk/shop/buy-watch/apple-watch', 'views': 1500} ]
    
    Omega1 = [
        {'title':'Speedmaster',
        'url':'https://www.omegawatches.com/watches/speedmaster', 'views': 1000}]

    Omega2 = [
        {'title':'Seamaster',
        'url':'https://www.omegawatches.com/watches/seamaster', 'views': 550}]
    
    RM11 = [
        {'title':'RM 11',
        'url':'https://www.richardmille.com/collections/rm-11-03-automatic-chronograph', 'views': 500}]
    

    cats = {'Rolex Cosmograph Daytona': {'vendor_page': Rolex1, 'type':'luxury', 'description':'Introduced in 1963, the Cosmograph Daytona was designed to meet the demands of professional racing drivers. It is an icon forever joined in name and function to the high-performance world of motorsport. More than 50 years after its creation, the Cosmograph Daytona remains in a class of its own among sports chronographs and continues to transcend time.', 'views': 1500, 'likes': 550, 'picture':'product_images/a.jpg'},
        'Rolex Submariner': {'vendor_page': Rolex2, 'type':'luxury', 'description':'A benchmark among divers’ watches, the Oyster Perpetual Submariner embodies the historic link between Rolex and the underwater world. It features a unidirectional rotatable bezel and solid-link Oyster bracelet. The latest generation Submariner and Submariner Date remain faithful to the original model launched in 1953. In watchmaking, the Submariner represented a historic turning point; it set the standard for divers’ watches.', 'views': 2000, 'likes': 100, 'picture':'product_images/b.jpg'},
        'Rolex GMT Master': {'vendor_page': Rolex3, 'type':'luxury', 'description':'Designed to show the time in two different time zones simultaneously, the GMT-Master, launched in 1955, was originally developed as a navigation instrument for professionals crisscrossing the globe. Heir to the original model, the Oyster Perpetual GMT-Master II was unveiled in 1982, with a new movement ensuring ease of use. Its combination of peerless functionality, robustness and instantly recognizable aesthetics has attracted a wider audience of world travellers.', 'views': 1800, 'likes': 100, 'picture':'product_images/c.jpg'},
        'Patek Phillipe Nautilus': {'vendor_page': Patek1, 'type':'luxury', 'description':'With the rounded octagonal shape of its bezel, the ingenious porthole construction of its case, and its horizontally embossed dial, the Nautilus has epitomized the elegant sports watch since 1976. Forty years later, it comprises a splendid collection of models for men and women.', 'views': 5000, 'likes': 550, 'picture':'product_images/d.jpg'},
        'Patek Phillipe Aquanaut': {'vendor_page': Patek2, 'type':'luxury', 'description':'Designed to be a true ocean-going watch, the Aquanaut boasts a depth rating of 120m thanks to a screw-down crown. This was the first time any watch with a sapphire case back had achieved that level of water resistance. To say the Aquanaut 5065A was immediately popular would be an understatement.', 'views': 900, 'likes': 200, 'picture':'product_images/e.jpg'},
        'Audemar Piguet Royal Oak': {'vendor_page': AD, 'type':'luxury', 'description':'Created by Mr Genta, the watch that would start the luxury sports watch revolution, the Aquanaut has stood the test of time and remains to be one of the most desirable watches in the world.', 'views': 1000, 'likes': 180, 'picture':'product_images/f.jpg'},
        'Hublot Big Bang': {'vendor_page': Hublot1, 'type':'luxury', 'description':'The highly controversial companies signature timepiece. This piece has seen many ups and downs and is still going strong with a strong fanbase.', 'views': 100, 'likes': 1, 'picture':'product_images/g.jpg'},
        'Hublot Classic Fusion': {'vendor_page': Hublot2, 'type':'luxury', 'description':'Considered to be one of the ugliest watches by true watch connoisseurs, this watch is sure to turn heads regardless of the reason. This watch has not been doing great in the market but with Hublot, expect the unexpected.', 'views': 150, 'likes': 2, 'picture':'product_images/h.jpg'},
        'Samsung Galaxy Watch 3': {'vendor_page': Samsung1, 'type':'smart', 'description':'The watch that watches out for you. Galaxy Watch3 combines smartphone-level productivity and leading health technology in one premium and classic device. Our most advanced Galaxy watch yet, Galaxy Watch3 helps you effortlessly manage your life and health — putting your well-being in your hands.', 'views': 250, 'likes': 4, 'picture':'product_images/i.jpg'},
        'Samsung Galaxy Fit 2': {'vendor_page': Samsung2, 'type':'smart', 'description':'The Samsung Galaxy Fit 2 feels like a more polished effort than the last Fit and is definitely one of the nicest-looking cheap fitness trackers you can put on your wrist right now. It largely delivers on those tracking basics too but comes unstuck when you turn to it for monitoring heart rate and tracking exercise.', 'views': 150, 'likes': 5, 'picture':'product_images/j.jpg'},
        'Apple Watch 6': {'vendor_page': Apple, 'type':'smart', 'description':'The true pioneers of the smart watch movement, Apple has been at the forefront of its game since it introduced the watch series. All these years later, it is still the best selling watch in the world.', 'views': 1500, 'likes': 160, 'picture':'product_images/k.jpg'},
        'Omega Speedmaster': {'vendor_page': Omega1, 'type':'luxury', 'description':'The first watch on the moon. Enough said. This watch is a Must-have collection in every collector’s home, as it brings class along with a big piece of history inside it.', 'views': 1000, 'likes': 165, 'picture':'product_images/l.jpg'},
        'Omega Seamaster': {'vendor_page': Omega2, 'type':'luxury', 'description':'The Seamaster is the watch of James Bond. Exemplifying class and simplicity, it is a highly recommended timepiece for everyone to consider.', 'views': 550, 'likes': 50, 'picture':'product_images/m.jpg'},
        'Richard Mille': {'vendor_page': RM11, 'type':'luxury', 'description':'The half a million-pound watch, may not live up to its hype, but it sure does turn head around. With its enormous price tag, if you own one, people will know who you are.', 'views': 500, 'likes': 3, 'picture':'product_images/n.jpg'}}

    users = [
        {'name':'editor',
        'password':'editor1234', 'email': 'editor@gmail.com', 'role':'editor'},
        {'name':'peter',
        'password':'peter1234', 'email': 'peter@gmail.com', 'role':''},        
        {'name':'david',
        'password':'david1234', 'email': 'david@gmail.com', 'role':''},       
        ]

    user_comments = {
        'editor': {
        '1' : {'content': 'Hey, wonderful watch.', 'rating':3},
        '2' : {'content': 'I hate it very much !', 'rating':4}},
        'peter':{
        '1' : {'content': 'Awsome watch i ever see in the world.', 'rating':3},
        '2' : {'content': 'Oh no wonderful pretty smart !', 'rating':4},
        '3' : {'content': 'hurra hurra come on !', 'rating':5}},
        'david' : {
        '1' : {'content': 'Oh yes, buy buy buy =)', 'rating':3},
        '2' : {'content': 'Oh no I do not like it =(', 'rating':1},
        '3' : {'content': 'Bargain but not good at all.', 'rating':2}}
    }

    # If you want to add more categories or pages,
    # add them to the dictionaries above.
    # Please be mindful that there are two categories of watches - luxury and smart

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    for cat, cat_data in cats.items():
        c = add_cat(cat,cat_data['views'],cat_data['likes'],cat_data['description'],cat_data['picture'],cat_data['type'],cat_data['vendor_page'][0]['url'])
        for p in cat_data['vendor_page']:
            add_page(c, p['title'], p['url'], p['views'])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

    for u in users:
        new_u = add_user(name=u['name'], email=u['email'], password=u['password'], role=u['role'])

    for user, comments in user_comments.items():
        for cat, c in comments.items():
            add_comment(c['content'],c['rating'],int(cat), user)

    update_recommend_buy_index()

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name,views,likes,description,picture,type,url):
    c = Category.objects.get_or_create(name=name,views=views,likes=likes)[0]
    c.slug = name.lower().replace(' ','-')
    c.description = description
    c.picture = picture
    c.type = type
    c.url = url
    c.save()
    return c

def add_user(name, email, password, role):
    u = User.objects.create_user(name, email, password)
    if len(role) > 0:
        assign_role(u, 'editor')
    u.save()
    return u

def add_comment(content, rating, category_id, user_name):
    u = User.objects.get(username=user_name)
    c = Comment.objects.get_or_create(content=content,rating=rating,category_id=category_id,user_id=u.id)[0]
    c.content = content
    c.rating = rating
    c.category_id = category_id
    c.user_id = u.id
    c.save()
    return c

def update_recommend_buy_index():
    categories = Category.objects.all()

    for c in categories:
        rating = 0
        comments= Comment.objects.filter(category=c)
        for comment in comments:
            rating = rating + comment.rating 
        c.recommend_buy = c.likes + rating
        c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()