from ezlab.parameters import *
from ezlab.utils import *


logger = logging.getLogger("ezua")


def precheck(APPCONFIG: dict = app.storage.general):
    """Fabric pre-checks for roles"""

    ezfabricctl_cmd = find_app("ezfabricctl")
    if ezfabricctl_cmd is None:
        return False

    write_precheck_yaml(APPCONFIG)

    # Results
    coordinator_ok = False
    compute_ok = False
    storage_ok = False
    proxy_ok = False
    dns_ok = False

    # output marker
    host = "LOCAL"
    role = ""

    for out in execute(f"{ezfabricctl_cmd} pc -i ./.ezlab/prechecksInput.yaml -s ./.ezlab/prechecksStatus.txt"):
        if "Running checks for Ezmeral " in out:
            # should use regex but too lazy for it
            # extracting from string '***** Running checks for Ezmeral Unified Analytics role "worker" on host "vm23.kaya.home"'
            hostrole = out.split('role "')[1]
            role = hostrole.split('"')[0]
            host = hostrole.split('"')[2]

        logger.info("[ %s %s ]: %s", role.upper(), host, out)

        if "Additional information for debugging is written to" in out:
            # reset the host/role pair
            host = "LOCAL"
            role = ""

        # Check aggregate results

        if "Coordinator hosts: SUCCESS" in out:
            coordinator_ok = True

        if "Compute hosts: SUCCESS" in out:
            compute_ok = True

        if "Storage hosts: SUCCESS" in out:
            storage_ok = True

        if "Proxy settings: SUCCESS" in out:
            proxy_ok = True

        if "DNS settings: SUCCESS" in out:
            dns_ok = True

    return all([coordinator_ok, compute_ok, storage_ok, proxy_ok, dns_ok])


def install(APPCONFIG: dict = app.storage.general):
    """
    UA orchestrator installation
    """

    ezfabricctl_cmd = find_app("ezfabricctl")
    if ezfabricctl_cmd is None:
        return False

    write_ezkf_input_yaml(APPCONFIG)

    result = False

    for out in execute(
        f"{ezfabricctl_cmd} o init -p ./ezfab-release.tgz -i ./.ezlab/ezkf-input.yaml -s ./.ezlab/ezkf-orch-status.txt --save-kubeconfig ./.ezlab/mgmt-kubeconfig"
    ):
        # ignore transfer messages, overloading UI
        if "Transferring to " not in out:
            logger.info(out)
            markword = "Save kubeconfig in "
            if markword in out:
                msg = out.split(markword)[1]
                APP_STATUS_CONTAINER.append(("Orchestrator Kubeconfig", msg.replace("./.ezlab", "/files", 1)))
                status_container.refresh()

    write_hostPoolConfig_yaml(APPCONFIG)

    for out in execute(f"{ezfabricctl_cmd} ph i -i ./.ezlab/hostPoolConfig.yaml -c ./.ezlab/mgmt-kubeconfig -s ./.ezlab/hostPoolConfigStatus.txt"):
        logger.info(out)

    write_clusterConfig_yaml(APPCONFIG)

    for out in execute(f"{ezfabricctl_cmd} w i -i ./.ezlab/clusterConfig.yaml -c ./.ezlab/mgmt-kubeconfig -s ./.ezlab/clusterConfigStatus.txt"):
        logger.info(out)

    for out in execute(
        f"{ezfabricctl_cmd} w g k -n {APPCONFIG[UA].get('clustername', 'ezlab')} -i ./.ezlab/clusterConfig.yaml -c ./.ezlab/mgmt-kubeconfig -s ./.ezlab/clusterConfigStatus.txt --save-kubeconfig ./.ezlab/workload-kubeconfig"
    ):
        logger.info(out)
        markword = "Fetched kubeconfig for "
        if markword in out:
            APP_STATUS_CONTAINER.append(("Workload Kubeconfig", "/files/workload-kubeconfig"))
            status_container.refresh()
            result = True

    return result


def deploy(APPCONFIG: dict = app.storage.general):
    """
    Submit ezkfWorkloadDeploy CR
    """
    kubectl_cmd = find_app("kubectl")
    if kubectl_cmd is None:
        return False

    write_ezkf_workloaddeploy_yaml(APPCONFIG)

    for out in execute(f"{kubectl_cmd} --kubeconfig=./.ezlab/workload-kubeconfig apply -f ./.ezlab/ezkfWorkloadDeploy.yaml"):
        logger.info(out)
        if f"ezkfworkloaddeploy.ezkfops.hpe.ezkf-ops.com/{APPCONFIG[UA].get('clustername', 'ezlab')}" in out and any(
            i in out for i in ["created", "configured", "unchanged"]
        ):
            # STATUS="kubectl --kubeconfig=./worker_kubeconfig get ezkfworkloaddeploy/$CLUSTER_NAME -n $CLUSTER_NAME -o json | jq -r '.status.status'"
            logger.info(
                f"""
                Monitor CR Status with:
                kubectl --kubeconfig=./.ezlab/workload-kubeconfig get ezkfworkloaddeploy -n {APPCONFIG[UA].get('clustername', 'ezlab')} -o json | jq '.status.genericaddonsstatus | .[] | select(.installstatus == "INSTALLING")'
                """
            )

    return True


def write_precheck_yaml(APPCONFIG: dict):
    """
    Write the file for prechecks
    """

    hosts_yaml = ""
    for host in APPCONFIG[UA]["workers"].split(","):
        hosts_yaml += f"      - host: {host}\n"

    input = f"""defaultHostCredentials:
  sshUserName: {APPCONFIG["config"]["username"]}
  sshPassword: {toB64(APPCONFIG["config"]["password"])}
  sshPort: 22
sudoPrefix: ""
prechecks:
  coordinator:
    controlplane:
      - host: {APPCONFIG[UA]["orchestrator"]}
  ua:
    controlplane:
      - host: {APPCONFIG[UA]["controller"]}
    worker:
{hosts_yaml}"""

    with open("./.ezlab/prechecksInput.yaml", "wt") as f:
        f.write(input)


def write_ezkf_input_yaml(APPCONFIG: dict):
    """
    Write the file for orchestrator deployment
    """

    input = f"""defaultHostCredentials:
  sshUserName: {APPCONFIG["config"]["username"]}
  sshPassword: {toB64(APPCONFIG["config"]["password"])}
  sshPort: 22
airgap:
  registryUrl: {APPCONFIG[UA].get("registryUrl", "''")}
  registryInsecure: {APPCONFIG[UA].get("registryInsecure", "true")}
orchestrator:
  deployTarget: pph
  controlPlane:
    enableHa: false
    externalUrl: ""
  network:
    pods:
      cidrBlocks: 10.224.0.0/16
    serviceDomain: cluster.local
    services:
      cidrBlocks: 10.96.0.0/12
hosts:
  - host: {APPCONFIG[UA]["orchestrator"]}
webproxy:
  httpProxy: {APPCONFIG["config"].get("proxy", "")}
  httpsProxy: {APPCONFIG["config"].get("proxy","")}
  noProxy: {NO_PROXY.format(vm_domain=APPCONFIG["config"]["domain"], vm_network=APPCONFIG["config"]["cidr"],no_proxy=APPCONFIG[UA].get("orchestrator", ""))}
"""
    with open("./.ezlab/ezkf-input.yaml", "wt") as f:
        f.write(input)


def write_hostPoolConfig_yaml(APPCONFIG: dict):
    """ """
    workers = APPCONFIG[UA]["workers"].split(",")
    input = f"""defaultHostCredentials:
  sshUserName: {APPCONFIG["config"]["username"]}
  sshPassword: {toB64(APPCONFIG["config"]["password"])}
  sshPort: 22
hosts:
  - host: {APPCONFIG[UA]["controller"]}
    labels:
    - role: controlplane
  - host: {workers[0]}
    labels:
    - role: worker
  - host: {workers[1]}
    labels:
    - role: worker
  - host: {workers[2]}
    labels:
    - role: worker

"""
    with open("./.ezlab/hostPoolConfig.yaml", "wt") as f:
        f.write(input)


