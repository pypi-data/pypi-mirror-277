'''
# `data_kubectl_path_documents`

Refer to the Terraform Registry for docs: [`data_kubectl_path_documents`](https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents).
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


class DataKubectlPathDocuments(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubectl.dataKubectlPathDocuments.DataKubectlPathDocuments",
):
    '''Represents a {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents kubectl_path_documents}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        pattern: builtins.str,
        disable_template: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        sensitive_vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents kubectl_path_documents} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param pattern: Glob pattern to search for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents#pattern DataKubectlPathDocuments#pattern}
        :param disable_template: Flag to disable template parsing of the loaded documents. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents#disable_template DataKubectlPathDocuments#disable_template}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents#id DataKubectlPathDocuments#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param sensitive_vars: Sensitive variables to substitute, allowing for hiding sensitive variables in terraform output. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents#sensitive_vars DataKubectlPathDocuments#sensitive_vars}
        :param vars: Variables to substitute. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents#vars DataKubectlPathDocuments#vars}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e71fbefec5f87f8d5dfaeb734bd4d1915eb172ddda0f966043fca889c012293)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataKubectlPathDocumentsConfig(
            pattern=pattern,
            disable_template=disable_template,
            id=id,
            sensitive_vars=sensitive_vars,
            vars=vars,
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
        '''Generates CDKTF code for importing a DataKubectlPathDocuments resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataKubectlPathDocuments to import.
        :param import_from_id: The id of the existing DataKubectlPathDocuments that should be imported. Refer to the {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataKubectlPathDocuments to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96c16e88ce152e37e4ced3ad5d34f61b9bd18404b17261c57f3e712b4f46c3e8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetDisableTemplate")
    def reset_disable_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableTemplate", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSensitiveVars")
    def reset_sensitive_vars(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSensitiveVars", []))

    @jsii.member(jsii_name="resetVars")
    def reset_vars(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVars", []))

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
    @jsii.member(jsii_name="documents")
    def documents(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "documents"))

    @builtins.property
    @jsii.member(jsii_name="manifests")
    def manifests(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "manifests"))

    @builtins.property
    @jsii.member(jsii_name="disableTemplateInput")
    def disable_template_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="patternInput")
    def pattern_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "patternInput"))

    @builtins.property
    @jsii.member(jsii_name="sensitiveVarsInput")
    def sensitive_vars_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sensitiveVarsInput"))

    @builtins.property
    @jsii.member(jsii_name="varsInput")
    def vars_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "varsInput"))

    @builtins.property
    @jsii.member(jsii_name="disableTemplate")
    def disable_template(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableTemplate"))

    @disable_template.setter
    def disable_template(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5031ba362f203bb7c25f071a71d4e9be12dabcf0f3c65e6845e804cde5eb134)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e7192ea7e2ef250225d8d04f26aa341a711f592d2b5515f1ec3f136dfcba885)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="pattern")
    def pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pattern"))

    @pattern.setter
    def pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7af70402696700853088c926022abed98b3f88cafbde095bc1854d8721219018)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pattern", value)

    @builtins.property
    @jsii.member(jsii_name="sensitiveVars")
    def sensitive_vars(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sensitiveVars"))

    @sensitive_vars.setter
    def sensitive_vars(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59d604b678927205181a49ffca794e315b4ae2bb8d7bf837988a228087ea8e5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sensitiveVars", value)

    @builtins.property
    @jsii.member(jsii_name="vars")
    def vars(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "vars"))

    @vars.setter
    def vars(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__439944b003f88077e0a467a766d7494ef5a8a3ad5b55d85258058711686acd9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vars", value)


@jsii.data_type(
    jsii_type="kubectl.dataKubectlPathDocuments.DataKubectlPathDocumentsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "pattern": "pattern",
        "disable_template": "disableTemplate",
        "id": "id",
        "sensitive_vars": "sensitiveVars",
        "vars": "vars",
    },
)
class DataKubectlPathDocumentsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        pattern: builtins.str,
        disable_template: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        sensitive_vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param pattern: Glob pattern to search for. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents#pattern DataKubectlPathDocuments#pattern}
        :param disable_template: Flag to disable template parsing of the loaded documents. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents#disable_template DataKubectlPathDocuments#disable_template}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents#id DataKubectlPathDocuments#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param sensitive_vars: Sensitive variables to substitute, allowing for hiding sensitive variables in terraform output. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents#sensitive_vars DataKubectlPathDocuments#sensitive_vars}
        :param vars: Variables to substitute. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents#vars DataKubectlPathDocuments#vars}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2578526c0f3df68e417546a52f7e74a146a6c675e13169253d2beeb65778afe6)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
            check_type(argname="argument disable_template", value=disable_template, expected_type=type_hints["disable_template"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument sensitive_vars", value=sensitive_vars, expected_type=type_hints["sensitive_vars"])
            check_type(argname="argument vars", value=vars, expected_type=type_hints["vars"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pattern": pattern,
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
        if disable_template is not None:
            self._values["disable_template"] = disable_template
        if id is not None:
            self._values["id"] = id
        if sensitive_vars is not None:
            self._values["sensitive_vars"] = sensitive_vars
        if vars is not None:
            self._values["vars"] = vars

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
    def pattern(self) -> builtins.str:
        '''Glob pattern to search for.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents#pattern DataKubectlPathDocuments#pattern}
        '''
        result = self._values.get("pattern")
        assert result is not None, "Required property 'pattern' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disable_template(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Flag to disable template parsing of the loaded documents.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents#disable_template DataKubectlPathDocuments#disable_template}
        '''
        result = self._values.get("disable_template")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents#id DataKubectlPathDocuments#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sensitive_vars(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Sensitive variables to substitute, allowing for hiding sensitive variables in terraform output.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents#sensitive_vars DataKubectlPathDocuments#sensitive_vars}
        '''
        result = self._values.get("sensitive_vars")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def vars(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Variables to substitute.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs/data-sources/path_documents#vars DataKubectlPathDocuments#vars}
        '''
        result = self._values.get("vars")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubectlPathDocumentsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataKubectlPathDocuments",
    "DataKubectlPathDocumentsConfig",
]

publication.publish()

def _typecheckingstub__4e71fbefec5f87f8d5dfaeb734bd4d1915eb172ddda0f966043fca889c012293(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    pattern: builtins.str,
    disable_template: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    sensitive_vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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

def _typecheckingstub__96c16e88ce152e37e4ced3ad5d34f61b9bd18404b17261c57f3e712b4f46c3e8(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5031ba362f203bb7c25f071a71d4e9be12dabcf0f3c65e6845e804cde5eb134(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e7192ea7e2ef250225d8d04f26aa341a711f592d2b5515f1ec3f136dfcba885(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7af70402696700853088c926022abed98b3f88cafbde095bc1854d8721219018(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59d604b678927205181a49ffca794e315b4ae2bb8d7bf837988a228087ea8e5d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__439944b003f88077e0a467a766d7494ef5a8a3ad5b55d85258058711686acd9f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2578526c0f3df68e417546a52f7e74a146a6c675e13169253d2beeb65778afe6(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    pattern: builtins.str,
    disable_template: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    sensitive_vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
