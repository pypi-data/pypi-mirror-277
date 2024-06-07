'''
# `snowflake_function_grant`

Refer to the Terraform Registry for docs: [`snowflake_function_grant`](https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant).
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


class FunctionGrant(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.functionGrant.FunctionGrant",
):
    '''Represents a {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant snowflake_function_grant}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        database_name: builtins.str,
        roles: typing.Sequence[builtins.str],
        argument_data_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_multiple_grants: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        function_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        on_all: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        on_future: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        privilege: typing.Optional[builtins.str] = None,
        revert_ownership_to_role_name: typing.Optional[builtins.str] = None,
        schema_name: typing.Optional[builtins.str] = None,
        shares: typing.Optional[typing.Sequence[builtins.str]] = None,
        with_grant_option: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant snowflake_function_grant} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param database_name: The name of the database containing the current or future functions on which to grant privileges. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#database_name FunctionGrant#database_name}
        :param roles: Grants privilege to these roles. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#roles FunctionGrant#roles}
        :param argument_data_types: List of the argument data types for the function (must be present if function has arguments and function_name is present). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#argument_data_types FunctionGrant#argument_data_types}
        :param enable_multiple_grants: When this is set to true, multiple grants of the same type can be created. This will cause Terraform to not revoke grants applied to roles and objects outside Terraform. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#enable_multiple_grants FunctionGrant#enable_multiple_grants}
        :param function_name: The name of the function on which to grant privileges immediately (only valid if on_future is false). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#function_name FunctionGrant#function_name}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#id FunctionGrant#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param on_all: When this is set to true and a schema_name is provided, apply this grant on all functions in the given schema. When this is true and no schema_name is provided apply this grant on all functions in the given database. The function_name, arguments, return_type, and shares fields must be unset in order to use on_all. Cannot be used together with on_future. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#on_all FunctionGrant#on_all}
        :param on_future: When this is set to true and a schema_name is provided, apply this grant on all future functions in the given schema. When this is true and no schema_name is provided apply this grant on all future functions in the given database. The function_name, arguments, return_type, and shares fields must be unset in order to use on_future. Cannot be used together with on_all. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#on_future FunctionGrant#on_future}
        :param privilege: The privilege to grant on the current or future function. Must be one of ``USAGE`` or ``OWNERSHIP``. To grant all privileges, use the value ``ALL PRIVILEGES`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#privilege FunctionGrant#privilege}
        :param revert_ownership_to_role_name: The name of the role to revert ownership to on destroy. Has no effect unless ``privilege`` is set to ``OWNERSHIP`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#revert_ownership_to_role_name FunctionGrant#revert_ownership_to_role_name}
        :param schema_name: The name of the schema containing the current or future functions on which to grant privileges. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#schema_name FunctionGrant#schema_name}
        :param shares: Grants privilege to these shares (only valid if on_future is false). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#shares FunctionGrant#shares}
        :param with_grant_option: When this is set to true, allows the recipient role to grant the privileges to other roles. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#with_grant_option FunctionGrant#with_grant_option}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa5159753af7e87b0f78180f3ce05db4dc4bab042c478bad2f28b515adf07fbf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = FunctionGrantConfig(
            database_name=database_name,
            roles=roles,
            argument_data_types=argument_data_types,
            enable_multiple_grants=enable_multiple_grants,
            function_name=function_name,
            id=id,
            on_all=on_all,
            on_future=on_future,
            privilege=privilege,
            revert_ownership_to_role_name=revert_ownership_to_role_name,
            schema_name=schema_name,
            shares=shares,
            with_grant_option=with_grant_option,
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
        '''Generates CDKTF code for importing a FunctionGrant resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the FunctionGrant to import.
        :param import_from_id: The id of the existing FunctionGrant that should be imported. Refer to the {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the FunctionGrant to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1902f1ac58b402174d21b9843f52d509876220633e0cad08325fa98b50e9997)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetArgumentDataTypes")
    def reset_argument_data_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgumentDataTypes", []))

    @jsii.member(jsii_name="resetEnableMultipleGrants")
    def reset_enable_multiple_grants(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableMultipleGrants", []))

    @jsii.member(jsii_name="resetFunctionName")
    def reset_function_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFunctionName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOnAll")
    def reset_on_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnAll", []))

    @jsii.member(jsii_name="resetOnFuture")
    def reset_on_future(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnFuture", []))

    @jsii.member(jsii_name="resetPrivilege")
    def reset_privilege(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivilege", []))

    @jsii.member(jsii_name="resetRevertOwnershipToRoleName")
    def reset_revert_ownership_to_role_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRevertOwnershipToRoleName", []))

    @jsii.member(jsii_name="resetSchemaName")
    def reset_schema_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaName", []))

    @jsii.member(jsii_name="resetShares")
    def reset_shares(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShares", []))

    @jsii.member(jsii_name="resetWithGrantOption")
    def reset_with_grant_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWithGrantOption", []))

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
    @jsii.member(jsii_name="argumentDataTypesInput")
    def argument_data_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argumentDataTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="enableMultipleGrantsInput")
    def enable_multiple_grants_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableMultipleGrantsInput"))

    @builtins.property
    @jsii.member(jsii_name="functionNameInput")
    def function_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="onAllInput")
    def on_all_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "onAllInput"))

    @builtins.property
    @jsii.member(jsii_name="onFutureInput")
    def on_future_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "onFutureInput"))

    @builtins.property
    @jsii.member(jsii_name="privilegeInput")
    def privilege_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privilegeInput"))

    @builtins.property
    @jsii.member(jsii_name="revertOwnershipToRoleNameInput")
    def revert_ownership_to_role_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "revertOwnershipToRoleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rolesInput")
    def roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rolesInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaNameInput")
    def schema_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sharesInput")
    def shares_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sharesInput"))

    @builtins.property
    @jsii.member(jsii_name="withGrantOptionInput")
    def with_grant_option_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "withGrantOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="argumentDataTypes")
    def argument_data_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "argumentDataTypes"))

    @argument_data_types.setter
    def argument_data_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54615701440d8fc6c4fc58d8b586e96cb09a713671892becbe0570061772e1a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "argumentDataTypes", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe07b23a4510778d4ea6a3396431b6fc0b4c9b4a7fa0db5b585b3b31bc5d735a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="enableMultipleGrants")
    def enable_multiple_grants(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableMultipleGrants"))

    @enable_multiple_grants.setter
    def enable_multiple_grants(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9dff4bc97242d613e0c7b360fff628196fc3391df335fc8a152774d26e070fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableMultipleGrants", value)

    @builtins.property
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionName"))

    @function_name.setter
    def function_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69b087d6465e7edac1c6c2a3a836eb09b96e6c19a53f41a398e4141986355956)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__018d4768cd0d6e764a1878e583ff39fc855bd7f626ece5691f3a713c564d1cd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="onAll")
    def on_all(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "onAll"))

    @on_all.setter
    def on_all(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47b5c9d1cb4d815c3b21246823f56941310b16d4f8332630855102c1b7f44f58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onAll", value)

    @builtins.property
    @jsii.member(jsii_name="onFuture")
    def on_future(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "onFuture"))

    @on_future.setter
    def on_future(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbcbca1d70c774c52c0e0d1649d6bdcc933122c3e9b02395394f8f4333424054)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onFuture", value)

    @builtins.property
    @jsii.member(jsii_name="privilege")
    def privilege(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privilege"))

    @privilege.setter
    def privilege(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cb70e83a99bdbccc5455d1f8e7fad9847f54524c027cae8ec53e796efb0f34b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privilege", value)

    @builtins.property
    @jsii.member(jsii_name="revertOwnershipToRoleName")
    def revert_ownership_to_role_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "revertOwnershipToRoleName"))

    @revert_ownership_to_role_name.setter
    def revert_ownership_to_role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43da9cf9da1bafbef797179c8f7faee71ee1c238e0af6e63484e1062dce46bd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revertOwnershipToRoleName", value)

    @builtins.property
    @jsii.member(jsii_name="roles")
    def roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "roles"))

    @roles.setter
    def roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1f3509864c7f34e73ffd00db854fe83639d30b885708d5e8187990d1725c821)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roles", value)

    @builtins.property
    @jsii.member(jsii_name="schemaName")
    def schema_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaName"))

    @schema_name.setter
    def schema_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98f5a42edf4fba0def0774469d6e1aeff61e78522f82cff6bb92e96849f5fe52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaName", value)

    @builtins.property
    @jsii.member(jsii_name="shares")
    def shares(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "shares"))

    @shares.setter
    def shares(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9facb05499da8ac400523334b733973dda79489cae7dca971b52491d3204f3bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shares", value)

    @builtins.property
    @jsii.member(jsii_name="withGrantOption")
    def with_grant_option(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "withGrantOption"))

    @with_grant_option.setter
    def with_grant_option(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e0d01916ce8b64f79bdedadee00491a018252a2c10d221600423ccda9b3fe08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "withGrantOption", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.functionGrant.FunctionGrantConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "database_name": "databaseName",
        "roles": "roles",
        "argument_data_types": "argumentDataTypes",
        "enable_multiple_grants": "enableMultipleGrants",
        "function_name": "functionName",
        "id": "id",
        "on_all": "onAll",
        "on_future": "onFuture",
        "privilege": "privilege",
        "revert_ownership_to_role_name": "revertOwnershipToRoleName",
        "schema_name": "schemaName",
        "shares": "shares",
        "with_grant_option": "withGrantOption",
    },
)
class FunctionGrantConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        database_name: builtins.str,
        roles: typing.Sequence[builtins.str],
        argument_data_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_multiple_grants: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        function_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        on_all: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        on_future: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        privilege: typing.Optional[builtins.str] = None,
        revert_ownership_to_role_name: typing.Optional[builtins.str] = None,
        schema_name: typing.Optional[builtins.str] = None,
        shares: typing.Optional[typing.Sequence[builtins.str]] = None,
        with_grant_option: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param database_name: The name of the database containing the current or future functions on which to grant privileges. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#database_name FunctionGrant#database_name}
        :param roles: Grants privilege to these roles. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#roles FunctionGrant#roles}
        :param argument_data_types: List of the argument data types for the function (must be present if function has arguments and function_name is present). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#argument_data_types FunctionGrant#argument_data_types}
        :param enable_multiple_grants: When this is set to true, multiple grants of the same type can be created. This will cause Terraform to not revoke grants applied to roles and objects outside Terraform. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#enable_multiple_grants FunctionGrant#enable_multiple_grants}
        :param function_name: The name of the function on which to grant privileges immediately (only valid if on_future is false). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#function_name FunctionGrant#function_name}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#id FunctionGrant#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param on_all: When this is set to true and a schema_name is provided, apply this grant on all functions in the given schema. When this is true and no schema_name is provided apply this grant on all functions in the given database. The function_name, arguments, return_type, and shares fields must be unset in order to use on_all. Cannot be used together with on_future. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#on_all FunctionGrant#on_all}
        :param on_future: When this is set to true and a schema_name is provided, apply this grant on all future functions in the given schema. When this is true and no schema_name is provided apply this grant on all future functions in the given database. The function_name, arguments, return_type, and shares fields must be unset in order to use on_future. Cannot be used together with on_all. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#on_future FunctionGrant#on_future}
        :param privilege: The privilege to grant on the current or future function. Must be one of ``USAGE`` or ``OWNERSHIP``. To grant all privileges, use the value ``ALL PRIVILEGES`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#privilege FunctionGrant#privilege}
        :param revert_ownership_to_role_name: The name of the role to revert ownership to on destroy. Has no effect unless ``privilege`` is set to ``OWNERSHIP`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#revert_ownership_to_role_name FunctionGrant#revert_ownership_to_role_name}
        :param schema_name: The name of the schema containing the current or future functions on which to grant privileges. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#schema_name FunctionGrant#schema_name}
        :param shares: Grants privilege to these shares (only valid if on_future is false). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#shares FunctionGrant#shares}
        :param with_grant_option: When this is set to true, allows the recipient role to grant the privileges to other roles. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#with_grant_option FunctionGrant#with_grant_option}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a073b2a253fb39d67b56763675b64355bbb725f9745709cbcb4da8554063ab07)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument argument_data_types", value=argument_data_types, expected_type=type_hints["argument_data_types"])
            check_type(argname="argument enable_multiple_grants", value=enable_multiple_grants, expected_type=type_hints["enable_multiple_grants"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument on_all", value=on_all, expected_type=type_hints["on_all"])
            check_type(argname="argument on_future", value=on_future, expected_type=type_hints["on_future"])
            check_type(argname="argument privilege", value=privilege, expected_type=type_hints["privilege"])
            check_type(argname="argument revert_ownership_to_role_name", value=revert_ownership_to_role_name, expected_type=type_hints["revert_ownership_to_role_name"])
            check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
            check_type(argname="argument shares", value=shares, expected_type=type_hints["shares"])
            check_type(argname="argument with_grant_option", value=with_grant_option, expected_type=type_hints["with_grant_option"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
            "roles": roles,
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
        if argument_data_types is not None:
            self._values["argument_data_types"] = argument_data_types
        if enable_multiple_grants is not None:
            self._values["enable_multiple_grants"] = enable_multiple_grants
        if function_name is not None:
            self._values["function_name"] = function_name
        if id is not None:
            self._values["id"] = id
        if on_all is not None:
            self._values["on_all"] = on_all
        if on_future is not None:
            self._values["on_future"] = on_future
        if privilege is not None:
            self._values["privilege"] = privilege
        if revert_ownership_to_role_name is not None:
            self._values["revert_ownership_to_role_name"] = revert_ownership_to_role_name
        if schema_name is not None:
            self._values["schema_name"] = schema_name
        if shares is not None:
            self._values["shares"] = shares
        if with_grant_option is not None:
            self._values["with_grant_option"] = with_grant_option

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
    def database_name(self) -> builtins.str:
        '''The name of the database containing the current or future functions on which to grant privileges.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#database_name FunctionGrant#database_name}
        '''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def roles(self) -> typing.List[builtins.str]:
        '''Grants privilege to these roles.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#roles FunctionGrant#roles}
        '''
        result = self._values.get("roles")
        assert result is not None, "Required property 'roles' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def argument_data_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of the argument data types for the function (must be present if function has arguments and function_name is present).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#argument_data_types FunctionGrant#argument_data_types}
        '''
        result = self._values.get("argument_data_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enable_multiple_grants(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When this is set to true, multiple grants of the same type can be created.

        This will cause Terraform to not revoke grants applied to roles and objects outside Terraform.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#enable_multiple_grants FunctionGrant#enable_multiple_grants}
        '''
        result = self._values.get("enable_multiple_grants")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def function_name(self) -> typing.Optional[builtins.str]:
        '''The name of the function on which to grant privileges immediately (only valid if on_future is false).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#function_name FunctionGrant#function_name}
        '''
        result = self._values.get("function_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#id FunctionGrant#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_all(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When this is set to true and a schema_name is provided, apply this grant on all functions in the given schema.

        When this is true and no schema_name is provided apply this grant on all functions in the given database. The function_name, arguments, return_type, and shares fields must be unset in order to use on_all. Cannot be used together with on_future.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#on_all FunctionGrant#on_all}
        '''
        result = self._values.get("on_all")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def on_future(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When this is set to true and a schema_name is provided, apply this grant on all future functions in the given schema.

        When this is true and no schema_name is provided apply this grant on all future functions in the given database. The function_name, arguments, return_type, and shares fields must be unset in order to use on_future. Cannot be used together with on_all.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#on_future FunctionGrant#on_future}
        '''
        result = self._values.get("on_future")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def privilege(self) -> typing.Optional[builtins.str]:
        '''The privilege to grant on the current or future function.

        Must be one of ``USAGE`` or ``OWNERSHIP``. To grant all privileges, use the value ``ALL PRIVILEGES``

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#privilege FunctionGrant#privilege}
        '''
        result = self._values.get("privilege")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def revert_ownership_to_role_name(self) -> typing.Optional[builtins.str]:
        '''The name of the role to revert ownership to on destroy.

        Has no effect unless ``privilege`` is set to ``OWNERSHIP``

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#revert_ownership_to_role_name FunctionGrant#revert_ownership_to_role_name}
        '''
        result = self._values.get("revert_ownership_to_role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_name(self) -> typing.Optional[builtins.str]:
        '''The name of the schema containing the current or future functions on which to grant privileges.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#schema_name FunctionGrant#schema_name}
        '''
        result = self._values.get("schema_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shares(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Grants privilege to these shares (only valid if on_future is false).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#shares FunctionGrant#shares}
        '''
        result = self._values.get("shares")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def with_grant_option(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''When this is set to true, allows the recipient role to grant the privileges to other roles.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/function_grant#with_grant_option FunctionGrant#with_grant_option}
        '''
        result = self._values.get("with_grant_option")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FunctionGrantConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "FunctionGrant",
    "FunctionGrantConfig",
]

publication.publish()

def _typecheckingstub__aa5159753af7e87b0f78180f3ce05db4dc4bab042c478bad2f28b515adf07fbf(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    database_name: builtins.str,
    roles: typing.Sequence[builtins.str],
    argument_data_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    enable_multiple_grants: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    function_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    on_all: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    on_future: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    privilege: typing.Optional[builtins.str] = None,
    revert_ownership_to_role_name: typing.Optional[builtins.str] = None,
    schema_name: typing.Optional[builtins.str] = None,
    shares: typing.Optional[typing.Sequence[builtins.str]] = None,
    with_grant_option: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__f1902f1ac58b402174d21b9843f52d509876220633e0cad08325fa98b50e9997(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54615701440d8fc6c4fc58d8b586e96cb09a713671892becbe0570061772e1a5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe07b23a4510778d4ea6a3396431b6fc0b4c9b4a7fa0db5b585b3b31bc5d735a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9dff4bc97242d613e0c7b360fff628196fc3391df335fc8a152774d26e070fa(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69b087d6465e7edac1c6c2a3a836eb09b96e6c19a53f41a398e4141986355956(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__018d4768cd0d6e764a1878e583ff39fc855bd7f626ece5691f3a713c564d1cd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47b5c9d1cb4d815c3b21246823f56941310b16d4f8332630855102c1b7f44f58(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbcbca1d70c774c52c0e0d1649d6bdcc933122c3e9b02395394f8f4333424054(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cb70e83a99bdbccc5455d1f8e7fad9847f54524c027cae8ec53e796efb0f34b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43da9cf9da1bafbef797179c8f7faee71ee1c238e0af6e63484e1062dce46bd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1f3509864c7f34e73ffd00db854fe83639d30b885708d5e8187990d1725c821(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98f5a42edf4fba0def0774469d6e1aeff61e78522f82cff6bb92e96849f5fe52(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9facb05499da8ac400523334b733973dda79489cae7dca971b52491d3204f3bd(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e0d01916ce8b64f79bdedadee00491a018252a2c10d221600423ccda9b3fe08(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a073b2a253fb39d67b56763675b64355bbb725f9745709cbcb4da8554063ab07(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    database_name: builtins.str,
    roles: typing.Sequence[builtins.str],
    argument_data_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    enable_multiple_grants: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    function_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    on_all: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    on_future: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    privilege: typing.Optional[builtins.str] = None,
    revert_ownership_to_role_name: typing.Optional[builtins.str] = None,
    schema_name: typing.Optional[builtins.str] = None,
    shares: typing.Optional[typing.Sequence[builtins.str]] = None,
    with_grant_option: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass
