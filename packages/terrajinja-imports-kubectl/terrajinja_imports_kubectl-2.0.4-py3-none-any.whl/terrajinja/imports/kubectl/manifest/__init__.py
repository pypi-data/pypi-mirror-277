'''
# `kubectl_manifest`

Refer to the Terraform Registry for docs: [`kubectl_manifest`](https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest).
'''
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


class Manifest(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubectl.manifest.Manifest",
):
    '''Represents a {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest kubectl_manifest}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        yaml_body: builtins.str,
        apply_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        field_manager: typing.Optional[builtins.str] = None,
        force_conflicts: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        force_new: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ignore_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        override_namespace: typing.Optional[builtins.str] = None,
        sensitive_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        server_side_apply: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["ManifestTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        validate_schema: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        wait: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        wait_for: typing.Optional[typing.Union["ManifestWaitFor", typing.Dict[builtins.str, typing.Any]]] = None,
        wait_for_rollout: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest kubectl_manifest} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param yaml_body: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#yaml_body Manifest#yaml_body}.
        :param apply_only: Apply only. In other words, it does not delete resource in any case. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#apply_only Manifest#apply_only}
        :param field_manager: Override the default field manager name. This is only relevent when using server-side apply. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#field_manager Manifest#field_manager}
        :param force_conflicts: Default false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#force_conflicts Manifest#force_conflicts}
        :param force_new: Default to update in-place. Setting to true will delete and create the kubernetes instead. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#force_new Manifest#force_new}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#id Manifest#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignore_fields: List of yaml keys to ignore changes to. Set these for fields set by Operators or other processes in kubernetes and as such you don't want to update. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#ignore_fields Manifest#ignore_fields}
        :param override_namespace: Override the namespace to apply the kubernetes resource to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#override_namespace Manifest#override_namespace}
        :param sensitive_fields: List of yaml keys with sensitive values. Set these for fields which you want obfuscated in the yaml_body output. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#sensitive_fields Manifest#sensitive_fields}
        :param server_side_apply: Default to client-side-apply. Setting to true will use server-side apply. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#server_side_apply Manifest#server_side_apply}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#timeouts Manifest#timeouts}
        :param validate_schema: Default to true (validate). Set this flag to not validate the yaml schema before applying. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#validate_schema Manifest#validate_schema}
        :param wait: Default to false (not waiting). Set this flag to wait or not for any deleted resources to be gone. This waits for finalizers. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#wait Manifest#wait}
        :param wait_for: wait_for block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#wait_for Manifest#wait_for}
        :param wait_for_rollout: Default to true (waiting). Set this flag to wait or not for Deployments and APIService to complete rollout. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#wait_for_rollout Manifest#wait_for_rollout}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__319b9d34a6064d8974a85db472a8e799b5c15c3939f4333b145155675f6fa8be)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ManifestConfig(
            yaml_body=yaml_body,
            apply_only=apply_only,
            field_manager=field_manager,
            force_conflicts=force_conflicts,
            force_new=force_new,
            id=id,
            ignore_fields=ignore_fields,
            override_namespace=override_namespace,
            sensitive_fields=sensitive_fields,
            server_side_apply=server_side_apply,
            timeouts=timeouts,
            validate_schema=validate_schema,
            wait=wait,
            wait_for=wait_for,
            wait_for_rollout=wait_for_rollout,
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
        '''Generates CDKTF code for importing a Manifest resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Manifest to import.
        :param import_from_id: The id of the existing Manifest that should be imported. Refer to the {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Manifest to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b0a091480bf20d7ab0d233e7722bec6adef33c96431b8bc3db8a19a09795b06)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#create Manifest#create}.
        '''
        value = ManifestTimeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWaitFor")
    def put_wait_for(
        self,
        *,
        field: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ManifestWaitForField", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param field: field block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#field Manifest#field}
        '''
        value = ManifestWaitFor(field=field)

        return typing.cast(None, jsii.invoke(self, "putWaitFor", [value]))

    @jsii.member(jsii_name="resetApplyOnly")
    def reset_apply_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplyOnly", []))

    @jsii.member(jsii_name="resetFieldManager")
    def reset_field_manager(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldManager", []))

    @jsii.member(jsii_name="resetForceConflicts")
    def reset_force_conflicts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceConflicts", []))

    @jsii.member(jsii_name="resetForceNew")
    def reset_force_new(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceNew", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIgnoreFields")
    def reset_ignore_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreFields", []))

    @jsii.member(jsii_name="resetOverrideNamespace")
    def reset_override_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverrideNamespace", []))

    @jsii.member(jsii_name="resetSensitiveFields")
    def reset_sensitive_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSensitiveFields", []))

    @jsii.member(jsii_name="resetServerSideApply")
    def reset_server_side_apply(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerSideApply", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetValidateSchema")
    def reset_validate_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidateSchema", []))

    @jsii.member(jsii_name="resetWait")
    def reset_wait(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWait", []))

    @jsii.member(jsii_name="resetWaitFor")
    def reset_wait_for(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitFor", []))

    @jsii.member(jsii_name="resetWaitForRollout")
    def reset_wait_for_rollout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForRollout", []))

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
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="liveManifestIncluster")
    def live_manifest_incluster(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "liveManifestIncluster"))

    @builtins.property
    @jsii.member(jsii_name="liveUid")
    def live_uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "liveUid"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ManifestTimeoutsOutputReference":
        return typing.cast("ManifestTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="waitFor")
    def wait_for(self) -> "ManifestWaitForOutputReference":
        return typing.cast("ManifestWaitForOutputReference", jsii.get(self, "waitFor"))

    @builtins.property
    @jsii.member(jsii_name="yamlBodyParsed")
    def yaml_body_parsed(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "yamlBodyParsed"))

    @builtins.property
    @jsii.member(jsii_name="yamlIncluster")
    def yaml_incluster(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "yamlIncluster"))

    @builtins.property
    @jsii.member(jsii_name="applyOnlyInput")
    def apply_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "applyOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldManagerInput")
    def field_manager_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldManagerInput"))

    @builtins.property
    @jsii.member(jsii_name="forceConflictsInput")
    def force_conflicts_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceConflictsInput"))

    @builtins.property
    @jsii.member(jsii_name="forceNewInput")
    def force_new_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceNewInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreFieldsInput")
    def ignore_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ignoreFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideNamespaceInput")
    def override_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "overrideNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="sensitiveFieldsInput")
    def sensitive_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sensitiveFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="serverSideApplyInput")
    def server_side_apply_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "serverSideApplyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "ManifestTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "ManifestTimeouts"]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="validateSchemaInput")
    def validate_schema_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "validateSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForInput")
    def wait_for_input(self) -> typing.Optional["ManifestWaitFor"]:
        return typing.cast(typing.Optional["ManifestWaitFor"], jsii.get(self, "waitForInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForRolloutInput")
    def wait_for_rollout_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitForRolloutInput"))

    @builtins.property
    @jsii.member(jsii_name="waitInput")
    def wait_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitInput"))

    @builtins.property
    @jsii.member(jsii_name="yamlBodyInput")
    def yaml_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "yamlBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="applyOnly")
    def apply_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "applyOnly"))

    @apply_only.setter
    def apply_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c67d327e3c077516491c550c8e2a4e0d3cec0fdb8aaedd611876c0a21a9f47cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applyOnly", value)

    @builtins.property
    @jsii.member(jsii_name="fieldManager")
    def field_manager(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldManager"))

    @field_manager.setter
    def field_manager(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98008e4b256d92564c374c0c676cb2d42245e2c4d86c1ac54bc6b4432071dc60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldManager", value)

    @builtins.property
    @jsii.member(jsii_name="forceConflicts")
    def force_conflicts(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forceConflicts"))

    @force_conflicts.setter
    def force_conflicts(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1295c6a4fe29ba25ac0d1549ce52cda57ea424c5ab60b6ff68de5ec257404f19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceConflicts", value)

    @builtins.property
    @jsii.member(jsii_name="forceNew")
    def force_new(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forceNew"))

    @force_new.setter
    def force_new(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a24e73f04286ea2998e79df3b8223411556062515ee20c4c68b2d2cd2274cc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceNew", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ccba5e47f090083c64820473918dee5fc5cf23d8b78cb627f1589dfc0a17cfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreFields")
    def ignore_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ignoreFields"))

    @ignore_fields.setter
    def ignore_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6459d7bdc477609fb1d180151265e1e0fe6526f33dc62876247b007ae2abe8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreFields", value)

    @builtins.property
    @jsii.member(jsii_name="overrideNamespace")
    def override_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "overrideNamespace"))

    @override_namespace.setter
    def override_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aa52eae6ab847e043ff174bb98037e6b5e3175c79a10c3adda76418a2d30285)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overrideNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="sensitiveFields")
    def sensitive_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sensitiveFields"))

    @sensitive_fields.setter
    def sensitive_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__697819b4f79071b360566fb12f514402c7b034569990d9b42f51d10d9b9a8323)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sensitiveFields", value)

    @builtins.property
    @jsii.member(jsii_name="serverSideApply")
    def server_side_apply(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "serverSideApply"))

    @server_side_apply.setter
    def server_side_apply(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__057db953b86eca9f527a11deed15dacc9e71d39f7fc6fed75bbd79d71a4aae85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSideApply", value)

    @builtins.property
    @jsii.member(jsii_name="validateSchema")
    def validate_schema(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "validateSchema"))

    @validate_schema.setter
    def validate_schema(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccbd85d32a3c95e400df3283e9e49db2156a9dd7d0a0438f0fdbf6fb1851eb1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validateSchema", value)

    @builtins.property
    @jsii.member(jsii_name="wait")
    def wait(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "wait"))

    @wait.setter
    def wait(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45317a0c18d84eca5f1cb5cc8afb88df720d18db06545cb7c92c199b0cd3b59b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wait", value)

    @builtins.property
    @jsii.member(jsii_name="waitForRollout")
    def wait_for_rollout(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "waitForRollout"))

    @wait_for_rollout.setter
    def wait_for_rollout(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5064061c4b00ec568cab0272da9efb8260e1daefe574d9603f1937b713aec51b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForRollout", value)

    @builtins.property
    @jsii.member(jsii_name="yamlBody")
    def yaml_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "yamlBody"))

    @yaml_body.setter
    def yaml_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81701e282310f32ab957ce83ba109f25728533ce51ac502a741c3afac61f049b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "yamlBody", value)


