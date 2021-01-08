






### Basic Authentication 
# MUST REQUIRE HTTPS IN PRODUCTION

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import User, Cluster
from EOH.models import Node, NodeToken

from django.http import JsonResponse

class InitNode(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }

        print(request.data)
        node = request.data


        for cluster in User.objects.get(pk=request.user.id).clusters.all():
            print(type(cluster.name), type(node['cluster']))
            if cluster.name == node['cluster']:
                cluster_obj = Cluster.objects.get(pk=cluster.id)
                new_node = Node(
                    name=node['name'], 
                    ip_address=node['ip_address'], 
                    cluster=cluster_obj
                )

                #new_node.save()

                token, created = NodeToken.objects.get_or_create(node=new_node)

                return JsonResponse({"token": token.key})

        cluster_name = node['cluster']
        return JsonResponse({'NameError': f'cluster: {cluster_name} does not exist for user, {request.user}'})