def write_clusterConfig_yaml(APPCONFIG: dict):
    """
    Create cluster configuration for deployment
    """

    input = f"""workload:
  deployTarget: pph
  deployEnv: ezkube
  workloadType: ezua
  clusterName: {APPCONFIG[UA].get('clustername', 'ezlab')}
  resources:
    vcpu: 96
  controlPlaneHostLabels:
    role: controlplane
  workerHostLabels:
    role: worker
  dataFabricHostLabels:
    role: worker
  gpuHostLabels:
    role: worker
  clusterLabels: {{}}
  controlplane:
    enableHa: false
    controlPlaneEndpoint: {APPCONFIG[UA]["controller"]}
  airgap:
    registryUrl: {APPCONFIG[UA].get("registryUrl", "''")}
    registryInsecure: {APPCONFIG[UA].get("registryInsecure", "true")}
  network:
    pods:
      cidrBlocks: "10.224.0.0/16"
    serviceDomain: "cluster.local"
    services:
      cidrBlocks: "10.96.0.0/12"

"""

    with open("./.ezlab/clusterConfig.yaml", "wt") as f:
        f.write(input)


def write_ezkf_workloaddeploy_yaml(APPCONFIG: dict):
    """
    Write the file for UA apps deployment
    """

    AUTH_DATA = f"""{{
        "admin_user": {{
            "fullname": "Ezmeral Admin",
            "email": "ezadmin@{APPCONFIG['config']['domain']}",
            "password": "{APPCONFIG['config']['password']}",
            "username": "admin"
        }}
    }}
    """

    input = f"""
apiVersion: v1
data:
  registryCaFile: "{APPCONFIG[UA].get("registryCaFile", "")}"
  userName: "{APPCONFIG[UA].get("registryUsername", "")}"
  password: "{toB64(APPCONFIG[UA].get("registryPassword", ""))}"
kind: Secret
metadata:
  name: airgap
  namespace: {APPCONFIG[UA].get('clustername', 'ezlab')}
type: Opaque

---
apiVersion: v1
data:
  internal_auth: {toB64(AUTH_DATA)}
kind: Secret
metadata:
  name: authconfig
  namespace: {APPCONFIG[UA].get('clustername', 'ezlab')}
type: Opaque


---
apiVersion: ezkfops.hpe.ezkf-ops.com/v1alpha1
kind: EzkfWorkloadDeploy
metadata:
  name: {APPCONFIG[UA].get('clustername', 'ezlab')}
  namespace: {APPCONFIG[UA].get('clustername', 'ezlab')}
spec:
  deploytarget: pph
  workloadtype: ezua
  clustername: {APPCONFIG[UA].get('clustername', 'ezlab')}
  domainname: {APPCONFIG[UA].get('clustername', 'ezlab')}.{APPCONFIG["config"]["domain"]}
  isAirgap: false
  deployallinfra: true
  genericaddons:
    machine: true
    ezkube: true
  proxy:
    httpProxy: {APPCONFIG["config"].get("proxy", "")}
    httpsProxy: {APPCONFIG["config"].get("proxy", "")}
    noProxy: {NO_PROXY.format(vm_domain=APPCONFIG["config"]["domain"], vm_network=APPCONFIG["config"]["cidr"],no_proxy=APPCONFIG[UA].get("orchestrator", ""))}
  workloadaddons:
    ua_prep: true
    hpecp_agent: true
    oidc: true
    kyverno: true
    monitoring: true
    keycloak: true
    chartmuseum: true
    ezaf_controller: true
  deployallapps: true # always set to true from UA
  authconfig:
    secret_name: "authconfig"
  airgap:
    secret_name: "airgap"
    registryUrl: {APPCONFIG[UA].get("registryUrl", "''")}
    registryInsecure: {APPCONFIG[UA].get("registryInsecure", "true")}

"""

    with open("./.ezlab/ezkfWorkloadDeploy.yaml", "wt") as f:
        f.write(input)
