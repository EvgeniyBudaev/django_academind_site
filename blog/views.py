from django.shortcuts import render
from datetime import date

all_posts = [
  {
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpeg",
    "author": 'Evgeniy',
    "date": date(2021, 3, 15),
    "title:": 'Mountain Hiking',
    "excerpt": "There's nothing like the views you get when hiking in the mountains!",
    "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cupiditate dicta eaque ex libero magnam molestiae quaerat quis quod reiciendis rem."
  },
  {
    "slug": "three",
    "image": "three.jpeg",
    "author": 'Evgeniy',
    "date": date(2021, 3, 15),
    "title:": 'Дерево',
    "excerpt": "Ваш шедевр готов!",
    "content": "Значимость этих проблем настолько очевидна, что новая модель организационной деятельности играет важную роль в формировании модели развития. Не следует, однако забывать, что укрепление и развитие структуры играет важную роль в формировании существенных финансовых и административных условий. Значимость этих проблем настолько очевидна, что консультация с широким активом обеспечивает широкому кругу (специалистов) участие в формировании систем массового участия."
  },
  {
    "slug": "iphone",
    "image": "cosmos.jpeg",
    "author": 'Evgeniy',
    "date": date(2021, 3, 15),
    "title:": 'Iphone',
    "excerpt": "Что-то новенькое!",
    "content": "Равным образом укрепление и развитие структуры позволяет выполнять важные задания по разработке системы"
  }
]

def get_date(post):
  return post['date']

# Create your views here.


def starting_page(request):
  sorted_posts = sorted(all_posts, key=get_date)
  latest_posts = sorted_posts[-3:]
  return render(request, "blog/index.html", {
    "posts": latest_posts
  })


def posts(request):
  return render(request, "blog/all-posts.html", {
    "all_posts": all_posts
  })


def post_detail(request, slug):
  identified_post = next(post for post in all_posts if post['slug'] == slug)
  return render(request, "blog/post-detail.html",{
    "post": identified_post
  })