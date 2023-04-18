from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

# # Create your views here.
# @login_required
# def course_chat_room(request, course_id):
#     try:
# # retrieve course with given id joined by the current user
#         course = request.user.courses_joined.get(id=course_id)
#     except:
# # user is not a student of the course or course does not exist
#         return HttpResponseForbidden()
#     return render(request, 'chat/room.html', {'course': course})
def index(request):
    return render(request, 'index.html', {})

def room(request, room_name):
    return render(request, 'chatroom.html',{
        'room_name': room_name
    })