from django.shortcuts import render
from datetime import date

posts = [
  {
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpeg",
    "author": 'Evgeniy',
    "date": date(2021, 3, 15),
    "title:": 'Mountain Hakking',
    "exccerpt": "There's nothing like the views you get when hiking in the mountains!",
    "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cupiditate dicta eaque ex libero magnam molestiae quaerat quis quod reiciendis rem."
  },
  {
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpeg",
    "author": 'Evgeniy',
    "date": date(2021, 3, 15),
    "title:": 'Mountain Hakking',
    "exccerpt": "There's nothing like the views you get when hiking in the mountains!",
    "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cupiditate dicta eaque ex libero magnam molestiae quaerat quis quod reiciendis rem."
  },
  {
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpeg",
    "author": 'Evgeniy',
    "date": date(2021, 3, 15),
    "title:": 'Mountain Hakking',
    "exccerpt": "There's nothing like the views you get when hiking in the mountains!",
    "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cupiditate dicta eaque ex libero magnam molestiae quaerat quis quod reiciendis rem."
  }
]

# Create your views here.


def starting_page(request):
  return render(request, "blog/index.html")


def posts(request):
  return render(request, "blog/all-posts.html")


def post_detail(request, slug):
  return render(request, "blog/post-detail.html")