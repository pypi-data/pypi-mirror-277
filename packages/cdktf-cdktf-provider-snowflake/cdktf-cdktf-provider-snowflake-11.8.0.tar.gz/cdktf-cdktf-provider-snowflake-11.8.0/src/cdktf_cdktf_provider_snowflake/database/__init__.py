'''
# `snowflake_database`

Refer to the Terraform Registry for docs: [`snowflake_database`](https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database).
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class Database(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.database.Database",
):
    '''Represents a {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database snowflake_database}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        data_retention_time_in_days: typing.Optional[jsii.Number] = None,
        from_database: typing.Optional[builtins.str] = None,
        from_replica: typing.Optional[builtins.str] = None,
        from_share: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        is_transient: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        replication_configuration: typing.Optional[typing.Union["DatabaseReplicationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database snowflake_database} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Specifies the identifier for the database; must be unique for your account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#name Database#name}
        :param comment: Specifies a comment for the database. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#comment Database#comment}
        :param data_retention_time_in_days: Number of days for which Snowflake retains historical data for performing Time Travel actions (SELECT, CLONE, UNDROP) on the object. A value of 0 effectively disables Time Travel for the specified database. Default value for this field is set to -1, which is a fallback to use Snowflake default. For more information, see `Understanding & Using Time Travel <https://docs.snowflake.com/en/user-guide/data-time-travel>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#data_retention_time_in_days Database#data_retention_time_in_days}
        :param from_database: Specify a database to create a clone from. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#from_database Database#from_database}
        :param from_replica: Specify a fully-qualified path to a database to create a replica from. A fully qualified path follows the format of ``"<organization_name>"."<account_name>"."<db_name>"``. An example would be: ``"myorg1"."account1"."db1"`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#from_replica Database#from_replica}
        :param from_share: Specify a provider and a share in this map to create a database from a share. As of version 0.87.0, the provider field is the account locator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#from_share Database#from_share}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#id Database#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_transient: Specifies a database as transient. Transient databases do not have a Fail-safe period so they do not incur additional storage costs once they leave Time Travel; however, this means they are also not protected by Fail-safe in the event of a data loss. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#is_transient Database#is_transient}
        :param replication_configuration: replication_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#replication_configuration Database#replication_configuration}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b15a50f89eb08aece66579f840c6fa677da88eecbc745d8303f4003e46439abf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DatabaseConfig(
            name=name,
            comment=comment,
            data_retention_time_in_days=data_retention_time_in_days,
            from_database=from_database,
            from_replica=from_replica,
            from_share=from_share,
            id=id,
            is_transient=is_transient,
            replication_configuration=replication_configuration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a Database resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Database to import.
        :param import_from_id: The id of the existing Database that should be imported. Refer to the {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Database to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e77891cb77202232aa5fdff4adeab90ba3a5bb42678747f900a74c6a3daa469f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putReplicationConfiguration")
    def put_replication_configuration(
        self,
        *,
        accounts: typing.Sequence[builtins.str],
        ignore_edition_check: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param accounts: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#accounts Database#accounts}.
        :param ignore_edition_check: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#ignore_edition_check Database#ignore_edition_check}.
        '''
        value = DatabaseReplicationConfiguration(
            accounts=accounts, ignore_edition_check=ignore_edition_check
        )

        return typing.cast(None, jsii.invoke(self, "putReplicationConfiguration", [value]))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetDataRetentionTimeInDays")
    def reset_data_retention_time_in_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataRetentionTimeInDays", []))

    @jsii.member(jsii_name="resetFromDatabase")
    def reset_from_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFromDatabase", []))

    @jsii.member(jsii_name="resetFromReplica")
    def reset_from_replica(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFromReplica", []))

    @jsii.member(jsii_name="resetFromShare")
    def reset_from_share(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFromShare", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsTransient")
    def reset_is_transient(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsTransient", []))

    @jsii.member(jsii_name="resetReplicationConfiguration")
    def reset_replication_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicationConfiguration", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="synthesizeHclAttributes")
    def _synthesize_hcl_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeHclAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="replicationConfiguration")
    def replication_configuration(
        self,
    ) -> "DatabaseReplicationConfigurationOutputReference":
        return typing.cast("DatabaseReplicationConfigurationOutputReference", jsii.get(self, "replicationConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="dataRetentionTimeInDaysInput")
    def data_retention_time_in_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dataRetentionTimeInDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="fromDatabaseInput")
    def from_database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fromDatabaseInput"))

    @builtins.property
    @jsii.member(jsii_name="fromReplicaInput")
    def from_replica_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fromReplicaInput"))

    @builtins.property
    @jsii.member(jsii_name="fromShareInput")
    def from_share_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "fromShareInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isTransientInput")
    def is_transient_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "isTransientInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="replicationConfigurationInput")
    def replication_configuration_input(
        self,
    ) -> typing.Optional["DatabaseReplicationConfiguration"]:
        return typing.cast(typing.Optional["DatabaseReplicationConfiguration"], jsii.get(self, "replicationConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e2a89dc8f0fc5f4ebbf143fe2e8f7040b61e3933fbac91752a1ed3b7e53e18a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="dataRetentionTimeInDays")
    def data_retention_time_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dataRetentionTimeInDays"))

    @data_retention_time_in_days.setter
    def data_retention_time_in_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eca2c028304080fa7ff570057044330e7d313c3be453bcf132c534f78bf04959)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataRetentionTimeInDays", value)

    @builtins.property
    @jsii.member(jsii_name="fromDatabase")
    def from_database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fromDatabase"))

    @from_database.setter
    def from_database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c57d58a97830a9ef27525ad784f1640e576aadff0a365f2e168eeb2702775234)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fromDatabase", value)

    @builtins.property
    @jsii.member(jsii_name="fromReplica")
    def from_replica(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fromReplica"))

    @from_replica.setter
    def from_replica(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f3e01a05ba9f63bd8e82d6accf5a9c1587fbb60d2fe92634ed56314823ee2cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fromReplica", value)

    @builtins.property
    @jsii.member(jsii_name="fromShare")
    def from_share(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "fromShare"))

    @from_share.setter
    def from_share(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__957d25f716ff1b8273f04349c6dda9b8e15c7a8f06c520a04597611b09858451)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fromShare", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cd1d980fc53ae3767f84154ae86a1f0f7561231ff3245856409f992ab3ca540)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isTransient")
    def is_transient(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "isTransient"))

    @is_transient.setter
    def is_transient(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43c2a7b99e3b917074cd9fbd8d72667638938c3856367106165056bde52ffda8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isTransient", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbccc96209c6e09ec18d2d3fc2bf18fc780c674c489bd1dee20dac62996024d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.database.DatabaseConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "comment": "comment",
        "data_retention_time_in_days": "dataRetentionTimeInDays",
        "from_database": "fromDatabase",
        "from_replica": "fromReplica",
        "from_share": "fromShare",
        "id": "id",
        "is_transient": "isTransient",
        "replication_configuration": "replicationConfiguration",
    },
)
class DatabaseConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        data_retention_time_in_days: typing.Optional[jsii.Number] = None,
        from_database: typing.Optional[builtins.str] = None,
        from_replica: typing.Optional[builtins.str] = None,
        from_share: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        is_transient: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        replication_configuration: typing.Optional[typing.Union["DatabaseReplicationConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Specifies the identifier for the database; must be unique for your account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#name Database#name}
        :param comment: Specifies a comment for the database. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#comment Database#comment}
        :param data_retention_time_in_days: Number of days for which Snowflake retains historical data for performing Time Travel actions (SELECT, CLONE, UNDROP) on the object. A value of 0 effectively disables Time Travel for the specified database. Default value for this field is set to -1, which is a fallback to use Snowflake default. For more information, see `Understanding & Using Time Travel <https://docs.snowflake.com/en/user-guide/data-time-travel>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#data_retention_time_in_days Database#data_retention_time_in_days}
        :param from_database: Specify a database to create a clone from. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#from_database Database#from_database}
        :param from_replica: Specify a fully-qualified path to a database to create a replica from. A fully qualified path follows the format of ``"<organization_name>"."<account_name>"."<db_name>"``. An example would be: ``"myorg1"."account1"."db1"`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#from_replica Database#from_replica}
        :param from_share: Specify a provider and a share in this map to create a database from a share. As of version 0.87.0, the provider field is the account locator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#from_share Database#from_share}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#id Database#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_transient: Specifies a database as transient. Transient databases do not have a Fail-safe period so they do not incur additional storage costs once they leave Time Travel; however, this means they are also not protected by Fail-safe in the event of a data loss. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#is_transient Database#is_transient}
        :param replication_configuration: replication_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#replication_configuration Database#replication_configuration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(replication_configuration, dict):
            replication_configuration = DatabaseReplicationConfiguration(**replication_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cb9ea0f5460322c2aa412891dea0477deedf7145dc8a299456e1d66c88827d3)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument data_retention_time_in_days", value=data_retention_time_in_days, expected_type=type_hints["data_retention_time_in_days"])
            check_type(argname="argument from_database", value=from_database, expected_type=type_hints["from_database"])
            check_type(argname="argument from_replica", value=from_replica, expected_type=type_hints["from_replica"])
            check_type(argname="argument from_share", value=from_share, expected_type=type_hints["from_share"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_transient", value=is_transient, expected_type=type_hints["is_transient"])
            check_type(argname="argument replication_configuration", value=replication_configuration, expected_type=type_hints["replication_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if comment is not None:
            self._values["comment"] = comment
        if data_retention_time_in_days is not None:
            self._values["data_retention_time_in_days"] = data_retention_time_in_days
        if from_database is not None:
            self._values["from_database"] = from_database
        if from_replica is not None:
            self._values["from_replica"] = from_replica
        if from_share is not None:
            self._values["from_share"] = from_share
        if id is not None:
            self._values["id"] = id
        if is_transient is not None:
            self._values["is_transient"] = is_transient
        if replication_configuration is not None:
            self._values["replication_configuration"] = replication_configuration

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Specifies the identifier for the database; must be unique for your account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#name Database#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Specifies a comment for the database.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#comment Database#comment}
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_retention_time_in_days(self) -> typing.Optional[jsii.Number]:
        '''Number of days for which Snowflake retains historical data for performing Time Travel actions (SELECT, CLONE, UNDROP) on the object.

        A value of 0 effectively disables Time Travel for the specified database. Default value for this field is set to -1, which is a fallback to use Snowflake default. For more information, see `Understanding & Using Time Travel <https://docs.snowflake.com/en/user-guide/data-time-travel>`_.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#data_retention_time_in_days Database#data_retention_time_in_days}
        '''
        result = self._values.get("data_retention_time_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def from_database(self) -> typing.Optional[builtins.str]:
        '''Specify a database to create a clone from.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#from_database Database#from_database}
        '''
        result = self._values.get("from_database")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def from_replica(self) -> typing.Optional[builtins.str]:
        '''Specify a fully-qualified path to a database to create a replica from.

        A fully qualified path follows the format of ``"<organization_name>"."<account_name>"."<db_name>"``. An example would be: ``"myorg1"."account1"."db1"``

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#from_replica Database#from_replica}
        '''
        result = self._values.get("from_replica")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def from_share(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Specify a provider and a share in this map to create a database from a share.

        As of version 0.87.0, the provider field is the account locator.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#from_share Database#from_share}
        '''
        result = self._values.get("from_share")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#id Database#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_transient(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specifies a database as transient.

        Transient databases do not have a Fail-safe period so they do not incur additional storage costs once they leave Time Travel; however, this means they are also not protected by Fail-safe in the event of a data loss.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#is_transient Database#is_transient}
        '''
        result = self._values.get("is_transient")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def replication_configuration(
        self,
    ) -> typing.Optional["DatabaseReplicationConfiguration"]:
        '''replication_configuration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#replication_configuration Database#replication_configuration}
        '''
        result = self._values.get("replication_configuration")
        return typing.cast(typing.Optional["DatabaseReplicationConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.database.DatabaseReplicationConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "accounts": "accounts",
        "ignore_edition_check": "ignoreEditionCheck",
    },
)
class DatabaseReplicationConfiguration:
    def __init__(
        self,
        *,
        accounts: typing.Sequence[builtins.str],
        ignore_edition_check: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param accounts: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#accounts Database#accounts}.
        :param ignore_edition_check: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#ignore_edition_check Database#ignore_edition_check}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71337d0808d2eda0c841ab8bd5812075b6abb3f277066b524c6e2b2e5136488d)
            check_type(argname="argument accounts", value=accounts, expected_type=type_hints["accounts"])
            check_type(argname="argument ignore_edition_check", value=ignore_edition_check, expected_type=type_hints["ignore_edition_check"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "accounts": accounts,
        }
        if ignore_edition_check is not None:
            self._values["ignore_edition_check"] = ignore_edition_check

    @builtins.property
    def accounts(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#accounts Database#accounts}.'''
        result = self._values.get("accounts")
        assert result is not None, "Required property 'accounts' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def ignore_edition_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/database#ignore_edition_check Database#ignore_edition_check}.'''
        result = self._values.get("ignore_edition_check")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseReplicationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseReplicationConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.database.DatabaseReplicationConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dd2210c7258397fa6283bae8e872ac35f74878122e87803cf36ed0fcfcad3ce)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIgnoreEditionCheck")
    def reset_ignore_edition_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreEditionCheck", []))

    @builtins.property
    @jsii.member(jsii_name="accountsInput")
    def accounts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "accountsInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreEditionCheckInput")
    def ignore_edition_check_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ignoreEditionCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="accounts")
    def accounts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "accounts"))

    @accounts.setter
    def accounts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13afbca86637ce372a04c551cb2a2134626d5013db29fdd47eb7dec21a957b12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accounts", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreEditionCheck")
    def ignore_edition_check(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ignoreEditionCheck"))

    @ignore_edition_check.setter
    def ignore_edition_check(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__568cdc9f7f4f999f68a11cabf16395cda729dda95dc7b7d8b27bb1d390abfeaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreEditionCheck", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatabaseReplicationConfiguration]:
        return typing.cast(typing.Optional[DatabaseReplicationConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseReplicationConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0ea55e6b52983e7354a543b1b21857824d92f603ae7dadf6799fa0a75871921)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Database",
    "DatabaseConfig",
    "DatabaseReplicationConfiguration",
    "DatabaseReplicationConfigurationOutputReference",
]

publication.publish()

def _typecheckingstub__b15a50f89eb08aece66579f840c6fa677da88eecbc745d8303f4003e46439abf(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    data_retention_time_in_days: typing.Optional[jsii.Number] = None,
    from_database: typing.Optional[builtins.str] = None,
    from_replica: typing.Optional[builtins.str] = None,
    from_share: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    is_transient: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    replication_configuration: typing.Optional[typing.Union[DatabaseReplicationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e77891cb77202232aa5fdff4adeab90ba3a5bb42678747f900a74c6a3daa469f(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e2a89dc8f0fc5f4ebbf143fe2e8f7040b61e3933fbac91752a1ed3b7e53e18a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eca2c028304080fa7ff570057044330e7d313c3be453bcf132c534f78bf04959(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c57d58a97830a9ef27525ad784f1640e576aadff0a365f2e168eeb2702775234(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f3e01a05ba9f63bd8e82d6accf5a9c1587fbb60d2fe92634ed56314823ee2cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__957d25f716ff1b8273f04349c6dda9b8e15c7a8f06c520a04597611b09858451(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cd1d980fc53ae3767f84154ae86a1f0f7561231ff3245856409f992ab3ca540(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43c2a7b99e3b917074cd9fbd8d72667638938c3856367106165056bde52ffda8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbccc96209c6e09ec18d2d3fc2bf18fc780c674c489bd1dee20dac62996024d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cb9ea0f5460322c2aa412891dea0477deedf7145dc8a299456e1d66c88827d3(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    data_retention_time_in_days: typing.Optional[jsii.Number] = None,
    from_database: typing.Optional[builtins.str] = None,
    from_replica: typing.Optional[builtins.str] = None,
    from_share: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    is_transient: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    replication_configuration: typing.Optional[typing.Union[DatabaseReplicationConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71337d0808d2eda0c841ab8bd5812075b6abb3f277066b524c6e2b2e5136488d(
    *,
    accounts: typing.Sequence[builtins.str],
    ignore_edition_check: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dd2210c7258397fa6283bae8e872ac35f74878122e87803cf36ed0fcfcad3ce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13afbca86637ce372a04c551cb2a2134626d5013db29fdd47eb7dec21a957b12(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__568cdc9f7f4f999f68a11cabf16395cda729dda95dc7b7d8b27bb1d390abfeaf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0ea55e6b52983e7354a543b1b21857824d92f603ae7dadf6799fa0a75871921(
    value: typing.Optional[DatabaseReplicationConfiguration],
) -> None:
    """Type checking stubs"""
    pass
