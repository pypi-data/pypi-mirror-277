'''
# `provider`

Refer to the Terraform Registry for docs: [`kubectl`](https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs).
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


class KubectlProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubectl.provider.KubectlProvider",
):
    '''Represents a {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs kubectl}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
        apply_retry_count: typing.Optional[jsii.Number] = None,
        client_certificate: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        cluster_ca_certificate: typing.Optional[builtins.str] = None,
        config_context: typing.Optional[builtins.str] = None,
        config_context_auth_info: typing.Optional[builtins.str] = None,
        config_context_cluster: typing.Optional[builtins.str] = None,
        config_path: typing.Optional[builtins.str] = None,
        config_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        exec: typing.Optional[typing.Union["KubectlProviderExec", typing.Dict[builtins.str, typing.Any]]] = None,
        host: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        load_config_file: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        password: typing.Optional[builtins.str] = None,
        proxy_url: typing.Optional[builtins.str] = None,
        tls_server_name: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs kubectl} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#alias KubectlProvider#alias}
        :param apply_retry_count: Defines the number of attempts any create/update action will take. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#apply_retry_count KubectlProvider#apply_retry_count}
        :param client_certificate: PEM-encoded client certificate for TLS authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#client_certificate KubectlProvider#client_certificate}
        :param client_key: PEM-encoded client certificate key for TLS authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#client_key KubectlProvider#client_key}
        :param cluster_ca_certificate: PEM-encoded root certificates bundle for TLS authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#cluster_ca_certificate KubectlProvider#cluster_ca_certificate}
        :param config_context: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#config_context KubectlProvider#config_context}.
        :param config_context_auth_info: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#config_context_auth_info KubectlProvider#config_context_auth_info}.
        :param config_context_cluster: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#config_context_cluster KubectlProvider#config_context_cluster}.
        :param config_path: Path to the kube config file, defaults to ~/.kube/config. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#config_path KubectlProvider#config_path}
        :param config_paths: A list of paths to kube config files. Can be set with KUBE_CONFIG_PATHS environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#config_paths KubectlProvider#config_paths}
        :param exec: exec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#exec KubectlProvider#exec}
        :param host: The hostname (in form of URI) of Kubernetes master. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#host KubectlProvider#host}
        :param insecure: Whether server should be accessed without verifying the TLS certificate. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#insecure KubectlProvider#insecure}
        :param load_config_file: Load local kubeconfig. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#load_config_file KubectlProvider#load_config_file}
        :param password: The password to use for HTTP basic authentication when accessing the Kubernetes master endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#password KubectlProvider#password}
        :param proxy_url: URL to the proxy to be used for all API requests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#proxy_url KubectlProvider#proxy_url}
        :param tls_server_name: Server name passed to the server for SNI and is used in the client to check server certificates against. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#tls_server_name KubectlProvider#tls_server_name}
        :param token: Token to authentifcate an service account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#token KubectlProvider#token}
        :param username: The username to use for HTTP basic authentication when accessing the Kubernetes master endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#username KubectlProvider#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94215b0ab3a3c1a3a9e445fdc6415c8f02fb391a48bded454edef2cf1df12928)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = KubectlProviderConfig(
            alias=alias,
            apply_retry_count=apply_retry_count,
            client_certificate=client_certificate,
            client_key=client_key,
            cluster_ca_certificate=cluster_ca_certificate,
            config_context=config_context,
            config_context_auth_info=config_context_auth_info,
            config_context_cluster=config_context_cluster,
            config_path=config_path,
            config_paths=config_paths,
            exec=exec,
            host=host,
            insecure=insecure,
            load_config_file=load_config_file,
            password=password,
            proxy_url=proxy_url,
            tls_server_name=tls_server_name,
            token=token,
            username=username,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a KubectlProvider resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the KubectlProvider to import.
        :param import_from_id: The id of the existing KubectlProvider that should be imported. Refer to the {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the KubectlProvider to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96e27b12d9d8408e74cdf6f3aeda28aedf67dd666eb790a4c4eca014cf0be1a7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetApplyRetryCount")
    def reset_apply_retry_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplyRetryCount", []))

    @jsii.member(jsii_name="resetClientCertificate")
    def reset_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificate", []))

    @jsii.member(jsii_name="resetClientKey")
    def reset_client_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientKey", []))

    @jsii.member(jsii_name="resetClusterCaCertificate")
    def reset_cluster_ca_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterCaCertificate", []))

    @jsii.member(jsii_name="resetConfigContext")
    def reset_config_context(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigContext", []))

    @jsii.member(jsii_name="resetConfigContextAuthInfo")
    def reset_config_context_auth_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigContextAuthInfo", []))

    @jsii.member(jsii_name="resetConfigContextCluster")
    def reset_config_context_cluster(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigContextCluster", []))

    @jsii.member(jsii_name="resetConfigPath")
    def reset_config_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigPath", []))

    @jsii.member(jsii_name="resetConfigPaths")
    def reset_config_paths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigPaths", []))

    @jsii.member(jsii_name="resetExec")
    def reset_exec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExec", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetInsecure")
    def reset_insecure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecure", []))

    @jsii.member(jsii_name="resetLoadConfigFile")
    def reset_load_config_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadConfigFile", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetProxyUrl")
    def reset_proxy_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyUrl", []))

    @jsii.member(jsii_name="resetTlsServerName")
    def reset_tls_server_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsServerName", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

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
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="applyRetryCountInput")
    def apply_retry_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "applyRetryCountInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateInput")
    def client_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="clientKeyInput")
    def client_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterCaCertificateInput")
    def cluster_ca_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterCaCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="configContextAuthInfoInput")
    def config_context_auth_info_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configContextAuthInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="configContextClusterInput")
    def config_context_cluster_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configContextClusterInput"))

    @builtins.property
    @jsii.member(jsii_name="configContextInput")
    def config_context_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configContextInput"))

    @builtins.property
    @jsii.member(jsii_name="configPathInput")
    def config_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configPathInput"))

    @builtins.property
    @jsii.member(jsii_name="configPathsInput")
    def config_paths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "configPathsInput"))

    @builtins.property
    @jsii.member(jsii_name="execInput")
    def exec_input(self) -> typing.Optional["KubectlProviderExec"]:
        return typing.cast(typing.Optional["KubectlProviderExec"], jsii.get(self, "execInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureInput")
    def insecure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecureInput"))

    @builtins.property
    @jsii.member(jsii_name="loadConfigFileInput")
    def load_config_file_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "loadConfigFileInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyUrlInput")
    def proxy_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proxyUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsServerNameInput")
    def tls_server_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsServerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55c167557a35137ccf0463f3e6f57356d3d339f339beaad178531d57c5d5977b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="applyRetryCount")
    def apply_retry_count(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "applyRetryCount"))

    @apply_retry_count.setter
    def apply_retry_count(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__031ce08ffe6068e571aa5141416b0b690a015129751cab77ab8fbcf413d41437)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applyRetryCount", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificate")
    def client_certificate(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificate"))

    @client_certificate.setter
    def client_certificate(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9c1a9d5a52213b8a8658ae0e76a3c3e776cbd2266f0b2dbf16a2018c038c866)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="clientKey")
    def client_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientKey"))

    @client_key.setter
    def client_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d01e842f1389a1ca32dc47116e75e111c4229dd531dcf247fcd8a371eaeeabb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientKey", value)

    @builtins.property
    @jsii.member(jsii_name="clusterCaCertificate")
    def cluster_ca_certificate(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterCaCertificate"))

    @cluster_ca_certificate.setter
    def cluster_ca_certificate(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__043bfd0187cb8cb1f90f5235d9f9424505facc98b3a22d83dcf22b6c1112a864)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterCaCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="configContext")
    def config_context(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configContext"))

    @config_context.setter
    def config_context(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56bbbabed6d42b020658b478f22057d0da098c4730ca15407b5f2179243b4ce5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configContext", value)

    @builtins.property
    @jsii.member(jsii_name="configContextAuthInfo")
    def config_context_auth_info(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configContextAuthInfo"))

    @config_context_auth_info.setter
    def config_context_auth_info(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bf45cf8572c0b1b4c736c6434870b2a5597f76f47c84cf99094755e8ce81f64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configContextAuthInfo", value)

    @builtins.property
    @jsii.member(jsii_name="configContextCluster")
    def config_context_cluster(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configContextCluster"))

    @config_context_cluster.setter
    def config_context_cluster(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11080aa22bc8b5f1cf4162bec5df6d338e0a5249ace4614de524e917cf5377a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configContextCluster", value)

    @builtins.property
    @jsii.member(jsii_name="configPath")
    def config_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configPath"))

    @config_path.setter
    def config_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d21bcc13cae6d6e848098a0a1908f6f3c5e1bfa3a3a0533c0e3af78e48745dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configPath", value)

    @builtins.property
    @jsii.member(jsii_name="configPaths")
    def config_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "configPaths"))

    @config_paths.setter
    def config_paths(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a924efaca7f6089f39a2450b43653062d49f4b770d6321b13ba101b1bb390083)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configPaths", value)

    @builtins.property
    @jsii.member(jsii_name="exec")
    def exec(self) -> typing.Optional["KubectlProviderExec"]:
        return typing.cast(typing.Optional["KubectlProviderExec"], jsii.get(self, "exec"))

    @exec.setter
    def exec(self, value: typing.Optional["KubectlProviderExec"]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__287c2cc7fb2a7bc335a872ddb50b9d7514f87929dd6beb5825cc4ff62d9e530b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exec", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "host"))

    @host.setter
    def host(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b55c8a14fe6acc936b01981ef7719f4e95a6774101fc7f45010f7b778663e2ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="insecure")
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecure"))

    @insecure.setter
    def insecure(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0750a7550e8379bab9451af4ca06b3d0a9d0c8a46c7e941b31e59e8a41f95f2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecure", value)

    @builtins.property
    @jsii.member(jsii_name="loadConfigFile")
    def load_config_file(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "loadConfigFile"))

    @load_config_file.setter
    def load_config_file(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e2451b5fa7a104d7d15cc25c5e2fbeb1ce0535326f4b041264f490e8c6eb5b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadConfigFile", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fb7cf0000ab21e5281dede203ead5f29de1d1e44015571351ca5f81c2b641f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="proxyUrl")
    def proxy_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proxyUrl"))

    @proxy_url.setter
    def proxy_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb182684986baf037c2331ad6e988b9019be1d21eb2b2027350334a9404f6099)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyUrl", value)

    @builtins.property
    @jsii.member(jsii_name="tlsServerName")
    def tls_server_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsServerName"))

    @tls_server_name.setter
    def tls_server_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ceddc3645504e669b407d32d8d55118b112cb5244986ac16e0cd0a1cdb6211a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsServerName", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "token"))

    @token.setter
    def token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0e7fc35975178e67bb5c59c0927f808f22d18e3280e00307d99b454d1021c95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "username"))

    @username.setter
    def username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17be06c78a2a899bb9f2289b4fd64512275917e0ec57122843a3ce211121d152)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="kubectl.provider.KubectlProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "apply_retry_count": "applyRetryCount",
        "client_certificate": "clientCertificate",
        "client_key": "clientKey",
        "cluster_ca_certificate": "clusterCaCertificate",
        "config_context": "configContext",
        "config_context_auth_info": "configContextAuthInfo",
        "config_context_cluster": "configContextCluster",
        "config_path": "configPath",
        "config_paths": "configPaths",
        "exec": "exec",
        "host": "host",
        "insecure": "insecure",
        "load_config_file": "loadConfigFile",
        "password": "password",
        "proxy_url": "proxyUrl",
        "tls_server_name": "tlsServerName",
        "token": "token",
        "username": "username",
    },
)
class KubectlProviderConfig:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        apply_retry_count: typing.Optional[jsii.Number] = None,
        client_certificate: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        cluster_ca_certificate: typing.Optional[builtins.str] = None,
        config_context: typing.Optional[builtins.str] = None,
        config_context_auth_info: typing.Optional[builtins.str] = None,
        config_context_cluster: typing.Optional[builtins.str] = None,
        config_path: typing.Optional[builtins.str] = None,
        config_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        exec: typing.Optional[typing.Union["KubectlProviderExec", typing.Dict[builtins.str, typing.Any]]] = None,
        host: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        load_config_file: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        password: typing.Optional[builtins.str] = None,
        proxy_url: typing.Optional[builtins.str] = None,
        tls_server_name: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#alias KubectlProvider#alias}
        :param apply_retry_count: Defines the number of attempts any create/update action will take. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#apply_retry_count KubectlProvider#apply_retry_count}
        :param client_certificate: PEM-encoded client certificate for TLS authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#client_certificate KubectlProvider#client_certificate}
        :param client_key: PEM-encoded client certificate key for TLS authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#client_key KubectlProvider#client_key}
        :param cluster_ca_certificate: PEM-encoded root certificates bundle for TLS authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#cluster_ca_certificate KubectlProvider#cluster_ca_certificate}
        :param config_context: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#config_context KubectlProvider#config_context}.
        :param config_context_auth_info: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#config_context_auth_info KubectlProvider#config_context_auth_info}.
        :param config_context_cluster: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#config_context_cluster KubectlProvider#config_context_cluster}.
        :param config_path: Path to the kube config file, defaults to ~/.kube/config. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#config_path KubectlProvider#config_path}
        :param config_paths: A list of paths to kube config files. Can be set with KUBE_CONFIG_PATHS environment variable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#config_paths KubectlProvider#config_paths}
        :param exec: exec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#exec KubectlProvider#exec}
        :param host: The hostname (in form of URI) of Kubernetes master. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#host KubectlProvider#host}
        :param insecure: Whether server should be accessed without verifying the TLS certificate. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#insecure KubectlProvider#insecure}
        :param load_config_file: Load local kubeconfig. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#load_config_file KubectlProvider#load_config_file}
        :param password: The password to use for HTTP basic authentication when accessing the Kubernetes master endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#password KubectlProvider#password}
        :param proxy_url: URL to the proxy to be used for all API requests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#proxy_url KubectlProvider#proxy_url}
        :param tls_server_name: Server name passed to the server for SNI and is used in the client to check server certificates against. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#tls_server_name KubectlProvider#tls_server_name}
        :param token: Token to authentifcate an service account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#token KubectlProvider#token}
        :param username: The username to use for HTTP basic authentication when accessing the Kubernetes master endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#username KubectlProvider#username}
        '''
        if isinstance(exec, dict):
            exec = KubectlProviderExec(**exec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f012c17cd90a5e3632bec96391abfd70ff3ae477d12a604beea9fed274a97ef)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument apply_retry_count", value=apply_retry_count, expected_type=type_hints["apply_retry_count"])
            check_type(argname="argument client_certificate", value=client_certificate, expected_type=type_hints["client_certificate"])
            check_type(argname="argument client_key", value=client_key, expected_type=type_hints["client_key"])
            check_type(argname="argument cluster_ca_certificate", value=cluster_ca_certificate, expected_type=type_hints["cluster_ca_certificate"])
            check_type(argname="argument config_context", value=config_context, expected_type=type_hints["config_context"])
            check_type(argname="argument config_context_auth_info", value=config_context_auth_info, expected_type=type_hints["config_context_auth_info"])
            check_type(argname="argument config_context_cluster", value=config_context_cluster, expected_type=type_hints["config_context_cluster"])
            check_type(argname="argument config_path", value=config_path, expected_type=type_hints["config_path"])
            check_type(argname="argument config_paths", value=config_paths, expected_type=type_hints["config_paths"])
            check_type(argname="argument exec", value=exec, expected_type=type_hints["exec"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument insecure", value=insecure, expected_type=type_hints["insecure"])
            check_type(argname="argument load_config_file", value=load_config_file, expected_type=type_hints["load_config_file"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument proxy_url", value=proxy_url, expected_type=type_hints["proxy_url"])
            check_type(argname="argument tls_server_name", value=tls_server_name, expected_type=type_hints["tls_server_name"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
        if apply_retry_count is not None:
            self._values["apply_retry_count"] = apply_retry_count
        if client_certificate is not None:
            self._values["client_certificate"] = client_certificate
        if client_key is not None:
            self._values["client_key"] = client_key
        if cluster_ca_certificate is not None:
            self._values["cluster_ca_certificate"] = cluster_ca_certificate
        if config_context is not None:
            self._values["config_context"] = config_context
        if config_context_auth_info is not None:
            self._values["config_context_auth_info"] = config_context_auth_info
        if config_context_cluster is not None:
            self._values["config_context_cluster"] = config_context_cluster
        if config_path is not None:
            self._values["config_path"] = config_path
        if config_paths is not None:
            self._values["config_paths"] = config_paths
        if exec is not None:
            self._values["exec"] = exec
        if host is not None:
            self._values["host"] = host
        if insecure is not None:
            self._values["insecure"] = insecure
        if load_config_file is not None:
            self._values["load_config_file"] = load_config_file
        if password is not None:
            self._values["password"] = password
        if proxy_url is not None:
            self._values["proxy_url"] = proxy_url
        if tls_server_name is not None:
            self._values["tls_server_name"] = tls_server_name
        if token is not None:
            self._values["token"] = token
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#alias KubectlProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def apply_retry_count(self) -> typing.Optional[jsii.Number]:
        '''Defines the number of attempts any create/update action will take.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#apply_retry_count KubectlProvider#apply_retry_count}
        '''
        result = self._values.get("apply_retry_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def client_certificate(self) -> typing.Optional[builtins.str]:
        '''PEM-encoded client certificate for TLS authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#client_certificate KubectlProvider#client_certificate}
        '''
        result = self._values.get("client_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_key(self) -> typing.Optional[builtins.str]:
        '''PEM-encoded client certificate key for TLS authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#client_key KubectlProvider#client_key}
        '''
        result = self._values.get("client_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_ca_certificate(self) -> typing.Optional[builtins.str]:
        '''PEM-encoded root certificates bundle for TLS authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#cluster_ca_certificate KubectlProvider#cluster_ca_certificate}
        '''
        result = self._values.get("cluster_ca_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_context(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#config_context KubectlProvider#config_context}.'''
        result = self._values.get("config_context")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_context_auth_info(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#config_context_auth_info KubectlProvider#config_context_auth_info}.'''
        result = self._values.get("config_context_auth_info")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_context_cluster(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#config_context_cluster KubectlProvider#config_context_cluster}.'''
        result = self._values.get("config_context_cluster")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_path(self) -> typing.Optional[builtins.str]:
        '''Path to the kube config file, defaults to ~/.kube/config.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#config_path KubectlProvider#config_path}
        '''
        result = self._values.get("config_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of paths to kube config files. Can be set with KUBE_CONFIG_PATHS environment variable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#config_paths KubectlProvider#config_paths}
        '''
        result = self._values.get("config_paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def exec(self) -> typing.Optional["KubectlProviderExec"]:
        '''exec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#exec KubectlProvider#exec}
        '''
        result = self._values.get("exec")
        return typing.cast(typing.Optional["KubectlProviderExec"], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The hostname (in form of URI) of Kubernetes master.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#host KubectlProvider#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether server should be accessed without verifying the TLS certificate.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#insecure KubectlProvider#insecure}
        '''
        result = self._values.get("insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def load_config_file(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Load local kubeconfig.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#load_config_file KubectlProvider#load_config_file}
        '''
        result = self._values.get("load_config_file")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The password to use for HTTP basic authentication when accessing the Kubernetes master endpoint.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#password KubectlProvider#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy_url(self) -> typing.Optional[builtins.str]:
        '''URL to the proxy to be used for all API requests.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#proxy_url KubectlProvider#proxy_url}
        '''
        result = self._values.get("proxy_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_server_name(self) -> typing.Optional[builtins.str]:
        '''Server name passed to the server for SNI and is used in the client to check server certificates against.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#tls_server_name KubectlProvider#tls_server_name}
        '''
        result = self._values.get("tls_server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''Token to authentifcate an service account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#token KubectlProvider#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The username to use for HTTP basic authentication when accessing the Kubernetes master endpoint.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#username KubectlProvider#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubectlProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubectl.provider.KubectlProviderExec",
    jsii_struct_bases=[],
    name_mapping={
        "api_version": "apiVersion",
        "command": "command",
        "args": "args",
        "env": "env",
    },
)
class KubectlProviderExec:
    def __init__(
        self,
        *,
        api_version: builtins.str,
        command: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param api_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#api_version KubectlProvider#api_version}.
        :param command: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#command KubectlProvider#command}.
        :param args: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#args KubectlProvider#args}.
        :param env: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#env KubectlProvider#env}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ca7df008c94634b03f140593e53c1bc15d030f3325758ea85ad286b4a09d7bd)
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_version": api_version,
            "command": command,
        }
        if args is not None:
            self._values["args"] = args
        if env is not None:
            self._values["env"] = env

    @builtins.property
    def api_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#api_version KubectlProvider#api_version}.'''
        result = self._values.get("api_version")
        assert result is not None, "Required property 'api_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def command(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#command KubectlProvider#command}.'''
        result = self._values.get("command")
        assert result is not None, "Required property 'command' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#args KubectlProvider#args}.'''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def env(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/alekc/kubectl/2.0.4/docs#env KubectlProvider#env}.'''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubectlProviderExec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "KubectlProvider",
    "KubectlProviderConfig",
    "KubectlProviderExec",
]

publication.publish()

def _typecheckingstub__94215b0ab3a3c1a3a9e445fdc6415c8f02fb391a48bded454edef2cf1df12928(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: typing.Optional[builtins.str] = None,
    apply_retry_count: typing.Optional[jsii.Number] = None,
    client_certificate: typing.Optional[builtins.str] = None,
    client_key: typing.Optional[builtins.str] = None,
    cluster_ca_certificate: typing.Optional[builtins.str] = None,
    config_context: typing.Optional[builtins.str] = None,
    config_context_auth_info: typing.Optional[builtins.str] = None,
    config_context_cluster: typing.Optional[builtins.str] = None,
    config_path: typing.Optional[builtins.str] = None,
    config_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    exec: typing.Optional[typing.Union[KubectlProviderExec, typing.Dict[builtins.str, typing.Any]]] = None,
    host: typing.Optional[builtins.str] = None,
    insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    load_config_file: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    password: typing.Optional[builtins.str] = None,
    proxy_url: typing.Optional[builtins.str] = None,
    tls_server_name: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96e27b12d9d8408e74cdf6f3aeda28aedf67dd666eb790a4c4eca014cf0be1a7(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55c167557a35137ccf0463f3e6f57356d3d339f339beaad178531d57c5d5977b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__031ce08ffe6068e571aa5141416b0b690a015129751cab77ab8fbcf413d41437(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9c1a9d5a52213b8a8658ae0e76a3c3e776cbd2266f0b2dbf16a2018c038c866(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d01e842f1389a1ca32dc47116e75e111c4229dd531dcf247fcd8a371eaeeabb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__043bfd0187cb8cb1f90f5235d9f9424505facc98b3a22d83dcf22b6c1112a864(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56bbbabed6d42b020658b478f22057d0da098c4730ca15407b5f2179243b4ce5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bf45cf8572c0b1b4c736c6434870b2a5597f76f47c84cf99094755e8ce81f64(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11080aa22bc8b5f1cf4162bec5df6d338e0a5249ace4614de524e917cf5377a2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d21bcc13cae6d6e848098a0a1908f6f3c5e1bfa3a3a0533c0e3af78e48745dc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a924efaca7f6089f39a2450b43653062d49f4b770d6321b13ba101b1bb390083(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__287c2cc7fb2a7bc335a872ddb50b9d7514f87929dd6beb5825cc4ff62d9e530b(
    value: typing.Optional[KubectlProviderExec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b55c8a14fe6acc936b01981ef7719f4e95a6774101fc7f45010f7b778663e2ce(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0750a7550e8379bab9451af4ca06b3d0a9d0c8a46c7e941b31e59e8a41f95f2c(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e2451b5fa7a104d7d15cc25c5e2fbeb1ce0535326f4b041264f490e8c6eb5b9(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fb7cf0000ab21e5281dede203ead5f29de1d1e44015571351ca5f81c2b641f8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb182684986baf037c2331ad6e988b9019be1d21eb2b2027350334a9404f6099(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ceddc3645504e669b407d32d8d55118b112cb5244986ac16e0cd0a1cdb6211a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0e7fc35975178e67bb5c59c0927f808f22d18e3280e00307d99b454d1021c95(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17be06c78a2a899bb9f2289b4fd64512275917e0ec57122843a3ce211121d152(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f012c17cd90a5e3632bec96391abfd70ff3ae477d12a604beea9fed274a97ef(
    *,
    alias: typing.Optional[builtins.str] = None,
    apply_retry_count: typing.Optional[jsii.Number] = None,
    client_certificate: typing.Optional[builtins.str] = None,
    client_key: typing.Optional[builtins.str] = None,
    cluster_ca_certificate: typing.Optional[builtins.str] = None,
    config_context: typing.Optional[builtins.str] = None,
    config_context_auth_info: typing.Optional[builtins.str] = None,
    config_context_cluster: typing.Optional[builtins.str] = None,
    config_path: typing.Optional[builtins.str] = None,
    config_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    exec: typing.Optional[typing.Union[KubectlProviderExec, typing.Dict[builtins.str, typing.Any]]] = None,
    host: typing.Optional[builtins.str] = None,
    insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    load_config_file: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    password: typing.Optional[builtins.str] = None,
    proxy_url: typing.Optional[builtins.str] = None,
    tls_server_name: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ca7df008c94634b03f140593e53c1bc15d030f3325758ea85ad286b4a09d7bd(
    *,
    api_version: builtins.str,
    command: builtins.str,
    args: typing.Optional[typing.Sequence[builtins.str]] = None,
    env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
