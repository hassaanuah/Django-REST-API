from django.db import models
from django.apps import AppConfig
from django.forms import ModelForm
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from django.contrib import messages



######################################################################
###		Firewall Tables



class User_Package(models.Model):
    Unique_ID =models.CharField(max_length=64, db_column="Unique_ID")
    Package =models.CharField(max_length=128, db_column="Package")
    Activated =models.BooleanField(db_column="Activated")
    Schedule_Start =models.DateTimeField(db_column="Schedule_Start")
    Schedule_End =models.DateTimeField(db_column="Schedule_End")
    class Meta:
        db_table='User_Package'


class Customer_Discretion(models.Model):
    Unique_ID =models.CharField(max_length=64, db_column="Unique_ID")
    Active =models.BooleanField(db_column="Active")
    Network_Support =models.CharField(max_length=128, db_column="Network_Support")
    S_IP =models.CharField(max_length=128, db_column="S_IP")
    S_Port =models.CharField(max_length=16, db_column="S_Port")
    D_IP =models.CharField(max_length=128, db_column="D_IP")
    D_Port =models.CharField(max_length=16, db_column="D_Port")
    Trans_Protocol =models.CharField(max_length=16, db_column="Trans_Protocol")
    Action =models.CharField(max_length=32, db_column="Action")
    Value =models.CharField(max_length=256, db_column="Value")
    Schedule_Start =models.DateTimeField(db_column="Schedule_Start")
    Schedule_End =models.DateTimeField(db_column="Schedule_End")
    Priority =models.CharField(max_length=16, db_column="Priority")
    class Meta:
        db_table='Customer_Discretion'


class Emergency(models.Model):
    Conditions =models.CharField(max_length=64, db_column="Conditions")
    Active =models.BooleanField(db_column="Active")
    Network_Support =models.CharField(max_length=128, db_column="Network_Support")
    S_IP =models.CharField(max_length=128, db_column="S_IP")
    S_Port =models.CharField(max_length=16, db_column="S_Port")
    D_IP =models.CharField(max_length=128, db_column="D_IP")
    D_Port =models.CharField(max_length=16, db_column="D_Port")
    Trans_Protocol =models.CharField(max_length=16, db_column="Trans_Protocol")
    Action =models.CharField(max_length=32, db_column="Action")
    Value =models.CharField(max_length=256, db_column="Value")
    class Meta:
        db_table='Emergency'




class GOP(models.Model):
    Subscription =models.CharField(max_length=64, db_column="Subscription")
    Package =models.CharField(max_length=64, db_column="Package")
    Location =models.CharField(max_length=64, db_column="Location")
    Active =models.BooleanField(db_column="Active")
    Network_Support =models.CharField(max_length=128, db_column="Network_Support")
    S_IP =models.CharField(max_length=128, db_column="S_IP")
    S_Port =models.CharField(max_length=16, db_column="S_Port")
    D_IP =models.CharField(max_length=128, db_column="D_IP")
    D_Port =models.CharField(max_length=16, db_column="D_Port")
    Trans_Protocol =models.CharField(max_length=16, db_column="Trans_Protocol")
    Action =models.CharField(max_length=32, db_column="Action")
    Value =models.CharField(max_length=256, db_column="Value")
    class Meta:
        db_table='GOP'



class Package(models.Model):
    Name =models.CharField(max_length=128, db_column="Name")
    Network_Support =models.CharField(max_length=128, db_column="Network_Support")
    S_IP =models.CharField(max_length=128, db_column="S_IP")
    S_Port =models.CharField(max_length=16, db_column="S_Port")
    D_IP =models.CharField(max_length=128, db_column="D_IP")
    D_Port =models.CharField(max_length=16, db_column="D_Port")
    Trans_Protocol =models.CharField(max_length=16, db_column="Trans_Protocol")
    Action =models.CharField(max_length=32, db_column="Action")
    Value =models.CharField(max_length=256, db_column="Value")
    class Meta:
        db_table='Package'


class Subscription(models.Model):
    Name =models.CharField(max_length=128, db_column="Name")
    Network_Support =models.CharField(max_length=128, db_column="Network_Support")
    S_IP =models.CharField(max_length=128, db_column="S_IP")
    S_Port =models.CharField(max_length=16, db_column="S_Port")
    D_IP =models.CharField(max_length=128, db_column="D_IP")
    D_Port =models.CharField(max_length=16, db_column="D_Port")
    Trans_Protocol =models.CharField(max_length=16, db_column="Trans_Protocol")
    Action =models.CharField(max_length=32, db_column="Action")
    Value =models.CharField(max_length=256, db_column="Value")
    class Meta:
        db_table='Subscription'



class UCOP(models.Model):
    Unique_ID =models.CharField(max_length=64, db_column="Unique_ID")
    Reputation =models.CharField(max_length=48, db_column="Reputation")
    Active =models.BooleanField(db_column="Active")
    Network_Support =models.CharField(max_length=128, db_column="Network_Support")
    S_IP =models.CharField(max_length=128, db_column="S_IP")
    S_Port =models.CharField(max_length=16, db_column="S_Port")
    D_IP =models.CharField(max_length=128, db_column="D_IP")
    D_Port =models.CharField(max_length=16, db_column="D_Port")
    Trans_Protocol =models.CharField(max_length=16, db_column="Trans_Protocol")
    Action =models.CharField(max_length=32, db_column="Action")
    Value =models.CharField(max_length=256, db_column="Value")
    class Meta:
        db_table='UCOP'



