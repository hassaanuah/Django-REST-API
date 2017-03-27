from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from mysite.models import User_Package, Customer_Discretion, Emergency, GOP, Package, Subscription, UCOP, ID_Table, CES_Negotiation_Policy, CES_Policy_Params, CES_Reputation_Table, Control_Policy_Params, HOST_ID, HOST_Negotiation_Policy, Host_Reputation_Table, Payload_Policies, RLOC_Policies

from mysite.serializers import UserPackageSerializer, Customer_DiscretionSerializer, EmergencySerializer, GOPSerializer, PackageSerializer, SubscriptionSerializer, UCOPSerializer, ID_TableSerializer, CES_Negotiation_PolicySerializer, CES_Policy_ParamsSerializer, CES_Reputation_TableSerializer, Control_Policy_ParamsSerializer, HOST_IDSerializer, HOST_Negotiation_PolicySerializer, Host_Reputation_TableSerializer, Payload_PoliciesSerializer, RLOC_PoliciesSerializer



class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def firewall1(request):
    if request.method == 'GET':
        snippets = User_Package.objects.all()
        snippets1 = Customer_Discretion.objects.all()
        serializer = UserPackageSerializer(snippets, many=True)
        serializer1 = Customer_DiscretionSerializer(snippets1, many=True)
        #return JSONResponse((*serializer, sep='\n')
        return JSONResponse(serializer.data + serializer1.data)
        #return (JSONResponse(serializer.data) + JSONResponse(serializer1.data))

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserPackageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)



@csrf_exempt
def firewall(request, parameter, value):
    if request.method == 'GET':
	subscription = Subscription.objects.using('default').all().filter(Name=(ID_Table.objects.using('default').values_list('Subscription').filter(**{parameter: value})))
	Subscription_serializer = SubscriptionSerializer(subscription, many=True)

	package = Package.objects.using('default').all().filter(Name=(User_Package.objects.using('default').values_list('Package').filter(Activated=1, Unique_ID = (ID_Table.objects.using('default').values_list('Unique_ID').filter(**{parameter: value})))))
	Package_serializer = PackageSerializer(package, many=True)

	customer_policies = Customer_Discretion.objects.using('default').all().filter(Unique_ID=(ID_Table.objects.using('default').values_list('Unique_ID').filter(**{parameter: value})))
        customer_policies_serializer = Customer_DiscretionSerializer(customer_policies, many=True)

	ucop = UCOP.objects.using('default').all().filter(Unique_ID=(ID_Table.objects.using('default').values_list('Unique_ID').filter(**{parameter: value})))
        UCOP_serializer = UCOPSerializer(ucop, many=True)

	gop = GOP.objects.using('default').all().filter(Active=1)
        GOP_serializer = GOPSerializer(gop, many=True)

	emergency = Emergency.objects.using('default').all().filter(Active=1)
        Emergency_serializer = EmergencySerializer(emergency, many=True)

	return JSONResponse(Subscription_serializer.data + Package_serializer.data + customer_policies_serializer.data + UCOP_serializer.data + GOP_serializer.data + Emergency_serializer.data)


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserPackageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


def ces(request, transport, link, repute):
    if request.method == 'GET':
	ces_negotiation_policy = CES_Negotiation_Policy.objects.using('CES').all().filter(Trans_Protocol=transport) #.filter(**{parameter: value})
	CES_Negotiation_Policy_Serializer = CES_Negotiation_PolicySerializer(ces_negotiation_policy, many=True)

	return JSONResponse(CES_Negotiation_Policy_Serializer.data)


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserPackageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


def host(request, parameter, value):
    if request.method == 'GET':
	host_id = HOST_ID.objects.using('CES').all().filter(**{parameter: value})
	HOST_ID_serializer = HOST_IDSerializer(host_id, many=True)

	return JSONResponse(HOST_ID_serializer.data)


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserPackageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

