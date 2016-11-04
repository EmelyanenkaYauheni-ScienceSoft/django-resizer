1. git clone ... channels_image_resizing
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py createsuperuser
5. python manage.py runserver
6. celery -A channels_image_resizing worker -l info
7. http://localhost:8000 -> api root
8. http://localhost:8000/statistics -> table with info

You can add image through DRF API GUI (7)
When you added image you can see on statictics/ page that new item has been inserted.
id  created_at  resized_at
1   time        Wait...

When resizing is done you will see
id  created_at  resized_at
1   time        time

Websocket send messages on create and update actions
{
    "payload": {
        "action": "create",
        "data": {
            "resized_at": null,
            "original_image": "original_images/moscow-russia-kremlin-city-3654_f1eWh2W.jpg",
            "resized_image": "",
            "created_at": "2016-11-04T10:17:06.403Z"
        },
        "model": "resizers.image",
        "pk": 67
    },
    "stream": "image"
}

{
    "payload": {
        "action": "update",
        "data": {
            "original_image": "original_images/moscow-russia-kremlin-city-3654_f1eWh2W.jpg",
            "resized_at": "2016-11-04T13:17:09.494",
            "created_at": "2016-11-04T10:17:06.403Z",
            "resized_image": "resized_images/moscow-russia-kremlin-city-3654_f1eWh2W.jpg"
        },
        "pk": 67,
        "model": "resizers.image"
    },
    "stream": "image"
}