@jsii.data_type(
    jsii_type="kubectl.manifest.ManifestConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "yaml_body": "yamlBody",
        "apply_only": "applyOnly",
        "field_manager": "fieldManager",
        "force_conflicts": "forceConflicts",
        "force_new": "forceNew",
        "id": "id",
        "ignore_fields": "ignoreFields",
        "override_namespace": "overrideNamespace",
        "sensitive_fields": "sensitiveFields",
        "server_side_apply": "serverSideApply",
        "timeouts": "timeouts",
        "validate_schema": "validateSchema",
        "wait": "wait",
        "wait_for": "waitFor",
        "wait_for_rollout": "waitForRollout",
    },
)
class ManifestConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        yaml_body: builtins.str,
        apply_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        field_manager: typing.Optional[builtins.str] = None,
        force_conflicts: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        force_new: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ignore_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        override_namespace: typing.Optional[builtins.str] = None,
        sensitive_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        server_side_apply: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["ManifestTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        validate_schema: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        wait: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        wait_for: typing.Optional[typing.Union["ManifestWaitFor", typing.Dict[builtins.str, typing.Any]]] = None,
        wait_for_rollout: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param yaml_body: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#yaml_body Manifest#yaml_body}.
        :param apply_only: Apply only. In other words, it does not delete resource in any case. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#apply_only Manifest#apply_only}
        :param field_manager: Override the default field manager name. This is only relevent when using server-side apply. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#field_manager Manifest#field_manager}
        :param force_conflicts: Default false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#force_conflicts Manifest#force_conflicts}
        :param force_new: Default to update in-place. Setting to true will delete and create the kubernetes instead. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#force_new Manifest#force_new}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#id Manifest#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignore_fields: List of yaml keys to ignore changes to. Set these for fields set by Operators or other processes in kubernetes and as such you don't want to update. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#ignore_fields Manifest#ignore_fields}
        :param override_namespace: Override the namespace to apply the kubernetes resource to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#override_namespace Manifest#override_namespace}
        :param sensitive_fields: List of yaml keys with sensitive values. Set these for fields which you want obfuscated in the yaml_body output. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#sensitive_fields Manifest#sensitive_fields}
        :param server_side_apply: Default to client-side-apply. Setting to true will use server-side apply. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#server_side_apply Manifest#server_side_apply}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#timeouts Manifest#timeouts}
        :param validate_schema: Default to true (validate). Set this flag to not validate the yaml schema before applying. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#validate_schema Manifest#validate_schema}
        :param wait: Default to false (not waiting). Set this flag to wait or not for any deleted resources to be gone. This waits for finalizers. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#wait Manifest#wait}
        :param wait_for: wait_for block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#wait_for Manifest#wait_for}
        :param wait_for_rollout: Default to true (waiting). Set this flag to wait or not for Deployments and APIService to complete rollout. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#wait_for_rollout Manifest#wait_for_rollout}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = ManifestTimeouts(**timeouts)
        if isinstance(wait_for, dict):
            wait_for = ManifestWaitFor(**wait_for)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c18bce968aa7acc2bbe6bab1707807b568f49457fb5dbafa7e2d5afee4b8e449)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument yaml_body", value=yaml_body, expected_type=type_hints["yaml_body"])
            check_type(argname="argument apply_only", value=apply_only, expected_type=type_hints["apply_only"])
            check_type(argname="argument field_manager", value=field_manager, expected_type=type_hints["field_manager"])
            check_type(argname="argument force_conflicts", value=force_conflicts, expected_type=type_hints["force_conflicts"])
            check_type(argname="argument force_new", value=force_new, expected_type=type_hints["force_new"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ignore_fields", value=ignore_fields, expected_type=type_hints["ignore_fields"])
            check_type(argname="argument override_namespace", value=override_namespace, expected_type=type_hints["override_namespace"])
            check_type(argname="argument sensitive_fields", value=sensitive_fields, expected_type=type_hints["sensitive_fields"])
            check_type(argname="argument server_side_apply", value=server_side_apply, expected_type=type_hints["server_side_apply"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument validate_schema", value=validate_schema, expected_type=type_hints["validate_schema"])
            check_type(argname="argument wait", value=wait, expected_type=type_hints["wait"])
            check_type(argname="argument wait_for", value=wait_for, expected_type=type_hints["wait_for"])
            check_type(argname="argument wait_for_rollout", value=wait_for_rollout, expected_type=type_hints["wait_for_rollout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "yaml_body": yaml_body,
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
        if apply_only is not None:
            self._values["apply_only"] = apply_only
        if field_manager is not None:
            self._values["field_manager"] = field_manager
        if force_conflicts is not None:
            self._values["force_conflicts"] = force_conflicts
        if force_new is not None:
            self._values["force_new"] = force_new
        if id is not None:
            self._values["id"] = id
        if ignore_fields is not None:
            self._values["ignore_fields"] = ignore_fields
        if override_namespace is not None:
            self._values["override_namespace"] = override_namespace
        if sensitive_fields is not None:
            self._values["sensitive_fields"] = sensitive_fields
        if server_side_apply is not None:
            self._values["server_side_apply"] = server_side_apply
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if validate_schema is not None:
            self._values["validate_schema"] = validate_schema
        if wait is not None:
            self._values["wait"] = wait
        if wait_for is not None:
            self._values["wait_for"] = wait_for
        if wait_for_rollout is not None:
            self._values["wait_for_rollout"] = wait_for_rollout

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
    def yaml_body(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#yaml_body Manifest#yaml_body}.'''
        result = self._values.get("yaml_body")
        assert result is not None, "Required property 'yaml_body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def apply_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Apply only. In other words, it does not delete resource in any case.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#apply_only Manifest#apply_only}
        '''
        result = self._values.get("apply_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def field_manager(self) -> typing.Optional[builtins.str]:
        '''Override the default field manager name. This is only relevent when using server-side apply.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#field_manager Manifest#field_manager}
        '''
        result = self._values.get("field_manager")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_conflicts(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Default false.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#force_conflicts Manifest#force_conflicts}
        '''
        result = self._values.get("force_conflicts")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def force_new(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Default to update in-place. Setting to true will delete and create the kubernetes instead.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#force_new Manifest#force_new}
        '''
        result = self._values.get("force_new")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#id Manifest#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of yaml keys to ignore changes to.

        Set these for fields set by Operators or other processes in kubernetes and as such you don't want to update.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#ignore_fields Manifest#ignore_fields}
        '''
        result = self._values.get("ignore_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def override_namespace(self) -> typing.Optional[builtins.str]:
        '''Override the namespace to apply the kubernetes resource to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#override_namespace Manifest#override_namespace}
        '''
        result = self._values.get("override_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sensitive_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of yaml keys with sensitive values. Set these for fields which you want obfuscated in the yaml_body output.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#sensitive_fields Manifest#sensitive_fields}
        '''
        result = self._values.get("sensitive_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def server_side_apply(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Default to client-side-apply. Setting to true will use server-side apply.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#server_side_apply Manifest#server_side_apply}
        '''
        result = self._values.get("server_side_apply")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ManifestTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#timeouts Manifest#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ManifestTimeouts"], result)

    @builtins.property
    def validate_schema(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Default to true (validate). Set this flag to not validate the yaml schema before applying.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#validate_schema Manifest#validate_schema}
        '''
        result = self._values.get("validate_schema")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def wait(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Default to false (not waiting).

        Set this flag to wait or not for any deleted resources to be gone. This waits for finalizers.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#wait Manifest#wait}
        '''
        result = self._values.get("wait")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def wait_for(self) -> typing.Optional["ManifestWaitFor"]:
        '''wait_for block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#wait_for Manifest#wait_for}
        '''
        result = self._values.get("wait_for")
        return typing.cast(typing.Optional["ManifestWaitFor"], result)

    @builtins.property
    def wait_for_rollout(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Default to true (waiting). Set this flag to wait or not for Deployments and APIService to complete rollout.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#wait_for_rollout Manifest#wait_for_rollout}
        '''
        result = self._values.get("wait_for_rollout")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManifestConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubectl.manifest.ManifestTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class ManifestTimeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#create Manifest#create}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c8451ebe50695383a947020538b43593d56ad31da089ee3cd2b411cabe445f7)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#create Manifest#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManifestTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManifestTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubectl.manifest.ManifestTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c842e058e6123b1e61fb16626fc9fd1939e73881cc6ab5f8aaee430e3756413)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16a79a2ed1b58cc954d9207db49cea0290e6d0a190ee88934d012bf510ae91ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ManifestTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ManifestTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ManifestTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4470a8809ee036cc8056f97fff9b184b3f4c3854b74b680e857a470028a14f87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubectl.manifest.ManifestWaitFor",
    jsii_struct_bases=[],
    name_mapping={"field": "field"},
)
class ManifestWaitFor:
    def __init__(
        self,
        *,
        field: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ManifestWaitForField", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param field: field block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#field Manifest#field}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f30702f2e16899218ab49d92715484385ed5ab24916f94f752dba3b24a6f56c7)
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "field": field,
        }

    @builtins.property
    def field(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ManifestWaitForField"]]:
        '''field block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#field Manifest#field}
        '''
        result = self._values.get("field")
        assert result is not None, "Required property 'field' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ManifestWaitForField"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManifestWaitFor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubectl.manifest.ManifestWaitForField",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value", "value_type": "valueType"},
)
class ManifestWaitForField:
    def __init__(
        self,
        *,
        key: builtins.str,
        value: builtins.str,
        value_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Key which should be matched from resulting object. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#key Manifest#key}
        :param value: Value to wait for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#value Manifest#value}
        :param value_type: Value type. Can be either a ``eq`` (equivalent) or ``regex``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#value_type Manifest#value_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab573ef93c6ad2d0dffde1e070034940240a4d61a5333af39d8987844e9f7d9b)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument value_type", value=value_type, expected_type=type_hints["value_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }
        if value_type is not None:
            self._values["value_type"] = value_type

    @builtins.property
    def key(self) -> builtins.str:
        '''Key which should be matched from resulting object.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#key Manifest#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value to wait for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#value Manifest#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value_type(self) -> typing.Optional[builtins.str]:
        '''Value type. Can be either a ``eq`` (equivalent) or ``regex``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/resources/manifest#value_type Manifest#value_type}
        '''
        result = self._values.get("value_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManifestWaitForField(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManifestWaitForFieldList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubectl.manifest.ManifestWaitForFieldList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ef02c5918700ae2b477c234d489ce28821f2e37481ea38d65158606f27103e1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ManifestWaitForFieldOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4211626ad7a78ab2a991c79febbf24b5c4f829d96209a1d932e6281fcd3e5f92)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ManifestWaitForFieldOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4b1b63b051975edffa45b94bb0517c343978e9623652c6533d0ca92fb364454)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b7a14370749bdf3ceb00f3cc773a458abd7bd6670c9b290edecfc820f5aee28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a5f3939691179b5c34703d937a275eeccf5fe9e560d687cc0c09095295c1d16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ManifestWaitForField]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ManifestWaitForField]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ManifestWaitForField]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45d72700f2d171bd7b6ff7014c643338532f87f074246177e70df93f1c27af7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManifestWaitForFieldOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubectl.manifest.ManifestWaitForFieldOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebd83c9d788aa1b7d549d9521e20ad1fa71d9385223242fe21036e42bda5eff7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValueType")
    def reset_value_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValueType", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="valueTypeInput")
    def value_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c188483b6222e79ba47472335f880132842261122a20afe463666d3050b4af7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0482a77fc39f73d546387ba271fc0f4ae1649d3f88748834d334ee5f8fbc4fe0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="valueType")
    def value_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "valueType"))

    @value_type.setter
    def value_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f5822ca156d5885a70044be17c06bbaece447baf2face4e1435aca04365a905)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ManifestWaitForField]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ManifestWaitForField]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ManifestWaitForField]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d4ffa6f91cd432341f71e900335726aa30d8749fbc61f9b54629c278c1db818)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManifestWaitForOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubectl.manifest.ManifestWaitForOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b150ef81c5a0fac75a82c4dcbf27d70cec5b18e96c6b28c6d5af8182430826b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putField")
    def put_field(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ManifestWaitForField, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66cabc02d210d306d07f3b9cf44cd71fe3f29715d0083e45e153a0b74794d827)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putField", [value]))

    @builtins.property
    @jsii.member(jsii_name="field")
    def field(self) -> ManifestWaitForFieldList:
        return typing.cast(ManifestWaitForFieldList, jsii.get(self, "field"))

    @builtins.property
    @jsii.member(jsii_name="fieldInput")
    def field_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ManifestWaitForField]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ManifestWaitForField]]], jsii.get(self, "fieldInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ManifestWaitFor]:
        return typing.cast(typing.Optional[ManifestWaitFor], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ManifestWaitFor]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e37352f72e6662a2b9b144d26717a999391d40c2bfd644d594c5acd37f69cc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Manifest",
    "ManifestConfig",
    "ManifestTimeouts",
    "ManifestTimeoutsOutputReference",
    "ManifestWaitFor",
    "ManifestWaitForField",
    "ManifestWaitForFieldList",
    "ManifestWaitForFieldOutputReference",
    "ManifestWaitForOutputReference",
]

