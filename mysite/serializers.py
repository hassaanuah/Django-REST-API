from rest_framework import serializers
from models import User_Package, Customer_Discretion, Emergency, GOP, Package, Subscription, UCOP, ID_Table, HOST_ID, CES_Negotiation_Policy, CES_Policy_Params, CES_Reputation_Table, Control_Policy_Params, HOST_ID, HOST_Negotiation_Policy, Host_Reputation_Table, Payload_Policies, RLOC_Policies


class UserPackageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_Package
        fields = ('Unique_ID', 'Package', 'Schedule_Start', 'Schedule_End')


class Customer_DiscretionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer_Discretion
        fields = ('Unique_ID', 'Network_Support', 'S_IP', 'S_Port', 'D_IP', 'D_Port', 'Trans_Protocol', 'Action', 'Value', 'Schedule_Start', 'Schedule_End', 'Priority')


class EmergencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Emergency
        fields = ('Conditions', 'Network_Support', 'S_IP', 'S_Port', 'D_IP', 'D_Port', 'Trans_Protocol', 'Action', 'Value')


class GOPSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GOP
        fields = ('Subscription', 'Package', 'Location', 'Network_Support', 'S_IP', 'S_Port', 'D_IP', 'D_Port', 'Trans_Protocol', 'Action', 'Value')


class PackageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = ('Name', 'Network_Support', 'S_IP', 'S_Port', 'D_IP', 'D_Port', 'Trans_Protocol', 'Action', 'Value')


class SubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscription
        fields = ('Name', 'Network_Support', 'S_IP', 'S_Port', 'D_IP', 'D_Port', 'Trans_Protocol', 'Action', 'Value')


class UCOPSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UCOP
        fields = ('Unique_ID', 'Reputation', 'Network_Support', 'S_IP', 'S_Port', 'D_IP', 'D_Port', 'Trans_Protocol', 'Action', 'Value')


class ID_TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ID_Table
        fields = ('FQDN', 'MSISDN', 'Unique_ID', 'Subscription')



class HOST_IDSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HOST_ID
        fields = ('Local_FQDN', 'ID_Type', 'Value')


class CES_Negotiation_PolicySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CES_Negotiation_Policy
        fields = ('Trans_Protocol', 'Link_Alias', 'Dest_CES_ID', 'Reputation', 'Direction', 'Policy_Required', 'Policy_Offer', 'Policy_Available', 'Policy_Required_Constraints')


class CES_Policy_ParamsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CES_Policy_Params
        fields = ('Trans_Protocol', 'Link_Alias', 'Dest_CES_ID', 'Reputation', 'Direction', 'Parameters', 'Value')


class CES_Reputation_TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CES_Reputation_Table
        fields = ('CES_FQDN', 'Reputation')


class Control_Policy_ParamsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Control_Policy_Params
        fields = ('Local_FQDN', 'Remote_FQDN', 'Direction', 'Valid', 'Parameters', 'Value')


class HOST_IDSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HOST_ID
        fields = ('Local_FQDN', 'ID_Type', 'Value')


class HOST_Negotiation_PolicySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HOST_Negotiation_Policy
        fields = ('Local_FQDN', 'Remote_FQDN', 'Reputation', 'Direction', 'Policy_Required', 'Policy_Offer', 'Policy_Available', 'Policy_Required_Constraints')


class Host_Reputation_TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host_Reputation_Table
        fields = ('Host_FQDN', 'Reputation')


class Payload_PoliciesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payload_Policies
        fields = ('Local_FQDN', 'Remote_FQDN', 'Payload_Type')


class RLOC_PoliciesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RLOC_Policies
        fields = ('Local_FQDN', 'Remote_FQDN', 'RLOC_Type', 'Value')







