# # to detect changes to shapes and trigger actions
# signals.py

# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer
# from .models import Shape
# from main_user.serializers import ShapeSerializer

# channel_layer = get_channel_layer()

# @receiver(post_save, sender=Shape)
# def shape_created(sender, instance, created, **kwargs):
#     serializer = ShapeSerializer(instance)
#     if created:
#         async_to_sync(channel_layer.group_send)(
#             "public_room",  # Broadcast to all clients connected to "shape_user" group
#             {
#                 "type": "send_created_shape",
#                 "shape_create": serializer.data,
#             },
#         )
#     else: #just update
#         async_to_sync(channel_layer.group_send)(
#             "public_room",
#             {
#                 "type": "send_updated_shape",
#                 "shape_update": serializer.data,
#             },
#         )
        
# @receiver(post_delete, sender=Shape)
# def shape_deleted(sender, instance, **kwargs):
#     serializer = ShapeSerializer(instance)
#     async_to_sync(channel_layer.group_send)(
#         "public_room",
#         {
#             "type": "send_deleted_shape",
#             "shape_delete": serializer.data,
#         },
#     )