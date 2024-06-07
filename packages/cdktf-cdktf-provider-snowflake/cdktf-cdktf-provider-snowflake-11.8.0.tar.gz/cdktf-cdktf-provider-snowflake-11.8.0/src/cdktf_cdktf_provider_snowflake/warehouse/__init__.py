'''
# `snowflake_warehouse`

Refer to the Terraform Registry for docs: [`snowflake_warehouse`](https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse).
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


class Warehouse(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.warehouse.Warehouse",
):
    '''Represents a {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse snowflake_warehouse}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        auto_resume: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_suspend: typing.Optional[jsii.Number] = None,
        comment: typing.Optional[builtins.str] = None,
        enable_query_acceleration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        initially_suspended: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        max_cluster_count: typing.Optional[jsii.Number] = None,
        max_concurrency_level: typing.Optional[jsii.Number] = None,
        min_cluster_count: typing.Optional[jsii.Number] = None,
        query_acceleration_max_scale_factor: typing.Optional[jsii.Number] = None,
        resource_monitor: typing.Optional[builtins.str] = None,
        scaling_policy: typing.Optional[builtins.str] = None,
        statement_queued_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        statement_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        wait_for_provisioning: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        warehouse_size: typing.Optional[builtins.str] = None,
        warehouse_type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse snowflake_warehouse} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Identifier for the virtual warehouse; must be unique for your account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#name Warehouse#name}
        :param auto_resume: Specifies whether to automatically resume a warehouse when a SQL statement (e.g. query) is submitted to it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#auto_resume Warehouse#auto_resume}
        :param auto_suspend: Specifies the number of seconds of inactivity after which a warehouse is automatically suspended. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#auto_suspend Warehouse#auto_suspend}
        :param comment: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#comment Warehouse#comment}.
        :param enable_query_acceleration: Specifies whether to enable the query acceleration service for queries that rely on this warehouse for compute resources. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#enable_query_acceleration Warehouse#enable_query_acceleration}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#id Warehouse#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initially_suspended: Specifies whether the warehouse is created initially in the ‘Suspended’ state. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#initially_suspended Warehouse#initially_suspended}
        :param max_cluster_count: Specifies the maximum number of server clusters for the warehouse. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#max_cluster_count Warehouse#max_cluster_count}
        :param max_concurrency_level: Object parameter that specifies the concurrency level for SQL statements (i.e. queries and DML) executed by a warehouse. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#max_concurrency_level Warehouse#max_concurrency_level}
        :param min_cluster_count: Specifies the minimum number of server clusters for the warehouse (only applies to multi-cluster warehouses). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#min_cluster_count Warehouse#min_cluster_count}
        :param query_acceleration_max_scale_factor: Specifies the maximum scale factor for leasing compute resources for query acceleration. The scale factor is used as a multiplier based on warehouse size. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#query_acceleration_max_scale_factor Warehouse#query_acceleration_max_scale_factor}
        :param resource_monitor: Specifies the name of a resource monitor that is explicitly assigned to the warehouse. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#resource_monitor Warehouse#resource_monitor}
        :param scaling_policy: Specifies the policy for automatically starting and shutting down clusters in a multi-cluster warehouse running in Auto-scale mode. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#scaling_policy Warehouse#scaling_policy}
        :param statement_queued_timeout_in_seconds: Object parameter that specifies the time, in seconds, a SQL statement (query, DDL, DML, etc.) can be queued on a warehouse before it is canceled by the system. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#statement_queued_timeout_in_seconds Warehouse#statement_queued_timeout_in_seconds}
        :param statement_timeout_in_seconds: Specifies the time, in seconds, after which a running SQL statement (query, DDL, DML, etc.) is canceled by the system. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#statement_timeout_in_seconds Warehouse#statement_timeout_in_seconds}
        :param wait_for_provisioning: Specifies whether the warehouse, after being resized, waits for all the servers to provision before executing any queued or new queries. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#wait_for_provisioning Warehouse#wait_for_provisioning}
        :param warehouse_size: Specifies the size of the virtual warehouse. Larger warehouse sizes 5X-Large and 6X-Large are currently in preview and only available on Amazon Web Services (AWS). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#warehouse_size Warehouse#warehouse_size}
        :param warehouse_type: Specifies a STANDARD or SNOWPARK-OPTIMIZED warehouse. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#warehouse_type Warehouse#warehouse_type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7a545b9470ddbc13f6797573fe9db4caad9ea0ec20a416254e98f74ad315894)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = WarehouseConfig(
            name=name,
            auto_resume=auto_resume,
            auto_suspend=auto_suspend,
            comment=comment,
            enable_query_acceleration=enable_query_acceleration,
            id=id,
            initially_suspended=initially_suspended,
            max_cluster_count=max_cluster_count,
            max_concurrency_level=max_concurrency_level,
            min_cluster_count=min_cluster_count,
            query_acceleration_max_scale_factor=query_acceleration_max_scale_factor,
            resource_monitor=resource_monitor,
            scaling_policy=scaling_policy,
            statement_queued_timeout_in_seconds=statement_queued_timeout_in_seconds,
            statement_timeout_in_seconds=statement_timeout_in_seconds,
            wait_for_provisioning=wait_for_provisioning,
            warehouse_size=warehouse_size,
            warehouse_type=warehouse_type,
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
        '''Generates CDKTF code for importing a Warehouse resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Warehouse to import.
        :param import_from_id: The id of the existing Warehouse that should be imported. Refer to the {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Warehouse to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__572da37f5bf450cb7fe3f011f5e0e5d584f32856d369188d26ecdd2bed0c8cea)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAutoResume")
    def reset_auto_resume(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoResume", []))

    @jsii.member(jsii_name="resetAutoSuspend")
    def reset_auto_suspend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoSuspend", []))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetEnableQueryAcceleration")
    def reset_enable_query_acceleration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableQueryAcceleration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInitiallySuspended")
    def reset_initially_suspended(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitiallySuspended", []))

    @jsii.member(jsii_name="resetMaxClusterCount")
    def reset_max_cluster_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxClusterCount", []))

    @jsii.member(jsii_name="resetMaxConcurrencyLevel")
    def reset_max_concurrency_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrencyLevel", []))

    @jsii.member(jsii_name="resetMinClusterCount")
    def reset_min_cluster_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinClusterCount", []))

    @jsii.member(jsii_name="resetQueryAccelerationMaxScaleFactor")
    def reset_query_acceleration_max_scale_factor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryAccelerationMaxScaleFactor", []))

    @jsii.member(jsii_name="resetResourceMonitor")
    def reset_resource_monitor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceMonitor", []))

    @jsii.member(jsii_name="resetScalingPolicy")
    def reset_scaling_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScalingPolicy", []))

    @jsii.member(jsii_name="resetStatementQueuedTimeoutInSeconds")
    def reset_statement_queued_timeout_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatementQueuedTimeoutInSeconds", []))

    @jsii.member(jsii_name="resetStatementTimeoutInSeconds")
    def reset_statement_timeout_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatementTimeoutInSeconds", []))

    @jsii.member(jsii_name="resetWaitForProvisioning")
    def reset_wait_for_provisioning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForProvisioning", []))

    @jsii.member(jsii_name="resetWarehouseSize")
    def reset_warehouse_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarehouseSize", []))

    @jsii.member(jsii_name="resetWarehouseType")
    def reset_warehouse_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarehouseType", []))

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
    @jsii.member(jsii_name="autoResumeInput")
    def auto_resume_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoResumeInput"))

    @builtins.property
    @jsii.member(jsii_name="autoSuspendInput")
    def auto_suspend_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autoSuspendInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="enableQueryAccelerationInput")
    def enable_query_acceleration_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableQueryAccelerationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="initiallySuspendedInput")
    def initially_suspended_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "initiallySuspendedInput"))

    @builtins.property
    @jsii.member(jsii_name="maxClusterCountInput")
    def max_cluster_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxClusterCountInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrencyLevelInput")
    def max_concurrency_level_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrencyLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="minClusterCountInput")
    def min_cluster_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minClusterCountInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="queryAccelerationMaxScaleFactorInput")
    def query_acceleration_max_scale_factor_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "queryAccelerationMaxScaleFactorInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceMonitorInput")
    def resource_monitor_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceMonitorInput"))

    @builtins.property
    @jsii.member(jsii_name="scalingPolicyInput")
    def scaling_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scalingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="statementQueuedTimeoutInSecondsInput")
    def statement_queued_timeout_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "statementQueuedTimeoutInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="statementTimeoutInSecondsInput")
    def statement_timeout_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "statementTimeoutInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForProvisioningInput")
    def wait_for_provisioning_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitForProvisioningInput"))

    @builtins.property
    @jsii.member(jsii_name="warehouseSizeInput")
    def warehouse_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warehouseSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="warehouseTypeInput")
    def warehouse_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warehouseTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="autoResume")
    def auto_resume(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoResume"))

    @auto_resume.setter
    def auto_resume(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59e363e0e719321b9f36ba95f42412180d8c83bca4f70f5f58bf54d11faaca1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoResume", value)

    @builtins.property
    @jsii.member(jsii_name="autoSuspend")
    def auto_suspend(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autoSuspend"))

    @auto_suspend.setter
    def auto_suspend(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e33c40876b47a58a42eafec0c16bfa190228c08a23a39eea9350f0f083d61dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoSuspend", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4c985a73dcb01e461dd3d79db0b1b2b150d1b6ad292921dd0553f38596bff56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="enableQueryAcceleration")
    def enable_query_acceleration(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableQueryAcceleration"))

    @enable_query_acceleration.setter
    def enable_query_acceleration(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17a9dd2dcf21eba130519e20959255cf814826077dc1a2486f912d9091569c61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableQueryAcceleration", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46603b6d33e982986e0b443f6a5696f6a33454cc6e0aa6678817badd8cd756ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="initiallySuspended")
    def initially_suspended(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "initiallySuspended"))

    @initially_suspended.setter
    def initially_suspended(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09d176a43f31805f67ca01f79890fb1058791b57d84f2115996086f337ed2e1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initiallySuspended", value)

    @builtins.property
    @jsii.member(jsii_name="maxClusterCount")
    def max_cluster_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxClusterCount"))

    @max_cluster_count.setter
    def max_cluster_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba9c5ca5c139d131448b0430ff14223b8e4d4bb0a0fd5b55adffbbe7796824f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxClusterCount", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrencyLevel")
    def max_concurrency_level(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrencyLevel"))

    @max_concurrency_level.setter
    def max_concurrency_level(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec1a76dc728c5c13221da328191e3e3c34cc72784972ed2e3fc82897c41a05e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrencyLevel", value)

    @builtins.property
    @jsii.member(jsii_name="minClusterCount")
    def min_cluster_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minClusterCount"))

    @min_cluster_count.setter
    def min_cluster_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b96edb769e4b81e3cd326f1bc18a50dd3c4dac86feefc24a81934fafe5f777a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minClusterCount", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7077b71c10d32de0bc3d3c8d12117d655ce00aa136fc82b6a7c73b6d0ec8599)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="queryAccelerationMaxScaleFactor")
    def query_acceleration_max_scale_factor(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "queryAccelerationMaxScaleFactor"))

    @query_acceleration_max_scale_factor.setter
    def query_acceleration_max_scale_factor(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f96be4446754d4205d1e9d99a2c4abcb4828cb58dbd27f26e599e94fb3c26020)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryAccelerationMaxScaleFactor", value)

    @builtins.property
    @jsii.member(jsii_name="resourceMonitor")
    def resource_monitor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceMonitor"))

    @resource_monitor.setter
    def resource_monitor(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8e4b5fc94f6dc0de4811839fa018a79668ca9d8203c01cfb6f125c1c11eb185)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceMonitor", value)

    @builtins.property
    @jsii.member(jsii_name="scalingPolicy")
    def scaling_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scalingPolicy"))

    @scaling_policy.setter
    def scaling_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da84474f179556752719c65f7b2440f46eb949691133a2f9714d5686438334d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="statementQueuedTimeoutInSeconds")
    def statement_queued_timeout_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "statementQueuedTimeoutInSeconds"))

    @statement_queued_timeout_in_seconds.setter
    def statement_queued_timeout_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3a106de57372b520a40ffb364b03b9b17f28f3178d2a39b83f02ec994035f8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statementQueuedTimeoutInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="statementTimeoutInSeconds")
    def statement_timeout_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "statementTimeoutInSeconds"))

    @statement_timeout_in_seconds.setter
    def statement_timeout_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__142317704b4892b91eab76a9f614fe8251c78e43a9ab129e89de9d627f23595b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statementTimeoutInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="waitForProvisioning")
    def wait_for_provisioning(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "waitForProvisioning"))

    @wait_for_provisioning.setter
    def wait_for_provisioning(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c819ec074e712e3da84a3865385ae14fb043c93073d4af8926ce2af78053dc70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForProvisioning", value)

    @builtins.property
    @jsii.member(jsii_name="warehouseSize")
    def warehouse_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warehouseSize"))

    @warehouse_size.setter
    def warehouse_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb682cffa8639019a3d246df698597f1933be487556ff7d66681abdaec17a65a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warehouseSize", value)

    @builtins.property
    @jsii.member(jsii_name="warehouseType")
    def warehouse_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warehouseType"))

    @warehouse_type.setter
    def warehouse_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e2ec6ca1e83f9784c4d21dfe7ac241ada21747ef3247184dfea371249ab7f05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warehouseType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.warehouse.WarehouseConfig",
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
        "auto_resume": "autoResume",
        "auto_suspend": "autoSuspend",
        "comment": "comment",
        "enable_query_acceleration": "enableQueryAcceleration",
        "id": "id",
        "initially_suspended": "initiallySuspended",
        "max_cluster_count": "maxClusterCount",
        "max_concurrency_level": "maxConcurrencyLevel",
        "min_cluster_count": "minClusterCount",
        "query_acceleration_max_scale_factor": "queryAccelerationMaxScaleFactor",
        "resource_monitor": "resourceMonitor",
        "scaling_policy": "scalingPolicy",
        "statement_queued_timeout_in_seconds": "statementQueuedTimeoutInSeconds",
        "statement_timeout_in_seconds": "statementTimeoutInSeconds",
        "wait_for_provisioning": "waitForProvisioning",
        "warehouse_size": "warehouseSize",
        "warehouse_type": "warehouseType",
    },
)
class WarehouseConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        auto_resume: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_suspend: typing.Optional[jsii.Number] = None,
        comment: typing.Optional[builtins.str] = None,
        enable_query_acceleration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        initially_suspended: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        max_cluster_count: typing.Optional[jsii.Number] = None,
        max_concurrency_level: typing.Optional[jsii.Number] = None,
        min_cluster_count: typing.Optional[jsii.Number] = None,
        query_acceleration_max_scale_factor: typing.Optional[jsii.Number] = None,
        resource_monitor: typing.Optional[builtins.str] = None,
        scaling_policy: typing.Optional[builtins.str] = None,
        statement_queued_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        statement_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        wait_for_provisioning: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        warehouse_size: typing.Optional[builtins.str] = None,
        warehouse_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Identifier for the virtual warehouse; must be unique for your account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#name Warehouse#name}
        :param auto_resume: Specifies whether to automatically resume a warehouse when a SQL statement (e.g. query) is submitted to it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#auto_resume Warehouse#auto_resume}
        :param auto_suspend: Specifies the number of seconds of inactivity after which a warehouse is automatically suspended. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#auto_suspend Warehouse#auto_suspend}
        :param comment: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#comment Warehouse#comment}.
        :param enable_query_acceleration: Specifies whether to enable the query acceleration service for queries that rely on this warehouse for compute resources. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#enable_query_acceleration Warehouse#enable_query_acceleration}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#id Warehouse#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initially_suspended: Specifies whether the warehouse is created initially in the ‘Suspended’ state. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#initially_suspended Warehouse#initially_suspended}
        :param max_cluster_count: Specifies the maximum number of server clusters for the warehouse. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#max_cluster_count Warehouse#max_cluster_count}
        :param max_concurrency_level: Object parameter that specifies the concurrency level for SQL statements (i.e. queries and DML) executed by a warehouse. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#max_concurrency_level Warehouse#max_concurrency_level}
        :param min_cluster_count: Specifies the minimum number of server clusters for the warehouse (only applies to multi-cluster warehouses). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#min_cluster_count Warehouse#min_cluster_count}
        :param query_acceleration_max_scale_factor: Specifies the maximum scale factor for leasing compute resources for query acceleration. The scale factor is used as a multiplier based on warehouse size. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#query_acceleration_max_scale_factor Warehouse#query_acceleration_max_scale_factor}
        :param resource_monitor: Specifies the name of a resource monitor that is explicitly assigned to the warehouse. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#resource_monitor Warehouse#resource_monitor}
        :param scaling_policy: Specifies the policy for automatically starting and shutting down clusters in a multi-cluster warehouse running in Auto-scale mode. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#scaling_policy Warehouse#scaling_policy}
        :param statement_queued_timeout_in_seconds: Object parameter that specifies the time, in seconds, a SQL statement (query, DDL, DML, etc.) can be queued on a warehouse before it is canceled by the system. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#statement_queued_timeout_in_seconds Warehouse#statement_queued_timeout_in_seconds}
        :param statement_timeout_in_seconds: Specifies the time, in seconds, after which a running SQL statement (query, DDL, DML, etc.) is canceled by the system. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#statement_timeout_in_seconds Warehouse#statement_timeout_in_seconds}
        :param wait_for_provisioning: Specifies whether the warehouse, after being resized, waits for all the servers to provision before executing any queued or new queries. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#wait_for_provisioning Warehouse#wait_for_provisioning}
        :param warehouse_size: Specifies the size of the virtual warehouse. Larger warehouse sizes 5X-Large and 6X-Large are currently in preview and only available on Amazon Web Services (AWS). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#warehouse_size Warehouse#warehouse_size}
        :param warehouse_type: Specifies a STANDARD or SNOWPARK-OPTIMIZED warehouse. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#warehouse_type Warehouse#warehouse_type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64f374449bfcb04875c974ead721be8454c4c46c8a3a696b4e9fd7fbc3003d99)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument auto_resume", value=auto_resume, expected_type=type_hints["auto_resume"])
            check_type(argname="argument auto_suspend", value=auto_suspend, expected_type=type_hints["auto_suspend"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument enable_query_acceleration", value=enable_query_acceleration, expected_type=type_hints["enable_query_acceleration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument initially_suspended", value=initially_suspended, expected_type=type_hints["initially_suspended"])
            check_type(argname="argument max_cluster_count", value=max_cluster_count, expected_type=type_hints["max_cluster_count"])
            check_type(argname="argument max_concurrency_level", value=max_concurrency_level, expected_type=type_hints["max_concurrency_level"])
            check_type(argname="argument min_cluster_count", value=min_cluster_count, expected_type=type_hints["min_cluster_count"])
            check_type(argname="argument query_acceleration_max_scale_factor", value=query_acceleration_max_scale_factor, expected_type=type_hints["query_acceleration_max_scale_factor"])
            check_type(argname="argument resource_monitor", value=resource_monitor, expected_type=type_hints["resource_monitor"])
            check_type(argname="argument scaling_policy", value=scaling_policy, expected_type=type_hints["scaling_policy"])
            check_type(argname="argument statement_queued_timeout_in_seconds", value=statement_queued_timeout_in_seconds, expected_type=type_hints["statement_queued_timeout_in_seconds"])
            check_type(argname="argument statement_timeout_in_seconds", value=statement_timeout_in_seconds, expected_type=type_hints["statement_timeout_in_seconds"])
            check_type(argname="argument wait_for_provisioning", value=wait_for_provisioning, expected_type=type_hints["wait_for_provisioning"])
            check_type(argname="argument warehouse_size", value=warehouse_size, expected_type=type_hints["warehouse_size"])
            check_type(argname="argument warehouse_type", value=warehouse_type, expected_type=type_hints["warehouse_type"])
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
        if auto_resume is not None:
            self._values["auto_resume"] = auto_resume
        if auto_suspend is not None:
            self._values["auto_suspend"] = auto_suspend
        if comment is not None:
            self._values["comment"] = comment
        if enable_query_acceleration is not None:
            self._values["enable_query_acceleration"] = enable_query_acceleration
        if id is not None:
            self._values["id"] = id
        if initially_suspended is not None:
            self._values["initially_suspended"] = initially_suspended
        if max_cluster_count is not None:
            self._values["max_cluster_count"] = max_cluster_count
        if max_concurrency_level is not None:
            self._values["max_concurrency_level"] = max_concurrency_level
        if min_cluster_count is not None:
            self._values["min_cluster_count"] = min_cluster_count
        if query_acceleration_max_scale_factor is not None:
            self._values["query_acceleration_max_scale_factor"] = query_acceleration_max_scale_factor
        if resource_monitor is not None:
            self._values["resource_monitor"] = resource_monitor
        if scaling_policy is not None:
            self._values["scaling_policy"] = scaling_policy
        if statement_queued_timeout_in_seconds is not None:
            self._values["statement_queued_timeout_in_seconds"] = statement_queued_timeout_in_seconds
        if statement_timeout_in_seconds is not None:
            self._values["statement_timeout_in_seconds"] = statement_timeout_in_seconds
        if wait_for_provisioning is not None:
            self._values["wait_for_provisioning"] = wait_for_provisioning
        if warehouse_size is not None:
            self._values["warehouse_size"] = warehouse_size
        if warehouse_type is not None:
            self._values["warehouse_type"] = warehouse_type

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
        '''Identifier for the virtual warehouse; must be unique for your account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#name Warehouse#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_resume(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specifies whether to automatically resume a warehouse when a SQL statement (e.g. query) is submitted to it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#auto_resume Warehouse#auto_resume}
        '''
        result = self._values.get("auto_resume")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auto_suspend(self) -> typing.Optional[jsii.Number]:
        '''Specifies the number of seconds of inactivity after which a warehouse is automatically suspended.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#auto_suspend Warehouse#auto_suspend}
        '''
        result = self._values.get("auto_suspend")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#comment Warehouse#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_query_acceleration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specifies whether to enable the query acceleration service for queries that rely on this warehouse for compute resources.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#enable_query_acceleration Warehouse#enable_query_acceleration}
        '''
        result = self._values.get("enable_query_acceleration")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#id Warehouse#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initially_suspended(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specifies whether the warehouse is created initially in the ‘Suspended’ state.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#initially_suspended Warehouse#initially_suspended}
        '''
        result = self._values.get("initially_suspended")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def max_cluster_count(self) -> typing.Optional[jsii.Number]:
        '''Specifies the maximum number of server clusters for the warehouse.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#max_cluster_count Warehouse#max_cluster_count}
        '''
        result = self._values.get("max_cluster_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_concurrency_level(self) -> typing.Optional[jsii.Number]:
        '''Object parameter that specifies the concurrency level for SQL statements (i.e. queries and DML) executed by a warehouse.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#max_concurrency_level Warehouse#max_concurrency_level}
        '''
        result = self._values.get("max_concurrency_level")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_cluster_count(self) -> typing.Optional[jsii.Number]:
        '''Specifies the minimum number of server clusters for the warehouse (only applies to multi-cluster warehouses).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#min_cluster_count Warehouse#min_cluster_count}
        '''
        result = self._values.get("min_cluster_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def query_acceleration_max_scale_factor(self) -> typing.Optional[jsii.Number]:
        '''Specifies the maximum scale factor for leasing compute resources for query acceleration.

        The scale factor is used as a multiplier based on warehouse size.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#query_acceleration_max_scale_factor Warehouse#query_acceleration_max_scale_factor}
        '''
        result = self._values.get("query_acceleration_max_scale_factor")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_monitor(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of a resource monitor that is explicitly assigned to the warehouse.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#resource_monitor Warehouse#resource_monitor}
        '''
        result = self._values.get("resource_monitor")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scaling_policy(self) -> typing.Optional[builtins.str]:
        '''Specifies the policy for automatically starting and shutting down clusters in a multi-cluster warehouse running in Auto-scale mode.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#scaling_policy Warehouse#scaling_policy}
        '''
        result = self._values.get("scaling_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statement_queued_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Object parameter that specifies the time, in seconds, a SQL statement (query, DDL, DML, etc.) can be queued on a warehouse before it is canceled by the system.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#statement_queued_timeout_in_seconds Warehouse#statement_queued_timeout_in_seconds}
        '''
        result = self._values.get("statement_queued_timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def statement_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Specifies the time, in seconds, after which a running SQL statement (query, DDL, DML, etc.) is canceled by the system.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#statement_timeout_in_seconds Warehouse#statement_timeout_in_seconds}
        '''
        result = self._values.get("statement_timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def wait_for_provisioning(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specifies whether the warehouse, after being resized, waits for all the servers to provision before executing any queued or new queries.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#wait_for_provisioning Warehouse#wait_for_provisioning}
        '''
        result = self._values.get("wait_for_provisioning")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def warehouse_size(self) -> typing.Optional[builtins.str]:
        '''Specifies the size of the virtual warehouse.

        Larger warehouse sizes 5X-Large and 6X-Large are currently in preview and only available on Amazon Web Services (AWS).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#warehouse_size Warehouse#warehouse_size}
        '''
        result = self._values.get("warehouse_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def warehouse_type(self) -> typing.Optional[builtins.str]:
        '''Specifies a STANDARD or SNOWPARK-OPTIMIZED warehouse.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/snowflake-labs/snowflake/0.92.0/docs/resources/warehouse#warehouse_type Warehouse#warehouse_type}
        '''
        result = self._values.get("warehouse_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WarehouseConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Warehouse",
    "WarehouseConfig",
]

publication.publish()

def _typecheckingstub__f7a545b9470ddbc13f6797573fe9db4caad9ea0ec20a416254e98f74ad315894(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    auto_resume: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_suspend: typing.Optional[jsii.Number] = None,
    comment: typing.Optional[builtins.str] = None,
    enable_query_acceleration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    initially_suspended: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    max_cluster_count: typing.Optional[jsii.Number] = None,
    max_concurrency_level: typing.Optional[jsii.Number] = None,
    min_cluster_count: typing.Optional[jsii.Number] = None,
    query_acceleration_max_scale_factor: typing.Optional[jsii.Number] = None,
    resource_monitor: typing.Optional[builtins.str] = None,
    scaling_policy: typing.Optional[builtins.str] = None,
    statement_queued_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    statement_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    wait_for_provisioning: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    warehouse_size: typing.Optional[builtins.str] = None,
    warehouse_type: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__572da37f5bf450cb7fe3f011f5e0e5d584f32856d369188d26ecdd2bed0c8cea(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59e363e0e719321b9f36ba95f42412180d8c83bca4f70f5f58bf54d11faaca1c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e33c40876b47a58a42eafec0c16bfa190228c08a23a39eea9350f0f083d61dd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4c985a73dcb01e461dd3d79db0b1b2b150d1b6ad292921dd0553f38596bff56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17a9dd2dcf21eba130519e20959255cf814826077dc1a2486f912d9091569c61(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46603b6d33e982986e0b443f6a5696f6a33454cc6e0aa6678817badd8cd756ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09d176a43f31805f67ca01f79890fb1058791b57d84f2115996086f337ed2e1f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba9c5ca5c139d131448b0430ff14223b8e4d4bb0a0fd5b55adffbbe7796824f7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec1a76dc728c5c13221da328191e3e3c34cc72784972ed2e3fc82897c41a05e8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b96edb769e4b81e3cd326f1bc18a50dd3c4dac86feefc24a81934fafe5f777a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7077b71c10d32de0bc3d3c8d12117d655ce00aa136fc82b6a7c73b6d0ec8599(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f96be4446754d4205d1e9d99a2c4abcb4828cb58dbd27f26e599e94fb3c26020(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8e4b5fc94f6dc0de4811839fa018a79668ca9d8203c01cfb6f125c1c11eb185(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da84474f179556752719c65f7b2440f46eb949691133a2f9714d5686438334d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3a106de57372b520a40ffb364b03b9b17f28f3178d2a39b83f02ec994035f8e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__142317704b4892b91eab76a9f614fe8251c78e43a9ab129e89de9d627f23595b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c819ec074e712e3da84a3865385ae14fb043c93073d4af8926ce2af78053dc70(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb682cffa8639019a3d246df698597f1933be487556ff7d66681abdaec17a65a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e2ec6ca1e83f9784c4d21dfe7ac241ada21747ef3247184dfea371249ab7f05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64f374449bfcb04875c974ead721be8454c4c46c8a3a696b4e9fd7fbc3003d99(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    auto_resume: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_suspend: typing.Optional[jsii.Number] = None,
    comment: typing.Optional[builtins.str] = None,
    enable_query_acceleration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    initially_suspended: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    max_cluster_count: typing.Optional[jsii.Number] = None,
    max_concurrency_level: typing.Optional[jsii.Number] = None,
    min_cluster_count: typing.Optional[jsii.Number] = None,
    query_acceleration_max_scale_factor: typing.Optional[jsii.Number] = None,
    resource_monitor: typing.Optional[builtins.str] = None,
    scaling_policy: typing.Optional[builtins.str] = None,
    statement_queued_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    statement_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    wait_for_provisioning: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    warehouse_size: typing.Optional[builtins.str] = None,
    warehouse_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