publication.publish()

def _typecheckingstub__319b9d34a6064d8974a85db472a8e799b5c15c3939f4333b145155675f6fa8be(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    yaml_body: builtins.str,
    apply_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    field_manager: typing.Optional[builtins.str] = None,
    force_conflicts: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    force_new: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    ignore_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    override_namespace: typing.Optional[builtins.str] = None,
    sensitive_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    server_side_apply: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeouts: typing.Optional[typing.Union[ManifestTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    validate_schema: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    wait: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    wait_for: typing.Optional[typing.Union[ManifestWaitFor, typing.Dict[builtins.str, typing.Any]]] = None,
    wait_for_rollout: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__2b0a091480bf20d7ab0d233e7722bec6adef33c96431b8bc3db8a19a09795b06(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c67d327e3c077516491c550c8e2a4e0d3cec0fdb8aaedd611876c0a21a9f47cb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98008e4b256d92564c374c0c676cb2d42245e2c4d86c1ac54bc6b4432071dc60(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1295c6a4fe29ba25ac0d1549ce52cda57ea424c5ab60b6ff68de5ec257404f19(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a24e73f04286ea2998e79df3b8223411556062515ee20c4c68b2d2cd2274cc4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ccba5e47f090083c64820473918dee5fc5cf23d8b78cb627f1589dfc0a17cfb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6459d7bdc477609fb1d180151265e1e0fe6526f33dc62876247b007ae2abe8b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aa52eae6ab847e043ff174bb98037e6b5e3175c79a10c3adda76418a2d30285(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__697819b4f79071b360566fb12f514402c7b034569990d9b42f51d10d9b9a8323(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__057db953b86eca9f527a11deed15dacc9e71d39f7fc6fed75bbd79d71a4aae85(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccbd85d32a3c95e400df3283e9e49db2156a9dd7d0a0438f0fdbf6fb1851eb1e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45317a0c18d84eca5f1cb5cc8afb88df720d18db06545cb7c92c199b0cd3b59b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5064061c4b00ec568cab0272da9efb8260e1daefe574d9603f1937b713aec51b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81701e282310f32ab957ce83ba109f25728533ce51ac502a741c3afac61f049b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c18bce968aa7acc2bbe6bab1707807b568f49457fb5dbafa7e2d5afee4b8e449(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    yaml_body: builtins.str,
    apply_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    field_manager: typing.Optional[builtins.str] = None,
    force_conflicts: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    force_new: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    ignore_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    override_namespace: typing.Optional[builtins.str] = None,
    sensitive_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    server_side_apply: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeouts: typing.Optional[typing.Union[ManifestTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    validate_schema: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    wait: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    wait_for: typing.Optional[typing.Union[ManifestWaitFor, typing.Dict[builtins.str, typing.Any]]] = None,
    wait_for_rollout: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c8451ebe50695383a947020538b43593d56ad31da089ee3cd2b411cabe445f7(
    *,
    create: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c842e058e6123b1e61fb16626fc9fd1939e73881cc6ab5f8aaee430e3756413(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16a79a2ed1b58cc954d9207db49cea0290e6d0a190ee88934d012bf510ae91ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4470a8809ee036cc8056f97fff9b184b3f4c3854b74b680e857a470028a14f87(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ManifestTimeouts]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f30702f2e16899218ab49d92715484385ed5ab24916f94f752dba3b24a6f56c7(
    *,
    field: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ManifestWaitForField, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab573ef93c6ad2d0dffde1e070034940240a4d61a5333af39d8987844e9f7d9b(
    *,
    key: builtins.str,
    value: builtins.str,
    value_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ef02c5918700ae2b477c234d489ce28821f2e37481ea38d65158606f27103e1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4211626ad7a78ab2a991c79febbf24b5c4f829d96209a1d932e6281fcd3e5f92(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4b1b63b051975edffa45b94bb0517c343978e9623652c6533d0ca92fb364454(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b7a14370749bdf3ceb00f3cc773a458abd7bd6670c9b290edecfc820f5aee28(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a5f3939691179b5c34703d937a275eeccf5fe9e560d687cc0c09095295c1d16(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45d72700f2d171bd7b6ff7014c643338532f87f074246177e70df93f1c27af7b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ManifestWaitForField]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebd83c9d788aa1b7d549d9521e20ad1fa71d9385223242fe21036e42bda5eff7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c188483b6222e79ba47472335f880132842261122a20afe463666d3050b4af7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0482a77fc39f73d546387ba271fc0f4ae1649d3f88748834d334ee5f8fbc4fe0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f5822ca156d5885a70044be17c06bbaece447baf2face4e1435aca04365a905(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d4ffa6f91cd432341f71e900335726aa30d8749fbc61f9b54629c278c1db818(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ManifestWaitForField]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b150ef81c5a0fac75a82c4dcbf27d70cec5b18e96c6b28c6d5af8182430826b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66cabc02d210d306d07f3b9cf44cd71fe3f29715d0083e45e153a0b74794d827(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ManifestWaitForField, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e37352f72e6662a2b9b144d26717a999391d40c2bfd644d594c5acd37f69cc3(
    value: typing.Optional[ManifestWaitFor],
) -> None:
    """Type checking stubs"""
    pass
