from channels import Group


def connect_blog(message):
    Group("binding.values").add(message.reply_channel)


def disconnect_blog(message):
    Group("binding.values").discard(message.reply_channel)