class ID_Table(models.Model):
    FQDN =models.CharField(max_length=128, db_column="FQDN")
    MSISDN =models.CharField(max_length=16, db_column="MSISDN")
    Unique_ID =models.CharField(max_length=64, db_column="Unique_ID")
    Subscription =models.CharField(max_length=128, db_column="Subscription")
    class Meta:
        db_table='ID_Table'



##################################################################################################################
#		CES TABLES



class CES_Negotiation_Policy(models.Model):
    Trans_Protocol =models.CharField(max_length=16, db_column="Trans_Protocol")
    Link_Alias =models.CharField(max_length=128, db_column="Link_Alias")
    Dest_CES_ID =models.CharField(max_length=128, db_column="Dest_CES_ID")
    Reputation =models.CharField(max_length=48, db_column="Reputation")
    Direction =models.CharField(max_length=16, db_column="Direction")
    Policy_Required =models.CharField(max_length=256, db_column="Policy_Required")
    Policy_Offer =models.CharField(max_length=256, db_column="Policy_Offer")
    Policy_Available =models.CharField(max_length=256, db_column="Policy_Available")
    Policy_Required_Constraints =models.CharField(max_length=256, db_column="Policy_Required_Constraints")
    class Meta:
        db_table='CES_Negotiation_Policy'



class CES_Policy_Params(models.Model):
    Trans_Protocol =models.CharField(max_length=16, db_column="Trans_Protocol")
    Link_Alias =models.CharField(max_length=128, db_column="Link_Alias")
    Dest_CES_ID =models.CharField(max_length=128, db_column="Dest_CES_ID")
    Reputation =models.CharField(max_length=48, db_column="Reputation")
    Direction =models.CharField(max_length=16, db_column="Direction")
    Valid =models.BooleanField(db_column="Valid")
    Parameters =models.CharField(max_length=128, db_column="Parameters")
    Value =models.CharField(max_length=128, db_column="Value")
    class Meta:
        db_table='CES_Policy_Params'



class CES_Reputation_Table(models.Model):
    CES_FQDN =models.CharField(max_length=128, db_column="CES_FQDN")
    Reputation =models.CharField(max_length=48, db_column="Reputation")
    class Meta:
        db_table='CES_Reputation_Table'



class Control_Policy_Params(models.Model):
    Local_FQDN =models.CharField(max_length=128, db_column="Local_FQDN")
    Remote_FQDN =models.CharField(max_length=128, db_column="Remote_FQDN")
    Direction =models.CharField(max_length=16, db_column="Direction")
    Valid =models.BooleanField(db_column="Valid")
    Parameters =models.CharField(max_length=128, db_column="Parameters")
    Value =models.CharField(max_length=128, db_column="Value")
    class Meta:
        db_table='Control_Policy_Params'


class HOST_ID(models.Model):
    Local_FQDN =models.CharField(max_length=128, db_column="Local_FQDN")
    ID_Type =models.CharField(max_length=48, db_column="ID_Type")
    Valid =models.BooleanField(db_column="Valid")
    Value =models.CharField(max_length=128, db_column="Value")
    class Meta:
        db_table='HOST_ID'



class HOST_Negotiation_Policy(models.Model):
    Local_FQDN =models.CharField(max_length=128, db_column="Local_FQDN")
    Remote_FQDN =models.CharField(max_length=128, db_column="Remote_FQDN")
    Reputation =models.CharField(max_length=48, db_column="Reputation")
    Direction =models.CharField(max_length=16, db_column="Direction")
    Policy_Required =models.CharField(max_length=256, db_column="Policy_Required")
    Policy_Offer =models.CharField(max_length=256, db_column="Policy_Offer")
    Policy_Available =models.CharField(max_length=256, db_column="Policy_Available")
    Policy_Required_Constraints =models.CharField(max_length=256, db_column="Policy_Required_Constraints")
    class Meta:
        db_table='HOST_Negotiation_Policy'



class Host_Reputation_Table(models.Model):
    Host_FQDN =models.CharField(max_length=128, db_column="Host_FQDN")
    Reputation =models.CharField(max_length=48, db_column="Reputation")
    class Meta:
        db_table='Host_Reputation_Table'



class Payload_Policies(models.Model):
    Local_FQDN =models.CharField(max_length=128, db_column="Local_FQDN")
    Remote_FQDN =models.CharField(max_length=128, db_column="Remote_FQDN")
    Valid =models.BooleanField(db_column="Valid")
    Payload_Type =models.CharField(max_length=64, db_column="Payload_Type")
    class Meta:
        db_table='Payload_Policies'



class RLOC_Policies(models.Model):
    Local_FQDN =models.CharField(max_length=128, db_column="Local_FQDN")
    Remote_FQDN =models.CharField(max_length=128, db_column="Remote_FQDN")
    Valid =models.BooleanField(db_column="Valid")
    RLOC_Type =models.CharField(max_length=64, db_column="RLOC_Type")
    Value =models.CharField(max_length=128, db_column="Value")
    class Meta:
        db_table='RLOC_Policies'






