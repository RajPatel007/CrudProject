from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import UserApis
from .serializers import UserApisSerializer
from .UserApi import UserApiForms


class UserApiView(APIView):

    def get(self, request):
        print(request.data)
        return Response("Query successsfully!")

    def createUser(request, id=0):
        if request.method == "GET":
            if id == 0:
                form = UserApiForms()
            else:
                user = UserApis.objects.get(pk=id)
                form = UserApiForms(instance=user)
            return render(request, 'blog_posts/post_form.html', {'form': form})
        else:
            if id == 0:
                form = UserApiForms(request.POST)
            else:
                user = UserApis.objects.get(pk=id)
                form = UserApiForms(request.POST, instance=user)
            if form.is_valid():
                form.save()
            return redirect('/list')

    def deleteUser(request, id):
        user = UserApis.objects.get(pk=id)
        user.delete()
        return redirect('/list')

    def listUser(request):
        context = {'user_list': UserApis.objects.all()}
        return render(request, 'blog_posts/post_list.html', context)

    def updateUser(request, pk):
        queryset = get_object_or_404(UserApis, pk=pk)
        serializer = UserApisSerializer(data=queryset)
        if serializer.is_valid():
            serializer.save()
            return redirect('listUser')
        return render(request, 'blog_posts/post_form.html', {'form': serializer})
